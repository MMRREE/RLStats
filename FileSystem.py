import re
import os
import sys
import json

RE_FILE = re.compile('\\w+\.\w+')


def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        directory = os.path.join(sys._MEIPASS, relative_path)
    else:
        directory = os.path.join(os.path.abspath("."), relative_path)
    return directory
# End of resource_path


def local_storage_path(relative_path):
    directory = os.path.join(os.path.abspath("."), relative_path)
    return directory
# End of local_storage_path


def checkFolderOrFileExists(path):
    path = path.replace("/", "\\")
    lastWord = path.split("\\")[-1]
    file = RE_FILE.search(path)
    if(file is not None):
        return os.path.isfile(path)
    else:
        return os.path.isdir(path)
# End of checkFolderOrFileExists


def checkExistsOrCreate(path):
    path = path.replace("/", "\\")
    file = RE_FILE.search(path.split('\\')[-1])
    if(not checkFolderOrFileExists(path)):
        # If does not exist check parent folder, if that does exist then create this folder
        newPath = "\\".join(path.split("\\")[0:-1])
        if(checkFolderOrFileExists(newPath)):
            # If parent does exist
            os.chmod(newPath, 0o777)
            if(file is not None):
                fileObj = open(path, 'w+')
                fileObj.close()
            else:
                os.makedirs(path)
        else:
            # Parent does not exist
            checkExistsOrCreate(newPath)
            checkExistsOrCreate(path)
    else:
        print("Folder or file already exists")
# End of checkExistsOrCreate


def loadJson(path):
    path = path.replace("/", "\\")
    if(not checkFolderOrFileExists(path)):
        checkExistsOrCreate(local_storage_path(path))
        file = open(path, 'w+')
        json.dump({}, file, indent=4, default=str)
        file.close()
        return {}
    else:
        file = open(path, 'r+')
        fileData = file.read()
        fileJson = json.loads(fileData)
        return fileJson
# End of loadJson


def writeJson(path, data):
    path = path.replace("/", "\\")
    checkExistsOrCreate(local_storage_path(path))
    file = open(path, 'w+')
    json.dump(data, file, indent=4, default=str)
    file.close()
    return data
# End of writeJson
