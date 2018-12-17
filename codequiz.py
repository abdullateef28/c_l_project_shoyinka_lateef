#)Display the purpose of the program
print(" this is a code lagos trivia quiz")
#2)Display the instructions
print("select a letter with the correct option")
score=0
#3)Ask the user a question
question1 =(input("How many Out of School centres does CodeLagos have?\n (a) 4\n (b) 12\n (c) 21\n (d) 30\n"))
#4)Wait for the answer
#5)If the question is correct, display: “Correct” and add 1 to the score
if (question1 == "c"):
    print("correct")
    score=score+10
else:
    print("wrong")
#6)Else display: “Wrong”


#7)Go back to step 3 until all the questions have been answered
#8)Print the score of the user
qst2 = input ("In what year did CodeLagos start?\n (a)2017\n (b) 2012\n (c) 1999\n (d) 2018\n")
if qst2== "a":
    print("correct")
    score=score+10
else:
    print("wrong")

qst3=  input("How many Lagosian does CodeLagos intend to train by 2020?\n (a)1,000,000\n (b) 2,000,000\n (c) 3,000,000\n (d) 4,000,000\n")
if qst3=="a":
    print("correct")
    score=score+10
else:
    print("wrong")

print("your score is", score)
    
    
