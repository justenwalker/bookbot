def get_num_words(text):
    return len(text.split())

def get_char_count(text):
    d = {}
    for c in text.lower():
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    return d