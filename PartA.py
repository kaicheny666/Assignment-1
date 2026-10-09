import sys

# Time: O(1). Only three character-range checks are needed.
def is_token_character(char):
    return (
        "a" <= char <= "z"
        or "A" <= char <= "Z"
        or "0" <= char <= "9"
    )


# Time: O(N)
# Extra space: O(B + L), for chunk size B and longest token length L.
def iter_tokens(file_path):
    # Replace malformed UTF-8 with delimiters to continue process.
    with open(file_path, "r", encoding="utf-8", errors="replace") as text_file:
        current_token = []
        while True:
            chunk = text_file.read(65536)
            if not chunk:
                break
            for char in chunk:
                if is_token_character(char):
                    current_token.append(char.lower())

                elif current_token:
                    yield "".join(current_token)
                    current_token.clear()

        # Preserve a final token even without a trailing delimiter.
        if current_token:
            yield "".join(current_token)

# Time: O(N). Extra space: O(N) in the worst case for the returned list.
def tokenize(file_path):
    tokens = []

    for token in iter_tokens(file_path):
        tokens.append(token)

    return tokens

# Expected time: O(T + C), where T is the number of tokens and C is their total character count, including the cost of string hashing.
# Extra space: O(U) dictionary entries for U unique tokens, plus the space occupied by their token text.
def computeWordFrequencies(tokens):
    frequencies = {}

    for token in tokens:
        if token in frequencies:
            frequencies[token] += 1
        else:
            frequencies[token] = 1

    return frequencies

# Time: O(U log U) comparisons plus output. Comparing tied tokens can cost O(L), 
# giving O(U log U * (L + 1) + S), where L is the longest
# token length and S is output size. Extra space: O(U).
def printFrequencies(frequencies):
    ordered = sorted(
        frequencies.items(),
        key=lambda item: (-item[1], item[0])
    )

    for token, count in ordered:
        print(f"{token}\t{count}")

# Expected time: O(N) for tokenization and counting, plus the sorting and output cost described above printFrequencies.
# Extra space: O(N).
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 PartA.py <text_file>", file=sys.stderr)
        return 2

    try:
        tokens = tokenize(sys.argv[1])
        frequencies = computeWordFrequencies(tokens)
        printFrequencies(frequencies)

    except (OSError, ValueError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
    