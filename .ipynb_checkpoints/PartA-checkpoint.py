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