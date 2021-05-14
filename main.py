from array_ds import Array

def array_ds_test():
    a = Array(6, "na")
    print("len:{}".format(a.__len__()))
    print("str:{}".format(a.__str__()))
    a.__setitem__(1, 300)
    a.__setitem__(2, 20.0)
    a.__rand_fill__()
    print("Random fill:{}".format(a))
    print("Sum str mode:{}".format(a.__sum__()))
    print("Sum num mode:{}".format(a.__sum__(False)))


if __name__ == '__main__':
    array_ds_test()
