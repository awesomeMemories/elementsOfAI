# Building AI

## Table of Contents

- [Shebang](#Shebang)
- [Install pip](#Install pip)
- [Install matplotlib](#Install matplotlib)


## Shebang
When you run a Python file from the command line on a Unix-like system (e.g. Linux, macOS), the shell reads the first line of the file to determine how to execute it. If the line begins with #!, it is interpreted as a shebang line, and the rest of the line is used to specify the interpreter that should be used to execute the file.

In the case of #!/usr/bin/env python, the shebang line tells the shell to use the env command to locate the python executable in the current environment. This allows you to specify the interpreter without having to know the exact path to the python executable on your system.

By including the shebang line in your Python file, you can make the file executable and run it from the command line without having to explicitly specify the Python interpreter. For example, if you have a file named my_program.py with the shebang line #!/usr/bin/env python, you can make it executable with the command chmod +x my_program.py, and then run it with the command ./my_program.py.

## Install pip
sudo apt install python3-pip

## Install matplotlib
pip install matplotlib

