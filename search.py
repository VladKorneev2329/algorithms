def liner(array: list, item) -> int:
    """
    Поиск элемента в списке линейным поиском
    :param array: Список
    :param item: Элемент, который нужно найти в списке
    :return: Возвращает индекс элемента в списке, если такого элемента нет в списке - False
    """
    for index in range(len(array)-1):
        if array[index] == item:
            return index
    return False

def binary(array: list, item) -> int:
    """
    Поиск элемента в списке бинарным поиском
    :param array: Отсортированный список
    :param item: Элемент, который нужной найти в списке
    :return: Возвращает индекс элемента в списке, если такого элемента нет в списке - False
    """
    low = 0
    high = len(array) - 1

    while low <= high:
        middle = (low + high) // 2

        if item == array[middle]:
            return middle
        elif item < array[middle]:
            high = middle -1
        else:
            low = middle + 1
    return False
