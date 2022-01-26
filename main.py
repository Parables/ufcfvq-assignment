
data = [6, 2, 22, 21, 24, 23, 8, 9, 5, 3, 11, 28, 14, 13, 12, 26, 29, 16, 15, 20, 25, 1, 10, 18, 27, 19, 7];

sum = lambda x, y: x + y;

def arithmetic_mean(listOfNumbers):
    return reduce(sum, listOfNumbers)/len(listOfNumbers);


def reduce(function, iterable=[], initialValue=None):
    
    """
    The reduce method applies a function against an accumulator 
    and each value of the array (from left-to-right) 
    to reduce it to a single value.

    Args:
        function (function(accumulator, currentElement)): The function is applied to all array elements one after another and “carries on” its result to the next call.
            Args:
            accumulator – is the result of the previous function call, equals initialValue the first time (if initialValue is provided).
            currentElement – is the current array element.
        iterable (list, optional): An iterable to be reduced. Defaults to [].
        initialValue ([type], optional): The initialValue of the accumulator. Defaults to None.

    Returns:
        [type]: Returns a single value based on the iterable
    """
    
    it = iter(iterable)
    accumulator = next(it) if initialValue is None else initialValue;
    for currentElement in it:
        accumulator = function(accumulator, currentElement);
    return accumulator;



arithmetic_mean(data);

