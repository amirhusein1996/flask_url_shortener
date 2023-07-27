import secrets
import string

allowed_chars: str = string.ascii_uppercase + string.digits


def generate_random_string(length: int = 6, allowed_chars: str = allowed_chars) -> str:
    """
    Generate a random string of specified length using the characters from the allowed_chars string.

    :param length: The length of the generated random string. Default value is 6.
    :type length: int
    :param allowed_chars: A string of characters that are allowed to be used in the generated random string.
    Default value is the global variable 'allowed_chars'.
    :type allowed_chars: str
    :return: The random string generated.
    :rtype: str
    """
    return ''.join(
        secrets.choice(allowed_chars) for _ in range(length)
    )
