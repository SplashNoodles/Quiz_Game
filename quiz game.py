print("Welcome to my quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("1.What is the fundamental unit of life? ")
if answer.lower() == "cell":
    print("Correct!")
    score += 4
else:
    print("Incorrect")
    print("Try to get the next one correct!")
    score -= 2

print(f"Your score is {score}")

answer = input("2.Which is the largest continent in the world? ")
if answer.lower() == "asia":
    print("Correct!")
    score += 4
else:
    print("Incorrect")
    print("Try to get the next one correct!")
    score -= 2

print(f"Your score is {score}")

answer = input("3.What is 2 * 5 / 5 + (4 + 6) ")
if answer.lower() == "12":
    print("Correct!")
    print("Keep it up!")
    score += 4
else:
    print("Incorrect")
    print("Try to get the next one correct!")
    score -= 2

print(f"Your score is {score}")

answer = input("4.What is the shortest distance from the initial point to the starting point called? ")
if answer.lower() == "displacement":
    print("Correct!")
    score += 4
else:
    print("Incorrect")
    print("Try to get the next one correct!")
    score -= 2

print(f"Your score is {score}")

answer = input("5.What are called the suicide bags of a cell? ")
if answer.lower() == "lysosomes":
    print("Correct!")
    score += 4
else:
    print("Incorrect")
    score -= 2

print(f"Your final score is {score}")

print("You got " + str((score / 20) * 100) + " %")

if int(score) > 15:
    print("You have done a fabulous job!")
elif 8 <= int(score) < 15:
    print("You did amazing but you could do better!")
elif 0 <= int(score) < 8:
    print("Better luck next time!")
else:
    print("You need to improve a lot")
