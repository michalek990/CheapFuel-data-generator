import random
import string

import numpy as np


# Every city is now a square XD
class City:

    def __init__(self, name, min_x, min_y, max_x, max_y, postcode):
        self.name = name
        self.min_x = min_x
        self.max_x = max_x
        self.min_y = min_y
        self.max_y = max_y
        self.postcode = postcode

    def random_point(self):
        x_t = np.random.uniform(self.min_x, self.max_x)
        y_t = np.random.uniform(self.min_y, self.max_y)

        return x_t, y_t

    def randomPostCode(self):
        num = random.randrange(200)
        s = str(num)

        if num < 10:
            s = "00" + str(num)
        elif num < 100:
            s = "0" + str(num)

        return self.postcode + s

    def randomStreetNumber(self):
        rdx = random.randrange(4)
        number = random.randrange(400)
        return str(number) if rdx != 1 else str(number) + random.choice(string.ascii_uppercase)
