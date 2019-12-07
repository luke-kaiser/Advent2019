# --- Day 4: Secure Container ---

'''
--- Part One ---

You arrive at the Venus fuel depot only to discover it's protected by a password. The Elves had written the password on a sticky note, but someone threw it out.

However, they do remember a few key facts about the password:

It is a six-digit number.
The value is within the range given in your puzzle input.
Two adjacent digits are the same (like 22 in 122345).
Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
Other than the range rule, the following are true:

111111 meets these criteria (double 11, never decreases).
223450 does not meet these criteria (decreasing pair of digits 50).
123789 does not meet these criteria (no double).
How many different passwords within the range given in your puzzle input meet these criteria?
'''

# take in puzzle input
puzzle_input = r'152085-670283'
range_low = int(puzzle_input.split('-')[0])
range_high = int(puzzle_input.split('-')[1]) + 1

# loop through range and check criteria
# given range is all six-digits, so check paired digits, ascending
passwords = 0
for candidate in range(range_low, range_high):
    candidate = str(candidate)
    doubles = False
    for i in range(1, len(candidate)):
        if candidate[i] < candidate[i - 1]:
            break
        if candidate[i] == candidate[i - 1]:
            if not doubles:
                doubles = True
        if i == len(candidate) - 1 and doubles:
            passwords += 1
print('Eligible Passwords, Part 1:', passwords)

'''
--- Part Two ---
An Elf just remembered one more important detail: the two adjacent matching digits are not part of a larger group of matching digits.

Given this additional criterion, but still ignoring the range rule, the following are now true:

112233 meets these criteria because the digits never decrease and all repeated digits are exactly two digits long.
123444 no longer meets the criteria (the repeated 44 is part of a larger group of 444).
111122 meets the criteria (even though 1 is repeated more than twice, it still contains a double 22).
How many different passwords within the range given in your puzzle input meet all of the criteria?
'''
# loop through range and check criteria
# check like before, but now keep track of digits in sequence for pure doubles
passwords = 0
for candidate in range(range_low, range_high):
    candidate = str(candidate)
    repeats = {}
    count = 1
    for i in range(1, len(candidate)):
        if candidate[i] < candidate[i - 1]:   # if descending, break
            break
        if candidate[i] == candidate[i - 1]:  # if same as last, store count
            count += 1
            repeats[candidate[i]] = count
        else:                                 # if not the same, reset count
            count = 1
        # if we are at the last digit and there exists a double, we're good
        if i == len(candidate) - 1 and 2 in repeats.values():
            passwords += 1
print('Eligible Passwords, Part 2:', passwords)