# Destiny Mendez
# 05/08/2024

# creating an empty list
lst = []

# Using a forloop to add the numbers 1-100 to the list
for b in range(1, 101):
    lst.append(b)

# printing the list lst
print(lst)

# creating an empty list named odd
odd = []

# Using a forloop to add the odd numbers 1-100 to the list odd
for b in range(1, 101, 2):
    odd.append(b)

# printing the list odd
print(odd)

# creating an empty list named even
even = []

# using a forloop to add the even numbers 1-100 to the list even
for b in range(2, 101, 2):
    even.append(b)

# printing the list even
print(even)

#create a variable named b that points to the first list you created
b=lst

#create a variable named joined that joins the even and odd lists using an operator
joined=even+odd

