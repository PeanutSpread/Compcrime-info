
""""
input_num = int(input("Please enter a number: "))
input_num_2 = int(input("Please enter a number: "))

num = input_num - input_num_2

if num >= 0:
    print (input_num,"is bigger.")
else:
    print (input_num_2,"is bigger.")
    
"""

"""
input_num = int(input("Please enter a number: "))
input_num_2 = int(input("Please enter a number: "))
input_num_3 = int(input("Please enter a number: "))

num = input_num - input_num_3
num_2 = input_num - input_num_2
num_3 = input_num_2 - input_num_3


if num_2 >= 0:
        print (input_num,"is bigger.")
elif  num >= 0:
        print (input_num,"is bigger.")
elif num_3 >= 0:
        print (input_num_2,"is bigger")
else:
        print (input_num_3,"is bigger.")
"""

input_num = int(input("Please enter a number: "))
input_num_2 = int(input("Please enter a number: "))
input_num_3 = int(input("Please enter a number: "))

num = input_num - input_num_3
num_2 = input_num - input_num_2
num_3 = input_num_2 - input_num_3


if num_2 >= 0:
        if num_3 >= 0:
                print (input_num)
                print (input_num_2)
                print (input_num_3)
        else:
                print (input_num)
                print (input_num_3)
                print (input_num_2)
                
elif  num >= 0:
        if num_3 >= 0:
                print (input_num) 
                print (input_num_2)
                print (input_num_3)
        else:
                print (input_num)
                print (input_num_3)
                print (input_num_2)
                
elif num_3 >= 0:
        print (input_num_2)
        print (input_num_3)
        print (input_num)
else:
        print (input_num_3)
        print (input_num_2)
        print (input_num)