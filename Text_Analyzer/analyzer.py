def preprocessing(data: str) -> str:
    """
    Remove special characters and convert text to lowercase

    :param data: text data
    :type data: str
    :return: preprocessed text data
    :rtype: str
    """
    data = data.lower()
    special = "~`!@#$%^&*()-_=+{[]}|:;\"'<,>.?/"
    for char in special:
        data = data.replace(char, "")
    return data


def count_words(processed: str) -> dict[str, int]:
    """
    count words and organize the data as a dict

    :param processed: preprocessed text data
    :type processed: str
    :return: organized data containing word and its count
    :rtype: dict[str, int]
    """
    words = processed.split()
    count = {}
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count


def top_words(count: dict[str, int], number: int) -> list:
    """
    Docstring for top_words

    :param count: dict containing word and its count
    :type count: dict
    :param number: number of words want to know
    :type number: int
    :return: list consist of words sorted in descending order of count
    :rtype: list
    """
    items = list(count.items())
    sorted_items = sorted(items, key=lambda x: x[1], reverse=True)

    return sorted_items[:number]
