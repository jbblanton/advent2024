# Open and read input file
# Each line is space-separated values
# Analyze each line and determine if it is valid
#   all increasing
#   all decreasing
#   max change of 3
#   min change of 1

safe_reports = 0

unsafe_reports = []

# Read input file
with open('day2_input.txt', 'r') as file:
    data = file.readlines()

# with open('test_day2.txt', 'r') as file:
#     data = file.readlines()

# Analyze each line
for line in data:
    line = line.strip().split()
    line = [int(i) for i in line]
    print(line)

    increasing = False
    decreasing = False

    # Check if line is valid
    for i in range(len(line) - 1):
        a = line[i]
        b = line[i + 1]
        if a == b:
            safe_reports += 0
            increasing = False
            decreasing = False
            break
        elif a < b:
            increasing = True
        elif a > b:
            decreasing = True

        if decreasing and a-b <= 3:
            i+=1
        elif increasing and b-a <= 3:
            i+=1
        else:
            safe_reports += 0
            increasing = False
            decreasing = False
            break

    if increasing and decreasing:
        print('Not safe')
        unsafe_reports.append(line)
    elif not increasing and not decreasing:
        print('Not safe')
        unsafe_reports.append(line)
    elif increasing or decreasing:
        safe_reports += 1
        print('Safe')


print('Total')
print(safe_reports)  # 663

# ******************* Part 2 *******************
# Are the unsafe reports fixable?
# If one number is removed, is the report valid?

fixed_reports = 0

for line in unsafe_reports:
    print('Orig ', line)
    for i in range(len(line)):
        new_line = line.copy()
        new_line.pop(i)
        print('Try ', new_line)
        increasing = False
        decreasing = False

        # Check if line is valid
        for i in range(len(new_line) - 1):
            a = new_line[i]
            b = new_line[i + 1]
            if a == b:
                fixed_reports += 0
                increasing = False
                decreasing = False
                break
            elif a < b:
                increasing = True
            elif a > b:
                decreasing = True

            if decreasing and a-b <= 3:
                i+=1
            elif increasing and b-a <= 3:
                i+=1
            else:
                fixed_reports += 0
                increasing = False
                decreasing = False
                break

        if increasing and decreasing:
            print('Not safe')
        elif not increasing and not decreasing:
            print('Not safe')
        elif increasing or decreasing:
            fixed_reports += 1
            print('Safe')
            break
    print('***')    

print('Fixed Reports')
print(fixed_reports)  # 29

print('Total Reports')
print(safe_reports + fixed_reports)  # 692