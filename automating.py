from pathlib import Path
import os
import re

#class for handling windows exceptions
if not getattr(__builtins__, "WindowsError", None):
    class WindowsError(OSError): pass

# a function to look up for the words in the documents
def lookUp(keyword, path):
    list = []
    for file in path.glob('*.txt'):
        with open(file, encoding='utf-8', errors='ignore') as f:
            list.append(str(f.readlines()))

        #list = Path(file, encoding=None, errors=None).read_text()
        

        if(re.findall(keyword, str(list), flags=re.IGNORECASE)):
            print("The Document You Are Looking For, Is in: ", file)

# a function to navigate through folders(parents->child)

def navigate(keyword, curpath):
    try:
        if curpath.is_dir(): 
            list = os.listdir(curpath)
            path = curpath

            if len(list) > 0 : 
                for folder in list:
                    path = curpath / folder
                    if path.is_dir():
                        #print(path)
                        lookUp(keyword, path)
                        navigate(keyword, path)
    except WindowsError as e:
        print(e)                


#driving code

keyword = 'scripting'


targetPath = Path.home() / Path('Documents/')

navigate(keyword, targetPath)











## print(os.path.abspath('.\\python.txt')) --> already returns the full path for the target


## print(os.path.dirname(targetPath)) I can use this function to go back

