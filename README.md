
# Polish Flashcard Application

This Python-based flashcard application helps users learn Polish vocabulary effectively. The program displays flashcards with Polish words and their English translations, allowing users to test their knowledge interactively. Known words are removed from the deck to focus on learning new vocabulary.

<img width="887" alt="image" src="https://github.com/EgemenErin/PolishPal/assets/113554575/c40a5af3-9fb3-4729-bd1e-3cf4877eeaac">


## Features

- **Interactive Flashcards**: Displays Polish words with an option to flip the card and view the English translation after a delay.
- **Progress Tracking**: Marks words as known and removes them from the deck, ensuring users only review unfamiliar words.
- **Data Persistence**: Saves progress to a `words_to_learn.csv` file, allowing users to pick up where they left off in future sessions.
- **Dynamic Loading**: Automatically loads words from `words_to_learn.csv` if it exists, or from the original dataset otherwise.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/EgemenErin/PolishPal.git
   cd PolishPal
   ```

2. **Install Dependencies**:
   Ensure you have Python installed, then install the required packages:
   ```bash
   pip install pandas
   ```

3. **Run the Application**:
   ```bash
   python PolishPal.py
   ```

## Usage

- **Start the Application**: The main window displays a Polish word.
- **Flip the Card**: The word will automatically flip to show the English translation after 3 seconds.
- **Mark as Known**: Press the ✅ button if you know the word. It will be removed from the deck and saved to `words_to_learn.csv`.
- **Show New Word**: Press the ❌ button to see a new word without marking the current one as known.

## Project Structure

```plaintext
polish-flashcards/
│
├── data/
│   ├── polish_words.csv       # Original dataset
│   └── words_to_learn.csv     # Updated dataset (auto-generated)
│
├── images/
│   ├── card_front.png
│   ├── card_back.png
│   ├── right.png
│   └── wrong.png
│
├── flashcards.py              # Main application script
├── README.md                  # Project description and instructions
└── requirements.txt           # List of dependencies
```

## Contributions

Contributions are welcome! Please fork this repository and submit a pull request with your improvements or bug fixes.
