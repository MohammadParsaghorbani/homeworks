#hello this is new homework
#this is quiz!
#at first we have test
import random as rnd
import time
print("\nwelcom to our quiz!\nscore:\n\t80 - 100 = grate\n\t60 - 80 = good\n\t60 = pass\n\telse you will fail!")
time.sleep(1)
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
again = "y"
while again == "y":
    score = 0
    quastions = {
        "what is 2*3-4?     1)-2     2)2    3)10    4)-10" : 2,
        "what is 2+2-4*7?       1)-24      2)0      3)9     4)32" : 1,
        "what is 2+2?      1)2      2)3     3)5     4)4" : 4,
        "what is the color of sky in evening?      1)red      2)blue     3)orange     4)black" : 3,
        "when schools will start?    1)mehr     2)aban      3)esfand      4)khordad" : 1,
        "what is 20 -10*2?      1)10     2)20      3)15     4)0" : 4,
        "midnight=?     1)12pm   2)9pm      3)6am    4)12am" : 1,
        "color of sheep?       1)black       2)white      3)green      4)red" : 2,
        "book make whit....      1)wood     2)paper     3)stone     4)1,2" : 4,
        "number of month = ?     1)10    2)12     3)6      4)4" : 2
        }  
    for i in range(10): 
        z = list(quastions.keys())
        x = rnd.choice(z)
        q = int(input(f"{x}\n"))
        if q == quastions[x]:
            score+=10
        del quastions[x]
    print(f"your score = {score}")
    if score >=80 and score<=100:
        print("grate!!")
    elif score >=60 and score<80:
        print("good")
    elif score == 50:
        print("ont bad,try again")
    else:
        print("sorry,you fail\ntry again")
    again = input("do you want to have quiz again?y/n ")