# shopping_list_diff.py

import difflib
import sys

file1 = open("my_shopping_list.txt").readlines()
file2 = open("friends_shopping_list.txt").readlines()

delta = difflib.unified_diff(file1, file2, "my_shopping_list.txt", "friends_shopping_list.txt")
sys.stdout.writelines(delta)
