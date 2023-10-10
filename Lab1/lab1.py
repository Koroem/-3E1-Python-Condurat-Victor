import math
def find_gcd(numbers):
    gcd = numbers[0]
    for num in numbers[1:]:
        gcd = math.gcd(gcd, num)
    return gcd

def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

def count_occurrences(substr, main_str):
    return main_str.count(substr)

def camel_to_snake(s):
    result = s[0].lower()
    for i in range(1, len(s)):
        if s[i].isupper():
            result += '_' + s[i].lower()
        else:
            result += s[i]
    return result


def is_palindrome(num):
    s = str(num)
    reversed_s = ''
    for char in s:
        reversed_s = char + reversed_s

    return s == reversed_s

def extract_number(text):
    num = ""
    for char in text:
        if char.isdigit():
            num += char
        elif num:
            break
    return int(num) if num else None

def count_bits(num):
    count = 0
    while num:
        count += num % 2
        num //= 2
    return count

def count_words(text):
    words = text.split(' ')
    return len(words)

def most_common_letter(s):
    s = s.lower()
    letters = [char for char in s if char.isalpha()]
    max_count = 0
    most_common = None
    for char in set(letters):
        char_count = letters.count(char)
        if char_count > max_count:
            max_count = char_count
            most_common = char
    return most_common, max_count

if __name__=="__main__":
    
    numbers = list(map(int, input("Enter numbers:").split(',')))
    print(find_gcd(numbers))

    s = input("Enter a string: ")
    print(count_vowels(s))

    substr = input("Enter substring: ")
    main_str = input("Enter main string: ")
    print(count_occurrences(substr, main_str))

    camel_string = input("Enter UpperCamelCase string: ")
    print(camel_to_snake(camel_string))

    num = input("Enter a number: ")
    print(is_palindrome(num))

    text_with_num = input("Enter a text with a number: ")
    print(extract_number(text_with_num))

    num_for_bits = int(input("Enter a number to count its 1-bits: "))
    print(count_bits(num_for_bits))

    sentence = input("Enter a sentence: ")
    print(count_words(sentence))

    string_for_letters = input("Enter a string to find the most common letter: ")
    letter, occurrence = most_common_letter(string_for_letters)
    print(f"Most common letter: {letter} (occurred {occurrence} times)")




