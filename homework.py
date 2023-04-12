# Exercise 1
# Given a list as a parameter,write a function that returns a list of numbers that are less than ten


# For example: Say your input parameter to the function is [1,11,14,5,8,9]...Your output should [1,5,8,9]


def my_list(list_items):
    new_list = []
    for i in list_items:
        if i < 10:
            new_list.append(i)
    
    print(new_list)

fred = [1,2,4,55,44,33,3,2]

my_list(fred)

# Exercise 2
# Write a function that takes in two lists and returns the two lists merged together and sorted
def combined_list(ted, bob):
    bill = ted + bob
    bill = sorted(bill)
    print(bill)

ted = [1,2,3,4,5,6]
bob = [11,22,3,2,1,44,]
combined_list(ted,bob)





                
    

