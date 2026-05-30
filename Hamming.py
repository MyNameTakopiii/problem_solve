def hamming(word_1:str, word_2:str):
    hamming = 0

    for i in range(len(word_1)):
        if word_1[i] != word_2[i]:
            hamming += 1
    
    print(hamming)

word1 = str(input())
word2 = str(input())
hamming(word1, word2)