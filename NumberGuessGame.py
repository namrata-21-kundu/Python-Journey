import random

def guess():
    secretNo = random.randint(1,100)
    attempts = 0
    print("Guess the number between 1 to 200")

    while True:
        myNo = int(input("Enter your number: "))
        attempts += 1

        if(secretNo == myNo):
            print(f"Correct guess in {attempts} attempts")
            break
        elif(secretNo <  myNo):
            print("Your number is higher")
        elif(secretNo > myNo):
            print("Your number is lower")

guess()