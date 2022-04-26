'''
##########
Lab 4.05
##########

1. Read through the following code
    def print_numbers(list):
        for i in range(1, len(list)+1):
            print(list[i])
​
    num_list = [1, 2, 3, 4, 5, 6]
    print_numbers(num_list)
In your notebook
Write down any bugs that you see in the program
- it does not call the function 
- object of type has no len
- list index is out of range

2. Read through the following code
    def swapping_stars():
    line_str = ""
        for line in range(0, 6):
            for char in range(0,6):
                if line % 2 == char % 2:
                    line_str += "*"
                else:
                    line_str += "-"
    print(line_str)
Continue in your notebook
Write down any bugs that you see in the program
- it does not call the function
- for should not be indented 
- need to change char in range to (0, 5)

3. In script mode
Fix the 2 programs above.
Create a program that asks the user which function they would like to run.
'''

num_list = [1, 2, 3, 4, 5, 6]
def print_numbers(list):
   for i in range(0, len(list) +1):
        print(list[i])

print_numbers(num_list)

def swapping_stars():
    line_str = ""
    for line in range(0, 6):
            for char in range(0,5):
                if line % 2 == char % 2:
                    line_str += "*"
                else:
                    line_str += "-"
    print(line_str)


user_input = input("Which function would you like to run: print numbers or swapping stars? ")

if user_input == 'print numbers':
    print_numbers(list)
elif user_input == 'swapping stars':
    swapping_stars()
else:
    print("Sorry, that is not an option!")