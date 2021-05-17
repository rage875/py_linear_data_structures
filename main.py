from array_ds import Array
from array_2d_ds import Grid
from single_linked_list_ds import SingleLinkedList
from double_linked_list_ds import DoubleLinkedList

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

def array_2d_ds_test():
    matrix = Grid(5, 3, 0)
    matrix[2][1] = "Naaa"
    matrix.__rand_fill__()

    print(matrix)

def single_linked_list_ds_test():
    linked_l = SingleLinkedList()
    linked_l.push("Pepe")
    linked_l.push("Luis")
    linked_l.append("Racer")
    linked_l.append(10)
    linked_l.append(20)
    linked_l.append(30)

    for l in linked_l.iter():
        print(l)

    linked_l.remove("Luis")
    linked_l.remove(10)
    linked_l.remove(30)
    linked_l.append(60)

    print("\n")
    for l in linked_l.iter():
        print(l)

    linked_l.search("Pepe")

def double_linked_list_ds_test():
    linked_l = DoubleLinkedList()
    linked_l.push("Pepe")
    linked_l.push("Luis")
    linked_l.append("Racer")
    linked_l.append(10)
    linked_l.append(20)
    linked_l.append(30)

    print("\nForward iteration")
    for l in linked_l.iterForward():
        print(l)

    print("\nBackward iteration")
    for l in linked_l.iterBackward():
        print(l)

    linked_l.remove("Luis")
    linked_l.remove(10)
    linked_l.remove(30)
    linked_l.append(60)

    print("\nForward iteration")
    for l in linked_l.iterForward():
        print(l)
    print("\nBackward iteration")
    for l in linked_l.iterBackward():
        print(l)

if __name__ == '__main__':
    #array_ds_test()
    #array_2d_ds_test()
    #single_linked_list_ds_test()
    double_linked_list_ds_test()
