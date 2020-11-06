#!/usr/bin/python3

# this script is a basic test of subprocess timeout, need to implement this
# and other "fail-check" type features into my main script, to avoid timeout issues

import subprocess
import shlex
from subprocess import Popen, PIPE


#proc = subprocess.run(["./radio.sh", "talk"], timeout=5, check=True, text=True)
#print(proc.returncode, result.stdout, result.stderr)


try:
    subprocess.run(["./radio.sh", "therapy"], timeout=5, text=True, check=True)
    print("try 1 failed")
except subprocess.TimeoutExpired:
    subprocess.run(["./radio.sh", "Sci Fi"], text=True)



#command = ["./radio.sh", "talk"]
#explore = subprocess.run(command, text=True, timeout=5)
#
#try:
#    output, error = explore()
#except subprocess.TimeoutExpired:
#    explore.kill()
#    outs, error = global_proc.communicate()

