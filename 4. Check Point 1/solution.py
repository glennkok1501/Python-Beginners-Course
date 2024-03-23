num = input("Enter number: ")

# write your solution below
error = False

if num[0] == "-" and len(num) > 2:
    if not num[1:].isdigit():
        error = True
elif not num.isdigit():
    error = True

if error == True:
    print("Error")
    exit()

num = int(num)

if num > 0:
    if num % 2 == 0:
        print("Positive Even")
    else:
        print("Positive Odd")
elif num < 0:
    print("Negative")
else:
    print("Zero")
