# AutoBackup-linux
Creating .tar.gz file then pushing that into ssh instance


Usage: backuper [OPTIONS]...
## Creating backups, sending via ssh...

This program requires tar, scp and sshpass programs on OS...
```
Options:
  -h, --help, printing help

  For creating archive
    -c, --create=[path] (required)
    -e, --exclude=[exclude file,next file,etc]
    -o, --output=[output filename]
    -z, --gunzip    compressing when you used -c before
  For sending archive via ssh (optional)
    -s, --send=[user@ip:/path/on/destination]
    -i, --identity=[/path/to/ssh/key]
    -p, --pass=[password for user]

Example of usage:
    main.py -c=~/Code -e=~/Code/C++,~/Code/WWW -o=zip.tar.gz -z -s=user@192.168.101.156:./kopia/ -p=pass
```
