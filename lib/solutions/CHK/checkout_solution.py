from collections import Counter

def _condense_skus(skus: str) -> str:    
    if not skus:
        return ''
    return Counter(list(skus))


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(*args) -> int:
    skus = args[0]  # as per spec which says param[0] i.e. expect a list

    # to allow the special prices, sort the string of SKUs and condense into algebraic notation
    # i.e. AAABBC -> 3A2B1C
    condensed = _condense_skus(skus)








