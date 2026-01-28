## unpack the following list into 3 variables


# the first variable should contain the first element
# the second variable should contain the second element
# the last variable should contain _the rest of the elements_

## hint: use the * unpacking operator.


def unpacking_values(my_list):
    
    a,b,*c=my_list
    print(a)
    print(b)
    print(c)

print(unpacking_values([1, 2, 3, 1, 23, 12, 31, 2, 2, 2, 2, 3, 2, 3, 2, 3, 2, 3, 21, 2, 3, 1]))

        
            
        
        

# def my_fun(name,last_name,*ages):
#     sum_ages=0
#     for i in ages:
#         sum_ages+=i
#     print(f"Hello {name} {last_name} these is the sum of your ages {sum_ages}")

# my_fun("Alejandro","Mohan",1,2,3,23,4,45,7,2,2,9,2,4)
