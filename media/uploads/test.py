import pytest
from task2 import SuffixTree


@pytest.fixture(scope='module')
def suffix():
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
    return suffix


def test_quantity_results(suffix):
    """ Test checks number of results. """
    suffix.search('38067')
    assert len(suffix.numbers) == 10
    suffix.search('380672')
    assert len(suffix.numbers) == 5
    suffix.search('3809')
    assert len(suffix.numbers) == 0


def test_type_of_numbers(suffix):
    """ Test checks that numbers are str(int). """
    suffix.search('')
    assert suffix.numbers == ["380672832505",
                              "380671232530",
                              "380675683254",
                              "380672831230",
                              "380672832503",
                              "380671323220",
                              "380672836400",
                              "380675632234",
                              "380672823457",
                              "380671657650",
                              "380674646346",
                              "380536235324",
                              "389675753463",
                              "385634554553",
                              "380534646532",
                              "380436235353"]


def test_results(suffix):
    """ Test checks results. """
    suffix.search('380672')
    assert suffix.numbers == ["380672832505",
                              "380672832503",
                              "380672831230",
                              "380672836400",
                              "380672823457"]


