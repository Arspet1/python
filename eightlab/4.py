import shutil


shutil.copy("data.txt", "backup_data.txt")

with open("backup_data.txt", "r") as f:
    print(f.read())