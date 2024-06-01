# noinspection PyUnusedLocal
# friend_name = unicode string
def hello(*args) -> str:
    if not args:
        return 'Hello'
    if args[0] is None:
        return 'Hello'
    return f'Hello, {args[0]}!'




