# Creating a bot that can 'read' a book and 'create a report', per BootDev.


character_dict = {}


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

        # counting all of the individual words in the text.
        num_words = len(file_contents.split())

        # counting each individual character and how many times it repeats
        lowercase_book = file_contents.lower().strip()
        for letter in lowercase_book:
            try:
                character_dict[letter]
            except KeyError:
                character_dict.update({letter: 0})
            character_dict[letter] += 1

        print("---- Book Report ----")
        print(f"The total number of words is: {num_words}/n")
        for key, value in character_dict.items():
            if key.isalpha():
                print(f"The {key} character appears {value} times.")


if __name__ == "__main__":
    main()
