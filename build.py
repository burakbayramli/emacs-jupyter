import sys, os

if sys.argv[1] == 'zip':
    os.system("zip /opt/Downloads/dotbkps/jupimacs.zip -r /home/burak/Documents/repos/jupimacs/.git/")
