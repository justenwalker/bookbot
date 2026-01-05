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

def sorted_char_count(d):
    pairs = []
    for k, v in d.items():
        pairs.append({
            'char': k,
            'num': v,
        })
    return sorted(pairs, key=lambda kv: kv['num'], reverse=True)