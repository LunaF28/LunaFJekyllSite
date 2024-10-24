---
layout: default
modal-id: "portfolio-4"
title: "Python Binary Search Tree"
date: 2022-12-01
img: cabin.png
alt: "Cabin Image"
project-date: 2022-12-01 12:00:00 -0400
client: HZ
category: Python Coding
description: "This is a set of Python 3 programs that work together to create and use a Binary Search Tree for 3 letter words"
---

## Binary Search Tree for Scrabble Words

This Python program creates a **[binary search tree](https://www.geeksforgeeks.org/binary-search-tree-data-structure/) (BST)** for Scrabble words. Specifically, it organizes **6-letter randomized strings** and allows you to search for words within that list using a Scrabble dictionary. 

### Key Features
- **Randomized Word List Creation**
    - Creates a list of random 6 letter string "words" of an amount of your choosing, and saves them to the file `random_words.txt`
- **BST Creation**:
  - 6 letter randomized strings from an unsorted file are inserted into the binary search tree, making it easier and faster to search.
  
- **Word Search**:
  - The program checks for words in the provided Scrabble dictionary file and lists the ones that are found in the tree.
  - You get to see the time it takes to both create the tree and search for words, giving you an idea of the program's efficiency.
 

### Steps
1. **Input Files**:
   - The program prompts for two files:
     - One containing unsorted words.
     - Another containing a Scrabble dictionary.
   - The file extension `.txt` is automatically appended if not provided.

2. **Tree Creation**:
   - The unsorted words are inserted into a binary search tree for quick lookup.

3. **Word Search**:
   - After the tree is created, the program searches through the Scrabble dictionary to find matching words from the tree.

### Outside Requirements:
- **Python 3.x**: This program is written in Python, so you’ll need to have a Python 3.x interpreter installed to run the scripts.
- **`random` module**: The `random` module is used to generate random characters for the creation of the randomized words in the `randStr` function. This is part of Python’s standard library, so no external installation is required.
- **`time` module**: The `time` module is used in the sorting and searching process to measure the time taken for various operations. It’s part of Python’s standard library.
### Download the Code
Here are the links to download the individual components of the program:

- [Download the program to make the randomized strings here!](programs/makeRandomWordFile.py)
- [Download the Binary Search Tree class here!](programs/BST.py)
- [Download the program to run the BST class here!](programs/sortAndSearch.py)
- [Download the 6 letter scrabble dictionary here!](programs/6-letter-scrabble.txt)