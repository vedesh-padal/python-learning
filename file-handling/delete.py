import os
# import shutil
path = "moving"
# os.remove(path)         # delete a file
# os.rmdir(path)          # delete an empty directory
# shutil.rmtree(path)        # delete a directory containing files (dangerous)

try:
    os.remove(path)
    # os.rmdir(path)
except IsADirectoryError:
    print("that is not a directory")
except FileNotFoundError:
    print("File was not found!")
except PermissionError:
    print("you do not have permission to delete that")
except OSError:
    print("you cannot delete that using that function") # when the folder to be deleted is not empty
else:
    print("path was deleted")
