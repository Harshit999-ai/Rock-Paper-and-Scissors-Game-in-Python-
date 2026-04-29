from random import choice

print("Welcome to rock,paer and scissors game.")
input("Press [V] to continue.")

def determine_winner(user,computer):
    if ((user == "r" and computer == "p")or 
        (user == "p" and computer == "s")or
        (user=="s" and computer == "r")):
        return 1
    elif(user==computer):
        return 0
    elif(not (user == "r" and computer == "p")and 
         not(user == "p" and computer == "s")and
        not (user=="s" and computer == "r")):
        return 2


def main():
    print("instuctions : enter r for rock,p for paer and s for scissors.")
    choices = ("r","p","s")
    user_score = 0
    computer_score = 0
    show_choice = {
        "r":"Rock",
        "p":"paper",
        "s":"scissors"
    }
    while(True):
        inp = input("Enter your choice  : ")
        if(inp not in choices):
            print("enter a valid choice.")
            continue
        computer = choice(choices)

        print(f"you choosed : {show_choice[inp]}\ncomputer choosed : {show_choice[computer]}")

        result = determine_winner(inp,computer)

        if(result == 1):
            print("computer won this match.")
            computer_score+=1;
        elif(result == 2):
            print("user won this match.")
            user_score+=1
        elif(result == 0):
            print("this match is draw")

        play_again = input("continue(Y/N) : ").lower()
        if(play_again == "y"):
            continue
        else:
            print("thanks for playing!")
            print(f"user score : {user_score}\ncomputer score: {computer_score}")
            break

main()