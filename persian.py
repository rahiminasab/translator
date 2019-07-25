import sys

def readfile(path):
    with open(path) as f:
        return f.readlines()

if __name__ == '__main__':

    file_path = sys.argv[1]
    lines = readfile(file_path)
    print(lines)
