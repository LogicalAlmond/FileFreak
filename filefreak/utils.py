import os

def fetch_files(directory):
    fp = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            fp.append(file_path)
    return fp