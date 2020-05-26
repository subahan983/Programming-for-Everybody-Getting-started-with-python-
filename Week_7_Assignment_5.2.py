smallest = None
largest = None
small = 3434
large = 0

while True:
    num = input("Enter a number: ")
    if num == "done" : break
    try:
        num = int(num)
        if(small > num):
            smallest = num
            small = num
        if(large < num):
            largest = num
            large = num
    except:
        print('Invalid input')

print("Maximum is",largest)
print('Minimum is',smallest)
