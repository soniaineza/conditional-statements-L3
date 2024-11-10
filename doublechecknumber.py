number = int(input("enter any number "))
print(number)

if number >50:
    print("number is greater than 50")
    if number % 2 ==0:
        print("number is an even ")
    else:
        print("number is an odd ")
else:
    print("number is less than 50")