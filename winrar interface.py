import os
import subprocess
working_dir = "F:\\tmp\\"
file_name = "filelist.txt"
file = open(working_dir+file_name, 'r')
lines = list()
for f in file:
    lines = lines + [f.strip('\n')]

file.close()

print(lines)
cmds = "cmd.exe /C dir /d"
output = subprocess.run(cmds, capture_output=True)

print(output.stdout)
print(output)

# Example of subprocess.run with arguments
#>>> subprocess.run(["ls", "-l", "/dev/null"], capture_output=True)
# CompletedProcess(args=['ls', '-l', '/dev/null'], returncode=0,
# stdout=b'crw-rw-rw- 1 root root 1, 3 Jan 23 16:23 /dev/null\n', stderr=b'')

#subprocess.run(args,...) takes in arguments where args is a list of parameters.
# The first parameter args[0] is the program we're running
# The rest of the parameters args[1...n] are the arguments passed
#   to the program we're running.

