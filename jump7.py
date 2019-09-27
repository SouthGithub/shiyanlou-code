num = 0     # loop variable

while num < 100:        # loop: 1-100
    num += 1            # num increase one
    if num % 7 == 0:    # number is multiple 7 next skip a cycle
        continue
    # num % 10 == 7 bit is 7, num // 10 ==7 ten palce is 7
    elif num % 10 == 7 or num // 10 == 7:
        continue        # skip a cycle
    print(num)          # print number

