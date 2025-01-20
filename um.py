from re import IGNORECASE, findall
def count(text: str)-> int:
    pattern = r'(\bum\b)+'
    return len(findall(pattern=pattern, string= text, flags=IGNORECASE))
def main()-> None:
    # test_text = 'hello world, this food is UM yummy'
    # print(f"um appears {count(test_text)} times. Expecting 1")
    print(count(input("Text: ")))

if __name__ == "__main__":
    main()