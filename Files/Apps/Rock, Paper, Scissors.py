import random

def play_rps(player_choice):
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    print(f"Player chooses: {player_choice}")
    print(f"Computer chooses: {computer_choice}")

    if player_choice == computer_choice:
        return "It's a tie!"
    elif (
        (player_choice == "rock" and computer_choice == "scissors") or
        (player_choice == "paper" and computer_choice == "rock") or
        (player_choice == "scissors" and computer_choice == "paper")
    ):
        return "Player wins!"
    else:
        return "Computer wins!"

def main():
    print("Welcome to Rock, Paper, Scissors!")
    print("Enter your choice: rock, paper, or scissors.")

    while True:
        player_choice = input("Your choice: ").lower()

        if player_choice in ["rock", "paper", "scissors"]:
            result = play_rps(player_choice)
            print(result)

            play_again = input("Play again? (yes/no): ").lower()
            if play_again != "yes":
                print("Thanks for playing!")
                break
        else:
            print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")

if __name__ == "__main__":
    main()
