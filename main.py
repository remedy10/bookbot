def sort_on(d):
    return d["num"]

def create_report(my_dict):
    # sorted_dict=sorted(my_dict.items(),key=lambda x:x[1]),
    # this code is recommended from tabnine ai but i can't figure out how that works
    print(my_dict)
    sorted_list = []
    for ch in my_dict:
        sorted_list.append({"char": ch, "num": my_dict[ch]})
    sorted_list.sort(reverse=True, key=lambda x: x["num"])
    #I discovered that
    return sorted_list

with open("books/frankenstein.txt")as f:
    contents=f.read()
    words=contents.split()
    char_dict=dict()
    for word in contents:
        if not word.isalpha():
            continue
        lowered=word.lower()
        if lowered not in char_dict:
            char_dict[lowered]=1
            continue
        char_dict[lowered]+=1
    sorted_list=create_report(char_dict)
    for char in sorted_list:
        print(f"The '{char['char']}' character was found {char['num']} times")
        
    
