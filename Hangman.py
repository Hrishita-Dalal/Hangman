from Word_List import word_list
from ascii_Art import stages,logo
print(logo)
lives=6    #player gets 6 lives
print(f"You have {lives} lives to guess the word.")
import random
word=random.choice(word_list).lower()
#creating blanks equal to no of letters in word
display=[]
for letter in word:
    display+='_'
print(f"{' '.join(display)}")
print(stages[lives])
end_of_game=False
already_guessed=[]
while not end_of_game:
    guess=input("Guess a letter: ").lower()
    #if user entered already guessed letter, tell them
    if guess in already_guessed:
        print(f"{guess} is already guessed.")
    #else check for guessed letter in word
    else:
        already_guessed+=guess
        for position in range(len(word)):
            #guessed letter is found
            if guess==word[position]:
                display[position]=guess
        #guessed letter is wrong
        if guess not in word:
            print(f"Wrong guess. You lose a life.")
            lives-=1
    print(f"{' '.join(display)}")
    print(stages[lives])
    #if word is guessed
    if '_' not in display:
        end_of_game=True
        print("You win!")
    #if lives are over
    elif lives==0:
        end_of_game=True
        print("You lose.")
        print(f"Correct word is {word}.")