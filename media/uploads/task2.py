from functools import wraps


def check_type(func):
    """Decorator for function which check type of numbers. """

    @wraps(func)
    def inner(self, number, *args, **kwargs):
        try:
            int(number)
            func(self, number)
        except ValueError:
            print('The wrong number: ' + number)

    return inner

class Node:
    def __init__(self):
        self.children = {}  # key = digit, value = links of children
        self.is_finished = False


class SuffixTree:
    def __init__(self):
        self.__root = Node()
        self.__numbers = []

    @check_type
    def add(self, number: str):
        """Adding new phone number"""
        node = self.__root
        for digit in list(number):
            if not node.children.get(digit):
                node.children[digit] = Node()
            node = node.children[digit]
        node.is_finished = True

    def search(self, prefix: str):
        """ Search numbers"""
        node = self.__root
        self.__numbers.clear()
        is_found = False
        temp_word = ''
        for digit in list(prefix):
            if not node.children.get(digit):
                is_found = True
                break
            temp_word += digit
            node = node.children[digit]

        if is_found:
            return 0
        elif node.is_finished and not node.children:
            return -1

        self.suggest(node, temp_word)

    def suggest(self, node: Node, number: str):
        if node.is_finished:
            self.__numbers.append(number)

        for digit, n in node.children.items():
            self.suggest(n, number + digit)

    @property
    def numbers(self):
        return self.__numbers[:10]


suffix = SuffixTree()
numbers = ["380672832505",
           "380671232530",
           "380675683254",
           "380672831230",
           "380672832503",
           "380671323220",
           "380672836400",
           "380675632234",
           "380672823457",
           "38067dfses24",
           "380671657650",
           "380674646346",
           "380536235324",
           "389675753463",
           "385634554553",
           "380534646532",
           "380436235353",
           "38067dfss254",
           "38067dfses24"]
for number in numbers:
    suffix.add(number)
suffix.search('380672')
print(suffix.numbers)

