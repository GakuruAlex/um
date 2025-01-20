from re import IGNORECASE, findall
def count(text: str)-> int:
    """_Find the number of times um occurs standalone in a string but not as a substring_

    Args:
        text (str): _Input string_

    Returns:
        int: _Number times um occurs in str_
    
    Example:
        >>> count("Hello world, this food is um yummy")
            1
        >>> count("Hello world")
            0
    """
    pattern = r'(\bum\b)+'
    return len(findall(pattern=pattern, string= text, flags=IGNORECASE))
def main()-> None:
    # test_text = 'hello world, this food is UM yummy'
    # print(f"um appears {count(test_text)} times. Expecting 1")
    print(count(input("Text: ")))

if __name__ == "__main__":
    main()