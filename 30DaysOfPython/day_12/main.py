from modules import *


if __name__ == "__main__":

    print("\n","-"*30,"Exercice: Level 1", "-"*30,"\n")

    print(f"1.\t Generated user_id : {random_user_id()}")

    print(f"2.\t Generated ids by the user : {user_id_gen_by_user()}")

    print(f"3.\t Random rgb : {rgb_color_gen()}")



    print("\n","-"*30,"Exercice: Level 2", "-"*30,"\n")

    print("1.\t List of 3 hexas : ",list_of_hexa_colors(3))

    print(f"2.\t List of 3 random rgb : {list_of_rgb_colors(3)}")

    print(f"3.\t 3 or 1 generated colors using hexa and rgb :\n\t\t {generate_colors('hexa', 3)}\n\t\t {generate_colors('hexa', 1)}\n\t\t {generate_colors('rgb', 3)}\n\t\t {generate_colors('rgb', 1)}")



    print("\n","-"*30,"Exercice: Level 3", "-"*30,"\n")
    
    liste = [1,2,3,4,5]
    
    print(f"1.\t Suffleling the list : {shuffle_list(liste)}")
            
    print(f"2.\t Random array of 7 unique digits : {random_sequence()}")
