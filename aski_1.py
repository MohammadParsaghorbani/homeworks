again = "y"
while again == "y":
    result = ""
    char = input("chr : ")
    for i in char:
        z = ord(i)*2+5
        result += chr(z)
    print(result) 
    again = input("y/n: ")