import random     
user_marks = 0 
comp_marks = 0
while(True):
    print("\n--------------------------------------------------------------------------------------")
    print("\tROCK PAPER SCISSOR GAME\n")
    select_list = ["rock", "paper", "scissor"]
    print("You need to enter rock, paper or scissor to play the game")
    user_choice = input("Enter your choice ->  ")
    comp_choice = random.choice(select_list)

    print(f"User Choice: {user_choice} , Computer Choice : {comp_choice}")

    if (user_choice == "rock"):
        if (comp_choice == "rock"):
            print("\nTie")
            print(f"Score of User = {user_marks}\nScore of Computer = {comp_marks}")
        elif (comp_choice == "paper"):
            print("\nPaper covers rock; User = 0 , Computer = 1")
            comp_marks += 1
            print(f"Score of User = {user_marks}\nScore of Computer = {comp_marks}")

        elif (comp_choice == "scissor"): 
            print("\nRock smashes scissor ; User = 1 , Computer = 0")
            user_marks += 1
            print(f"Score of User = {user_marks}\nScore of Computer = {comp_marks}")

    elif (user_choice == "paper"):
        if (comp_choice == "paper"):
            print("\nTie")
            print(f"Score of User = {user_marks}\nScore of Computer = {comp_marks}")
        elif (comp_choice == "rock"):
            print("\nPaper covers rock; User = 1 , Computer = 0")
            user_marks += 1
            print(f"Score of User = {user_marks}\nScore of Computer = {comp_marks}")
        elif (comp_choice == "scissor"):
            print("\nScissor cuts paper; User = 0 , Computer = 1")
            comp_marks += 1
            print(f"Score of User = {user_marks}\nScore of Computer = {comp_marks}")

    elif (user_choice == "scissor"):
        if (comp_choice == "scissor"):
            print("\nTie")
            print(f"Score of User = {user_marks}\nScore of Computer = {comp_marks}")
        elif (comp_choice == "paper"):
            print("\nScissor cuts paper; User = 1 , Computer = 0")
            user_marks += 1
            print(f"Score of User = {user_marks}\nScore of Computer = {comp_marks}")
        elif (comp_choice == "rock"):
            print("\nRock smashes scissor ; User = 0 , Computer = 1")
            comp_marks += 1
            print(f"Score of User = {user_marks}\nScore of Computer = {comp_marks}")

    replay= input("\nWant to play again? YES or NO ").upper()
    if (replay == "YES"):
        continue 
    elif (replay == "NO"):
        print("\nTOTAL MARKS - \n")
        print(f"Score of User = {user_marks}\nScore of Computer = {comp_marks}")
        if (user_marks > comp_marks):
            print("\nUser is the Winner! Congratulations User!!")
        elif (comp_marks > user_marks):
            print("\nComputer is the Winner! Congratulations Computer!!")
        else:
            print("\nTie between User and Computer!")
            print("\nEXITING GAME...")
        break




