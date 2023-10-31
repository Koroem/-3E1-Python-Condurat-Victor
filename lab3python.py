def lists_to_sets(a, b):
    intersection = []
    union = []
    a_minus_b = []
    b_minus_a = []

    for elem in a:
        if elem in b:
            intersection.append(elem)
        else:
            a_minus_b.append(elem)
        union.append(elem)

    for elem in b:
        if elem not in a:
            b_minus_a.append(elem)
            union.append(elem)

    return [set(intersection), set(union), set(a_minus_b), set(b_minus_a)]

def count_chars(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def compare_dicts(d1, d2):
    if len(d1) != len(d2):
        return False

    for key in d1:
        if key not in d2:
            return False

        val1 = d1[key]
        val2 = d2[key]

        if type(val1) != type(val2):
            return False

        if isinstance(val1, dict):
            if not compare_dicts(val1, val2):
                return False
        else:
            if val1 != val2:
                return False

    return True

def build_xml_element(tag, content, **attributes):
    attr_str = ''
    for key in attributes:
        attr_str += ' ' + key + '="' + attributes[key] + '"'
    return '<' + tag + attr_str + '> ' + content + ' </' + tag + '>'

def validate_dict(rules, d):
    for key, prefix, middle, suffix in rules:
        if key not in d:
            return False
        value = d[key]
        if not value.startswith(prefix) or not value.endswith(suffix) or middle not in value.replace(prefix, '').replace(suffix, ''):
            return False

    return True

def count_elements(lst):
    unique = set(lst)
    duplicates = len(lst) - len(unique)
    return (len(unique), duplicates)

def set_operations(*sets):
    result = {}
    for i, set1 in enumerate(sets):
        for j, set2 in enumerate(sets):
            if i != j:
                result["{} | {}".format(set1, set2)] = set1 | set2
                result["{} & {}".format(set1, set2)] = set1 & set2
                result["{} - {}".format(set1, set2)] = set1 - set2
                result["{} - {}".format(set2, set1)] = set2 - set1

    return result

def loop(mapping):
    key = 'start'
    visited = []

    while key in mapping and key not in visited:
        visited.append(key)
        key = mapping[key]

    return visited

def compare_args(*args, **kwargs):
    count = 0
    for arg in args:
        if arg in kwargs.values():
            count += 1
    return count

