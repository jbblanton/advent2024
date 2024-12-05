'''
All of the instructions have been jumbled up!

It seems like the goal of the program is just to multiply some numbers. It does that with instructions like mul(X,Y), where X and Y are each 1-3 digit numbers. For instance, mul(44,46) multiplies 44 by 46 to get a result of 2024. Similarly, mul(123,4) would multiply 123 by 4.

However, because the program's memory has been corrupted, there are also many invalid characters that should be ignored, even if they look like part of a mul instruction. Sequences like mul(4*, mul(6,9!, ?(12,34), or mul ( 2 , 4 ) do nothing.

For example, consider the following section of corrupted memory:

xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
Only the four highlighted sections are real mul instructions. Adding up the result of each instruction produces 161 (2*4 + 5*5 + 11*8 + 8*5).

Scan the corrupted memory for uncorrupted mul instructions. What do you get if you add up all of the results of the multiplications?
'''

# Read the input file
# Find all the mul instructions - mul(X,Y)
# Calculate X*Y
# Add up all the results

def multiply(x, y):
    print(x, y)
    return x * y

total = 0

with open('day3_input.txt', 'r') as file:
# with open('test_day3.txt', 'r') as file:
    for line in file:
        print(line)
        for i in range(len(line)):
            if line[i] == 'm' and line[i+1] == 'u' and line[i+2] == 'l' and line[i+3] == '(':
                x = ''
                y = ''
                for j in range(i+4, len(line)):
                    if line[j].isdigit():
                        x += line[j]
                    elif line[j] == ',':
                        for k in range(j+1, len(line)):
                            if line[k].isdigit():
                                y += line[k]
                            elif line[k] == ')':
                                total += multiply(int(x), int(y))
                                break
                            else:
                                break
                        break
                    else:
                        break

print(total)  # 166357705


'''
There are two new instructions you'll need to handle:

The do() instruction enables future mul instructions.
The don't() instruction disables future mul instructions.
Only the most recent do() or don't() instruction applies. At the beginning of the program, mul instructions are enabled.

For example:

xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
This corrupted memory is similar to the example from before, but this time the mul(5,5) and mul(11,8) instructions are disabled because there is a don't() instruction before them. The other mul instructions function normally, including the one at the end that gets re-enabled by a do() instruction.

This time, the sum of the results is 48 (2*4 + 8*5).

Handle the new instructions; what do you get if you add up all of the results of just the enabled multiplications?
'''

second_total = 0
do = True

# with open('test2_day3.txt', 'r') as file:
with open('day3_input.txt', 'r') as file:
    for line in file:
        print(line)
        for i in range(len(line)):
            if do:
                if line[i] == 'm' and line[i+1] == 'u' and line[i+2] == 'l' and line[i+3] == '(':
                    x = ''
                    y = ''
                    for j in range(i+4, len(line)):
                        if line[j].isdigit():
                            x += line[j]
                        elif line[j] == ',':
                            for k in range(j+1, len(line)):
                                if line[k].isdigit():
                                    y += line[k]
                                elif line[k] == ')':
                                    if do:
                                        second_total += multiply(int(x), int(y))
                                    break
                                else:
                                    break
                            break
                        else:
                            break
            if line[i] == 'd' and line[i+1] == 'o' and line[i+2] != 'n':
                do = True
                print('Mul enabled')
            elif line[i] == 'd' and line[i+1] == 'o' and line[i+2] == 'n' and line[i+3] == "'" and line[i+4] == 't':
                do = False
                print('Mul disabled')
            else:
                continue
            
print(second_total)  # 88811886

print(second_total < total)  # True