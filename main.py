from tkinter import Tk
from github import Github
import ast
from datetime import datetime
from gitFile import File as GitFile

GITHUB_TOKEN = "YOUR_REPO_TOKEN"
REPO_NAME = "YOUR_USERNAME/YOUR_REPO_NAME"

g = Github(GITHUB_TOKEN)

try:
    repo = g.get_repo(REPO_NAME)
except:
    print('NETWORK ISSUES')
    exit()
keys = []
files = []
searchKeys = []

def exitable_input():
    i = input()
    if i == 'EXIT': exit()
    return i

def list_files():
    files.clear()
    keys.clear()
    contents = repo.get_contents("")
    while contents:
        file_content = contents.pop(0)
        if file_content.type != "dir" and file_content.path[-4:] == ".mli":
            f = GitFile(repo, file_content.path)
            files.append(f)
            keys.extend(f.keys)
    print('library is loaded successfully!')



def candinate_files_list():
    global keys
    candinateFiles = []
    for file in files:
        flag = True
        for key in searchKeys:
            if key not in file.keys:
                flag = False
                break
        if flag: candinateFiles.append(file)
    return candinateFiles

def show_files_list(candinateFiles):
    for i in range(0, len(candinateFiles)):
        print(str(1+i)+') ',candinateFiles[i].path)

def search():
    searchKeys.clear()
    list_files()
    global keys
    # entering keywords
    print('ENTER KEYWORDS AND END ENTERING WITH \'EOF\' OR TYPE \'SHOW\' TO DISPLAY FILES AND CONTINUE ENTERING:')
    searchInput = ''
    while True:
        searchInput = exitable_input()
        if searchInput == 'EOF':
            break
        elif searchInput == 'SHOW':
            show_files_list(candinate_files_list())
            continue
        elif searchInput not in keys:
            print('THE KEY YOU HAVE ENTERED IS NOT VALID...')
            continue
        searchKeys.append(searchInput)
    
    # search in files[]
    print('------------------')
    candinateFiles = candinate_files_list()
    l = len(candinateFiles)
    show_files_list(candinateFiles)
    print('------------------')

    # show contents
    print('CHOOSE FILE NUMBER:')
    while True:
        index = int(exitable_input()) - 1
        if index >= 0 and index < l:
            break
        print('Please enter a valid index')

    print('========================')
    print('========================')
    print(candinateFiles[index].path)
    print('------------------------')
    print('FAMILY:', candinateFiles[index].family)
    print('------------------------')
    print(candinateFiles[index].code)
    print('------------------------')
    for ip in candinateFiles[index].inputs:
        print('-', ip)
    print('------------------------')
    print('RETURN TYPE:', candinateFiles[index].returnValue)
    print('------------------------')
    print(candinateFiles[index].description)
    print('------------------------')
    print(', '.join(candinateFiles[index].keys))
    print('------------------------')
    print('CREATION TIME:', candinateFiles[index].date or '', '          LAST EDIT:', candinateFiles[index].lastEdit)
    print('========================')
    print('========================')
    print('ENTER ONE OF THE FOLLOWING COMMANDS:\nSEARCH\nEDIT\nDELETE\nCOPY')
    
    while True:
        command = exitable_input()
        if command == 'SEARCH':
            search()
            break
        elif command == 'DELETE':
            print('ARE YOU SURE YOU WANT TO DELETE', candinateFiles[index].path, '?', '[Y/n]')
            if exitable_input() == 'Y':
                candinateFiles[index].delete()
                if candinateFiles[index].status: print(candinateFiles[index].path, 'WAS DELETED SUCCESSFULLY')
                else: print('ERROR:', candinateFiles[index].message)
                break
        elif command == 'COPY':
            root = Tk()
            root.withdraw()
            root.clipboard_clear()
            root.clipboard_append(candinateFiles[index].code)
            root.update()
            print('CODE IS COPPIED SUCCESSFILLY')
            break
        elif command == 'EDIT':
            print('========================')
            print('USE \'NO\' TO UNCHANGE A PROPERITY:')
            print('EDIT FAMILY ?')
            i = exitable_input()
            if i != 'NO': candinateFiles[index].family = i
            print('========================')
            print('EDIT CODE ?')
            i = exitable_input()
            if i != 'NO': candinateFiles[index].code = i
            print('========================')
            print('EDIT INPUTS ? [USE \'EOF\' TO END ADDING INPUTS]')
            inputs = []
            while True:
                i = exitable_input()
                if i == 'NO': break
                if i == 'EOF':
                    candinateFiles[index].inputs = inputs = i
                    break
                inputs.append(i)
            print('========================')
            print('EDIT RETURN TYPE ?')
            i = exitable_input()
            if i != 'NO': candinateFiles[index].returnValue = i
            print('========================')
            print('EDIT DESCRIPTION ?')
            i = exitable_input()
            if i != 'NO': candinateFiles[index].description = i
            print('========================')
            print('EDIT KEYS ? [USE \'EOF\' TO END ADDING INPUTS]')
            fileKeys = []
            while True:
                i = exitable_input()
                if i == 'NO': break
                if i == 'EOF':
                    candinateFiles[index].keys = keys
                    break
                fileKeys.append(i)
            print('========================')
            print('ARE YOU SURE YOU WANT TO COMMIT CHANGES ? [Y/n]')
            if exitable_input() == 'Y': 
                candinateFiles[index].edit()
                print('FILE IS EDITED SUCCESSFULLY')
                break

def appendLib():
    file = GitFile(repo)
    print('========================')
    print('USE \'CANCEL\' TO CANCEL APPENDING:')
    print('ENTER FILE NAME :')
    file.path = exitable_input() + '.mli'
    print('========================')
    print('ENTER FAMILY :')
    file.family = exitable_input()
    print('========================')
    print('ENTER CODE :')
    file.code = exitable_input()
    print('========================')
    print('ENTER INPUTS [USE \'EOF\' TO END ADDING INPUTS]:')
    inputs = []
    while True:
        i = exitable_input()
        if i == 'EOF':
            file.inputs = inputs
            break
        inputs.append(i)
    print('========================')
    print('ENTER RETURN TYPE :')
    file.returnValue = exitable_input()
    print('========================')
    print('ENTER DESCRIPTION :')
    file.description = exitable_input()
    print('========================')
    print('ENTER KEYS [USE \'EOF\' TO END ADDING INPUTS]:')
    fileKeys = []
    while True:
        i = exitable_input()
        if i == 'EOF':
            file.keys = fileKeys
            break
        fileKeys.append(i)
    print('========================')
    print('ARE YOU SURE YOU WANT TO APPEND FILES ? [Y/n]')
    if exitable_input() == 'Y':
        file.add()
        if file.status: print('FILE IS APPENDED SUCCESSFULLY')
        else: print(file.message)

print('WELCOME TO MyLIB APP BY M.MAHER')
while True:
    print('========================')
    print('SELECT OPTION:\n1) search in library\n2) append to library')
    option = exitable_input()
    if option == '1':
        search()
    elif option == '2':
        appendLib()