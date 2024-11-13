import os
import sys
import math

def split_file(file_path):
    if not os.path.isfile(file_path):
        print(f"Error: File '{file_path}' not found")
        return

    chunk_size = 20 * 1024 * 1024  # 20 MB
    file_name = os.path.basename(file_path)
    folder_name = os.path.splitext(file_name)[0]
    os.makedirs(folder_name, exist_ok=True)

    total_size = os.path.getsize(file_path)
    total_chunks = math.ceil(total_size / chunk_size)

    with open(file_path, 'rb') as file:
        chunk_number = 0
        print(f"Splitting file '{file_name}' into chunks...")
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break
            with open(os.path.join(folder_name, f"{file_name}_part{chunk_number}"), 'wb') as chunk_file:
                chunk_file.write(chunk)
            chunk_number += 1
            progress = (chunk_number / total_chunks) * 100
            print(f"Progress: {progress:.2f}% ({chunk_number}/{total_chunks} chunks)", end='\r')

    print(f"\nFile successfully split into {chunk_number} parts in folder '{folder_name}'")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 splitfile.py <filename>")
    else:
        file_path = sys.argv[1]
        split_file(file_path)
