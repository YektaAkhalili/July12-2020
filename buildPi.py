with open("pi_digits.txt") as file_object: 
    lines = file_object.readlines()

pi_str = ''

for line in lines: 
    pi_str += line.rstrip()

print("Pi to the " + str(len(pi_str)) + "th digit:")
print(pi_str)