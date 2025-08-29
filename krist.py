import re
def convert_to_camel_case(text):
    if not text:
        return ""

    first_char_is_upper = text[0].isupper()

    words = re.split(r'[-_]', text)

    camel_case_words = [words[0]] + [word.capitalize() for word in words[1]]

    result = "".join(camel_case_words)

    if not first_char_is_upper:
        return result[0].lower() + result[1:]
    else:
        return result
        