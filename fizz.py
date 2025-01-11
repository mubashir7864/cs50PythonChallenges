

def fizz(n):
    for i in range(1,n+1):
        if i%3 == 0:
            print("buzz")
        elif i%5 ==0:
            print("fizz")
        else:
            print(i)
    print()


fizz(10)