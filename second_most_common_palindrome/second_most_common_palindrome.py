from collections import Counter

# Function to split text into words
def split_text_into_words(text):
    words = []
    current_word = ''
    for char in text.lower():
        if char.isalnum():
            current_word += char
        else:
            if current_word:
                words.append(current_word)
                current_word = ''
    if current_word:
        words.append(current_word)
    return words


# Function to count occurrences of palindromes
def count_palindromes(words):
    # Filter out words that are palindromes and longer than 1 character
    palindromes = [word for word in words if len(word) > 1 and word == word[::-1]]
    return palindromes


# Main function to find the second most common palindrome appearing in a single text
def second_frequent(text):
    words = split_text_into_words(text)
    palindromes = count_palindromes(words)

    if len(palindromes) < 2:
        return "There are fewer than two palindromes in the text."

    # Count occurrences of each palindrome
    palindrome_counts = Counter(palindromes)

    # Get the list of all values and sort it in descending order
    frequencies = sorted(palindrome_counts.values(), reverse=True)

    if len(frequencies) < 2:
        return "There is no second most common palindrome."

    # Find the second largest frequency
    second_largest_frequency = frequencies[1]

    # Traverse dictionary and find the key (palindrome) that has the second largest frequency
    for palindrome, count in palindrome_counts.items():
        if count == second_largest_frequency:
            return palindrome

    return "There is no second most common palindrome."


# Function to read texts from a file and filter out empty lines
def get_texts_from_file(file_path):
    with open(file_path, 'r') as file:
        texts = [line.strip() for line in file if line.strip()]
    return texts


# Main execution
def main():
    file_path = "example_text.txt"  # File with at least 3 pieces of text
    user_texts = get_texts_from_file(file_path)

    # Check if the number of lines in the file is less than 3
    if len(user_texts) < 3:
        print("The file contains fewer than 3 pieces of text. Please add at least 3 rows to the file.")
        return

    # Process each text and find the second most common palindrome
    for i, text in enumerate(user_texts, start=1):
        result = second_frequent(text)
        print(f"Text {i}: The second most common palindrome is: {result}")


if __name__ == "__main__":
    main()
