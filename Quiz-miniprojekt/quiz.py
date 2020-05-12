from datetime import date
import requests
import random
import json
import html

amount = 10
name = "Anonymous"

while 1:
    print("""
 ______________
|              |
|     The      |
|     EBic     |
|     Quiz!    |
|______________|

1: Start the quiz.
2: Quit.""")
    print("3: Change the amount of questions. (Currently "+str(amount)+")")
    print("4: Change your username. (Currently '"+name+"')")
    val = input("> ")
    1
    if val == "1":
        print("Generating a quiz with "+str(amount)+" questions...")
        break

    if val == "2":
        exit()

    if val == "3":
        newAmount = input("\nHow many questions do you want? (max 50)\n> ")
        amount = int(newAmount)
        if amount > 50: 
            amount = 50
            print("\nSetting the amount of questions to",str(amount)+"...")
        else:
            print("\nSetting the amount of questions to",str(amount)+"...")

    if val == "4":
        newName = input("\nWhat will your new name be?\n> ")
        name = newName
        print("Your new name will be '"+name+"'")

url = "https://opentdb.com/api.php?amount="+str(amount)
res = requests.get(url)
Res_Dict = res.json()

streak = 0
bestStreak = 0
correctAnswers = 0

for x in Res_Dict["results"]:
    lenght = len(x["incorrect_answers"])+1
    x["incorrect_answers"].append(x["correct_answer"])
    random.shuffle(x["incorrect_answers"])
    print("\n"+ html.unescape(x["question"]))

    for i in range(lenght):
        if lenght > i:
            print(i+1,"|", html.unescape(x["incorrect_answers"][i]))

    while 1:
        inp = input("What is your answer?\n> ")
        
        try:
            inp = int(inp)
            
            if x["incorrect_answers"][inp-1] in html.unescape(x["correct_answer"]):
                streak += 1
                correctAnswers += 1
                print("Correct answer!\nYour streak is",str(streak))

            elif x["incorrect_answers"][inp-1] not in html.unescape(x["correct_answer"]):
                streak = 0
                print("\nWrong answer :(\nYour streak is 0")

            if streak > bestStreak:
                bestStreak = streak

            print("\nThe correct answer was: " + html.unescape(x["correct_answer"]))
            break

        except:
            print("\nType a number next time >:(\nYour streak is 0")
            print("\nThe correct answer was: " + html.unescape(x["correct_answer"]))
            streak = 0
            break

print("\nYou got",str(correctAnswers),"answers correct out of",str(amount),"questions!\nYour best streak was",str(bestStreak))

save = input("\nWould you like to save your highscore? y/n > ")
if save == "y":
        print("Saving...")
        today = date.today()
        with open("highscore.txt","a") as FishPog:
                FishPog.write(str(today)+": The highscore was "+str(correctAnswers)+" out of "+str(amount)+" questions with a best streak of "+str(bestStreak)+". Achieved by the majestic: "+name+"\n"+"-"*150+"\n")
        FishPog.close()

else:
    print("Didnt save")

exec(open('quiz.py').read())