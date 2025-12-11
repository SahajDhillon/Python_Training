import random
word_list = ["escape", "treasure", "flower"]
word = random.choice(word_list)
print(word)
placeholder = ""
for letter in range(1, len(word)):
    placeholder += "_"
print(placeholder)

chances = 5
game_over = False
correct_letters = []

while not game_over:
    display = ""
    choice = input("Enter a letter: ")
    for letter in word:
        if choice == letter:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if choice not in word:
        chances -= 1
        print(f"lives Remaining: {chances}")
        if chances == 0:
            print("game over")
            game_over = True
            print(f"The correct word was {word}")

    if "_" not in display:
        print("you Win!!")
        game_over = True
#