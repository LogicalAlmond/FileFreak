import hashlib

def generate_hash(file_path, output_file, algorithm='sha1'):
    hash_func = hashlib.new(algorithm)
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            hash_func.update(chunk)
        with open(output_file, 'a') as f:
            f.write(hash_func.hexdigest() + "\n")

def generate_hashes(file_paths, algorithm='sha1'):
    return({file_path: generate_hash(file_path, algorithm) for file_path in file_paths})
