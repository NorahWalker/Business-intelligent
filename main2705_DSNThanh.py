# Name: Dong Sy Nhat Thanh
# ID: GCS210033
# Class: GCS1003A

number_list = [i for i in range(1, 21)]

# Slicing 1st half and 2nd half
first_half = number_list[:len(number_list)//2]
second_half = number_list[len(number_list)//2:]

# Remove n elements from 1st list and 2nd list
n = int(input("Enter the value of n: "))
sublist = number_list[n:len(number_list)-n]

# Put those 2 elements above to a new list (2n elements)
new_list = number_list[:n] + number_list[-n:]

print("First half:", first_half)
print("Second half:", second_half)
print(f"The list after remove 2n elements:", sublist)
print(f"New list with:", new_list)
