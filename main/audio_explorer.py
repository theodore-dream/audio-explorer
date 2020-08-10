#!/usr/bin/python3

import subprocess

try:
    subprocess.run(["./radio.sh", "therapy"], timeout=5, text=True)
    print("try 1 failed")
except subprocess.TimeoutExpired:
    subprocess.run(["./radio.sh", "talk"])



#command = ["./radio.sh", "talk"]
#explore = subprocess.run(command, text=True, timeout=5)
#
#try:
#    output, error = explore()
#except subprocess.TimeoutExpired:
#    explore.kill()
#    outs, error = global_proc.communicate()

