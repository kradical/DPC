# Daily Programmer
https://www.reddit.com/r/dailyprogrammer

[![Language](https://img.shields.io/badge/language-python-brightgreen.svg?style=flat
)](https://www.python.org)

Daily Programming Challenge

Organized by difficulty and then number!

## EASY:

### 1user input

create a program that will ask the users name, age, and reddit username. have it tell them the information back, in the format:
your name is (blank), you are (blank) years old, and your username is (blank)
for extra credit, have the program log this information in a file to be accessed later.


### 2determinant calculator

Hello, coders! An important part of programming is being able to apply your programs, so your challenge for today is to create a calculator application that has use in your life. It might be an interest calculator, or it might be something that you can use in the classroom. For example, if you were in physics class, you might want to make a F = M * A calc.
EXTRA CREDIT: make the calculator have multiple functions! Not only should it be able to calculate F = M * A, but also A = F/M, and M = F/A!


### 3caesar cipher

Welcome to cipher day!
write a program that can encrypt texts with an alphabetical caesar cipher. This cipher can ignore numbers, symbols, and whitespace.
for extra credit, add a "decrypt" function to your program!


### 4password generator

You're challenge for today is to create a random password generator!
For extra credit, allow the user to specify the amount of passwords to generate.
For even more extra credit, allow the user to specify the length of the strings he wants to generate!


### 5password protected

Your challenge for today is to create a program which is password protected, and wont open unless the correct user and password is given.
For extra credit, have the user and password in a seperate .txt file.
for even more extra credit, break into your own program :)


### 216TexasHoldem

Theme Week:

I got the whole week so I am merging all 3 challenges into a theme of Texas Hold 'em Poker. All 3 challenges will be related on this popular card game of poker.
Description:

For those who want to know more about Texas Hold 'Em Poker or just need a refresher. Check Wikipedia Article on Texas Hold 'Em Poker
For the first challenge we will simulate the dealing part of the game.
Input:

You will be asked how many players 2 to 8. You will always be one of the players and you are facing 1 to 7 other computer controlled players.
Output:

Display the 2 cards each player is dealt and the display the 5 community cards.
Format is left up to you. (The exact method of the output a card. For my examples I am using verbal words but someone might use unicode symbols for the card suit or other. You design this as long as we can tell the cards apart it is all good)
Example:

How many players (2-8) ? 3

Your hand: 2 of Clubs, 5 of Diamonds
CPU 1 Hand: Ace of Spades, Ace of Hearts
CPU 2 Hand: King of Clubs, Queen of Clubs

Flop: 2 of Hearts, 5 of Clubs, Ace of Clubs
Turn: King of Hearts
River: Jack of Hearts
Dealing Cards:

To keep things close to the game you will be dealing from 1 deck of standard playing cards. Once you deal that card you cannot deal it again. The exact method is part of the challenge and for you to decide, design and implement.
In Texas Hold em you burn a card (draw and discard without looking at it) before you do the flop, turn and river. It removes these cards from the pool of possible cards that can be dealt. If you wish to show these cards (I did not in my example) then please for science go for it.
Looking ahead for the Intermediate:

In the intermediate you will be asked to compare various hands of poker to find which hand is the winning hand.


## INTERMEDIATE:

### 1scheduling app

create a program that will allow you to enter events organizable by hour. There must be menu options of some form, and you must be able to easily edit, add, and delete events without directly changing the source code.
(note that by menu i dont necessarily mean gui. as long as you can easily access the different options and receive prompts and instructions telling you how to use the program, it will probably be fine)


### 215Network Sort

When we computer programmers learn all about how computers sort lists of numbers, we are usually taught about sorting algorithms like Quicksort and Heapsort. There is, however, an entirely different model for how computers can sort numbers called sorting networks. Sorting networks are very useful for implementing sorting in hardware, and they have found a use for designing sorting algorithms in GPUs. Today, we are going to explore these strange and fascinating beasts.

In a sorting network, a list of numbers travel down idealized "wires" that are connected with so-called "comparators". Each comparator connects two wires and swaps the values between them if they're out of order (the smaller value going to the top wire, and the larger to the bottom wire). This image shows the principle clearly, and this image demonstrates a full run of a 4-wire sorting network wtih 5 comparators (both images courtesy of wikipedia, which has an excellent article on sorting networks if you are interested in learning more). Notice that the list on the right is correctly sorted top to bottom.

It is easy to see why that particular network correctly sorts a list of numbers: the first four comparators "float" the smallest value to the top and "sinks" the largest value to the bottom, and the final comparator sorts out the middle two values.

In general, however, there's often no easy way to tell whether or not a sorting network will actually correctly sort a list of numbers, and the only way to tell is to actually test it. This seems like a daunting task, since for a sorting network with N wires, there's N! (i.e. "N factorial") possible input permutations. That function grows extremely quickly, and become prohibitively large for even N of 14 or 15.
The zero-one principle

Thankfully, there's a better way, thanks to the so-called "zero-one principle", which is as follows:

    If an N-wire sorting network can correctly sort all 2N possible sequences of 0's and 1's, it will correctly sort all possible input sequences.

So, instead of having to try and check all N! possible permutations of the input sequence, we can just check all 2N sequences consisting of 0's and 1's. While this is still exponential, it is far smaller than N!.

Today, you will be given a sorting network and your challenge will be to check whether or not that network will correctly sort all inputs.
Formal inputs & outputs
Inputs

The input will first consist of a single line with two numbers on it separated by a space. The first number is the number of wires in the sorting network, and the second number is the total number of comparators on the network.

After that, there will follow a number of lines, each of which describes one comparator. The lines will consist of two numbers separated by a space describing which two wires the comparator connects. The first number will always be smaller than the second number

The "top" wire of the sorting network is wire 0, and the bottom wire is wire N-1. So, for a 16-wire sorting network, the top wire (which will hold the smallest number at the end, hopefully) is wire 0, and the bottom wire is wire 15 (which will hold the highest number at the end, hopefully).

Note that in most sorting networks, several comparators compare numbers in parallel. For the purposes of this problem, you can ignore that and assume that all comparators work in sequence, following the order provided in the input.
Output

The output will consist of a single line which will either be "Valid network" if the network will indeed sort all sequences correctly, or "Invalid network" if it won't.
Sample inputs and outputs

Input 1
This is the example 4-wire, 5-comparator sorting network from the description:
4 5
0 2
1 3
0 1
2 3
1 2

Output 1
Valid network

Input 2
8 19
0 2
1 3
0 1
2 3
1 2
4 6
5 7
4 5
6 7
5 6
0 4
1 5
2 6
3 7
2 4
3 5
1 2
3 4
6 7

Output 2
Invalid network


## HARD:

### 1guessing game

we all know the classic "guessing game" with higher or lower prompts. lets do a role reversal; you create a program that will guess numbers between 1-100, and respond appropriately based on whether users say that the number is too high or too low. Try to make a program that can guess your number based on user input and great code!

### 2stopwatch

Your mission is to create a stopwatch program. this program should have start, stop, and lap options, and it should write out to a file to be viewed later.

### 203minecraft
http://www.reddit.com/r/dailyprogrammer/comments/2xdqg0/2015227_challenge_203_hard_minecraft_there_and/
Description:
In the popular game Minecraft (http://en.wikipedia.org/wiki/Minecraft) you navigate a 3-D block world. Each block can be various types. You gather blocks to place blocks. More or less.
Part of the challenge is navigating this world such that you have to mine down and be able to get back up. So for this challenge we will be throwing at you some combined challenges to solve. Users can select which level of involvement. If you feel you have time or ability solve which challenges you can.
The 3 challenges to solve (Easy, Intermediate and Hard)
Generate a 3-D Minecraft Map with a fixed starting point and fixed point for the goal.
Navigate the map to find a shortest and safepath down and back again. (if possible)
Generate a 3-D map with a fixed starting point but a random end point. You must develop an agent program to seek out the unknown goal safely and return.
The Map
To generate a world we are going to keep our minecraft world simple. Each block can be the following:
Air - Basically nothing
Dirt - Block which can be removed
Sand - Block which can be removed but obeys differently than dirt
Lava - Dangerous block which we have to avoid. *Diamond block - Our goal block we wish to mine that block and leave air.

### 220SubstitutionCryptanalysis
A substitution cipher is one where each letter in the alphabet is substituted for another letter. It's like a Caesar shift cipher, but where every letter is ciphered independently. For example, look at the two rows below.

abcdefghijklmnopqrstuvwxyz
YOJHZKNEALPBRMCQDVGUSITFXW

To encode something, find the letter on the top row, and swap it with the letter on the bottom row - and vice versa. For example, the plaintext:

hello world

Becomes:

EZBBC TCVBH

Now, how would you go about decrypting something like this? Let's take another example, with a different key.

IAL FTNHPL PDDI DR RDNP WF IUD

You're also given the following hints: A is ciphered to H and O is ciphered to D. You know the text was in English, so you could plausibly use a word list to rule out impossible decrypted texts - for example, in the third words PDDI, there is a double-O in the middle, so the first letter rules out P being the letter Q, as Q is always followed by a U.

Your challenge is to decrypt a cipher-text into a list of possible original texts using a few letters of the substitution key, and whichever means you have at your disposal.
Input Description

On the first line of input you will be given the ciphertext. Then, you're given a number N. Finally, on the next N lines, you're given pairs of letters, which are pieces of the key. For example, to represent our situation above:

IAL FTNHPL PDDI DR RDNP WF IUD
2
aH
oD

Nothing is case-sensitive. You may assume all plain-texts are in English. Punctuation is preserved, including spaces.
Output Description

Output a list of possible plain-texts. Sometimes this may only be one, if your input is specific enough. In this case:

the square root of four is two

You don't need to output the entire substitution key. In fact, it may not even be possible to do so, if the original text isn't a pangram.
