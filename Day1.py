'''
Pair up the smallest number in the left list with the smallest number in the right list, then the second-smallest left number with the second-smallest right number, and so on.

Within each pair, figure out how far apart the two numbers are; you'll need to add up all of those distances. For example, if you pair up a 3 from the left list with a 7 from the right list, the distance apart is 4; if you pair up a 9 with a 3, the distance apart is 6.

In the example list above, the pairs and distances would be as follows:

The smallest number in the left list is 1, and the smallest number in the right list is 3. The distance between them is 2.
The second-smallest number in the left list is 2, and the second-smallest number in the right list is another 3. The distance between them is 1.
The third-smallest number in both lists is 3, so the distance between them is 0.
The next numbers to pair up are 3 and 4, a distance of 1.
The fifth-smallest numbers in each list are 3 and 5, a distance of 2.
Finally, the largest number in the left list is 4, while the largest number in the right list is 9; these are a distance 5 apart.
To find the total distance between the left list and the right list, add up the distances between all of the pairs you found. In the example above, this is 2 + 1 + 0 + 1 + 2 + 5, a total distance of 11!

Your actual left and right lists contain many location IDs. What is the total distance between your lists?
'''

left_column = []
right_column = []

# Open input and build lists
with open('day1_input.txt', 'r') as f:
    for line in f:
        line = line.strip().split('  ')
        left_column.append(int(line[0]))
        right_column.append(int(line[-1]))

# Sort the lists
left_column.sort()
right_column.sort()

# Subtract left from right, taking absolute value
total = 0
for i in range(len(left_column)):
    total +=  abs(left_column[i] - right_column[i])

# Output the total
print(total)  # 2367773


'''
This time, you'll need to figure out exactly how often each number from the left list appears in the right list. Calculate a total similarity score by adding up each number in the left list after multiplying it by the number of times that number appears in the right list.

Here are the same example lists again:

3   4
4   3
2   5
1   3
3   9
3   3
For these example lists, here is the process of finding the similarity score:

The first number in the left list is 3. It appears in the right list three times, so the similarity score increases by 3 * 3 = 9.
The second number in the left list is 4. It appears in the right list once, so the similarity score increases by 4 * 1 = 4.
The third number in the left list is 2. It does not appear in the right list, so the similarity score does not increase (2 * 0 = 0).
The fourth number, 1, also does not appear in the right list.
The fifth number, 3, appears in the right list three times; the similarity score increases by 9.
The last number, 3, appears in the right list three times; the similarity score again increases by 9.
So, for these example lists, the similarity score at the end of this process is 31 (9 + 4 + 0 + 0 + 9 + 9).

Once again consider your left and right lists. What is their similarity score?
'''

similarity_score = 0
unique_left = []

# Loop the left, count its occurence in the right, and calculate the similarity score
for i in range(len(left_column)):
    count = right_column.count(left_column[i])
    similarity_score += left_column[i] * count
    # Collect a list of unique numbers in the left list
    if not count == 0:
        unique_left.append(left_column[i])

print('Similarity score: ')
print(similarity_score)  # 21271939

# Output the unique numbers in the left list
print('Unique left: ')
print(unique_left)

# [13958, 14216, 14521, 20405, 23131, 26386, 29422, 32104, 35057, 35819, 43948, 44088, 46924, 47057, 47438, 54539, 55364, 57168, 57702, 58014, 62129, 66940, 67828, 67927, 70030, 73266, 74331, 77151, 82701, 83861, 85199, 85851, 88787, 92129, 93643, 96240, 98740]