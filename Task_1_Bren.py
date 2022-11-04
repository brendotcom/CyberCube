import sys

class Node():
    def __init__(self, s, t):
       assert len(t) - len(s) == 1, "Invalid Input"
       self.s = s
       self.t = t
       self.sDict = {}

    def function(self):
       # Iterates through t string and adds every letter(key) and count(value) to dictionary.
       for i in self.t:
           if i in self.sDict:
               self.sDict[i] += 1
           else:
               self.sDict[i] = 1

           # Deletes every letter count(value) from dictionary that's in s string variable and leaves randomly added letter
           # with value 1.
       for i in self.s:
           self.sDict[i] -= 1

           # After loop prints added letter with value 1 from dictionary which is the letter
           # that was randomly added before.
       for i in self.t:
           if self.sDict[i] == 1:
               print(i)
               break

def main(argv):
    node = Node(argv[0], argv[1])
    node.function()

if __name__ == "__main__":
    main(sys.argv[1:])
