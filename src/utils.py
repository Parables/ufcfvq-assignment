
data = [6, 2, 22, 21, 24, 23, 8, 9, 5, 3, 11, 28, 14,
        13, 12, 26, 29, 16, 15, 20, 25, 1, 10, 18, 27, 19, 7]

# A lambda function that returns the sum of x and y
sum = lambda x, y: x+y;

square_root = lambda n: n ** (1./2);

squared = lambda x: (x-mean)**2

# a lambda function that returns the reduce function which reduces a list into a single value by applying fn(defaults to sum) to each element
reducer =lambda list,fn=sum : reduce( list, fn );

def reduce( iterable, function, initialValue=None):
    """
    The reduce method applies the function against an accumulator
    and each value of the array (from left-to-right)
    to reduce it to a single value.

    Args:
        iterable (list, optional): An iterable to be reduced.
        function (function(accumulator, currentElement)): The function is applied to all array elements one after another and “carries on” its result to the next call.
            Args:
            accumulator – is the result of the previous function call, equals initialValue the first time (if initialValue is provided).
            currentElement – is the current array element.
        initialValue ([type], optional): The initialValue of the accumulator. Defaults to None.

    Returns:
        [type]: Returns the initialValue if iterable is None, 
        otherwise returns a single value based on the iterable
    """
    if(iterable == None): return initialValue;
    it = iter(iterable)
    accumulator = next(it) if initialValue is None else initialValue
    for currentElement in it:
        accumulator = function(accumulator, currentElement)
    return accumulator





