


def string_to_list(strg):
    strg = strg.split()  # 2 + 3 * 5 - 6 / 8
    for i in range(len(strg)):
        if strg[i].isdigit() == True: strg[i] = int(strg[i])
    return strg


def calc(list):
    res = 0
    while '/' in list:
        i = list.index('/')
                
        res = (list[i-1])/(list[i+1])
        
        del list[(i-1):(i+2)]
        list.insert(i-1,res)

    
    while  '*' in list:
        i = list.index('*')
                
        res = (list[i-1])*(list[i+1])
        
        del list[(i-1):(i+2)]
        list.insert(i-1,res)

        
    while  '-' in list:
        i = list.index('-')
                
        res = (list[i-1])-(list[i+1])
        
        del list[(i-1):(i+2)]
        list.insert(i-1,res)

    while  '+' in list:
        i = list.index('+')
                
        res = (list[i-1])+(list[i+1])
        
        del list[(i-1):(i+2)]
        list.insert(i-1,res)   
    res = str(list)
    return res