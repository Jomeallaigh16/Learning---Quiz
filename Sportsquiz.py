print("Welcome to the worlds greatest sports quiz")

playing = input("Would you like to play? yes/no ")

if playing.lower() != "yes":
    quit()

print("Alright! Lets begin..")
score = 0

answer = input("Who won the English Premier League 2022? ").lower()
if answer == "manchester city":
    print("Correct! Well done")
    score += 1
else:
    print("Incorrect! Next question")


answer = input("Who was the top goal scorer in the same season? Please state full name. ")
if answer.lower() == "erling haaland":
    print("Correct! Well done")
    score += 1
else:
    print("Incorrect! Next question")


answer = input("Who captained Manchester United during their treble season? ")
if answer.lower() == "roy keane":
    print("Correct! Well done")
    score += 1
else:
    print("Incorrect! Next question")


answer = input("Who managed Manchester United during the same season? ")
if answer.lower() == "alex ferguson":
    print("Correct! Well done. Final question")
    score += 1
else:
    print("Incorrect! Final question")

answer = input("What club has won the most Premier League titles? ")
if answer.lower() == "manchester united":
    print("Correct! Thank you for playing")
    score += 1
else:
    print("Incorrect!\n")
    print("Well done on completing the quiz!\n")
    print("Here are your scores\n")
    print("You got " + str(score) + " questions correct out of a possible 5\n")
    
    print("Thank you for playing\n")
    

input("Press Enter again to exit")


    

    
