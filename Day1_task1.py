# Make 2 lists, right and left
# Sort ascending
# loop each, subtract left from right
# total the values

left_column = []
right_column = []

# Open day1_input.txt and read text
with open(day1_input.txt, 'r') as f:
    for line in f:
        print(line)
        line = line.strip().split(' ')
        left_column.append(int(line[0]))
        right_column.append(int(line[1]))

# Sort the lists
left_column.sort()
right_column.sort()
print(left_column[0])
print(left_column[-1])

# Subtract left from right
total = 0
for i in range(len(left_column)):
    total += right_column[i] - left_column[i]

# Output the total
print(total)


