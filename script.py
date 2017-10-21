import os, time

DAYS = 5    #Maximal age of file stay
FOLDERS = [
    "/home/../../..",
    "/home/../../..",
    "/home/../../.."
]

TOTAL_DELETED_SIZE = 0 #Total deleted size of all files in BYTES
TOTAL_DELETED_FILE = 0 #Total deleted files
TOTAL_DELETED_DIRS = 0 #Total deleted empty folders

nowTime = time.time()                       # Get current time in SECONDS
ageTime = nowTime - 60*60*24*DAYS           # Minus Days in sedonds

def delete_old_files(folder):
    """Delete files older than X Days"""
    global TOTAL_DELETED_FILE
    global TOTAL_DELETED_SIZE
    for path, dirs, files in os.walk(folder):
        for file in files:
            fileName = os.path.join(path, file)
            fileTime = os.path.getmtime(fileName)
            if fileTime < ageTime:
                sizeFile = os.path.getsize(fileName)
                TOTAL_DELETED_SIZE += sizeFile       # Count deleted free space
                TOTAL_DELETED_FILE += 1              # Count deleted files
                print("Deleted file: " + str(fileName))
                os.remove(fileName)

def delete_empty_dir(folder):
    global TOTAL_DELETED_DIRS
    for path, dirs, files in os.walk(folder):
        if(not dirs) and (not files):
            TOTAL_DELETED_DIRS += 1
            print("Deleted Empty Dir: " + str(path))
            os.rmdir(path)

#=====================MAIN=============================

starttime = time.asctime()

for folder in FOLDERS:
    delete_old_files(folder) #Delet old file
    delete_empty_dir(folder) #Delet empty folders

finishtime = time.asctime()

print("==================================================")
print("START TIME: "                    + str(starttime))
print("TOTAL DELETED SIZE: "            + str(TOTAL_DELETED_SIZE/1024/1024) + "Mb")
print("TOTAL DELETED FILES: "           + str(TOTAL_DELETED_FILE))
print("TOTAL DELETED EMPTY FOLDERS: "   + str(TOTAL_DELETED_DIRS))
print("FINISH TIME: "                   + str(finishtime))
print("=======================END========================")
