filename = 'garage.txt'

try:
    with open(filename) as file_obj:
        contents = file_obj.read()
        print(contents)
except FileNotFoundError:
    print("Sorry, the file " + filename + " does not exist.")    