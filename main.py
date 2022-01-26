
data = [6, 2, 22, 21, 24, 23, 8, 9, 5, 3, 11, 28, 14,
        13, 12, 26, 29, 16, 15, 20, 25, 1, 10, 18, 27, 19, 7]


# A lambda function that returns the sum of x and y
sum = lambda x, y: x+y;


# a lambda function that reduces a list by applying fn to each element
reducer =lambda fn, list: reduce(fn, list);


def reduce(function, iterable, initialValue=None):
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
        [type]: Returns the initialValue if iterable is None, 
        otherwise returns a single value based on the iterable
    """
    if(iterable == None): return initialValue;
    it = iter(iterable)
    accumulator = next(it) if initialValue is None else initialValue
    for currentElement in it:
        accumulator = function(accumulator, currentElement)
    return accumulator

def x_diff_mean_squared(mean, iterable):
    return list(map(lambda x: (x-mean)**2, iterable));

def variance(squaredDifferenceList):
    return arithmetic_mean(reducer, squaredDifferenceList);

def sampleVariance(squaredDifferenceList):
    return arithmetic_mean(reducer, squaredDifferenceList, True);

def square_root(number):
    return number ** (1./2);

# FR1:
def arithmetic_mean(reducerFunction, iterable, sampleVariance =False):
    """Calculates the mean of an iterable

    Args:
        reducerFunction (function(fn, list)): a function that reduces a list into a single value by applying fn to every element of the list
        iterable (iterable): the iterable to perform the mean calculation on
        sampleVariance: if True returns sum/(n-1), otherwise sum/(n-0)=sum/n

    Returns:
        [type]: Returns None if iterable is None, otherwise the mean of the iterable
    """
    if(len(iterable)==0): return None;
    return reducerFunction(sum, iterable)/(len(iterable)-sampleVariance)

# FR2:
def standard_deviation(mean ,iterable, sampleStandardDeviation= False):
    """Calculates the Standard Deviation from an iterable.
    NOTE: The same data MUST BE passed both the arithmetic_mean's iterable parameter and the standard_deviation's iterable parameter
    NOTE: if sampleStandardDeviation is set to True, then iterable MUST BE a sample data not a population data

    Args:
        mean (function(reducerFunction, iterable, sampleVariance =False)): Uses the arithmetic_mean function to find the mean of the iterable
        iterable ([type]): The iterable to performthe standard deviation calculations on
        sampleStandardDeviation (bool, optional): If True, calculates a Sample Standard Deviation.
            Otherwise calculates a Population Standard Deviation. Defaults to False.

    Returns:
        [type]: [description]
    """
    squaredDifferenceList = x_diff_mean_squared(mean, iterable);
    return square_root(sampleVariance(squaredDifferenceList)) if sampleStandardDeviation else square_root(variance(squaredDifferenceList))

# Alternatives
def simple_arithmetic_mean(list):
    if(len(list)==0): return None;
    sum = 0
    for x in list:
        sum += x;
    result = sum/len(list);
    print(result)
    return result;

# Tests
print(arithmetic_mean(reducer, data));
populationTestData = [9, 2, 5, 4, 12, 7, 8, 11, 9, 3, 7, 4, 12, 5, 4, 10, 9, 6, 9, 4];
sampleTestData = [9, 2, 5, 4, 12, 7];
print(standard_deviation(arithmetic_mean(reducer, populationTestData),populationTestData, False));
print(standard_deviation(arithmetic_mean(reducer, sampleTestData),sampleTestData, True));
# print(simple_arithmetic_mean({'a':1,'b':5,'c':6}));


