import os
import re

for path, subdirs, files in os.walk(os.curdir):
    for name in files:
        new_filename = re.sub(
            r"(\d+)", lambda m: m.group(1).zfill(3),
            name
        )
        old_file_path = os.path.join(path, name)
        new_file_path = os.path.join(path, new_filename)
        print(old_file_path, new_file_path, '\n')
        os.rename(old_file_path, new_file_path)

for path, subdirs, files in os.walk(os.curdir):
    for name in subdirs:
        new_filename = re.sub(
            r"(\d+)", lambda m: m.group(1).zfill(3),
            name
        )
        old_file_path = os.path.join(path, name)
        new_file_path = os.path.join(path, new_filename)
        print(old_file_path, new_file_path, '\n')
        os.rename(old_file_path, new_file_path)

for path, subdirs, files in os.walk(os.curdir):
    for name in files:
        new_filename = re.sub(
            r"(\d+)$", "4",
            name
        )
        old_file_path = os.path.join(path, name)
        new_file_path = os.path.join(path, new_filename)
        print(old_file_path, new_file_path, '\n')
        os.rename(old_file_path, new_file_path)
