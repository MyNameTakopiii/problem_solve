def fusion():
    cat_list = ['Siamese', 'Persian', 'Korat']
    word_list = []
    
    for i in range(3):
        word = str(input())
        word_list.append(word)
    
    result = word_list + cat_list
    
    return result

print(fusion())
        
