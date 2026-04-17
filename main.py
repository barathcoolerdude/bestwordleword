import string
from linked_list import Linkedlist

def main():
    # read the valid words
    with open("wordlewords.txt") as file:
        lines = [line.strip() for line in file]
        
    # list to store the linkedlist
    linkedlist = []
    
    # create dict to store letters and count
    for i in range(5):
        counts = {letter: 0 for letter in string.ascii_lowercase}
        # print(counts)
        for word in lines:
            if word[i] in counts:
                counts[word[i]] += 1

        # letters of count printed out
        # print(counts)

        # make a linked list
        li = Linkedlist()
    
        for letter, number in counts.items():
            li.append(letter, number)

        # add linkedlist to list
        linkedlist.append(li)

    # for linked in linkedlist:
    #     print(linked.display())

    # scores each word 
    
    word_score_list = {}
    for word in lines:
        score = 0
        for i in range(5):
            number = linkedlist[i].find(word[i])
            score += number
        word_score_list[word] = score


    # sorting words as pre scores
    sorted_list = sorted(word_score_list.items(), key=lambda x:x[1],reverse = True)

    # finding the best first word
    for word in sorted_list:
        if len(set(word[0])) == 5:
            print(f"{word[0]} : {word[1]}") 
            break
            
        
if __name__ == "__main__":
    main()