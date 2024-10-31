#Your code goes here. 

import math

def safe_divide(a, b):
#example with b= 0
 
    try:
        #attempt to perform division
        return a/b 
    except ZeroDivisionError: 
        return #cannot divide by ZERO
      

#def process_list(input_list):
#sum of squares

#inisalising list
 #test_list= [1,2,3,4,5,6,7,8,9,10]

 #print orginal list
 #print("The original list is : " + str(test_list))

 # using list comprehension
# sum of squares
    # try:
    #     res = sum([i**2 for i in test_list])
    #     expect:



#def nested_operations(a, b):


#def process_input():


main()
    print(safe_divide(10, 2))
    print(safe_divide(10, 0))
    # print(process_list([1, '2', 3, 'four', 5]))    
    # print(nested_operations(16, 4))
    # print(nested_operations(10, 0))
    # print(nested_operations('a', 5))
    # process_input()

