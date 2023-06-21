import hashlib
import os
import platform
from datetime import datetime
import json

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
    for dirpath, dirnames, filenames in os.walk('/'):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            try:
                file_hash = calculate_hash(filepath)
                if file_hash in signatures:
                    matches.append(filepath)
            except PermissionError:
                pass
    return matches

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
    matches = scan_system_for_files_with_signatures(signatures)
    system_details = get_system_details()

    current_time = datetime.now().strftime('%Y-%m-%d %I:%M:%S %p')

    report = {
        'time': current_time,
        'system_details': system_details,
        'matches': matches,
    }
    
    with open('BlackCat_Scan_Results.txt', 'w') as outfile:
        outfile.write(json.dumps(report, indent=4))

if __name__ == '__main__':
    main()
