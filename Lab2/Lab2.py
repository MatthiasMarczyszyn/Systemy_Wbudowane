
def char_counter_string(string_name: str) -> dict:
    """A simple function that counts how many letters are in the word

    Parameters
    ----------
    string_name : str
        A word in witch we want to counts the letters

    Returns
    -------
    dict
        A dictionery with letters as keys and the number of ech letter as values

    Example
    -------
    >>> char_counter_string("ala")
    {'a' : 2, 'l' : 1}
    """
    # remove all non letter chars from out string
    string_name = "".join(c for c in string_name if c.isalpha())
    # create a empty dictionary
    char_dict = {}
    # counting and writing each number in string to dictionary
    for char in string_name.lower():
        if char in char_dict.keys():
            char_dict[char] = char_dict[char] + 1
        else:
            char_dict[char] = 1
    return char_dict


def char_counter_file(file_name: str) -> dict:
    """A simple function thant read a text file into string sho itw and counts letters in this file 

    Parameters
    ----------
    file_name : str
        A name of chosen file 

    Returns
    -------
    dict
        A dictionary with letters as keys and the number of ech letter as values
    Example
    -------
    >>> char_counter_file("Text.tx")
    ala fasfsafa
    ;;;fsdgdhdf
    dasfas[][]
    {'a': 7, 'l': 1, 'f': 6, 's': 5, 'd': 4, 'g': 1, 'h': 1}
    """
    #opening and save data from file to string
    with open(file_name) as f:
        file_content = f.read()
    #printing data from file
    print(file_content)
    #using char_counter_string to count letters in file
    return char_counter_string(file_content)


def list_min_value(number_list: list) -> dict:
    """A simple function that detect the smallest value inth list and show her all idexes

    Parameters
    ----------
    number_list : list
        List of numbers

    Returns
    -------
    dict
        Dictionary with smallest value and it idexes
    >>> list_min_value([1,2,3,4,1,2,4,23,1])
    {'Minimal Values' : 1, 'Indexes' : [0,4,8]}
    """
    #search the minmum in list
    min_value = min(number_list)
    #create a list of all indexes witch include minimum
    index_list = [each for each in range(len(number_list)) if number_list[each] == min_value]
    return {"Minimal Value:": min_value, "Indexes": index_list}

