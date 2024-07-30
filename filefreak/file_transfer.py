import shutil

def transfer_file(src, dst):
    shutil.copy2(src, dst)

def transfer_files(src_dir, dst_dir):
    for file in src_dir:
        shutil.copy2(file, dst_dir)