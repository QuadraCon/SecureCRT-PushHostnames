import os
from termcolor import colored

try:
    #Select Sessions folder. This is recursive, all other folders down from here will also be queried
     path = "C:\\path\\HighestFolder"
except Exception as catchAllConnectionException:
    print('--------------------------------------------------------')
    print(colored(catchAllConnectionException, 'red'))
    print('--------------------------------------------------------')
else:
    print('--------------------------------------------------------')
    print(colored(f'Pushing new hostsnames to {path}', "green"))
    try:
        #os.walk makes it recursive
        for path, dirs, files in os.walk(path):
            for filename in files:
                fileContents  = []
                fullpath = os.path.join(path, filename)
                with open(fullpath, 'r') as readFile:
                    lines = readFile.readlines()
                for line in lines:
                    if line.find('"Hostname"=') != -1:
                        line = line.replace('old.local', 'new.local')
                    fileContents.append(line)
                with open(fullpath, 'w') as writeFile:
                    for line in fileContents:
                        writeFile.write(line)
                print(colored(f'{filename} has been rewritten',"green"))
        print(colored('Script done', 'green'))
        print('--------------------------------------------------------')                               
    except Exception as catchAllOutputException:
        print(colored(catchAllOutputException, 'red'))
        print('--------------------------------------------------------')    