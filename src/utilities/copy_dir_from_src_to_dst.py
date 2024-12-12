import os
import shutil
from pathlib import Path

def copy_directory_from_src_to_dest(src, dst):
    try:
        src_path = Path(src)
        if not src_path.is_absolute():
            src_path = os.path.abspath(src)

        dest_path = Path(dst)
        if not dest_path.is_absolute():
            dest_path = os.path.abspath(dst)
        

        if os.path.exists(dest_path):
            shutil.rmtree(dest_path)
        os.mkdir(dest_path)

        if os.path.commonpath([src_path, dest_path]) == src_path:
            raise ValueError("Destination directory cannot be within the source directory to avoid recursion.")

        for entry in os.listdir(src_path):
            entry_path = os.path.join(src_path, entry)
            if os.path.isfile(entry_path) or os.path.islink(entry_path):
                shutil.copy(entry_path, dest_path)
            elif os.path.isdir(entry_path):
                copy_directory_from_src_to_dest(entry_path, os.path.join(dest_path, entry))
            else:
                raise ValueError("Target is not a file, link or directory")

    except OSError as e:
        print(e)
        raise OSError(e)
