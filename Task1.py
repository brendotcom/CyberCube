import random
import string

# Random letter generator.
random_letter = random.choice(string.ascii_lowercase)
# User inputted letters.
t_string = input("Enter some letters: ")
print("Your string of letters is:", t_string)
# Getting s from t and adding random letter.
s_string = t_string + random_letter
# This shuffles s_string.
shuffled = ''.join(random.sample(s_string, len(s_string)))
print("Shuffled string with extra letter is: ", shuffled)

# Empty dictionary for finding added letter.
sDict = {}
# Iterates through shuffled string and adds every letter(key) and count(value) to dictionary.
for i in shuffled:
    if i in sDict:
        sDict[i] += 1
    else:
        sDict[i] = 1
# Deletes every letter count(value) from dictionary that's in t_string variable and leaves randomly added letter
# with value 1.
for i in t_string:
    sDict[i] -= 1
# After loop prints leftover letter with value 1 from dictionary which is the letter
# that was randomly added before.
for i in shuffled:
    if sDict[i] == 1:
        print("Program added {}. ".format(i))
        break
