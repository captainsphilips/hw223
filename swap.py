def swap_list(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list
    
    
List = [1,2,3,4,5,6]


  


pos1, pos2  = 3 , 6
 
print(swap_list(List, pos1-1, pos2-1))