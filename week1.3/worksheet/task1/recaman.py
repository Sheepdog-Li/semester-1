# Worksheet 1.3: Task 1

L = int(input("Length of sequence: ")) # this should be your only input


sequence = []
seen = set()

if L > 0:
    current = 0
    sequence.append(current)
    seen.add(current)

for k in range(1,L):
    prev =sequence[-1]
    candidate = prev - k
    if  candidate > 0 and candidate not in  seen:
        current = candidate
    else:
        current = prev + k

    sequence.append(current)
    seen.add(current)

    
# Your code for the Recaman Sequence
# You should store the sequence in an appropriate data structure named 'sequence'


# You may wish to use further output for testing purposes while you develop your code

[print(item) for item in sequence]    # this method is reasonably independent of the choice of data structure

# The web page https://en.wikipedia.org/wiki/Recam%C3%A1n%27s_sequence shows about 80 numbers in the sequence