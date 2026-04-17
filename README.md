This is a project on finding the best words you can use in wordle that will give the maximum chances of finding the word.

There are 14,000 valid words in wordle, our goal is to find the first few words that will give you the most chances of finding the word of the day.

How are we finding the best word? 

We will use a scoring system. based on "what is the probability of a letter occuring in this position?".

for each word in the wordle list we will get a score. thats how we find the best possible word.

detailed steps:
create linked list for each position in the word
like for poisiton 1 create a linked list has with node the letter and the number of times it has appeared in that position