# Regular, um, Expressions # 

# Problem Statement #

Given a line of text as input as a str, find the number of times that “um” appears in that text, case-insensitively, as a word unto itself, not as a substring of some other word

## Input ##

A line of text i.e 'hello, um, world'

## Output ##

Number of occurrences of um i.e 1 in the above input


# Test #

## test cases ##

1. An empty str eg. ''

2. um appearing at the start of the string eg. 'um, hello, world'

3. um appearing at the end of the string eg.  'hello, world. um'

4. um appearing at the middle of the string 'hello, um, world'

5. um appearing once 'hello, um, world'

6. um appearing 0 times 'hello, world'

7. um appearing multiple times 'um, hello, I am Jane, um, and I am an, um.'

8. um as a substring of another word in the text 'this food is yummy'

9. um appearing as UM or um or both

10. A text of just um eg. 'um um um um um'


##  test ##

    tests =

    [
        {
            'input': 'um, hello, world',
            'output': 1
        },

        {
            'input': 'hello, um, world',
            'output': 1
        },

        {
            'input': 'hello, world',
            'output': 0
        },

        {
            'input': '',
            'output': 0
        },

        {
            'input': 'Hello UM world, um, I am Jane. I work at um.',
            'output': 3
        },

        {
            'input': 'um um um um um',
            'output': 5
        },

        {
            'input': 'UM um Um uM',
            'output': 4
        },
        {
            'input': 'hello, world um',
            'output': 1
        }
    ]

## Sol ##

1. Create a variable to hold the number of occurrences and initialize it to 0

2. Using reqular expression, scan the input text

3. Increament occurences by 1 if um is found


