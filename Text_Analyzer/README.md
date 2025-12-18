# Word Frequency Analyzer

A simple and efficient Python tool that analyzes text files to determine word frequency. It preprocesses the text by removing special characters and filtering out common "stop words" (like the, is, and) to provide a meaningful analysis of the most important content words.

## 📂 Project Structure

- `main.py`:  The entry point of the program. Handles user input and displays results.

- `analyzer.py`: The core logic module. Handles text preprocessing, stop word loading, and frequency counting.

- `stopwords.txt`: A list of common words to exclude from analysis.

- `text.txt`: (Optional) Example text file for analysis.

## ✨ Features

- **Text Preprocessing**: Automatically converts text to lowercase and removes punctuation/special characters.

- **Stop Word Filtering**: Uses a customizable list (`stopwords.txt`) to ignore common words that do not add semantic value.

- **Frequency Counting**: Calculates how often each word appears in the provided file.

- **Customizable Output**: Allows the user to specify how many "top words" to display (e.g., Top 5, Top 10).

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed on your system.

### Installation

1. Download the files (`main.py`, `analyzer.py`, `stopwords.txt`) to a local directory.

2. Ensure all files are in the same folder.

## 💻 Usage

1. Open your terminal or command prompt.

2. Navigate to the directory containing the files.

3. Run the main script:
```
python main.py
```

4. When prompted, enter the name of the text file you wish to analyze (e.g., text.txt).

5. Enter the number of top words you want to see ranking.

### Example Run

```
insert file name: text.txt
325 words in file
Number of words to display: 5
==============================
  1: belgium         10
  2: russia          8
  3: eu              8
  4: ukraine         7
  5: money           6
==============================
```

## 🛠️ Code Modules

### `main.py`

The driver script that handles user interaction:

1. Reads the target file using UTF-8 encoding.

2. Calls analyzer.preprocessing() to clean the text.

3. Calls analyzer.count_words() to generate frequency data.

4. Calls analyzer.top_words() to sort and retrieve the most frequent words.

5. Formats and prints the results in a clean table.

### `analyzer.py`

Contains three key functions:

- `preprocessing(data)`: Cleans the text by removing special characters (e.g., ~ ! @ # $ etc.) and converting to lowercase.

- `load_stopwords(filepath)`: Reads the excluded words from stopwords.txt.

- `count_words(processed)`: Tokenizes the text and builds a frequency dictionary, skipping words found in the stop words list.

- `top_words(count, number)`: Sorts the frequency dictionary in descending order and returns the top N results.

## ⚙️ Customization

To change which words are ignored by the analyzer, simply edit the `stopwords.txt` file. Add or remove words (one per line).