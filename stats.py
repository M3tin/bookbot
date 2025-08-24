def get_num_words(book_str):
    return len(book_str.split())

def get_num_chars(book_str):
    book_str=book_str.lower()
    char_dict={}
    for char in book_str:
        if char not in char_dict.keys():
            char_dict[char]=0
        char_dict[char]+=1
    return sort_by_occ_as_list(char_dict)

def num_sorter(items):
    return items["num"]

def sort_by_occ_as_list(dict):
    char_list=[]
    for char in dict:
        temp = {}
        temp["char"]=char
        temp["num"]=dict[char]
        char_list.append(temp)
    char_list.sort(reverse=True,key=num_sorter)
    return char_list
