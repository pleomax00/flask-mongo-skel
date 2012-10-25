import os, sys

# Thirdparty modules goes into 3rd party, lets add it to path.
dirname, filename = os.path.split (os.path.abspath (__file__))
sys.path.append (os.path.join (dirname, "thirdparty"))

from fallenthrone import app as application


