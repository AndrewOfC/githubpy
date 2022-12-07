
|File   | Purpose|
| ----- | ------ |
|octocat.py| Renders the github mascot as ascii art with a custom message|
|qtartifactcleaner|PyQt5 GUI tool that scans your repos for artifacts and lists them for possible deletion.<BR><BR>Handy for keeping your storage costs down|
|workflow_list.py | simple list of workflows|
|issuelister.py|produce a CSV list of issues for a repo<br>Handy for collecting hero stats for the boss|
|workflowcleaner.py|clean workflow runs.  Good for getting rid of a long list of failed runs|
|workflow_dispatch.py|Allows launching of Action workflows from the command line |


# Artifact Cleaner

Note:  you will needed to have PyQt5 installed:

```bash
pip install PyQt5
```

Usage:
```bash
python3 --owner <owner> --token <GITHUB_TOKEN> example
```

![](images/artifactcleaner.png)


# Credits
- Refresh Icon By: https://icons-for-free.com/refresh+icon-1320183705440102854/
- X icon by: https://icons-for-free.com/icon+x+icon-1320183702540076171/![<Display Name>](