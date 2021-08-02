import sys

def read_paths():
    print("Reading paths available for Python to read from..")
    py_paths = sys.path

    for ndex, path in enumerate(py_paths, 1):
        print(f"{ndex} -> {path}")

#the import is redundant but this is only an example
#enumerate(py_paths, 1)
#py_paths = a list
#1 = starts the number value to 1 instead of 0 from default list
#BUT, it will still read all the contents of the list as is, no loss