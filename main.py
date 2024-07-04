

def calculate_word_count(data):
    return len(data.split())


def main(book_path):
    with open(book_path, "r") as f:
        data = f.read()
    return data


def count_characters(data):
    count = {}
    for char in data:
        char = char.lower()
        if char.isalpha():
            if count.get(char):
                count[char] = count[char] + 1
            else:
                count[char] = 1
    return count


if __name__ == "__main__":
    data = main("books/frankenstein.txt")
    word_count = calculate_word_count(data)
    _character_count = count_characters(data)
    character_count = []
    for key, value in _character_count.items():
        character_count.append({
            "character": key,
            "count": value
        })
    character_count.sort(reverse=True, key=lambda k: k["count"])
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    print("")
    for item in character_count:
        character = item["character"]
        count = item["count"]
        print(f"The '{character}' character was found {count} times")
    print("--- End report ---")
