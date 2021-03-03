'''
Implement the following functions based on the question. Retain the name of the functions, and parameters as is in the question. 


=================


1. string_max_length(strings_list) --> 30% 
Get a string list as input from the user and calculate the length of each string. Return the longest string. 
If multiple strings have same max value, return the first one.

------------------------------------------------

2. matrix_multiplication(matrix_1, matrix_2) --> 40%

----------------------------------------------------------------

3. working_numbers_set(input_list) --> 30% 
 
To the function, send an input list such that it has duplicates. Return a new list such that it has only unique elements from the list.

BONUS: If the function has only one line -- +20%

'''


def string_max_length(strings_list):
    longest_string=max(strings_list, key = len)
    
    return longest_string




def matrix_multiplication(matrix_1,matrix_2):
    #sorry but I have no clue how I would do this, I also don't even know the math clearly enough
    pass



def working_numbers_set(input_list):
    return set(input_list)

if __name__=="__main__":#string max length
    list_1=["hello","grape","hi","world","outsider"]
    print(f"The Original List is: {list_1}")
    string_1=string_max_length(list_1)
    print(f"The Longest String in the List is: {string_1}")
    pass



if __name__=="__main__":#working numbers set
    list_1=[14,23,14,89,98,23,23,89,98]
    print(f"List with Dupicates: {list_1}")
    new_list=working_numbers_set(list_1)
    print(f"List with Duplicates Removed: {new_list}")
    pass

