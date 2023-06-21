import hashlib
import os
import platform
from datetime import datetime
import json
import itertools
import time
import sys

def calculate_hash(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def read_signatures(file_path):
    with open(file_path, 'r') as file:
        signatures = file.read().splitlines()
    return signatures

def scan_system_for_files_with_signatures(signatures):
    matches = []
    inaccessible_files = []
    spinner = itertools.cycle(['-', '/', '|', '\\'])
    print("Scanning system. This may take a while, please be patient...\n")
    for dirpath, dirnames, filenames in os.walk('/'):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            if os.path.islink(filepath):
                try:
                    filepath = os.readlink(filepath)
                except OSError:
                    inaccessible_files.append(filepath)
                    continue
            try:
                sys.stdout.write(next(spinner))  # write the next character
                sys.stdout.flush()               # flush stdout buffer (actual character display)
                sys.stdout.write('\b')           # erase the last written character
                file_hash = calculate_hash(filepath)
                if file_hash in signatures:
                    matches.append({"signature": file_hash, "file_path": filepath})
            except PermissionError:
                inaccessible_files.append(filepath)
            except OSError:
                inaccessible_files.append(filepath)
    return matches, inaccessible_files

def get_system_details():
    details = {
        'system': platform.system(),
        'node': platform.node(),
        'release': platform.release(),
        'version': platform.version(),
        'machine': platform.machine(),
        'processor': platform.processor(),
    }
    return details

def main():
    signatures = read_signatures('signatures.txt')
    matches, inaccessible_files = scan_system_for_files_with_signatures(signatures)
    system_details = get_system_details()

    current_time = datetime.now().strftime('%Y-%m-%d %I:%M:%S %p')

    report = {
        'time': current_time,
        'system_details': system_details,
        'matches': matches,
        'inaccessible_files': inaccessible_files
    }
    
    with open('BlackCat_Scan_Results.txt', 'w') as outfile:
        outfile.write(json.dumps(report, indent=4))
    print("\nScan complete. Results written to BlackCat_Scan_Results.txt")

if __name__ == '__main__':
    main()
