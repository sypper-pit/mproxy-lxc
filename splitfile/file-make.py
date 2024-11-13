import os
import sys
import shutil

def assemble_file(folder_path):
    if not os.path.isdir(folder_path):
        print(f"Error: Directory '{folder_path}' not found")
        return

    print(f"Contents of '{folder_path}':")
    for item in os.listdir(folder_path):
        print(f"  {item}")

    parts = sorted([f for f in os.listdir(folder_path) if '_part' in f])
    if not parts:
        print("Error: No file parts found in the specified directory")
        return

    print(f"Found {len(parts)} file parts:")
    for part in parts:
        print(f"  {part}")

    output_file_name = parts[0].split('_part')[0]
    output_path = os.path.join(folder_path, output_file_name)

    total_parts = len(parts)

    with open(output_path, 'wb') as output_file:
        print(f"Assembling file from parts...")
        for i, part in enumerate(parts, 1):
            part_path = os.path.join(folder_path, part)
            with open(part_path, 'rb') as part_file:
                output_file.write(part_file.read())
            progress = (i / total_parts) * 100
            print(f"Progress: {progress:.2f}% ({i}/{total_parts} parts)", end='\r')

    print(f"\nFile successfully assembled: '{output_path}'")

    # Move file to parent directory
    parent_dir = os.path.dirname(folder_path)
    new_file_path = os.path.join(parent_dir, output_file_name)
    print(f"Moving file to parent directory...")
    shutil.move(output_path, new_file_path)
    print(f"File moved to: '{new_file_path}'")

    # Delete all parts and the folder
    print("Cleaning up...")
    for part in parts:
        part_path = os.path.join(folder_path, part)
        os.remove(part_path)
        print(f"Deleted: {part_path}")

    os.rmdir(folder_path)
    print(f"Deleted folder: {folder_path}")
    print("Cleanup complete. Only the assembled file remains in the parent directory.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 file-make.py <dir>")
    else:
        folder_path = sys.argv[1]
        assemble_file(folder_path)
