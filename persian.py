
import sys


def readfile(path):
    with open (path) as f:
        return f.readlines()

def translate(lines):
    #TODO: implement the translation
    return lines

if __name__ == "__main__":
    file_path = sys.argv[1]
    lines = readfile(file_path)
    translated_lines = translate(lines)
    print(lines)
