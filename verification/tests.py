"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""
TESTS = {
    "Basics": [
        {
            "input": [[3000, 2200, 2000, 1800, 1600, 1300]],
            "answer": 100,
            "explanation": [[2200, 2000, 1800], [1300, 1600, 3000]],
        },
        {
            "input": [[4000, 4000, 4000]],
            "answer": 6000,
            "explanation": [[4000], [4000], [4000]],
        },
        {
            "input": [[1]],
            "answer": 5999,
            "explanation": [[1]],
        },
        {
            "input": [[3000, 2200, 2000, 1800, 1600, 1400]],
            "answer": 0,
            "explanation":[[2200, 2000, 1800], [1400, 1600, 3000]], 
        },
        {
            "input": [[3000, 2200, 1900, 1800, 1600, 1300]],
            "answer": 200,
            "explanation": [[2200, 1900, 1800], [1300, 1600, 3000]],
        },
        {
            "input": [[3000]],
            "answer": 3000,
            "explanation":[[3000]],
        },
        {
            "input": [[3001, 3001]],
            "answer": 5998,
            "explanation": [[3001], [3001]],
        },
    ],
}