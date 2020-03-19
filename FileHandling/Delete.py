# Deleting a File
import os
filePath = "C:/Users/inasahu/PycharmProjects/DemoText_create.txt"
if os.path.exists(filePath):
    os.remove(filePath)
else:
    print("The File does not exists")


# Delete a Folder
os.rmdir("C:/Users/inasahu/PycharmProjects/deleteThisFolder")
