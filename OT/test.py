# constraints = ["-1x1 + -1x2 < -1","-2x1 + -3x2 < -2"]
# z           = "-3x1 + -1x2"
 

# 1 2 3 4
# 


# 0 2 2 1
# 4 6 8 6
# 6 8 10
def to_superscript(text):
    superscript_chars = {
        '0': '⁰',
        '1': '¹',
        '2': '²',
        '3': '³',
        '4': '⁴',
        '5': '⁵',
        '6': '⁶',
        '7': '⁷',
        '8': '⁸',
        '9': '⁹',
        '[': '⁽',
        ']': '⁾',
        '|': '‖',
        '_': '₍₎'
    }

    superscript_text = ''.join(superscript_chars.get(char, char) for char in text)
    return superscript_text

# Example usage
print(to_superscript("x^2 + y[3]|4_5"))