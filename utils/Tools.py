PURPLE = '\033[95m'
CYAN = '\033[96m'
DARK_CYAN = '\033[36m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
END = '\033[0m'


def represents_int(i):
    if i is None:
        return False
    try:
        int(i)
        return True
    except ValueError:
        return False
