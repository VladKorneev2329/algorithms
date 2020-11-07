def bubble(array: list) -> list:
    """
    Сортрует список методом пузырька
    :param array: Не отсортированный список
    :return: Отсортированный список
    """
    if len(array) == 0 or len(array) == 1:
        return array
    for count_iterations in range(len(array) - 1, -1, -1):
        for index in range(len(array) - 1):
            if array[index] > array[index + 1]:
                array[index], array[index + 1] = array[index + 1], array[index]
    return array


def choice(array: list) -> list:
    """
    Сортирует список методом выбора
    :param array: Не отсортированный список
    :return: Отсортированный список
    """
    if len(array) == 0 or len(array) == 1:
        return array
    for index_sorted in range(len(array) - 1):
        for index_not_sorted in range(index_sorted + 1, len(array) - 1):
            if array[index_sorted] > array[index_not_sorted]:
                array[index_sorted], array[index_not_sorted] = array[index_not_sorted], array[index_sorted]
    return array


def insert(array: list):
    """
    Сортирует список методом вставки
    :array: Не отсортированный список
    :return: Сортированный список
    """
    return array
