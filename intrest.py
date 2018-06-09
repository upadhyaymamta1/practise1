def intrest(p,r,t):
    if p<1000:
        print('principal is low')
    if r>10:
        print('rate is  too high')
    if t>5:
        print('time is too much')
    if p>=1000 and r<=10 and t<=5:
        i = p*r*t/100
        print("intrest =" + str(i))
        print("amount =" + str(i+p))


def intrest_elif(p,r,t):
    if p<1000:
        print('principal is low')
    elif r>10:
        print('rate is  too high')
    elif t>5:
        print('time is too much')
    else:
        i = p*r*t/100
        print("intrest =" + str(i))
        print("amount =" + str(i+p))