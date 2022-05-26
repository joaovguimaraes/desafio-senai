a = [31, -41, 59, 26, -53, 58, 97, -93, -23, 84]

def joazinho(a,size):
     
    maximo =a[0]
    curr_max = a[0]
     
    for i in range(1,size):
        curr_max = max(a[i], curr_max + a[i])
        maximo = max(max_so_far,curr_max)
         
    return max_so_far
 
 
print(joazinho(a,len(a)))