from collections import Counter
from copy import deepcopy


PRICES = {
    'A': {1: 50, 3: 130, 5: 200},
    'B': {1: 30, 2: 45},
    'C': {1: 20},
    'D': {1: 15},
    'E': {1: 40},
    'F': {1: 10},
    'G': {1: 20},
    'H': {1: 10, 5: 45, 10: 80},
    'I': {1: 35},
    'J': {1: 60},
    'K': {1: 70, 2: 120},
    'L': {1: 90},
    'M': {1: 15},
    'N': {1: 40},
    'O': {1: 10},
    'P': {1: 50, 5: 200},
    'Q': {1: 30, 3: 80},
    'R': {1: 50},
    'S': {1: 20},
    'T': {1: 20},
    'U': {1: 40},
    'V': {1: 50, 2: 90, 3: 130},
    'W': {1: 20},
    'X': {1: 17},
    'Y': {1: 20},
    'Z': {1: 21},
}

FREEBIES = [
    # tuple of products and required quantities as key
    # freebie amounts as values
    # put the most valuable freebie offers first
    {
        ('E', 2): {'B': 1},
    },
    {
        ('F', 2+1): {'F': 1},
    },
    {
        ('N', 3): {'M': 1},
    },
    {
        ('R', 3): {'Q': 1},
    },
    {
        ('U', 3+1): {'U': 1},
    },
]


GROUP_DISCOUNTS = {
    # put most expensive products at start to remove as many of those as possible
    (3, ('Z', 'Y', 'S', 'T', 'X')): 45,
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

    # Apply freebies first. They are a better saving that multi-buys? Not sure if always true...
    # Need to update a freebie cart variable. Otherwise, we will apply freebies forever.
    freebie_cart = deepcopy(cart)
    checking = True
    while checking:
        checking = False

        for freebie_desc in FREEBIES:
            for requirements, freebies in freebie_desc.items():
                meets_requirements = []
                for i in range(int(len(requirements) / 2)):
                    product, required_quantity = requirements[i], requirements[i+1]
                    if product in freebie_cart and freebie_cart[product] >= required_quantity:
                        meets_requirements.append(True)
                    else:
                        meets_requirements.append(False)
                        break
                
                if all(meets_requirements):
                    # update BOTH carts
                    for product, freebie_quantity in freebies.items():
                        if product in cart and cart[product] >= freebie_quantity:
                            cart[product] -= freebie_quantity
                            for i in range(int(len(requirements) / 2)):
                                freebie_product = requirements[i]
                                required_quantity = requirements[i+1]
                                freebie_cart[freebie_product] -= required_quantity
                                checking = True

    # the freebie code above isn't very clean... but it works. And refactoring is outside of scope 
    # given that this is a timed test.
    # I can see how this would be much cleaner with some classes for each of these domains...
    # might try that later. But not now.

    total = 0

    # apply group discounts. Not convinced they are always better value than multi-buys though...
    checking = True
    while checking:
        checking = False

        for discount_spec, discount_price in GROUP_DISCOUNTS.items():
            quantity, products = discount_spec


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






