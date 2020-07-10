import numpy as np


class myParent:

    def __init__(self):

        self.x = np.random.ranf(100)


class myChild(myParent):

    def __init__(self, y):

        self.y = y
        super(myChild, self).__init__()

    def prep_y(self):

        self.y += np.random.randint(0, 9)

    def mymethod(self):

        for _ in range(1000000):
            self.prep_y()

        self.z = self.x ** 2 + self.y


def prep_child(init_val):

    return myChild(init_val)


def get_sum(val_tuple):

    return np.around(np.sum(val_tuple))


def myfunc():

    a = prep_child(10)
    b = prep_child(20)

    for letter in (a, b):
        letter.mymethod()

    c = get_sum((a.z, b.z))

    print('c =', c)


def main():

    myfunc()


if __name__ == '__main__':
    main()
