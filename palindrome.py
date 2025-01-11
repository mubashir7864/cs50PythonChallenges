


def palindrome(kki):
    kki = kki.lower().strip().replace(",","").replace(" ","")
    leng=len(kki)
    newstr =""
    for i in range(leng-1,-1,-1):
        newstr += kki[i]
    if kki == newstr:
        print("its a palindrome")
    else:
        print("its not a palindrome")

    return newstr


print(palindrome("A man, a plan, a canal, Panama"))



