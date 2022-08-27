import random


def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors): ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)

    choices_of_players = {"player": player_choice, "computer": computer_choice}
    return choices_of_players


def check_win(player, computer):
    results = "Let the game begin"
    if player == computer:
        tie_message = f"You chose {player}, computer chose {computer}."
        results = f"It's a tie! {tie_message}"
    elif player == "rock":
        if computer == "scissors":
            results = "Rock smashes scissors! You win!"
        else:
            results = "Paper covers rock! You lose."
    elif player == "paper":
        if computer == "scissors":
            results = "Scissors cut paper! You lose."
        else:
            results = "Paper covers rock! You win!"
    elif player == "scissors":
        if computer == "rock":
            results = "Rock smashes scissors! You lose."
        else:
            results = "Scissors cut paper! You win!"

    return results


choices = get_choices()
result_of_the_game = check_win(choices["player"], choices["computer"])
print(result_of_the_game)
