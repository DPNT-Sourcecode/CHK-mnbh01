
def _condense_skus(skus_sorted: str) -> str:
    pass

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(*args):
    skus = args[0]  # as per spec which says param[0] i.e. expect a list

    # to allow the special prices, sort the string of SKUs and condense into algebraic notation
    # i.e. AAABBC -> 3A2B1C
    skus_sorted = sorted(skus)

