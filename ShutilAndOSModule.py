import os
import shutil
import send2trash

# Clears console
os.system('cls')

# Prints current working directory
print(os.getcwd())
print()

# Prints the list of items in the directory
print(os.listdir())
print()

# Moves a file from source to destination
# shutil.move('D:\\My_Project\\NewFile.txt', os.getcwd())
# print(os.listdir())

# Deleting a file to trash bin
# send2trash.send2trash('NewFile.txt')
# print(os.listdir())

for folder , sub_folders , files in os.walk("Example_Top_Level"):
    
    print("Currently looking at folder: "+ folder)
    print('\n')
    print("THE SUBFOLDERS ARE: ")
    for sub_fold in sub_folders:
        print("\t Subfolder: "+sub_fold )
    
    print('\n')
    
    print("THE FILES ARE: ")
    for f in files:
        print("\t File: "+f)
    print('\n')