from collections import Counter


PRICES = {
    'A': {1: 50, 3: 130},
    'B': {1: 30, 2: 45},
    'C': {1: 20},
    'D': {1: 15},
}


def _condense_skus(skus: str) -> dict:
    if not skus:
        return {}
    return dict(Counter(list(skus)))


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(*args) -> int:
    skus = args[0]  # as per spec which says param[0] i.e. expect a list

    condensed = _condense_skus(skus)
    for product, quantity in condensed.items():
        prices = PRICES.get(product)
        if not prices:
            return -1  # cart invalid, as per spec
        
        # find the maximum multi-buy and apply that
        multibuys_sorted = sorted(quantity.keys(), reverse=True)


