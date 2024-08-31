#encrypt , decrypt
out_put = ""
out_put2 = ""
while True:
    print("your option:\n\t1)encrypt\n\t2)decrypt\n\t3)exit")
    user_choise = int(input("choose on: "))
    if user_choise == 1:
        text = input("enter your text: ")
        for i in text:
            z = ord(i)+11
            out_put += chr(z)
        print(f"out put = \n{out_put}")
    elif user_choise == 2:
        way = int(input("we have to way for decrypt,which one? "))
        text = input("enter yor text: ")
        if way == 1:
            for i in text:
                z = ord(i)*2
                out_put2 += chr(z)
            print(f"your text = {out_put2}")
        elif way == 2:
            for i in text:
                z = ord(i)-11
                out_put2 += chr(z)
            print(f"your text = {out_put2}")
    elif user_choise == 3:
        print("good bye!")
        break