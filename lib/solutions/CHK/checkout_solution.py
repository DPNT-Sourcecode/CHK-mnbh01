
def _condense_skus(skus: str) -> str:
    skus_sorted = sorted(skus)
    import pdb; pdb.set_trace()
    
    if not skus_sorted:
        return ''
    if len(skus_sorted) == 1:
        return f'1{skus_sorted}'

    result = ''
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





