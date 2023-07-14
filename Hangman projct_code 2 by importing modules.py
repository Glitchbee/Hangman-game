import random
import hangman_wordlist
import hangman_art

chosen_word=random.choice(hangman_wordlist.word_list)
from hangman_art import logo
print(logo)
print(f"Hint: chosen word is {chosen_word}")
display=[]
for letter in range(len(chosen_word)):
    display+='_'
lives=6
end_of_game=False
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    for position in range(len(chosen_word)):
        holds_char = chosen_word[position]
        if holds_char == guess:
            display[position] = holds_char
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print('You lose!')
    print(f"{' '.join(display)}")#*******Important ##here they converted the list into string using syntax:- ' '.join(list)*********.
    if "_" not in display:
        end_of_game = True
        print("You win.")
    print(hangman_art.stages[lives])





