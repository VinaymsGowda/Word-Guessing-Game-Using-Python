import random
name=input("Enter your Name:")
print("Good Luck "+name)
words = ['kindly', 'recite', 'repeat', 'tree', 'display', 'geeks', 'coader', 'programmer', 'python', 'premium', 'watch'] 

word=random.choice(words)

# print(word)
attempt=0
ans=[]

for index in range(len(word)):
    ans.append("_")

print("Guess The Character:")
final="".join(ans)
print(final)

while(final!=word):
    predict=input("Enter A Character:")
    if predict in word:
        for i in range(len(word)):
            if word[i]==predict:
                if predict in final:
                    print("Character Repeated Guess Again")
                    break
                ans[i]=predict
    else:
        print("Input Character not Present in Word")
    attempt=attempt+1
    final="".join(ans)
    print(final)
    print(f"Number of attempts Remaining:{10-attempt}")
    if attempt>9:
        print("You Failed To guess The Word! Game Over !!!")
        break

if word==final:
    print("You Guessed the Word correctly !! ")
    print(f"The Word was is {final}")
    print(f"The Number Of attempts Taken is {attempt}")
    with open("HighScoreofWG.txt","r") as f:
        high=int(f.read())
        if(high==0):
            with open("HighScoreofWG.txt","w") as f:
                f.write(str(attempt))                                   #typecasted to str bcoz we cannot append a integer into file
                print(f"HighScore of {attempt} has been created by {name}")
        elif(attempt<high):
            with open("HighScoreofWG.txt","w") as f:
                f.write(str(attempt))                                   #typecasted to str bcoz we cannot append a integer into file
                print(f"HighScore of {attempt} has been created by {name}")

else:
    print("You Failed To guess The Word! Game Over !!!")
    print(f"The Word was {word}")
    print(f"The Number Of attempts Taken is {attempt}")
