#!/usr/bin/env python3

# Author ID: cklau9


import subprocess

def free_space():
    # Start a subprocess that runs a shell command to check disk space usage
    free_space = subprocess.Popen("df -h | grep '/$' | awk '{print $4}'", stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    
    # Communicate with the above free_space to get the output
    output = free_space.communicate()
    
    # Decode stdout to utf-8 and  has newline characters strip off any newline characters
    stdout = output[0].decode('utf-8').strip()
    
    # Return the processed stdout
    return stdout

if __name__ == '__main__':
    # Print the free disk space
    print(free_space())
