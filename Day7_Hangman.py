import random

word_list = ["Python", "Django", "Flask","Hello","SpiderMan","IronMan","Avengers","Infinity War"
             "Doctor Strange", "Pune", "Goa", "Hyderabad", "Banglore"]

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

chosen_word = random.choice(word_list)
chosen_word = chosen_word.lower()
word_length = len(chosen_word)
lives = 6
display = []

for letter in chosen_word:
  display.append('_')
print(display)


word_end = False
while not word_end:
  guess = input("Guess a letter : ").lower()[0]
  
  
  for ind in range(word_length):
    letter = chosen_word[ind]
    if guess == letter:
      display[ind] = guess

  
  if '_' not in display:
    word_end = True
    print("You Won!!!")


  if guess not in chosen_word:
    lives -= 1
    if lives == 0:
      word_end = True
      print("You Lose ")

    
  print(f"{' '.join(display)}")
  
  print(stages[lives])
  print("Lives Remaining : ", lives)

print("The Word :" , chosen_word)



    
