#!/usr/bin/env python
print "--Calling Bash Command ls -l"
import subprocess
subprocess.call("ls -l", shell=True)
