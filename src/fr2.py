from fr1 import arithmetic_mean
from utils import  squared, square_root

# FR2:
def standard_deviation(iterable, sampleStandardDeviation= False):
    """Calculates the Standard Deviation from an iterable.
    NOTE: if sampleStandardDeviation is set to True, then iterable MUST BE a sample data not a population data

    Args:
        mean (function(reducerFunction, iterable, sampleVariance =False)): Uses the arithmetic_mean function to find the mean of the iterable
        iterable ([type]): The iterable to performthe standard deviation calculations on
        sampleStandardDeviation (bool, optional): If True, calculates a Sample Standard Deviation.
            Otherwise calculates a Population Standard Deviation. Defaults to False.

    Returns:
        [type]: [description]
    """
    mean = arithmetic_mean(iterable)
    squaredDifferenceList = x_diff_mean_squared(iterable, mean);
    return square_root(sampleVariance(squaredDifferenceList)) if sampleStandardDeviation \
        else square_root(variance(squaredDifferenceList));


# Finds teh squared difference of each element and the mean
def x_diff_mean_squared( iterable,mean):
    """ Transforms an iterable by subtracting the mean from each element and squaring the difference

    Args:
        mean (number): The arithemetic_mean value for the iterable
        iterable ([type]): The iterable to be transformed

    Returns:
        [type]: The squared difference of each element in the iterable and the mean
    """
    return list(map(squared, iterable));

# Calculates the variance of a distribution
def variance(squaredDifferenceList):
    return arithmetic_mean(squaredDifferenceList);

# Calculates the sample variance of a distribution
def sampleVariance(squaredDifferenceList):
    return arithmetic_mean(squaredDifferenceList, True);
