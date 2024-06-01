from typing import Any

# noinspection PyUnusedLocal
# friend_name = unicode string
def hello(friend_name: Any) -> str:
    if friend_name is None:
        return 'hello'
    return f'hello {friend_name}'


