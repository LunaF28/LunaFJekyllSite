class Node:
    def __init__(self, word):
        self.left = None
        self.right = None
        self.word = word
    def __repr__(self):
        return str(self.word)
    def getWord(self):
        return self.word
    def getNum(self, letter):
        nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for n, i in enumerate(alphabet):
            if str(i) == letter:
                return str(nums[n])
    def getValue(self,word):
        store = ""
        for n, i in enumerate(self.word):
            store+=word.getNum(self.word[n])
        return store
class BST:
    def __init__(self,seed,amnt_of_nodes):
        self.root = Node(seed)
        totalNodes = amnt_of_nodes
    def insert(self,word):
        if word.getValue(word) < self.root.getValue():
            if check.left:
                #print(check.left)
                word.insert(word,check.left)
            else:
                check.left = word
                return True
        elif word.getValue(word) > check.getValue(check):     
            if check.right:
                #print(check.right)
                word.insert(word,check.right)
            else:
                check.right = word
                return True
        else:
            return False
    def makeWordList(self):
        firstWord = self.word
        for i in [7,39,20,25,10,8,2,18,42,50,47]:
            newNode = None
            newNode = Node.insert("Why does this work?",Node(i),firstWord)
