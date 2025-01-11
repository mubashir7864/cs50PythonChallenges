def intInput():

    x= int(input("what is num: "))
    print(f"{x}")


def recur(fun):
    try:
        fun
    except ValueError:
        print("invalid entry....reenter")
        fun



recur(intInput)