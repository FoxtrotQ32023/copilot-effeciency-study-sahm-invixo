def ass02_main():
    """
    This function loads the stringmultimatching.in file in the current directory and does the following:
    1. The first line contains a number specifying the amount of substrings to search for. We call this number N
    2. The next N lines are the substrings to search for
    3. The next line after that is the string to search in
    4. The code then searches the substring for each of the substrings, and returns a list of index positions for each substring
    """
    with open("Assignment02/stringmultimatching.in") as inputFile:
        lines = [line.rstrip() for line in inputFile]

    # Loop through all lines and split them into individual test sets. We know the first line is the number of substring that belong to the test-set, and that N+1 is the line that contains the string to search in and should therefore also be included in the test set.
    test_sets = []
    current_test_set = []
    is_first_line_of_set = True
    for line in lines:
        if is_first_line_of_set:
            current_test_set = []
            is_first_line_of_set = False
        current_test_set.append(line)
        if len(current_test_set) == int(current_test_set[0])+2: # +2 because we need to include the line with the number of substrings and the line with the string to search in
            test_sets.append(current_test_set)
            is_first_line_of_set = True

    # For each test case, output n lines, where the _i_’th line contains the positions of all the occurrences of the _i_’th pattern in text, from first to last, separated by a single space.
    return_string = ""
    for test_set in test_sets:
        number_of_substrings = int(test_set[0])
        substrings = test_set[1:number_of_substrings+1]
        string = test_set[number_of_substrings+1]
        index_positions = find_substring_in_string(substrings, string)
        for index_position in index_positions:
            return_string += " ".join(map(str, index_position)) + "\n"
    
    print(return_string)
    return return_string

def find_substring_in_string(substrings, string):
    """
    This function takes a list of substrings and a string and returns a list of index positions for each substring
    """
    index_positions = []
    for substring in substrings:
        index_positions.append(find_substring_in_string_single(substring, string))
    return index_positions

def find_substring_in_string_single(substring, string):
    """
    This function takes a single substring and a string and returns a list of index positions for the substring
    """
    index_positions = []
    for i in range(len(string)-len(substring)+1):
        if string[i:i+len(substring)] == substring:
            index_positions.append(i)
    return index_positions

if __name__ == "__main__":
    ass02_main()