#//GROUP MEMBBERS
#// MUA EMMANUEL CIT-227-011/2021
#// JUDE TULEL CIT-227-023/2021
#// VICTOR KIARIE CIT-227-026/2021
#// KIMEU SOLIDAD CIT-227-012/2021

import random
import time

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = random.choice(arr)
        less = [x for x in arr if x < pivot]
        equal = [x for x in arr if x == pivot]
        greater = [x for x in arr if x > pivot]
        return quicksort(less) + equal + quicksort(greater)

# Function to measure the time taken by quicksort
def time_quicksort(arr):
    start_time = time.time()
    sorted_list = quicksort(arr)
    end_time = time.time()
    return sorted_list, end_time - start_time

# Get user input for the number of elements to sort
try:
    num_elements = int(input("Enter the number of elements to sort: "))
except ValueError:
    print("Please enter a valid integer.")
    exit()

# Generate a list of random numbers for sorting
my_list= [random.randint(1, 10000) for _ in range(num_elements)]

# Perform quicksort and measure time
sorted_list, time_taken = time_quicksort(my_list)

# Display results
print("Original list(Random selected values):",my_list)
print("Sorted list:", sorted_list)
print("Time taken:", time_taken, "seconds")