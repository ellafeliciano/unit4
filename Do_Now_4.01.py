Do Now 4.01

1. In your console
Type the following Code
    single_fruit = ['apple', 'banana', 'watermelon', 'grape']
    multi_fruit = []
    multi_fruit.append(single_fruit[0] + 's')
    multi_fruit.append(single_fruit[1] + 's')
    multi_fruit.append(single_fruit[2] + 's')
    multi_fruit.append(single_fruit[3] + 's')
    print(multi_fruit)

In your notebook
Respond to the following
Briefly write down what happened. What would happen if you added 100 items to the list single_fruit? It printed all the fruits in the list. 
Write down how you would update multi_fruit.

2. In your console
Type the following
    list_of_numbers = [3, 5, 10, 23]
    for num in list_of_numbers:
        print(f"num is " + {num})
        
Continue in your notebook
Respond to the following
Briefly write down what happened. How would this change if you added 100 items to list_of_numbers? It printed all the numbers in the list. 

3. In your console
Rewrite the code from part 1 using knowledge from part 2.

print(single_fruit)
multi_fruit = []
for item in single fruit:
    print(f"{item}s")

for item in single_fruit:
    multi_fruit.append(f"{item}s")
print(multi_fruit) 

for item in multi_fruit:
    print(item)

for i in range(5):
    print(i)

for i in range(len(multi_fruit)):
    print(multi_fruit[i])
