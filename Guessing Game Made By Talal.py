print("Welcome to the guessing game made By Talal")
num = 18
print("You have 9 attempts to guess the right number.")
i=1
while i <= 8:
    inp1 = int(input("Please guess the  number?: "))
    if inp1 > num:
        print("Your number is greater than the secret number. Take another guess.")
    elif inp1 < num:
        print("Your number is less than the secret number. Take another guess.")
    elif inp1==num:
        print("Good job, you guessed the number right")
        break
    i += 1
if i==9:
    print("You have used all your attempts. Better luck next time.")