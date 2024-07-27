### Task 1
**Closure in Programming**: A closure is a function that retains references to the variables from its lexical context, i.e., from the scope in which it was declared.

Implement a function `caching_fibonacci` that creates and uses a cache to store and reuse previously computed Fibonacci numbers.

**Fibonacci Sequence**: The Fibonacci sequence is a series of numbers such as 0, 1, 1, 2, 3, 5, 8, ..., where each subsequent number is obtained by adding the two preceding numbers. To compute the n-th Fibonacci number, the expression:
\[ F_n = F_{n-1} + F_{n-2} \]
is used.

This task can be solved recursively by calling the function that computes Fibonacci numbers until the calls reach values of n less than or equal to 1, where the sequence is defined.

**Requirements**:
- The `caching_fibonacci()` function should return an inner function `fibonacci(n)`.
- `fibonacci(n)` computes the n-th Fibonacci number. If the number is already in the cache, the function should return the cached value.
- If the number is not in the cache, the function should compute it, store it in the cache, and return the result.
- Use recursion to compute Fibonacci numbers.

**Recommendations**:
- We will provide pseudocode for the task.
- Pseudocode is a way to describe an algorithm or code that is understandable to humans. It is not meant to be executed directly but helps developers clearly understand and plan how a program or algorithm will work.

**Pseudocode for `caching_fibonacci`**:
```
FUNCTION caching_fibonacci
    Create an empty dictionary cache

    FUNCTION fibonacci(n)
        If n <= 0, return 0
        If n == 1, return 1
        If n is in cache, return cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        Return cache[n]

    Return the function fibonacci
END FUNCTION caching_fibonacci
```

The `caching_fibonacci` function creates an inner `fibonacci` function and a `cache` dictionary to store Fibonacci results. Each time `fibonacci(n)` is called, it first checks if the value for `n` is in the cache. If it is, the cached value is returned, significantly reducing the number of recursive calls. If not, it is computed recursively and stored in the cache. The `caching_fibonacci` function returns the inner `fibonacci` function, which can now compute Fibonacci numbers using caching.

**Evaluation Criteria**:
- Correct implementation of `fibonacci(n)` with caching.
- Effective use of recursion and caching for optimization.
- Code cleanliness, including readability and comments.

**Usage Example**:
```
# Get the fibonacci function
fib = caching_fibonacci()

# Use the fibonacci function to compute Fibonacci numbers
print(fib(10))  # Output: 55
print(fib(15))  # Output: 610
```

In this example, when `fib(10)` or `fib(15)` is called, the `fibonacci` function inside `caching_fibonacci` computes the corresponding Fibonacci numbers, storing previous results in the cache. This makes subsequent calls for the same values much faster, as they return the cached result. Closures allow `fibonacci(n)` to "remember" the state of `cache` between calls, which is crucial for caching results.

---

### Task 2
Create a function `generator_numbers` that will analyze text, identify all valid numbers considered parts of income, and return them as a generator. Valid numbers in the text are correctly formatted and clearly separated by spaces on both sides. Also, implement a function `sum_profit` that uses `generator_numbers` to sum these numbers and calculate the total profit.

**Requirements**:
- The `generator_numbers(text: str)` function should take a string as an argument and return a generator that iterates over all valid numbers in the text. Valid numbers are correctly formatted and separated by spaces.
- The `sum_profit(text: str, func: Callable)` function should use the `generator_numbers` generator to compute the total sum of numbers in the input string and take it as an argument.

**Recommendations**:
- Use regular expressions to identify valid numbers in the text, considering that numbers are clearly separated by spaces.
- Use the `yield` keyword in the `generator_numbers` function to create a generator.
- Ensure `sum_profit` correctly processes data from `generator_numbers` and sums all numbers.

**Evaluation Criteria**:
- Correct identification and return of valid numbers by `generator_numbers`.
- Accurate computation of the total sum in `sum_profit`.
- Code cleanliness, including comments and adherence to PEP8 coding style.

**Usage Example**:
```
text = "The total income consists of several parts: 1000.01 as base income, supplemented by additional revenues of 27.45 and 324.00 dollars."
total_income = sum_profit(text, generator_numbers)
print(f"Total income: {total_income}")
```

**Expected Output**:
```
Total income: 1351.46
```

---

### Task 3 (Optional)
Develop a Python script to analyze log files. The script should read a log file provided as a command-line argument and display statistics by logging level, such as INFO, ERROR, DEBUG. Additionally, the user can specify a logging level as a second command-line argument to retrieve all records of that level.

**Requirements**:
- The script must accept a log file path as a command-line argument.
- The script must accept an optional command-line argument for filtering by logging level.
- The script should read and analyze the log file, counting entries for each logging level (INFO, ERROR, DEBUG, WARNING).
- Implement the following functions:
  - `parse_log_line(line: str) -> dict` for parsing log lines.
  - `load_logs(file_path: str) -> list` for loading logs from a file.
  - `filter_logs_by_level(logs: list, level: str) -> list` for filtering logs by level.
  - `count_logs_by_level(logs: list) -> dict` for counting records by logging level.
  - `display_log_counts(counts: dict)` for formatting and displaying results.

**Recommendations**:
- Familiarize yourself with the log file structure, including date, time, logging levels, and message format.
- Divide the task into logical blocks and functions for better readability and extensibility.
- Ensure error handling for file issues and other exceptions using try/except blocks.

**Evaluation Criteria**:
- Script meets all requirements, accurately analyzing log files and displaying information.
- Correct error handling for issues like missing files or incorrect formats.
- Use of functional programming elements such as lambda functions, list comprehensions, or filter functions.
- Well-structured, clear code with comments where necessary.

**Usage Example**:
```
python main.py /path/to/logfile.log
```

**Expected Output**:
```
Logging Level | Count
--------------|-------
INFO          | 4
DEBUG         | 3
ERROR         | 2
WARNING       | 1
```

For filtering by a specific level:
```
python main.py /path/to/logfile.log error
```

**Expected Output**:
```
Logging Level | Count
--------------|-------
INFO          | 4
DEBUG         | 3
ERROR         | 2
WARNING       | 1

Details for level 'ERROR':
2024-01-22 09:00:45 - Database connection failed.
2024-01-22 11:30:15 - Backup process failed.
```

---

### Task 4
Enhance the console assistant bot from the previous homework by adding error handling using decorators.

**Requirements**:
- All user input errors should be handled using the `input_error` decorator. This decorator should return messages like "Enter user name," "Give me name and phone please," etc.
- The `input_error` decorator should handle exceptions that occur in the functions - handlers, including `KeyError`, `ValueError`, `IndexError`. When an exception occurs, the decorator should return the corresponding message to the user. The program should continue running.

**Recommendations**:
- As an example, we add the `input_error` decorator for handling `ValueError`.
```
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."

    return inner
```
- Decorate other command-handling functions with `input_error` to handle different types of errors and return appropriate messages.

**Evaluation Criteria**:
- Presence of the `input_error` decorator that handles user input errors for all commands.
- Handling of `KeyError`, `ValueError`, `IndexError` exceptions in functions with the `input_error` decorator.
- Correct bot response to different commands and error handling without terminating the program.

**Usage Example**:
Upon running the script, the dialog with the bot should look like this:
```
Enter a command: add
Enter the argument for the command
Enter a command: add Bob
Enter the argument for the command
Enter a command: add Jime 0501234356
Contact added.
Enter a command: phone
Enter the argument for the command
Enter a command: all
Jime: 0501234356
Enter a command:
```
