# Programming Task 1

## FR1: Develop a function to find the arithmetic mean

**Objective:**

Develop a function to find the arithmetic mean

**Approach:**

The mean of a list of

1. Calculate the sum of all the elements in the list
2. Divide the sum by the total number of elements in the list

**Strengths:**

1. Uses functional programming approach to calculate mean
2. Improves code readability and reuse by breaking the process into simple individual functions.
3. handles edge cases like when an empty iterable is supplied
4. Because its uses a reducer function to calculate the sum of all elements, it can be reused work with any complex iterable

**Weakness:**

1. Might be a bit boilerplate because of the use of multiple functions to calculate the result

**Alternatives:**

1. A simple for-loop and a sum accumulator variable could have been used.

```python
def simple_arithmetic_mean(list):
    if(len(list)==0): return None;

    sum = 0;

    for x in list:
        sum += x;

    result = sum/len(list);

    return result;
```

This approach wasn't used simply because it will only work for a iterable of numbers and its can't be reused for other complex iterables

---

## FR2: Develop a function to find the standard deviation

**Definition:**

> Standard deviation formula is used to find the values of a particular data that is dispersed. In simple words, the standard deviation is defined as the deviation of the values or data from an average mean. Lower standard deviation concludes that the values are very close to their average. Whereas higher values mean the values are far from the mean value. It should be noted that the standard deviation value can never be negative.
> Standard Deviation is of two types:
    1. Population Standard Deviation
    2. Sample Standard Deviation

**Approach:**

1. Work out the Mean (the simple average of the numbers)
2. Then for each number: subtract the Mean and square the result
3. Then work out the mean of those squared differences.
4. Take the square root of that and we are done!

**Strengths:**

1. Uses functional programming approach to calculate mean
2. Improves code readability and reuse by breaking the process into simple individual functions.
3. handles edge cases like when an empty iterable is supplied
4. Because its uses a reducer function to calculate the sum of all elements, it can be reused work with any complex iterable

**Weakness:**

1. Might be a bit boilerplate because of the use of multiple functions to calculate the result

**Alternatives:**

1. A simple for-loop and a sum accumulator variable could have been used.

```python
def mean(list):
    if(len(list)==0): return None;

    sum = 0;

    for x in list:
        sum += x;

    result = sum/len(list);

    return result;
```

This approach wasn't used simply because it will only work for a iterable of numbers and its can't be reused for other complex iterables
