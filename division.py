print("Give me two numbers to divide:")
print("Push 'q' to quit. ")

while True:
    num1 = input("\nFirst Number: ")
    if num1 == 'q':
        break
    num2 = input("\nSecond Number: ")
    if num2 == 'q':
        break 
    try:
        div = int(num1) / int(num2)
        print("Result is: " + str(div))
    except ZeroDivisionError:
        print("Second number can't be zero.")    