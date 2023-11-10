import os
import os.path
import random #for helper function
import base64 as bs #for helper function
import hashlib

class Directory():
    def __init__(self, path) -> None:
        self.path = path
        
        






def generate_random_files(path) -> None:
    """ DEBUG Generate random binary files (helper function)

    Args:
        path (path): working directory
    """
    count = 5
    maxsize = 100
    try: # create test-data
        os.mkdir(os.path.join(path, "testfiles"))
        print(os.path.join(path, "testfiles"))
    except FileExistsError:
        print("Directory exists.")
    else: # Create testdata and subdirectory
        for i in range(count):
            with open(f"{os.path.join(path, 'testfiles', 'random')}_{i}", 'wb') as f:
                f.write(bs.b64encode(os.urandom(random.randint(1, maxsize))))
            print(f"{os.path.join(path, 'testfiles', 'random')}_{i}") 
        os.mkdir(os.path.join(path, "testfiles", "subdir1"))
        for i in range(count):
            with open(f'{os.path.join(path, "testfiles", "subdir1", "random")}_{i}', 'wb') as f:
                f.write(bs.b64encode(os.urandom(random.randint(1, maxsize))))
            print(f'{os.path.join(path, "testfiles", "subdir1", "random")}_{i}')
    finally:
        print("Test-Data created.")    


def shasum(file) -> str:
    with open(file, "rb") as f:
        checksum = hashlib.file_digest(f, "sha256").hexdigest()
    return checksum

    
def compare_file(directory, file, hashvalue) -> str:
    if shasum(os.path.join(directory,file)) == hashvalue:
        return "OK"
    else:
        return "MISMATCH"
    
def list_files(path) -> list:
    """returns directories filelist

    Args:
        directory (FileDescriptorOrPath): Working directory

    Returns:
        list (list): list of files in working directory excluding directories
    """
    return sorted([element.name for element in os.scandir(path) if element.is_file()])


def list_directories(path, recursive: bool) -> list:
    if recursive:
        directories = [os.path.join(root, d) for root, dirs, files in os.walk(path) for d in dirs]
        directories.append(path)
    else:
        directories = [path]
    return sorted(directories)


def read_checksumfile(path, checksumfile) -> dict:
    try:
        with open(os.path.join(path, checksumfile), "r") as f:
            # for line in f:       replaced by nestedt list/dictionary comprehension             
            #     value, key = line.split("  ", maxsplit=1)
            #     shasums[key.strip()] = value.strip()
            return {value.strip(): key.strip() for key, value in [line.split("  ", maxsplit=1) for line in f]}
    except FileNotFoundError:
        return {}
    

def create_chksumfiles(path, checksumfile, recursive: bool) -> None:
    
    directories = list_directories(path, recursive)
    for directory in directories:
        print(directory)
        if len(os.listdir(directory)) == 0:
            print("Empty")
            continue
        if not os.path.isfile(os.path.join(directory, checksumfile)):
            with open(os.path.join(directory, checksumfile), "x") as f:
                for filename in list_files(directory):
                    if filename == checksumfile: # Do not process checksumfile itself
                        continue
                    print(f"{shasum(os.path.join(directory, filename))}  {filename}")
                    f.write(f"{shasum(os.path.join(directory, filename))}  {filename}\n")
        else:
            shasums = read_checksumfile(directory, checksumfile)
            for filename in list_files(directory):
                if filename == checksumfile: # Do not process checksumfile itself
                    continue
                elif filename in shasums:
                    print(filename, compare_file(directory, filename, shasums[filename]))
                else:
                    shasums[filename] = shasum(os.path.join(directory, filename))
                    print(f"{shasums[filename]}  {filename}")
            with open(os.path.join(directory, checksumfile), "w") as f:
                for key, value in sorted(shasums.items()):
                    f.write(f"{value}  {key}\n")

      
def sha_checkfile(path, checksumfile, recursive: bool) -> None:
    mismatch = []
    for directory in list_directories(path, recursive):
        # Get shasums from checksum file and create dictionary (reverse order!)
        print(directory)  
        try:
            # compare against computed values
            for i in read_checksumfile(directory, checksumfile): #!!!!!!! LOGIC!!!
                print(shasums[i], i, shasums[i] == shasum(os.path.join(directory, i)))
        except FileNotFoundError:
            print(f"No such file: {os.path.join(directory, checksumfile)}")
    
def test(path):
    directories = list_directories(path, False)
    #print(directories)
    for directory in directories:
        print([file for file in os.listdir(directory) if os.path.isfile(os.path.join(directory,file))])
        