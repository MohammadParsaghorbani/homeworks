import random as rnd
import datetime as dt

today = dt.datetime.now()

name = input("enter your name here: ")
last_name = input("enter your last name please: ")

with open(f'{name} {last_name}_result.txt' , "a") as file:
    file.write(f"today = {today.year}/{today.month}/{today.day} - {today.time()}\nname = {name}\nlast name = {last_name}\n")

while True:
    score = 0
    quastions = {
        "a = (1,2,3)\nprint(list(a))\n1)[1,2,3]\t2)(1,2,3)\n3)1,2,3 \t4)error" : 1,
        "which one is not str?\n1)'1'\t\t2)str('2')\n3)ord('a') \t4)chr(90)".format(name) :  3,
        "we use ____ for remove item from list:\n1)remove\t2)pop\n3)delete \t4)1 and 2" : 4,
        "we use ___ to make arrey:\n1)list \t\t2)numpy\n3)tuple \t4)set" : 2
    }
    for i in range(4):
        res = ""
        z = list(quastions.keys())
        x = rnd.choice(z)
        for i in x:
            if i == "[":
                i.replace("[","")
            elif i == "]":
                i.replace("]","")
            res += i
        with open(f'{name} {last_name}_result.txt' , "a") as file:
            file.write(f"***********************\n{res}\n\n")
        q = int(input(f"***********************\n{res}\n***********************\nyour answer = "))
        with open(f'{name} {last_name}_result.txt' , "a") as file:
            file.write(f"answer = {q}\ncorrect answer = {quastions[x]} ")
        file = open(f'{name} {last_name}_result.txt' , "a")
        if q == quastions[x]:
            score+=25
            file.write("\ncorrect\n")
        else:
            file.write("\nwrong\n")
        
        
        del quastions[x]
    if score >=80 and score<=100:
        print(f"your score = {score},grate!!")
    elif score >=60 and score<80:
        print(f"your score = {score},good")
    elif score == 50:
        print(f"your score = {score},not bad,try again")
    else:
       print(f"your score = {score},sorry,you fail\ntry again")
    break
