from os import system
from sys import argv

def compress(path : str, exclude : list, output : str, compress):
    command = 'tar c'
    if compress == True:
        command+=f'zf {output} '
    else:
        command+=f'f {output} '

    if exclude:
        for item in exclude:
            command+=f'--exclude {item} '
    command+=path
    system(command)


def print_help():
    print('Usage: backuper [OPTIONS]...')
    print('Creating backups, sending via ssh...')
    print('')
    print('This program requires tar, scp and sshpass programs on OS...')
    print('')
    print('Options:')
    print('  For creating archive')
    print('    -c, --create=[path]')
    print('    -e, --exclude=[exclude file,next file,etc]')
    print('    -o, --output=[output filename]')
    print('    -z, --gunzip    compressing when you used -c before')
    print('  For sending archive via ssh')
    print('    -s, --send=[user@ip:/path/on/destination]')
    print('    -i, --identity=[/path/to/ssh/key]')
    print('    -p, --pass=[password for user]')
    print('')
    print('  -h, --help, printing help')

def compose_options(args : list):
    HELP=False
    CREATE=False
    EXCLUDE=False
    OUTPUT=False
    GUNZIP=False
    SEND=False
    IDENTITY=False
    PASSWORD=False
    args.pop(0)
    if not args:
        HELP=True
    for option in args:
        option=str(option)
        if option.startswith('-h') or option.startswith('--help'):
            HELP=True
        elif option.startswith('-c') or option.startswith('--create'):
            try:
                option.index('=')
                CREATE=option[option.index('=')+1:]
            except:
                print('Use -c, --create with = symbol')
                print('    --create=/path/to/dir')
        elif option.startswith('-o') or option.startswith('--output'):
            try:
                option.index('=')
                OUTPUT=option[option.index('=')+1:]
            except:
                print('Use -o, --output with = symbol')
                print('    --output=/path/to/output')
        elif option.startswith('-e') or option.startswith('--exclude'):
            try:
                option.index('=')
                EXCLUDE=option[option.index('=')+1:].split(',')
            except:
                print('Use -e, --exclude with = symbol')
                print('    --exclude=/path/to/exclude')
        elif option.startswith('-s') or option.startswith('--send'):
            try:
                option.index('=')
                SEND=option[option.index('=')+1:]
            except:
                print('Use -s, --send with = symbol')
                print('    --send=user@ip:/path/on/destination')
        elif option.startswith('-i') or option.startswith('--identity'):
            try:
                option.index('=')
                IDENTITY=option[option.index('=')+1:]
            except:
                print('Use -i, --identity with = symbol')
                print('    --identity=/path/to/key')
        elif option.startswith('-p') or option.startswith('--pass'):
            try:
                option.index('=')
                PASSWORD=option[option.index('=')+1:]
            except:
                print('Use -p, --pass with = symbol')
                print('    --pass=password')
        
        
        elif option=='-z' or option=='--gunzip':
            GUNZIP=True
    if HELP:
        print_help()
        quit()
    
    return [CREATE, EXCLUDE, OUTPUT, GUNZIP, SEND, IDENTITY, PASSWORD]
    
def send_file(file, command, identity=False, password=False):
    if identity:
        command = f'scp -i {identity} {file} {command}'
    elif password:
        command = f'sshpass -p {password} scp {file} {command}'
    else:
        print('No password or identity file...')
        command = f'scp {file} {command}'
    
    system(command)


create, exclude, output, gunzip, send, identity, password = compose_options(argv)
if create:
    if not output:
        output="backup"
    compress(create, exclude, output, gunzip)
    if send:
        send_file(output, send, identity, password)

    print('Program ended work')