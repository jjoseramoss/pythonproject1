import random

def comp_answer():
    num = random.randint(1,3)
    ans = "placeholder"

    if num == 1:
       ans = "Rock"
    elif num == 2:
       ans ="Paper"
    elif num == 3:
        ans ="Scissors"
    return ans

def compare(user_ans, computer):
    if user_ans == computer:
        print("It is a Tie!")
    elif user_ans == "Rock" and computer == "Paper":
        print("Computer Wins!")
    elif computer == "Rock" and user_ans == "Paper":
        print("You Win!")
    elif user_ans == "Rock" and computer == "Scissors":
        print("You Win!")
    elif computer == "Rock" and user_ans == "Scissors":
        print("Computer Wins!")
    elif user_ans == "Scissors" and computer == "Paper":
        print("You Win!")
    elif computer == "Scissors" and user_ans == "Paper":
        print("Computer Wins!")




print("Welcome, Let's Play Rock Paper Scissors!")

user_ans = str(input("Choose between \"Rock\" \"Paper\" and \"Scissors\": "))
computer = comp_answer()

print(f"\nComputer's choice is {computer}")

compare(user_ans, computer)

