import random
import json
import datetime

# Funcion que hace jugar el juego

def play_game(level="easy"):
    secret = random.randint(1, 30)
    attempts = 0
    wrong_guesses = []
    score_list = get_score_list()

    name = input("What's your name?: ")

    while True:
        guess = int(input("Guess the secret number (between 1 and 30): "))
        attempts += 1        # attempts = attempts + 1

        if guess == secret:
            current_time = str(datetime.datetime.now())
            score_data = {"User name": name, "secret_number": secret, "attempts": attempts,
                          "Unsuccessful guesses": wrong_guesses, "date": current_time}
            score_list.append(score_data)

            with open("score_list.txt", "w") as score_file:
                b = json.dumps(score_list)
                score_file.write(b)

            print("You've guessed it - congratulations! It's number " + str(secret))
            print("Attempts needed: " + str(attempts))
            print(current_time)
            break
        elif guess > secret and level == "easy":
            print("Your guess is not correct... try something smaller")
            wrong_guesses.append(guess)
        elif guess < secret and level == "easy":
            print("Your guess is not correct... try something bigger")
            wrong_guesses.append(guess)
        elif level == "hard":
            print("Wrong guess. Game Over!")
            break

# Función que lee score_list y devuelve los valores de la lista

def get_score_list():
    with open("score_list.txt", "r") as score_file:
        score_list = json.loads(score_file.read())
        return score_list

# Función que recoge los valores de def get_score_list y devuelve los 3 mejores resultados

def get_top_scores():
    score_list = get_score_list()
    best_3 = sorted(score_list, key=lambda x: x['attempts'])[:3]

    for score_dict in best_3:
        score_text = "Player {0} had {1} attempts on {2}. The secret number was {3}. The wrong guesses were: {4}". \
            format(score_dict.get("User name"), str(score_dict.get("attempts")), score_dict.get("date"),
                   score_dict.get("secret_number"), score_dict.get("Unsuccessful guesses"))
        print(score_text)
        return best_3

while True:
    selection = input("Would you like to A) play a new game, B) see the best scores, or C) quit? ")

    if selection.upper() == "A":
        play_game()
    elif selection.upper() == "B":
        for score_dict in get_top_scores():
            print(str(score_dict["attempts"]) + " attempts, date: " + score_dict.get("date"))
    else:
        break


# Función para ejecutar el juego
def main():

    while True:
        game_init = input("Would you like to: Play [A], See best scores [B], or Exit[C] ?")

        if game_init.upper() == "A":
            difficulty = input("Level [easy] or [hard]:")
            difficulty.lower()
            if difficulty == "easy":
                play_game("easy")
            elif difficulty == "hard":
                play_game("hard")
        elif game_init.upper() == "B":
            for score_dict in get_top_scores():
                print(str(score_dict["attempts"]) + " attempts, date: " + score_dict.get("date"))
        else:
            break


if __name__ == "__main__":
    main()