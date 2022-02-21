##
## Copyright (c) 2022 Andrew E Page
## 
## Permission is hereby granted, free of charge, to any person obtaining a copy
## of this software and associated documentation files (the "Software"), to deal
## in the Software without restriction, including without limitation the rights
## to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
## copies of the Software, and to permit persons to whom the Software is
## furnished to do so, subject to the following conditions:
## 
## The above copyright notice and this permission notice shall be included in all
## copies or substantial portions of the Software.
## 
## THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
## EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
## MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
## IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
## DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
## OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
## OR OTHER DEALINGS IN THE SOFTWARE.
##

import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread, QMutex, QWaitCondition, pyqtSignal, pyqtSlot, Qt
from PyQt5 import QtGui
from datetime import datetime
from operator import attrgetter

import githubV3py
from githubV3py import GitHubClient, Artifact
    
    
def SizeStr(size):
    if size >= 1e12:
        return f"{size/(1024**4):.1f}T"
    if size >= 1e9:
        return f"{size/(1024**3):.1f}G"
    if size >= 1e6:
        return f"{size/(1024**2):.1f}M"
    if size >= 1e3:
        return f"{size/1024:.1f}K"
    return f"{size}"

class AritfactThread(QThread):
    
    output = pyqtSignal(str, Artifact)
    complete = pyqtSignal(int, datetime)
    running = pyqtSignal(bool)
    
    def __init__(self, owner, token, parent=None):
        QThread.__init__(self, parent)
        
        self._token = token
        self._owner = owner
        
        self._mutex = QMutex()
        self._cond = QWaitCondition()
        self._runningcond = QWaitCondition()
        self._runflag = True

        self._loopflag = True
        self._isRunning = False
        
        
    def run(self):
        self._mutex.lock()
        
        while True:
            
            self._isRunning = False
            self._runningcond.wakeAll()
            
            self._cond.wait(self._mutex)
            if not self._runflag:
                return
            
            self._isRunning = True
            self._runningcond.wakeAll()            
            
            ghc = GitHubClient(token=self._token, usesession=True)
            for repo in GitHubClient.generate(ghc.ReposListForAuthenticatedUser):
                if not self._loopflag:
                    break
                
                for artifact in GitHubClient.generate(ghc.ActionsListArtifactsForRepo, self._owner, repo.name, extractor=attrgetter('artifacts')):
                    
                    if not self._loopflag:
                        break 
                    
                    if not artifact.ok and artifact.status_code == 404:
                        break # expected if repo has no artifacts
                    
                    
                    if artifact.expired:
                        continue
                    self.output.emit(repo.name, artifact)
            self.complete.emit(ghc.rateLimitRemaining, ghc.rateLimitReset)
                    
            
    @pyqtSlot()
    def stop(self):
        
        self._mutex.lock()
        self._loopflag = False
        
        while self._isRunning:
            self._runningcond.wait(self._mutex)
        
        self._mutex.unlock()
        
    @pyqtSlot()
    def fetchartifacts(self, owner, token):   
        self._owner = owner
        self._token = token
        self._mutex.lock()
        self._cond.wakeAll()
        self._mutex.unlock()

class ArtifactWindow(object):
    def __init__(self, token, owner, geometry=(500, 100, 600, 600)):
        self._artifacts = []
        self._thread = AritfactThread(owner, token)
        
        self._thread.start()
        
        self._thread.output[str, Artifact].connect(self._addArtifact)
        self._thread.complete[int, datetime].connect(self._artifactsComplete)
    
        self._mainw = mainW = QMainWindow()
        mainW.setWindowTitle("Artifact Cleaner")
            
        baseDir = os.path.dirname(__file__)
            
        menuBar = mainW.menuBar()
        
        tb = mainW.addToolBar("")
        self._fetchAction = fetchAction = tb.addAction(QtGui.QIcon(os.path.join(baseDir, "data/refresh+icon-1320183705440102854_64.png")), "Fetch Artifacts")
        fetchAction.triggered.connect(self._fetch_artifacts)
        
        
        self._stopAction = tb.addAction(QtGui.QIcon(os.path.join(baseDir, "data/stop64x64.png")), "Stop Fetch")
        self._stopAction.triggered.connect(self._stopFetch)
        self._stopAction.setEnabled(False)
        
        self._deleteAction = tb.addAction(QtGui.QIcon(os.path.join(baseDir, "data/icon+x+icon-1320183702540076171_64.png")), "Delete Check Items")
        self._deleteAction.triggered.connect(self._delete_artifacts)
        
        tb.addSeparator()
        
        tb.addWidget(QLabel("owner:"))
        self._ownerInput = QLineEdit(text=owner)
        tb.addWidget(self._ownerInput)        
    
        tb.addWidget(QLabel("token:"))
        self._tokenInput = QLineEdit(text=token, echoMode=QLineEdit.Password)
        tb.addWidget(self._tokenInput)        
    
        table = self._table = QTableWidget()
        table.setColumnCount(6)
        table.setRowCount(0)
        
        checkHeader = QTableWidgetItem()
        table.setHorizontalHeaderItem(0, checkHeader)
        self._checkAllState = True
        
        table.setColumnWidth(0, 50)
        
        idheader = QTableWidgetItem("ID")
        table.setHorizontalHeaderItem(1, idheader)
        table.setColumnWidth(1, 100)
        
        repoHeader = QTableWidgetItem("Repo")
        table.setHorizontalHeaderItem(2, repoHeader)
        table.setColumnWidth(2, 250)
        
        artifactHeader = QTableWidgetItem("Artifact")
        table.setHorizontalHeaderItem(3, artifactHeader)
        table.setColumnWidth(3, 200)
        
        sizeHeader = QTableWidgetItem("Size")
        table.setHorizontalHeaderItem(4, sizeHeader)
        table.setColumnWidth(4, 75)
        
        expiresHeader = QTableWidgetItem("Expires")
        table.setHorizontalHeaderItem(5, expiresHeader)
        table.setColumnWidth(5, 175)
        
        mainW.setCentralWidget(self._table)
        
        header = table.horizontalHeader()
        header.setSectionsClickable(True)
        header.sectionClicked.connect(self._headerSectionClicked)
        
        self._tableIndex = 0
        self._totalSize = 0
        
        mainW.setGeometry(*geometry)
        
    def _headerSectionClicked(self, item):
        if item == 0:
            self._checkAll(self._checkAllState)
            self._checkAllState = not self._checkAllState
            
    def _checkAll(self, state=True):
        for row in range(self._table.rowCount()):
            w = self._table.cellWidget(row, 0) 
            w.setChecked(state)
            
        
    def _artifactsComplete(self, rateLimitRemaining, rateLimitReset):
        self._fetchAction.setEnabled(True)
        self._stopAction.setEnabled(False)
        resetT = rateLimitReset.strftime("%I:%M%p")
        self._mainw.statusBar().showMessage(f"{rateLimitRemaining} remaining  reset:  {resetT}  total={SizeStr(self._totalSize)}")
        
    def _addArtifact(self, reponame, artifact):
        isinstance(artifact, Artifact)
        self._totalSize += artifact.size_in_bytes
        self._artifacts.append((reponame, artifact))
        table = self._table
        
        table.setRowCount(self._tableIndex+1)
        table.setCellWidget(self._tableIndex, 0, QCheckBox())
        
        
        idcell = QTableWidgetItem(f"{artifact.id}")
        table.setItem(self._tableIndex, 1, idcell)
        
        repoCell = QTableWidgetItem(reponame)
        table.setItem(self._tableIndex, 2, repoCell)
        
        
        artifactCell = QTableWidgetItem(artifact.name)
        table.setItem(self._tableIndex, 3, artifactCell)
        
        sizeCell = QTableWidgetItem(SizeStr(artifact.size_in_bytes))
        table.setItem(self._tableIndex, 4, sizeCell)
        
        dateStr = artifact.expires_at.strftime("%m/%d/%y %I:%M%p UTC")
        dateCell = QTableWidgetItem(dateStr)
        
        table.setItem(self._tableIndex, 5, dateCell)
        self._tableIndex += 1        
        
        
    def _stopFetch(self):
        
        self._thread.stop()
        
        self._artifacts.clear()
                
        table = self._table
        table.clearContents()
        table.setRowCount(0)
        self._fetchAction.setEnabled(False)
        self._stopAction.setEnabled(True)
        
        self._tableIndex = 0
        self._totalSize = 0
        return
        
    def _fetch_artifacts(self):
        
        token    = self._tokenInput.text()
        owner    = self._ownerInput.text()
        
        if not token:
            QMessageBox.information(self._tokenInput, "Credentials", "Need to specify token")
            return
        
        self._fetchAction.setEnabled(False)
        self._stopAction.setEnabled(True)
        self._artifacts.clear()
        
        
        table = self._table
        table.clearContents()
        table.setRowCount(0)
        self._tableIndex = 0
        self._totalSize = 0
        
        self._thread.fetchartifacts(owner, token)
        
    
    def _delete_artifacts(self):
        
        owner = self._ownerInput.text()
        token = self._tokenInput.text()
        
        col = 0
        n = 0
        toDelete = []
        for row in range(self._table.rowCount()):
            w = self._table.cellWidget(row, col) 
            if w.isChecked():
                n += 1
                toDelete.append(self._artifacts[row])
        
        msgBox = QMessageBox(QMessageBox.Warning, "Delete", 
                             f"YOU ARE ABOUT TO DELETE {n} ARTIFACTS\nAre you sure?", 
                             QMessageBox.Ok | QMessageBox.Cancel)
        
        result = msgBox.exec()
        if result == QMessageBox.Cancel:
            return
        
        ghc = GitHubClient(token=token, usesession=True)
        for reponame, artifact in toDelete:
            result = ghc.ActionsDeleteArtifact(owner, reponame, artifact.id)
            assert(isinstance(result, githubV3py.HttpResponse))
        
        
        
        self._fetch_artifacts()
        return
    
    def show(self):
        self._mainw.show()
        


def main():
    import argparse
    
    parser = argparse.ArgumentParser()
    
    parser.add_argument("-o", "--owner")
    parser.add_argument("-t", "--token")
    
    options = parser.parse_args()
    
    app = QApplication(sys.argv)
    

    size = app.primaryScreen().size()
    
    w = size.width()//2
    h = size.height()//2
    
    geometry = ((size.width()-w)//2, (size.height()-h)//2,
                w, h)

    
    AW = ArtifactWindow(token=options.token, owner=options.owner, 
                        geometry=geometry)
    AW.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()