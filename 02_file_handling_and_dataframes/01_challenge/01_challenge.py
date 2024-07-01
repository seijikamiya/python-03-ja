import os
import json
import shutil
from pathlib import Path

book_dict = {}
target_path = "data/text_files/"

for file in os.listdir(target_path):
    if "Chapter" not in file:
        if  ".txt" in file:
            with open(target_path+file, "r") as f:
                book_dict[file] = f.read()

with open(target_path+"book.json", "w") as f:
    json.dump(book_dict, f, indent=2)

os.mkdir(target_path+"library")
for file in os.listdir(target_path):
    if "Chapter" in file:
        if  ".txt" in file:
            shutil.copyfile(target_path+file, target_path+"library/"+file)

p = Path(target_path+"library")
for path in p.iterdir():
    size = path.stat().st_size
    print(path, f'{size}bytes')