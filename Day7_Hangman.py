import random
import hangman_art
import hangman_word

print(hangman_art.logo,"\n\n")
chosen_word = random.choice(hangman_word.word_list)
chosen_word = chosen_word.lower()
word_length = len(chosen_word)
lives = 6
display = []
print(chosen_word)

for letter in chosen_word:
  display.append('_')
print(display)


word_end = False
while not word_end:
  guess = input("Guess a letter : ").lower()[0]

  if guess in display:
      print(f"You have already guessed {guess}")
      
  
  for ind in range(word_length):
    letter = chosen_word[ind]
    if guess == letter:
      display[ind] = guess

  
  if '_' not in display:
    word_end = True
    print("You Won!!!")


  if guess not in chosen_word:
    lives -= 1
    print(f"You have guessed {guess} which is not in present in word, you lose a life.\nRemaining Life {lives} ")
    if lives == 0:
      word_end = True
      
      
  print(f"{' '.join(display)}")
  print(hangman_art.stages[lives])
  

print("The Word :" , chosen_word)



    
