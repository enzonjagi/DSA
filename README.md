# DSA - Data structures and algorithm practice 
## Python(round one), C(round_two), and Java(round three)
# Problems We'll be solving
<p>Borrowed from the article below</p>

* [By Taha Sufiyan](https://www.simplilearn.com/coding-interview-questions-article)
* <b>DISCLAIMER: </b> Although there are solutions in the article, the purpose of this repo is to do the challenges by creating my own personalized solutions to the problems

## 1. How do you determine if a number is a palindrome?
### Python Solution [palindrome.py](/python/palindrome.py)
#### Usage:

```
python palindrome.py <list value as arguments>
```
- e.g

```
python python/palindrome.py 34 44 676 009 0 free stits 12.21
```
- Output

```
Value: 34 --> Not Palindrome
Value: 44 --> Palindrome
Value: 676 --> Palindrome
Value: 009 --> Not Palindrome
Value: 0 --> Palindrome
Value: free --> Not Palindrome
Value: stits --> Palindrome
Value: 12.21 --> Palindrome
```
## 2. How do you reverse a string?
### Python Solution: [reverse_string.py](/python/reverse_string.py)
#### Usage:

```
python reverse_str.py <list value as arguments>
```
- e.g

```
python python/reverse_string.py 34 44 676 009 0 free stits 12.21
```
- Output

```
Value: 34 --> Reversed as: 43
Value: 44 --> Reversed as: 44
Value: 676 --> Reversed as: 676
Value: 009 --> Reversed as: 900
Value: 0 --> Reversed as: 0
Value: free --> Reversed as: eerf
Value: stits --> Reversed as: stits
Value: 12.21 --> Reversed as: 12.21
```
## 3. Find the number of occurrences of a character in a String?
### Python Solution [char_occurence.py](/python/char_occurrence.py)
#### Usage:

```
python python/char_occurrence.py <char> <string>

```
- e.g

```
python python/char_occurrence.py 2 333323
```
- Output

```
The char '2' appeared 1 time(s) in the string '333323'.
```
## 4. How to find out if the given two strings are anagrams or not?
### Python Solution [anagrams.py](/python/anagrams.py)
#### Usage:

```
python python/anagrams.py <string_a> <string_b>

```
- e.g

```
python python/anagrams.py  "I'm a dot in place." "A decimal point"
```
- Output

```
'I'm a dot in place.' and 'A decimal point' are anagrams

```
eg.2
```
python python/anagrams.py  "njagi ndungo" "omar njagi"
```
- Output

```
'njagi ndungo' and 'omar njagi' are not anagrams

```
## 5. How do you calculate the number of vowels and consonants in a String?
### Python Solution [cons_vow.py](/python/cons_vow.py)
#### Usage:

```
 python python/cons_vow.py <string_a> <string_b>

```
- e.g

```
 python python/cons_vow.py "aba" "sugar" "osama bin laden" "smooth sailor" "muslimah"
```
- Output

```
aba has 2 vowels and 1 consonants.
sugar has 2 vowels and 3 consonants.
osama bin laden has 6 vowels and 7 consonants.
smooth sailor has 5 vowels and 7 consonants.
muslimah has 3 vowels and 5 consonants.
```
eg.2
```
 python python/cons_vow.py
```
- Output

```
No arguments provided
```
## 6. How do you get the matching elements in an integer array?
### Python Solution [matching_elements.py](/python/matching_elements.py)
#### Usage:

```
python python/matching_elements.py <a list of integers>

```
- e.g

```
 python python/matching_elements.py 1 2 3 4 5 5 6 6 7 8 9 10
```
- Output

```
The elements [5, 6] have a match in the array [1, 2, 3, 4, 5, 5, 6, 6, 7, 8, 9, 10].
```
eg.2
```
 python python/matching_elements.py 1 2 3 4 5 6 7 8 9 10
```
- Output

```
The array [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] has no matching elements.
```
eg.3
```
 python python/matching_elements.py
```
- Output

```
Please input a list of integers.
```
eg.4
```
 python python/matching_elements.py a 2 3 4 5 6 7 8 9 1q
```
- Output

```
The array [2, 3, 4, 5, 6, 7, 8, 9] has no matching elements.
```
## 7. How would you implement the bubble sort algorithm?
## 8. How would you implement the insertion sort algorithm?
## 9. How do you reverse an array?
### Python Solution [anagrams.py](/python/anagrams.py)
#### Usage:

```
python python/reverse_array.py <arr_item_a> <arr_item_b> ...

```
- e.g

```
 python python/reverse_array.py
```
- Output

```
please input an array in list form, with items separated in spaces
```
eg.2
```
python python/reverse_array.py 2
```
- Output

```
The array [2] is reversed to: [2]
```
eg.3
```
 python python/reverse_array.py 2 3 4 5 6 7 8 9
```
- Output

```
The array [2, 3, 4, 5, 6, 7, 8, 9] is reversed to: [9, 8, 7, 6, 5, 4, 3, 2]
```
## 10. How would you swap two numbers without using a third variable?
## 11. Print a Fibonacci series using recursion?
## 12. How do you find the factorial of an integer?
## 13. How do you reverse a Linked List?
## 14. How would you implement Binary Search?
## 15. How would you find the second-largest number in an array?
## 16. How do you remove all occurrences of a given character from the input string?
## 17. Showcase Inheritance with the help of a program?
## 18. Explain overloading and overriding with the help of a program?
## 19. How do you check if the given number is prime?
## 20. How do you sum all the elements in an array?

# Top 40 Coding Interview Questions You Should Know
[By Taha Sufiyan](https://www.simplilearn.com/coding-interview-questions-article)

Coding Interview Questions On Conceptual Understanding

1. What is a Data Structure?
2. What is an Array?
3. What is a Linked List?
4. What is LIFO?
5. What is a Stack?
6. What is FIFO?
7. What is a Queue?
8. What are Binary Trees?
9. What is Recursion?

10. What is the OOPs concept?
11. What are the concepts introduced in OOPs?
12. Explain what a Binary Search Tree is.
13. Explain Doubly Linked Lists?
14. What is a Graph?
15. Differentiate between linear and non-linear data structure?
16. What is a Deque?
A deque is a double-ended queue.
17. What’s the difference between Stack and Array?
18. Which sorting algorithm is the best?
19. How does variable declaration affect memory?
20. What are dynamic data structures?



