def computepay(h,r):
    if(h > 40):
        return (h - 40) * rate * 1.5 + 40 * rate
    else:
        return h * rate

hrs = input("Enter Hours:")

hrs = int(hrs)

rate = input('Enter rate ')

rate = float(rate)

p = computepay(hrs, rate)

print("Pay",p)
