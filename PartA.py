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