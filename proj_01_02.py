
"""
Lab set 01 - Project 01 - Re-acquainting with Python

01.02 - 10 pts.
"""

# First let's try reading in and displaying the sonnets.

# Read in the file for all the sonnets along with the header and footer garbage
sonnets = open("wssnt10.txt", "r")
# print the number of lines in the file
line_count = 0
sonnet_list = []
for line in sonnets:
    line_count += 1
    line = line.rstrip("\n")
    sonnet_list.append(line)
print("There are",line_count,"lines in the file.")
# Print the entire sonnet file to the console, without the extra line breaks!
for line in sonnet_list:
    print(line)






