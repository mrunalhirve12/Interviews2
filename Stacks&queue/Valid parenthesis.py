def vaild(text):
    char_stack = []

    opening = ['(', '{', '[']
    char_match_map = {'(':')', '[':']', '{':'}'}

    for c in text:
        if c in opening:
            char_stack.append(c)
        else:
            if char_stack:
                opening_char = char_stack.pop()
                if char_match_map[opening_char] != c:
                    return False
            else:
                return False

    return not char_stack