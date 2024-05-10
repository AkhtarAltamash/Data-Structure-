# import array as ar

# arr = ar.array('i', [1, 2, 3, 4, 5, 6]) 
# # print(arr1)

# for i in range(0, len(arr)):
#     print(arr[i],end=" ")


# ________________

# Static Array Example
static_array = [1, 2, 3, 4, 5]  # Creating a static array of size 5
print("Static Array:", static_array)

print("___________________________")

# Dynamic Array Example
dynamic_array = []  # Creating an empty dynamic array
print("Initial Dynamic Array:", dynamic_array)

# Appending elements dynamically
dynamic_array.append(10)
dynamic_array.append(2)
dynamic_array.append(30)
dynamic_array.append(4)
dynamic_array.append(50)
print("Dynamic Array After Appending:", dynamic_array)

# Removing elements dynamically
dynamic_array.pop()  # Remove the last element
print("Dynamic Array After Removing:", dynamic_array)
dynamic_array.append(90)
print(dynamic_array)