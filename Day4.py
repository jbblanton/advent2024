'''
As the search for the Chief continues, a small Elf who lives on the station tugs on your shirt; she'd like to know if you could help her with her word search (your puzzle input). She only has to find one word: XMAS.

This word search allows words to be horizontal, vertical, diagonal, written backwards, or even overlapping other words. It's a little unusual, though, as you don't merely need to find one instance of XMAS - you need to find all of them. Here are a few ways XMAS might appear, where irrelevant characters have been replaced with .:


..X...
.SAMX.
.A..A.
XMAS.S
.X....
The actual word search will be full of letters instead. For example:

MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
In this word search, XMAS occurs a total of 18 times; here's the same word search again, but where letters not involved in any XMAS have been replaced with .:

....XXMAS.
.SAMXMS...
...S..A...
..A.A.MS.X
XMASAMX.MM
X.....XA.A
S.S.S.S.SS
.A.A.A.A.A
..M.M.M.MM
.X.X.XMASX
Take a look at the little Elf's word search. How many times does XMAS appear?
'''

# Open the input
# Loop. If it's an X, check surrounding for M
#    If found, note direction, move one further and check for A
#        If found, continue in same direction checking for S
# Count found XMAS instances


# with open("test_day4.txt", "r") as f:
#     data = f.read().splitlines()
with open("day4_input.txt", "r") as f:
    data = f.read().splitlines()

# print(data)
# ['MMMSXXMASM', 'MSAMXMSMSA', 'AMXSXMAAMM', 'MSAMASMSMX', 'XMASAMXAMM', 'XXAMMXXAMA', 'SMSMSASXSS', 'SAXAMASAAA', 'MAMMMXMMMM', 'MXMXAXMASX']

total_hor = 0
total_ver = 0
total_dr = 0
total_dl = 0
total_ur = 0
total_ul = 0

direction = ''

# Lines 0,1,2 can only search R, L, D, DR, DL
# Lines -1,-2,-3 can only search R, L, U, UR, UL
# Columns 0,1,2 can only search D, U, R, DR, UR
# Columns -1,-2,-3 can only search D, U, L, DL, UL
# Otherwise, search all 8 directions D, U, L, R, DR, DL, UR, UL


# MMMSXXMASM
# MSAMXMSMSA
# AMXSXMAAMM
# MSAMASMSMX
# XMASAMXAMM
# XXAMMXXAMA
# SMSMSASXSS
# SAXAMASAAA
# MAMMMXMMMM
# MXMXAXMASX

# ....XXMAS.
# .SAMXMS...
# ...S..A...
# ..A.A.MS.X
# XMASAMX.MM
# X.....XA.A
# S.S.S.S.SS
# .A.A.A.A.A
# ..M.M.M.MM
# .X.X.XMASX


rows = len(data)
cols = len(data[0])

# Loop through the data
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == 'X':
            # print(f"Checking at {i},{j}")
            # print(data[i][j])

            # Horizontal search, forward and backward
            if j+3 < cols:
                if data[i][j+1] == 'M' and data[i][j+2] == 'A' and data[i][j+3] == 'S':
                    # print(f"XMAS found hor-for at {i},{j} to {i},{j+3}")
                    total_hor += 1
            if j-3 >= 0:
                if data[i][j-1] == 'M' and data[i][j-2] == 'A' and data[i][j-3] == 'S':
                    # print(f"SAMX found hor-back at {i},{j-3} to {i},{j}")
                    total_hor += 1

            # Vertical search, up and down
            if i+3 < rows:
                if data[i+1][j] == 'M' and data[i+2][j] == 'A' and data[i+3][j] == 'S':
                    # print(f"XMAS found vert-down at {i},{j} to {i+3},{j}")
                    total_ver += 1
            if i-3 >= 0:
                # print(data[i][j], data[i-1][j], data[i-2][j], data[i-3][j])
                if data[i-1][j] == 'M' and data[i-2][j] == 'A' and data [i-3][j] == 'S':
                    # print(f"SAMX found vert-up at {i-3},{j} to {i},{j}")
                    total_ver += 1

            # Diagonal search, down-right 
            if i+3 < rows and j+3 < cols:
                if data[i+1][j+1] == 'M' and data[i+2][j+2] == 'A' and data[i+3][j+3] == 'S':
                    # print(f"XMAS found diag-dr at {i},{j} to {i+3},{j+3}")
                    # print(data[i+1][j+1], data[i+2][j+2], data[i+3][j+3])
                    total_dr += 1

            # Diagonal search, down-left 
            if i+3 < rows and j-3 >= 0:
                if data[i+1][j-1] == 'M' and data[i+2][j-2] == 'A' and data[i+3][j-3] == 'S':
                    # print(f"XMAS found diag-dl at {i},{j} to {i+3},{j-3}")
                    total_dl += 1

            # Diagonal search, up-left
            if i-3 >= 0 and j-3 >= 0:
                if data[i-3][j-3] == 'S' and data[i-2][j-2] == 'A' and data[i-1][j-1] == 'M':
                    # print(f"SAMX found diag-ul at {i-3},{j-3} to {i},{j}")
                    # print(data[i-3][j-3], data[i-2][j-2], data[i-1][j-1])
                    total_ul += 1

            # Diagonal search, up-right
            if i-3 >= 0 and j+3 < rows:
                if data[i-3][j+3] == 'S' and data[i-2][j+2] == 'A' and data[i-1][j+1] == 'M':
                    # print(f"SAMX found diag-ur at {i-3},{j+3} to {i},{j}")
                    total_ur += 1

        else:
            continue

# print(total_hor)
# print(total_ver)
# print(total_dr)
# print(total_dl)
# print(total_ur)
# print(total_ul)
print(total_hor + total_ver + total_dr + total_dl + total_ur + total_ul)  # 2633


'''
The Elf looks quizzically at you. Did you misunderstand the assignment?

Looking for the instructions, you flip over the word search to find that this isn't actually an XMAS puzzle; it's an X-MAS puzzle in which you're supposed to find two MAS in the shape of an X. One way to achieve that is like this:

M.S
.A.
M.S
Irrelevant characters have again been replaced with . in the above diagram. Within the X, each MAS can be written forwards or backwards.

Here's the same example from before, but this time all of the X-MASes have been kept instead:

.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
..........
In this example, an X-MAS appears 9 times.

Flip the word search from the instructions back over to the word search side and try again. How many times does an X-MAS appear?
'''

# Search for MAS in diagonal directions only
# Track where the A is found as tuples (i,j)
# Count shared A locations

dr = []
dl = []
ur = []
ul = []

for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == 'M':
            # Diagonal search, down-right 
            if i+2 < rows and j+2 < cols:
                if data[i+1][j+1] == 'A' and data[i+2][j+2] == 'S':
                    dr.append((i+1,j+1))

            # Diagonal search, down-left 
            if i+2 < rows and j-2 >= 0:
                if data[i+1][j-1] == 'A' and data[i+2][j-2] == 'S':
                    dl.append((i+1,j-1))

            # Diagonal search, up-right
            if i-2 >= 0 and j+2 < cols:
                if data[i-1][j+1] == 'A' and data[i-2][j+2] == 'S':
                    ur.append((i-1,j+1))

            # Diagonal search, up-left
            if i-2 >= 0 and j-2 >= 0:
                if data[i-1][j-1] == 'A' and data[i-2][j-2] == 'S':
                    ul.append((i-1,j-1))

# print(dl, dr, ul, ur)

all_a = dr + dl + ur + ul
shared = []
# print(all_a)
print(len(all_a))

for i in all_a:
    # print(i, all_a.count(i))
    if all_a.count(i) == 2:
        shared.append(i)

# print(shared)
print(len(shared))  # 

total = len(shared) // 2    
print(total)  # 1936