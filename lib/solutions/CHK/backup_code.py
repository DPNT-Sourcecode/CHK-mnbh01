# creating a backup file because I don't want to use git in not-my-repo


from collections import defaultdict

def _condense_skus(skus: str) -> str:    
    if not skus:
        return ''
    if len(skus) == 1:
        return f'1{skus}'

    skus_sorted = ''.join(sorted(skus))  # can't sort a string in-place -> gets converted to list

    # output as str means it needs to be re-parsed. Instead, output as dict
    # This was actually wayyy easier than I made it, dammit...
    result = defaultdict(int)
    count = 1
    for i in range(1, len(skus_sorted)):
        if skus_sorted[i] != skus_sorted[i-1]:
            result += f'{count}{skus_sorted[i-1]}'
            count = 1
        else:
            count += 1

    result += f'{count}{skus_sorted[i]}'
    return result


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(*args) -> int:
    skus = args[0]  # as per spec which says param[0] i.e. expect a list

    # to allow the special prices, sort the string of SKUs and condense into algebraic notation
    # i.e. AAABBC -> 3A2B1C
    condensed = _condense_skus(skus)
