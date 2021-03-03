import random

'''
Implement the following functions based on the question. Retain the name of the functions, and parameters as is in the question. 

=================


1. construct_matrix(m, n) --> 30% 
Get the row and column of matrix, and return a Matrix with random float values.  

------------------------------------------------

2. return_below_n(input_list, value) --> 40%
 
Get an input list with random values, and a value from the user. Create another list with only values lesser than value and return it to the user. 

----------------------------------------------------------------

3. search_for_item(input_list, item) --> 30% 

Generate an input array and get an input for a number to search from the user. Return the index in which the item is found, or return -1 if not found. 


'''

def construct_matrix(m,n):
    matrix=[]
    for i in range(m):
        temp_row=[]
        for j in range(n):
            temp_row.append(random.randint(1,50))
        matrix.append(temp_row)
    return matrix
    

n=6
input_list=[]
for i in range(n):
        input_list.append(random.randint(1,1000))
print(input_list)
new_list=[]
def return_below_n(input_list,value):
    for i in range(n):
        new_list.append(random.randint(1,value))
    pass

def search_for_item(input_list,item):
    if item in input_list:
        index=input_list.index(item)
        return index
    else:
        return False
    pass


if __name__=="__main__":#construct matrix
    m=int(input("How many Rows Should the Matrix Have?: "))
    n=int(input("How many Columns Should the Matrix Have?: "))
    matrix_1=construct_matrix(m,n)
    print(matrix_1)
    pass


if __name__=="__main__":#return below n

    value=int(input("Enter a Number for the List. The Second List Will be Smaller than this Number: "))
    return_below_n(input_list,value)
    print(new_list)



if __name__=="__main__":# search for item
    print(f"Here is a Randomly Generated List:{input_list}")
    item=int(input("Enter a Number from the List: "))
    
    search_for_item(input_list,item)
    if "index":
        print(f"The Index is: {search_for_item(input_list,item)}.")
    if item not in input_list:
        print(-1)
    


