"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [1, 1, 1],
            "answer": True
        },
        {
            "input": [1, 2, 1],
            "answer": False
        },
        {
            "input": [],
            "answer": True,
            "explanation": "All elements in empty list are equal"
        },
        {
            "input": [1],
            "answer": True,
            "explanation": "List contains only one element."
        }
    ],
    "Extra": [
        {
            "input": [1, 'a', 1],
            "answer": False
        },
        {
            "input": [600000],
            "answer": True
        },
        {
            "input": [10000, 99999],
            "answer": False
        }
    ]
}
