# Algorithms and data structures challenges (in Python)

My sandbox and playground for algorithm implementation and CS challenges.

Be aware that most of the code is not complete and might not even compile/run.

>This repository contains only python implementation. If you are interested in 
>Java implementation, head to my 
>[algorithm-challenges-lab repository](https://github.com/jmetzz/algorithm-challenges-lab). 

## Running the code

I usually run the code inside Intellij IDEA. Thus, if you mark the 
`src` directory as the `Root Source` it should work straightaway.
However, if you are using another IDE, you might fiddle a bit with the path configuration. 

Instead of fiddling with path, a better alternative is just run the example code 
as a module from the command line:

```bash
# cd src
$ python -m challenges.fundamentals.sorting.quick_sort  
```

If you are using VS Code, make sure to add the correct configuration.
It is important the set the `PYTHONPATH` variable correctly in order to 
get the `imports` working properly.

To run as a script you can add the following lines before the imports of local modules:

```python
# Local application imports
import sys
print('Python %s on %s' % (sys.version, sys.platform))
sys.path.extend(['/path/to/algorithms-challenges-lab-python/src', 
                 '/path/to/algorithms-challenges-lab-python/resources'])
```
Remember to replace `/path/to/` part of the path with the correct path 
where the code base is located.

To debug inside the IDE, add a configuration:

```json
    "configurations": [
        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "env": {
                "PYTHONPATH": "/path/to/algorithms-challenges-lab-python/src:/path/to/algorithms-challenges-lab-python/resources"
            },
            "console": "integratedTerminal"
        }
    ]
```


## Divide and conquer algorithms and problems

| Algorithm  | Status |
|---|---|
| Merge sort - naive            | done |
| Merge sort - top down         | done |
| Merge sort - bottom up        | done |
| Quick sort - recursive & naive pivot      | done |
| Quick sort - recursive & random pivot     |   |
| Quick sort - iterative |   |
| Count inversions in a list    | done |
| Matrix multiplication         | done |
| Closes pair ||
| Fast power ||

## Dynamic programming algorithms and problems

| Algorithm  | Status |
|---|---|
| Fibonacci - naive recursion           | done |
| Fibonacci - cached                    | done |
| Fibonacci - memoization               | done |
| Fibonacci - dynamic                   | done |
| Integer multiplication - grade school | done |
| Integer multiplication - Recursive    | done |
| Integer multiplication - Karatsuba    | done |
| Knapsack - recursive                  | done |
| Knapsack - cached                     | done |
| Knapsack - memoization                | done |
| Checker board path - recursive        | done |
| Checker board path - dynamic          | done |
| Matrix multiplication sequence        | done |
| String edit distance                  | done |
| String longest common subsequence     | done |
| Longest common substring              |  |
| Longest increasing subsequence        |  |
| Graph - tree width ||
| Graph - clique width ||
| Graph - tree decomposition ||
| CYK Cocke-Younger-Kasami ||
| Reliable shortest path ||
| Tower of Hanoi ||
| Egg dropping puzzle ||


# Unclassified yet

- String compression (cracking the code 1.6)
- Matrix rotation (cracking the code 1.7)
- Zero Matrix (cracking the code 1.8)
- String rotation (cracking the code 1.9)
- Suffix array longest common prefix, longest repeated substring, KWIC - keyword in context


