import random
import string

class Node():
    def __init__(self):
        # Random letter generator.
        self.random_letter = random.choice(string.ascii_lowercase)

        # Empty dictionary for finding added letter.
        self.sDict = {}

    def function(self):
        # User inputted letters.
        self.t_string = input("Enter some letters: ")
        print("Your string of letters is:", self.t_string)

        # Getting s from t and adding random letter.
        self.s_string = self.t_string + self.random_letter

        # This shuffles s_string.
        self.shuffled = ''.join(random.sample(self.s_string, len(self.s_string)))

        # Iterates through shuffled string and adds every letter(key) and count(value) to dictionary.
        for i in self.shuffled:
            if i in self.sDict:
                self.sDict[i] += 1
            else:
                self.sDict[i] = 1

        # Deletes every letter count(value) from dictionary that's in t_string variable and leaves randomly added letter
        # with value 1.
        for i in self.t_string:
            self.sDict[i] -= 1

        # After loop prints leftover letter with value 1 from dictionary which is the letter
        # that was randomly added before.
        for i in self.shuffled:
            if self.sDict[i] == 1:
                print("Program added {}. ".format(i))
                break
                
def main():
    node = Node()
    node.function()

if __name__ == "__main__":
    main()
