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
