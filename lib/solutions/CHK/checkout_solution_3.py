from collections import Counter
from copy import deepcopy


PRICES = {
    'A': {1: 50, 3: 130, 5: 200},
    'B': {1: 30, 2: 45},
    'C': {1: 20},
    'D': {1: 15},
    'E': {1: 40},
    'F': {1: 10},
}

FREEBIES = [
    # tuple of products and required quantities as key
    # freebie amounts as values
    # put the most valuable freebie offers first
    {
        ('E', 2): {'B': 1},
    },
    {
        ('F', 3): {'F': 1},
    }
]


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

    # in order to apply the same freebie multiple times, we need to update a cart variable
    # Otherwise, we will apply freebies forever
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
                                freebie_product, required_quantity = requirements[i], requirements[i+1]
                                freebie_cart[freebie_product] -= required_quantity
                                checking = True

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
