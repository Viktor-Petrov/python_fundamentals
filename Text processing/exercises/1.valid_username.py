def length_validation(name):
    if 3 <= len(name) <= 16:
        return True
    return False


def letter_validation(name):
    for ch in name:
        if not (ch.isalnum() or ch == "-" or ch == "_"):
            return False
    return True


def redundunt_symbol(name):
    if " " in name:
        return False
    return True


def validation_code(name):
    if length_validation(name) and letter_validation(name) and redundunt_symbol(name):
        return True
    return False


passwords = input().split(", ")
for word in passwords:
    if validation_code(word):
        print(word)



