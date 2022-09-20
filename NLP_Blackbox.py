import random
import string



def bx():
    words = ("pass", "fail", "review")
    num = "Random " + random.choice(words)

    reason = ''.join(random.choice(string.ascii_letters) for i in range(20))
    ReasonOut = "Random Reason: " + reason
    return [num, ReasonOut]


if __name__ == '__main__':
    bx()

