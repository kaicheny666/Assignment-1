import sys
from PartA import iter_tokens

# Expected time: O(N1 + N2), including tokenization and string hashing.
# Extra space: O(V1 + B + L), where V1 is the stored vocabulary size
# of token text and set entries, B is the chunk size, and L is the longest token length.
def count_common_tokens(file_path1, file_path2):
    remaining_tokens = set()

    # Store each distinct token from the first file once.
    for token in iter_tokens(file_path1):
        remaining_tokens.add(token)

    common_count = 0
    # Stream the second file without storing its token list.
    for token in iter_tokens(file_path2):
        if token in remaining_tokens:
            common_count += 1

            # Remove matches so repeated occurrences cannot count again.
            remaining_tokens.remove(token)

    return common_count

# Expected time: O(N1 + N2).
# Extra space: O(V1 + B + L), as explained above.
def main():
    if len(sys.argv) != 3:
        print(
            "Usage: python3 PartB.py <text_file1> <text_file2>",
            file=sys.stderr
        )
        return 2

    try:
        result = count_common_tokens(sys.argv[1], sys.argv[2])
        print(result)

    except (OSError, ValueError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())