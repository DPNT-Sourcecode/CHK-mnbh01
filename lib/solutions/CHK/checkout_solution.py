from collections import Counter


PRICES = {
    'A': {1: 50, 3: 130, 5: 200},
    'B': {1: 30, 2: 45},
    'C': {1: 20},
    'D': {1: 15},
    'E': {1: 40}
}

FREEBIES = {
    'E': {2: {'B': 1}}  # can see the next iteration saying 'buy 4 Es, get 3Bs free'
}


def _condense_skus(skus: str) -> dict:
    if not skus:
        return {}
    return dict(Counter(list(skus)))


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(*args) -> int:
    skus = args[0]  # as per spec which says param[0] i.e. expect a list

    cart = _condense_skus(skus)

    # with the introduction of freebies, it's really interesting - 
    # which do we apply first: the freebies, or the multi-buy discount?!
    # I figure this is what the 'always favor the customer' statement is about...
    # here's my logic -> the multi-buy on Bs is worth 15 to the customer, but a free B
    # is worth 30 -> so if we can give them a free B, we do that BEFORE applying multi-buys

    for product, freebie_desc in FREEBIES.items():
        required_quantity = freebie_desc.keys()
        qualifies = product in cart and cart[product] >= required_quantity
        if qualifies:
            freebie = freebie_desc.values()[0]


    total = 0
    for product, quantity in cart.items():
        prices = PRICES.get(product)
        if not prices:
            return -1  # cart invalid, as per spec
        
        # find the maximum multi-buy and apply that
        multibuys_sorted = sorted(prices.keys(), reverse=True)
        while quantity > 0:
            for multibuy in multibuys_sorted:
                if quantity >= multibuy:
                    quantity -= multibuy
                    total += prices[multibuy]
                    break  # break out of FOR - want to re-apply the highest possible multibuy
        
    return total


