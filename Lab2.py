# EX1
"""Write a function to return a list of the first n numbers in the Fibonacci string."""
def fibonacci(n):
    fib = [0] * n
    fib[0], fib[1] = 0, 1
    for i in range(2, n):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib


# EX2
"""Write a function that receives a list of numbers and returns a list of the prime numbers found in it."""
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def primes_in_list(lst):
    primes = []
    for num in lst:
        if is_prime(num):
            primes.append(num)
    return primes


# EX3
"""Write a function that receives as parameters two lists a and b and returns: 
(a intersected with b, a reunited with b, a - b, b - a)"""
def list_operations(a, b):
    intersection = []
    union = []
    a_minus_b = []
    b_minus_a = []

    for num in a:
        if num in b and num not in intersection:
            intersection.append(num)
        if num not in union:
            union.append(num)
        if num not in b:
            a_minus_b.append(num)

    for num in b:
        if num not in union:
            union.append(num)
        if num not in a:
            b_minus_a.append(num)

    return intersection, union, a_minus_b, b_minus_a
#EX 4
"""Write a function that receives as a parameters a list of musical notes (strings), 
a list of moves (integers) and a start position (integer). 
The function will return the song composed by going though the musical notes beginning with the start position 
and following the moves given as parameter. Example :
compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2) 
will return ["mi", "fa", "do", "sol", "re"]
"""
def compose(notes, moves, start_pos):
    song = []
    current_pos = start_pos
    for move in moves:
        song.append(notes[current_pos])
        current_pos += move
        if current_pos >= len(notes):
            current_pos %= len(notes)
        elif current_pos < 0:
            current_pos += len(notes)
    return song
#EX 5
"""Write a function that receives as parameter a matrix and will return the matrix obtained by 
replacing all the elements under the main diagonal with 0 (zero)."""
def zero_under_diagonal(matrix):
    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j] = 0
    return matrix
#EX 6
"""Write a function that receives as a parameter a variable number of lists and a whole number x. 
Return a list containing the items that appear exactly x times in the incoming lists. 
Example: For the [1,2,3], [2,3,4],[4,5,6], [4,1, "test"] 
and x = 2 lists [1,2,3 ] # 1 is in list 1 and 4, 2 is in list 1 and 2, 3 is in lists 1 and 2."""
def items_appear_x_times(*args, x):
    # counts={item->nr of apratitions}
    counts = {}
    for lst in args:
        for item in lst:
            if item in counts:
                counts[item] += 1
            else:
                counts[item] = 1

    result = []
    for key, value in counts.items():
        if value == x:
            result.append(key)
    return result
#EX 7
"""Write a function that receives as parameter a list of numbers (integers) and will return a tuple with 2 elements. The first element of the tuple will be the 
number of palindrome numbers found in the list and the second element will be the greatest palindrome number."""
def is_palindrome(num):
    # ::-1 = string reversal
    return str(num) == str(num)[::-1]

def palindrome_info(lst):
    palindromes = []
    for num in lst:
        if is_palindrome(num):
            palindromes.append(num)
    if len(palindromes) > 0:
        return (len(palindromes), max(palindromes))
    return (0, None)
#EX 8
"""Write a function that receives a number x, default value equal to 1, a list of strings, 
and a boolean flag set to True. For each string, generate a list containing the characters that have the ASCII code 
divisible by x if the flag is set to True, otherwise it should contain characters that have the ASCII code not divisible by x. Example:
x = 2, ["test", "hello", "lab002"], flag = False 
will return (["e", "s"], ["e"]) . Note: The function must return list of lists."""
def generate_lists(x=1, words=[], flag=True):
    # ord('char')  returns its interger value unicode
    result = []
    for word in words:
        current_list = []
        for char in word:
            if (flag and ord(char) % x == 0) or (not flag and ord(char) % x != 0):
                current_list.append(char)
        if len(current_list) > 0:
            result.append(current_list)
    return result
#EX 9
"""Write a function that receives as paramer a matrix which represents the heights of the spectators in a stadium and will return a list of tuples 
(line, column) each one representing a seat of a spectator which can't see the game. A spectator can't see the game 
if there is at least one taller spectator standing in front of him. All the seats are occupied. All the seats are at the same level. 
Row and column indexing starts from 0, beginning with the closest row from the field. Example:

########FIELD######
[[1, 2, 3, 2, 1, 1], row 0
 [2, 4, 4, 3, 7, 2], row 1
 [5, 5, 2, 5, 6, 4], row 2
 [6, 6, 7, 6, 7, 5]] row 3
Will return : [(2, 2), (3, 4), (2, 4"""
def obstructed_seats(matrix):
    obstructed = []
    for j in range(len(matrix[0])):
        max_height = 0
        for i in range(len(matrix)):
            if matrix[i][j] > max_height:
                max_height = matrix[i][j]
            else:
                obstructed.append((i, j))
    return obstructed

#EX 11
"""Write a function that will order a list of string tuples based on the 3rd character of the 2nd element in the tuple. Example:
('abc', 'bcd'), ('abc', 'zza')] ==> [('abc', 'zza'), ('abc', 'bcd')]"""
def order_tuples(tuples_list):
    # x[1][2] al 3-lea caracter pt al 2-lea element din tuplu
    return sorted(tuples_list, key=lambda x: x[1][2])

#EX 12
"""Write a function that will receive a list of words as parameter and will return a list of lists of words, grouped by rhyme.
 Two words rhyme if both of them end with the same 2 letters. 
Example: group_by_rhyme(['ana', 'banana', 'carte', 'arme', 'parte']) will return [['ana', 'banana'], ['carte', 'parte'], ['arme']]"""
def group_by_rhyme(words):
    rhymes = {}
    for word in words:
        end_letters = word[-2:]
        if end_letters not in rhymes:
            rhymes[end_letters] = []
        rhymes[end_letters].append(word)
    return list(rhymes.values())

