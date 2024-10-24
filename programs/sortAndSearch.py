from MyTree import *
from time import *
def main():
    while True:
        unsorted = input("Enter the name of the file with unsorted words: ")
        if unsorted[-4:] != (".txt"):
            unsorted+=".txt"
            try:
                library = open(unsorted, "r").readlines()
                break
            except:
                print("Error: File not found.")
    while True:
        words = input("Enter the name of the file with the scrabble dictionary: ")
        if words[-4:] != (".txt"):
            words+=".txt"
            try:
                dictionary = open(words, "r").readlines()
                break
            except:
                print("Error: File not found.")
    start = time()
    tree = BST(library[0])
    for i in library[1:]:
        tree.insert(i)
    print("Seconds spent creating the tree:", time()-start)
    start2 = time()
    newList = []
    for i in dictionary:
        if tree.find(i):
            newList.append(i[:-1])
            print(i)
    print("Time spent searching for words:", time() - start2)
    print("Total time spent:", time()-start)
    print(newList)
main()
