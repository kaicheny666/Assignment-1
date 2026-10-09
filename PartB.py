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

