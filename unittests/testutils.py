

import sys, random

def PlatformString():
    "Return a string uniquely identifying platorm and python version"
    return f"{sys.version_info.major}.{sys.version_info.minor}-{sys.platform}"

def randstring(n=10, seed="abcdefghijklmnopqrtstuvwxyzABCDEFGHIJKLMNOPQRTSTUVWXYZ"):
    "Generate a random string"
    return ''.join(random.choices(seed, k=n))
