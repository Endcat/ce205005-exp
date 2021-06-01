from collections import Counter

def get_freq_list(str):
    count = dict(Counter(str))
    for item in count:
        count[item] = count[item] / len(count)

    return count

# get_freq_list("endcat")