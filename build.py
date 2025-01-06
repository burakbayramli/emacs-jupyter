import sys, os

if sys.argv[1] == 'zip':
    os.system("zip /opt/Downloads/dotbkps/emacs-jupyter.zip -r /home/burak/Documents/repos/emacs-jupyter/.git/")
