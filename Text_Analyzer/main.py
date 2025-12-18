import analyzer


def main():
    file_name = input("insert file name:")
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            data = ""
            for line in f:
                data += line.strip()
        # str -> remove special char, convert lower -> str
        processed = analyzer.preprocessing(data)
        # str -> count words -> dic
        count = analyzer.count_words(processed)
        print(f"{len(count)} words in file")
        # dic -> sort in descending order-> list

    except FileNotFoundError:
        print(f"File {file_name} not found")


if __name__ == "__main__":
    main()
