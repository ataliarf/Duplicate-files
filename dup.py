
import os, sys, hashlib

#maps size of file to file path
def mapBySizes(mainFolder):
    mapOfSizes = {}
    for root, dirs, files in os.walk(mainFolder):
        for file in files:
            path = os.path.join(root, file)
            size= os.stat(path).st_size
            if size in mapOfSizes:
                mapOfSizes[size].append(path)
            else:
                mapOfSizes[size] = [path]
    return mapOfSizes

#maps hash of file to file path
def mapByDupes(mapOfSizes):
    dupesMap = {}
    listsOfFiles = mapOfSizes.values()
    for list in listsOfFiles:
        if len(list) > 1:
            for f in list:
                file_hash = fileHash(f)
                if file_hash in dupesMap:
                    dupesMap[file_hash].append(f)
                else:
                    dupesMap[file_hash] = [f]
    return dupesMap

def fileHash(path):
    with open(path, 'rb') as f:
        bytes = f.read()
        hash = hashlib.md5(bytes).hexdigest()
        f.close()
    return hash 

def printDuplicateFiles(dupesMap):
    found = 0
    values = dupesMap.values()
    for listOfFiles in values:
        if len(listOfFiles) > 1:
            found = 1
            print('* duplicate files: \n'),
            print('\n'.join(listOfFiles))     
    if found==0:               
        print('no duplicate files.')
 
if __name__ == '__main__':
    argumentsNum = len(sys.argv)
    if argumentsNum > 1:
        sizes = {}
        arg = sys.argv[1:]
        path = arg[0]
        if os.path.exists(path)== False : 
            print('input is not a valid path')
            sys.exit()
        else:
            sizes = mapBySizes(path)
            duplicates = mapByDupes(sizes)
            printDuplicateFiles(duplicates)
    else:
        print('please insert path')