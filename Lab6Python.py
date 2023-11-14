import sys
import os

#1 
"""Create a Python script that does the following:
Takes a directory path and a file extension as command line arguments (use sys.argv).
Searches for all files with the given extension in the specified directory (use os module).
For each file found, read its contents and print them.
Implement exception handling for invalid directory paths, incorrect file extensions, and file access errors."""



def print_file_contents(directory, extension):
    try:
        # List all files in the directory
        for filename in os.listdir(directory):
            if filename.endswith(extension):
                filepath = os.path.join(directory, filename)
                try:
                    with open(filepath, 'r') as file:
                        print(file.read())
                except Exception as e:
                    print(f"Error reading file {filename}: {e}")
    except FileNotFoundError:
        print("Directory not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
#2

"""Write a script using the os module that renames all files in a specified directory to have a sequential number prefix.
For example, file1.txt, file2.txt, etc. Include error handling for cases like the directory not existing or files that can't be renamed."""
    
def rename_files(directory):
    try:
        files = os.listdir(directory)
        for i, filename in enumerate(files):
            new_name = f"{i+1}_{filename}"
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))
    except FileNotFoundError:
        print("Directory not found.")
    except PermissionError:
        print("Permission denied.")
    except Exception as e:
        print(f"An error occurred: {e}")

#3
"""
Create a Python script that calculates the total size of all files in a directory provided as a command line argument. The script should:
Use the sys module to read the directory path from the command line.
Utilize the os module to iterate through all the files in the given directory and its subdirectories.
Sum up the sizes of all files and display the total size in bytes.
Implement exception handling for cases like the directory not existing, permission errors, or other file access issues.
"""
def calculate_total_size(directory):
    total_size = 0
    try:
        for root, dirs, files in os.walk(directory):
            for file in files:
                total_size += os.path.getsize(os.path.join(root, file))
        print(f"Total size: {total_size} bytes")
    except FileNotFoundError:
        print("Directory not found.")
    except PermissionError:
        print("Permission denied.")
    except Exception as e:
        print(f"An error occurred: {e}")

#4
"""
Write a Python script that counts the number of files with each extension in a given directory. The script should:
Accept a directory path as a command line argument (using sys.argv).
Use the os module to list all files in the directory.
Count the number of files for each extension (e.g., .txt, .py, .jpg) and print out the counts.
Include error handling for scenarios such as the directory not being found, no read permissions, or the directory being empty.
"""
def count_file_extensions(directory):
    extension_count = {}
    try:
        for filename in os.listdir(directory):
            if os.path.isfile(os.path.join(directory, filename)):
                ext = os.path.splitext(filename)[1]
                extension_count[ext] = extension_count.get(ext, 0) + 1
        for ext, count in extension_count.items():
            print(f"{ext}: {count}")
    except FileNotFoundError:
        print("Directory not found.")
    except PermissionError:
        print("Permission denied.")
    except Exception as e:
        print(f"An error occurred: {e}")
