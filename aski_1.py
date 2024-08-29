again = "y"
while again == "y":
    char = input("chr : ")
    key = ord(char) * 2 +5
    encrypt = chr(key)
    print(encrypt) 
    again = input("y/n: ")