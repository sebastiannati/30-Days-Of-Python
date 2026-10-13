

from random import random,randint,shuffle
import string

def random_user_id():
    user_id = ""
    char = string.ascii_letters
    for i in range(6):
        # 50% of chance to get a string and 50% to get a number
        if random() > 0.25:
            random_char = randint(0,len(char)-1)
            random_str = char[random_char]
        else:
            random_str = randint(0,9)
        
        user_id += str(random_str)
            
    return user_id

def user_id_gen_by_user():
    nb_chars = int(input(" \t\t Enter the lenght of the user_id : "))
    nb_ids = int(input("  \t\t Enter the number of IDs to generate : "))
    ids = []
    char = string.ascii_letters
    for i in range(nb_ids):
        user_id_i = ""
        for j in range(nb_chars):
            # 50% of chance to get a string and 50% to get a number
            if random() > 0.25:
                random_char = randint(0,len(char)-1)
                random_str = char[random_char]
            else:
                random_str = randint(0,9)
        
            user_id_i += str(random_str)
        ids.append(user_id_i)
            
    return ids
    

def rgb_color_gen():
    res = "rgb("
    for i in range(3):
        res += str(randint(0,255))
        if i < 2:
            res+=','
    res+=")"
    return res

def list_of_hexa_colors(number):
    letters = string.ascii_letters[:6]
    hexas = []
    for i in range(number):
        hexa_i = "#"
        for i in range(6):
            # 50% of chance to get a string and 50% to get a number
            if random() > 0.25:
                random_char = randint(0,len(letters)-1)
                random_str = letters[random_char]
            else:
                random_str = str(randint(0,9))
            
            hexa_i += random_str
        hexas.append(hexa_i)
    return hexas

def list_of_rgb_colors(number):
    rgbs = []
    for i in range(number):
        rgbs.append(rgb_color_gen())
    return rgbs

def generate_colors(mode="hexa", number = 1):
    if mode == "hexa":
        return list_of_hexa_colors(number)
    elif mode == "rgb":
        return list_of_rgb_colors(number)
    else:
        print("Not a format of colors")
        return []

def shuffle_list(liste):
    
    return shuffle(liste)
    
def random_sequence():
    res = []
    while len(res) < 7:
        new_n = randint(0,9)
        if new_n in res:
            continue
        res.append(new_n)
    return res
