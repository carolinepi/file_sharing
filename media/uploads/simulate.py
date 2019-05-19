import sys
from math import ceil
import itertools
from random import shuffle
from copy import deepcopy


class Simulate:
    def __init__(self, quantity):
        self.__quantity = quantity
        self._number = 100
        self.table = []

    def _print_table(self):
        for iterator, row in enumerate(itertools.zip_longest(*self.table)):
            string_row = self.__quantity * "{:<7}"
            try:
                print(string_row.format(*row))
            except TypeError:
                row = ['' if number is None else number for number in row]
                print(string_row.format(*row))

    def _check(self):
        max_count = 0
        for i, iterator in enumerate(self.table):
            count = 0
            for j, jterator in enumerate(self.table):
                if i != j:
                    intersection = iterator.intersection(jterator)
                    # print(intersection)
                    if intersection:
                        count += 1
            if count > max_count:
                max_count = count
            # print(100 * max_count / (len(self.table) - 1))
            # print('---------')
        return "Killing 2 arbitrary servers results in data loss in {:.0%} cases".format(max_count / (len(self.table) - 1))

    def __str__(self):
        self._print_table()
        return self._check()


class Random(Simulate):
    def __init__(self, quantity):
        super(Random, self).__init__(quantity)
        self.__quantity = quantity
        self.__remainder = (self._number * 2 % self.__quantity)
        self.__array = self.__create_shuffle_array()
        self.__create_table()

    def __create_shuffle_array(self):
        deck = list(range(1, self._number + 1))
        shuffle(deck)
        temp = deepcopy(deck)
        shuffle(temp)
        deck.extend(temp)
        return deck

    def __create_table(self):
        for _ in range(self.__quantity):
            self.table.append(self.__create_set())

    def __create_set(self):
        length = 0
        new_set = set()
        iterator = 0
        numbers_in_server = int(self._number * 2 / self.__quantity)
        if self.__remainder:
            numbers_in_server += 1
            self.__remainder -= 1
        for _ in range(numbers_in_server):
            new_set.add(self.__array[iterator])
            if len(new_set) == length + 1:
                length += 1
                self.__array.pop(iterator)
            else:
                iterator += 1
        return new_set


class Mirror(Simulate):
    def __init__(self, quantity):
        super(Mirror, self).__init__(quantity)
        self.__quantity = quantity
        self.table = self.__create_table()

    def __create_table(self):
        temp = ceil(100 / amount * 2)
        self.table = [{j for j in range((i * temp) + 1, ((i+1) * temp) + 1) if j <= 100} for i in range(int(amount / 2))]
        self.table.extend(self.table)
        return self.table


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("I need more args")
    else:
        try:
            amount = int(sys.argv[2])
            value = sys.argv[3]
            if len(sys.argv) != 4 or sys.argv[1] != '-n' and value.startswith('--') or amount <= 0:
                print("Error. Write correct request!")
                sys.exit(1)
        except ValueError:
            print("Error. Write correct request!")
            sys.exit(1)

        if value == '--random':
            print(Random(amount))
        elif value == '--mirror':
            print(Mirror(amount))
        else:
            print("Error. Write correct request!")
