import random
import string
import numpy as np

import datasc


def bx():
    words = ("pass", "fail", "review")
    num = "Random " + random.choice(words)

    reason = ''.join(random.choice(string.ascii_letters) for i in range(10))
    ReasonOut = "Random Reason: " + reason
    return [num, ReasonOut]


if __name__ == '__main__':
    bx()
