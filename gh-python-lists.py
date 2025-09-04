# in-class exercise for Lecture 03 List

# 1. Fill in the missing code to produce the output: ['honda', 'yamaha', 'suzuki', 'kawasaki']
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
#<<insert your missing code here>>
del motorcycles[-1]
motorcycles.append("kawasaki")
#print(motorcycles)


# 2. Please double each element in the list 
my_list = [1, [4, 6, 12], 7, 8]
#<<insert your missing code here>>
my_list = my_list + my_list
#print(my_list)

# 3. Fill in the code to produce the following output:  [3, 6, 99, 45, 29, 34] 
#    You can insert multiple lines of code, obtain target_list based on list1 and list2
list1 = [3,6,99,12]
list2 = [64,45,29,34]
#<<Insert your code here>>
del list1[3]
del list2[0]
target_list = list1 + list2
#target_list = [] # comment out this line 
#print(target_list)

# Try it yourself exercise
# 3-8. Seeing the World: Think of at least five places in the world you’d like to visit
# (1) Store the locations in a list
places_To_Visit = ["shanghi", "greece", "romaina", "italy", "scotland"]
# (2) Print your list in its original order
print(places_To_Visit)
# (3) Print your list in alphabetical order without modifying the actual list
sorted_places_To_Visit = sorted(places_To_Visit)
#places_To_Visit.sort()
print(sorted_places_To_Visit)
#print(places_To_Visit)
# (4) Show that your list is still in its original order by printing it
print(places_To_Visit)
# (5) Change the order of your list in reverse order and print it
places_To_Visit.reverse()
print(places_To_Visit)
# (6) Change your list so it’s stored in reverse-alphabetical order, and print it 
places_To_Visit.sort(reverse=True)
print(places_To_Visit)
# 4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive. 
for value in range (1,21):
    print(value)
print("\n")
# 4-7. Threes: Make a list of the multiples of 3, from 3 to 30. Use a for loop to print the numbers in your list. 
for value in range(1,11):
    print(value*3)
print("\n")
# 4-8. Cubes: A number raised to the third power is called a cube. For example, the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), and use a for loop to print out the value of each cube. 
for value in range(1,11):
    print(value**3)
print("\n")
# 4-9. Cube Comprehension: Use a list comprehension to generate a list of the first 10 cubes.
cubes = []
for value in range (0,11):
    cubes.append(value**3)
print(cubes)


# in-class code
import copy

list1 = [1, 2, 3, 4, ["a", "b"]]
list2 = list1 # list1 -> list 2
list3 = list1[:] #makes a copy
list4 = list1.copy() #mnakes a copy
list5 = copy.copy(list1) #new copy
list6 = copy.deepcopy(list1) #related to old coppy

list2.append(5)
list3[4].append("c") 
list4[0] = 100
list5[4][-1] = "w" 
list6[-1].append("c")


# discuss the answers befor runing the following code
print(f"list1: {list1}") # [1,2,3,4,[a,b],c,5]
print(f"list2: {list2}") # [1,2,3,4,[a,b,c], 5]
print(f"list3: {list3}") # [1,2,3,4,[a,b,w]]
print(f"list4: {list4}") # [100, 2, 3, 4, ['a', 'b', 'w']]
print(f"list5: {list5}")  # [1,2,3,4,[a,b,w]]
print(f"list6: {list6}") # [1,2,3,4,[a,b,c]]
