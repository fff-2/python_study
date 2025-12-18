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
            # dic -> sort in descending order-> list()
            n = int(input("Number of words to display:"))
            top_words = analyzer.top_words(count, n)
            print("=" * 30)
            for rank, (word, number) in enumerate(top_words, start=1):
                print(f"{rank: >3}: {word: <15} {number}")
            print("=" * 30)
    except FileNotFoundError:
        print(f"File {file_name} not found")


if __name__ == "__main__":
    main()
