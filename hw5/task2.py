# Создайте программу для игры в ""Крестики-нолики"" человек vs человек.
# 1 | 2 | X
# 4 | X | O
# X | 8 | O



def print_table (list):
    print(f"{list[0]} | {list[1]} | {list[2]}")
    print(f"{list[3]} | {list[4]} | {list[5]}")
    print(f"{list[6]} | {list[7]} | {list[8]}")


def exam_win (list):
      if  (list[0] == list[1] == list[2]   or
           list[3] == list[4] == list[5]  or  
           list[6] == list[7] == list[8]  or
           list[0] == list[3] == list[6]  or
           list[1] == list[4] == list[7]  or
           list[2] == list[5] == list[8]  or
           list[0] == list[4] == list[8]  or
           list[2] == list[4] == list[6] ):
           return True


table = [1,2,3,4,5,6,7,8,9]
count_pl1 = 0
count_pl2 = 0
count = 0

print_table(table)

while count !=9  or  exam_win(table) == True: 
    while count_pl1 != 1:
        if exam_win(table) == True or count == 9: break  
        move_pl1 = int(input(" Игрок 1 введите позицию вашего хода "))
        if table[move_pl1-1] != "X" and table[move_pl1-1] != "O":
            table[move_pl1-1] = "X"
            count_pl1 = 1
            count_pl2 = 0
            count +=1
            print_table(table)
            
          
        else: print("позиция занята ")
    
        
    if exam_win(table) == True: break  


    while count_pl2 != 1:
        if exam_win(table) == True or count == 9: break  
        move_pl2 = int(input(" Игрок 2 введите позицию вашего хода "))
        
        if table[move_pl2-1] != "X" and table[move_pl2-1] != "O":
            table[move_pl2-1] = "O"
            count_pl1 = 0
            count_pl2 = 1
            count +=1
            print_table(table)
            
          
        else: print("позиция занята ")
        
    

if exam_win(table) == True: 
    if count_pl1 == 1: print("player1 Win!")
    elif count_pl2 == 1: print("player2 Win!") 
else: print("Победила дружба!")   

