import os

def create_file(file_name):
    try:
        with open(file_name, 'x') as f:
            pass
        print("File created successfully!")
    except FileExistsError:
        print("File already exists.")

def write_to_file(file_name, data):
    with open(file_name, 'w') as f:
        f.write(data)
    print("Data written successfully!")

def read_from_file(file_name):
    if os.path.exists(file_name):
        with open(file_name, 'r') as f:
            content = f.read()
        print("File Content:\n" + content)
    else:
        print("File does not exist.")

def append_to_file(file_name, data):
    with open(file_name, 'a') as f:
        f.write("\n" + data)
    print("Data appended successfully!")
