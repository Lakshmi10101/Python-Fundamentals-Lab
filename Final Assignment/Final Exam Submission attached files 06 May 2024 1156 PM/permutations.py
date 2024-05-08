def get_permutations(sequence):
    '''
    Enumerates all permutations of a given string

    sequence (string): an arbitrary string to permute. Assumes that it is a
    non-empty string.  

    Using recursion for this part.

    Returns: a list of all permutations of sequence including the sequence itself.

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: the order of the permutations does not matter.
    '''

    if len(sequence) == 1:
        # Base case: if the sequence has only one character, return it as a list
        return [sequence]

    permutations = []

    for i in range(len(sequence)):
        # Fix the current character as the first character
        current_char = sequence[i]

        # Get the remaining characters (excluding the current character)
        remaining_chars = sequence[:i] + sequence[i + 1:]

        # Recursively find permutations of the remaining characters
        remaining_permutations = get_permutations(remaining_chars)

        # Combine the current character with each permutation of the remaining characters
        for perm in remaining_permutations:
            permutations.append(current_char + perm)

    return permutations

if __name__ == '__main__':
   # EXAMPLE
   example_input = 'abc'
   print('Input:', example_input)
   print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
   print('Actual Output:', get_permutations(example_input))