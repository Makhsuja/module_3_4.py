def  single_root_words(root_word,  *other_words):
    same_words = []
    for i in other_words:
        if i.lower().startswith(root_word.lower()) or root_word.lower().startswith(i.lower()):
            same_words.append(i)
    return same_words



print(single_root_words('rich' ,'richiest', 'orichalcum', 'cheers', 'richies' ))
print(single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel'))
