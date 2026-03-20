"""Lecture 03 practice problems.

Implement each class/function below so tests pass.
Rules:
- Do not change names/signatures.
- Use only the Python standard library.

Problems:
1. Countdown iterator
2. Step iterator
3. Unique consecutive iterator
4. Circular iterator
6. File word reader generator
7. Batch generator
8. Recursive flatten generator (optional)
9. log_calls decorator
10. measure_time decorator
11. count_calls decorator
12. ensure_non_negative decorator
13. retry decorator (optional)
14. lru_cache decorator (optional)
"""

from __future__ import annotations

from collections.abc import Callable, Iterable, Iterator, Sequence
from typing import Any


class Countdown:
    """Problem 1. Countdown iterator.

    Build an iterator class that starts at `n` and yields down to `0` inclusive.

    Example:
    >>> list(Countdown(3))
    [3, 2, 1, 0]
    """

    def __init__(self, n: int) -> None:
        self.start = n
        self.current = n
        

    def __iter__(self) -> Iterator[int]:
        self.current = self.start
        return self

    def __next__(self) -> int:
        if self.current < 0:
            raise StopIteration
        val = self.current
        self.current -= 1
        return val


class StepIterator:
    """Problem 2. Step iterator.

    Iterate through a list by taking every `step`-th element.
    Default `step` is `2`.
    Raise `ValueError` when `step <= 0`.

    Example:
    >>> list(StepIterator([10, 20, 30, 40, 50, 60]))
    [10, 30, 50]
    >>> list(StepIterator([1, 2, 3, 4, 5, 6, 7], step=3))
    [1, 4, 7]
    """

    def __init__(self, values: list[Any], step: int = 2) -> None:
        if step <= 0:
            raise ValueError
        
        self.values = values
        self.step = step
        self.index = 0

    def __iter__(self) -> Iterator[Any]:
        return self

    def __next__(self) -> Any:
        if self.index >= len(self.values):
            raise StopIteration
        
        val = self.values[self.index]
        self.index += self.step
        return val
            


class UniqueConsecutiveIterator:
    """Problem 3. Unique consecutive iterator.

    Yield values while removing only *consecutive* duplicates.

    Example:
    >>> list(UniqueConsecutiveIterator([1, 1, 2, 2, 2, 3, 1, 1]))
    [1, 2, 3, 1]
    """

    def __init__(self, values: list[Any]) -> None:
        self.values = values
        self.index = 0
        self.prev = object()

    def __iter__(self) -> Iterator[Any]:
        return self

    def __next__(self) -> Any:
        while self.index < len(self.values):
            current = self.values[self.index]
            self.index += 1
            if current != self.prev:
                self.prev = current
                return current
        raise StopIteration
                
            
            
            


class CircularIterator:
    """Problem 4. Circular iterator.

    Return exactly `k` values by cycling through `sequence`.
    Raise `ValueError` when sequence is empty or when `k < 0`.

    Example:
    >>> list(CircularIterator(["A", "B", "C"], 8))
    ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B']
    """

    def __init__(self, sequence: Sequence[Any], k: int) -> None:
        if not sequence or k < 0:
            raise ValueError
        self.sequence = sequence
        self.k = k
        self.count = 0
        self.index = 0
        

    def __iter__(self) -> Iterator[Any]:
        return self

    def __next__(self) -> Any:
      if self.count >= self.k:
        raise StopIteration
      val = self.sequence[self.index]
      self.index = (self.index + 1) % len(self.sequence)
      self.count += 1
      return val  


class FlattenIterator:
    """Problem 5 (optional). Flatten iterator.

    Build an iterator class that yields scalar values from nested lists
    of arbitrary depth.

    Example:
    >>> list(FlattenIterator([1, [2, 3], [4, [5, 6]], 7]))
    [1, 2, 3, 4, 5, 6, 7]
    """

    def __init__(self, data: list[Any]) -> None:
        raise NotImplementedError

    def __iter__(self) -> Iterator[Any]:
        raise NotImplementedError

    def __next__(self) -> Any:
        raise NotImplementedError


def read_words(filename: str) -> Iterator[str]:
    """Problem 6. File word reader generator.

    Yield one word at a time from a text file without loading the whole
    file into memory.

    Example:
    >>> list(read_words("sample.txt"))
    ['one', 'two', 'three']
    """
    with open(filename, "r") as f:
        for line in f:
            for word in line.split():
                yield word
            


def batch(iterable: Iterable[Any], size: int) -> Iterator[list[Any]]:
    """Problem 7. Batch generator.

    Yield lists containing at most `size` items from `iterable`.
    Raise `ValueError` when `size <= 0`.

    Example:
    >>> list(batch([1, 2, 3, 4, 5, 6, 7], 3))
    [[1, 2, 3], [4, 5, 6], [7]]
    """
    if size <= 0:
        raise ValueError
    lst = []
    for item in iterable:
        lst.append(item)
        if len(lst) == size:
            yield lst
            lst = []
        
    if lst:
        yield lst
        
        
def flatten(data: list[Any]) -> Iterator[Any]:
    """Problem 8 (optional). Recursive flatten generator.

    Recursively yield all scalar values from a nested list.

    Example:
    >>> list(flatten([1, [2, 3], [4, [5, 6]], 7]))
    [1, 2, 3, 4, 5, 6, 7]
    
    """
    for item in data:
      if isinstance(item, list):
        yield from flatten(item)
      else:
        yield item


def log_calls(func: Callable[..., Any]) -> Callable[..., Any]:
    """Problem 9. `log_calls` decorator.

    Print each function call in this format:
    `name(arg1, arg2, kw=value) -> result`

    Hint:
    - Function name: `func.__name__`
    - Positional values: `args`
    - Keyword names/values: `kwargs.items()`

    Example:
    >>> @log_calls
    ... def add(a, b):
    ...     return a + b
    >>> add(2, 3)
    add(2, 3) -> 5
    5
    """
    
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        args_str = ", ".join(str(a) for a in args)
        kwargs_str = ", ".join(f"{k}={v}" for k, v in kwargs.items())

        all_args = ", ".join(filter(None, [args_str, kwargs_str]))

        print(f"{func.__name__}({all_args}) -> {result}")
        return result
    return wrapper


def measure_time(func: Callable[..., Any]) -> Callable[..., Any]:
    """Problem 10. `measure_time` decorator.

    Measure function execution time and print:
    `Executed in <milliseconds> ms`

    Example:
    >>> @measure_time
    ... def work():
    ...     return "done"
    >>> work()
    done
    """
       
    import time


    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Executed in", (end - start) * 1000, "ms")
        return result
    return wrapper

def count_calls(func: Callable[..., Any]) -> Callable[..., Any]:
    """Problem 11. `count_calls` decorator.

    Count how many times the wrapped function is called.
    Store the counter in `wrapper.calls`.

    Example:
    >>> @count_calls
    ... def ping():
    ...     return "ok"
    >>> ping(); ping()
    'ok'
    >>> ping.calls
    2
    """
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return func(*args, **kwargs)

    wrapper.calls = 0
    return wrapper
    


def ensure_non_negative(func: Callable[..., Any]) -> Callable[..., Any]:
    """Problem 12. `ensure_non_negative` decorator.

    Raise `ValueError` when the decorated function returns a negative number.

    Example:
    >>> @ensure_non_negative
    ... def diff(a, b):
    ...     return a - b
    >>> diff(5, 2)
    3
    """
    
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result < 0:
            raise ValueError
        return result
    return wrapper


def retry(times: int) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """Problem 13 (optional). `retry(times)` decorator.

    Retry a function up to `times` retries after the initial attempt.
    Raise `ValueError` when `times < 0`.

    Example:
    >>> @retry(2)
    ... def flaky():
    ...     ...
    """
    raise NotImplementedError


def lru_cache(maxsize: int) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """Problem 14 (optional). `lru_cache(maxsize)` decorator factory.

    Implement cache with Least Recently Used eviction policy.
    Keep only the last `maxsize` used results.
    Solve this one using a class.

    Example:
    >>> @lru_cache(2)
    ... def square(x):
    ...     return x * x
    >>> square(2), square(3), square(2)
    (4, 9, 4)
    """
    raise NotImplementedError
