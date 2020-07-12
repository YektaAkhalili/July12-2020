filename = "pi_digits.txt"

with open(filename) as file_object:
    #put things in a line, so you can work with it outside the 
    #"with" block
    #otherwise you can't
    contents_list = file_object.readlines()

for line in contents_list:
    print(line.rstrip())