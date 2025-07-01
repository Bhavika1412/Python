def read_file(filename):
    try:
        with open(filename, 'r') as file:
            print("File contents:\n")
            for line in file:
                print(line, end='')
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")


read_file("sample.txt")
