import random 

highscores =[]
file = open("Scores.txt")
for line in file:
    highscores.append(line)
print("HIGHSCORES ")
for line in highscores:
    print(line)

def getscore(str):
    index = str.find(",")
    return int(str[index+1:])

username = input("Enter Your Name => ")
print("Your name is " + username + " correct?")
anwser = input("Answer yes or no => ")
while anwser != "yes":
    Name = username = input("Enter Your Name => ")
    print("Your name is " + username + " correct?")
    anwser = input("Answer yes or no => ")

if anwser == "yes":
    print("Lets Continue")


user_wins = 0
num_matches = 0
loss = False
random_num = random.randint(1, 10)
while (loss == False):
    num_matches = num_matches + 1
    for i in range(3):
        choice = int(input("Enter a number 1 through 10 => "))
        if choice == random_num:
            print("You gussed the right number")
            user_wins = user_wins + 1
            break
        if choice < random_num:
            print("Too low")
        if choice > random_num:
            print("Too high")
    if choice is not random_num:
        print("You Lose")
        print("Points:" + str(user_wins))
        print("The random number was " + str(random_num))
        loss = True
    random_num = random.randint(1, 10)

file.close() 
file = open("scores.txt","w")

for index in range(len(highscores)): 
    tempscore = getscore(highscores[index])
    #print(tempscore)

   
    if user_wins > tempscore:
        highscores[index]= username + "," + str(user_wins)
        break
    if user_wins < tempscore:
        range(len(highscores) + 1)

for index in range(len(highscores)):
    tempscore = highscores[index]
    print(tempscore)

    
    file.write(str(tempscore))
    #break

file.close() 