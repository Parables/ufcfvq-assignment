from utils import round_up_down, nearest_int


# Calcuting the percentile using the nearest-rank methid
def _ordinal_rank(iterable, pthPercentile):
    """
    The ordinal rank n is calculated using this formula
    
    n = (P/100) * N
    
    where P is the pthPercentile amd N is the total number of observation

    Args:
        iterable ([type]): [description]
        pthPercentile ([type]): [description]

    Returns:
        [type]: [description]
    """
    N = len(iterable)
    n = (pthPercentile/100) * N
    # if n is a decimal, find the round up to the nearest int
    return nearest_int(n)
    


def _percentile_value(iterable, ordinalRank):
    # sort the iterable
    iterable.sort()
    # since index of a list starts at 0, _percentile_value is  index-1
    # but if index-1 == 0, then just use the index
    # as this usually represents the zeroth percentile although is is not universally accepted
    index = ordinalRank if  (ordinalRank-1)<0 else (ordinalRank-1)
    return iterable[index];

def percentile(iterable, pthPercentile):
    return _percentile_value(iterable, _ordinal_rank(iterable, pthPercentile));


# tests
data = [15, 20, 35, 40, 50]
print(data)
print(percentile(data, 5))
print(percentile(data, 30))
print(percentile(data, 40))
print(percentile(data, 50))
print(percentile(data, 100))

data = [3, 6, 7, 8, 8, 10, 13, 15, 16, 20]
print(data)
print("25th", percentile(data, 25))
print("50th", percentile(data, 50))
print("75th", percentile(data, 75))
print("100th", percentile(data, 100))


data = [3, 6, 7, 8, 8, 9, 10, 13, 15, 16, 20]
print(data)
print("25th", percentile(data, 25))
print("50th", percentile(data, 50))
print("75th", percentile(data, 75))
print("100th", percentile(data, 100))

# def kthPercentile(iterable, ):
#     """
#     1. Rank the values in the data set in order from smallest to largest.
    
#     2. Multiply k (percent) by n (total number of values in the data set). 
#     This is the index. You'll refer to this in the next steps as the position of a value in your data set (first, second, third...).
    
#     3.If the index is not a round number, round it up (or down, if it's closer to the lower number) to the nearest whole number.
    
#     4. Use your ranked data set to find your percentile. 
#     Refer to the value that correlates with the index number, as determined in step 3. 
#     Since the value for the kth percentile must be greater than the values that precede the index, 
#     the next ranked value would be the kth percentile. 
#     Similarly, when using the 'greater than or equal to' method, steps 1-3 remain the same, 
#     but this time we would include the index value. 
#     The kth percentile is then calculated by taking the average of the index value in your data set and the next ranked value.

#     Args:
#         iterable ([type]): [description]
#     """
#     pass


# def nthPercentile(nthPercentile, iterable):
#     """The nthPercentile is given by the formular
#     Px =x(N+1)/100
#     where Px is the value at which x percentage of the data lie below that value
#     N is the total number of observations

#     Returns:
#         [type]: [description]
#     """
#     pass






# # Percentile = (n/N) x 100

#     """
#     • Percentiles can be calculated using the formula n = (P/100) x N, where P = percentile, N = number of values in a data set (sorted from smallest to largest), and n = ordinal rank of a given value.

# • Percentiles are frequently used to understand test scores and biometric measurements.
# P=n/N*100
#     """

# def percentile(iterable, quarterly, option='below'):
#     iterable.sort()
#     N = len(iterable)
#     n = round_up_down((percentile*N)/100)
#     return number_of_values(iterable, n, option)



# def number_of_values(iterable, n, option='below'):
#     """[summary]

#     Args:
#         option (str, optional): 
#             Available option are 'below', 'belowOrEqualTo' 'above' 'aboveOrEqualTo', 'between'. 
#             Defaults to 'below'.
#     """
#     if (option == 'below'):
#         return iterable[(n-1)]
#     elif (option == 'belowOrEqualTo'):
#         return iterable[n]
#     elif (option == 'above'):
#         return iterable[len(iterable)-(n+1)]
#     else:
#         return iterable[len(iterable)-(n)]


# # data = [50, 100, 70, 80, 56, 60, 80, 75]

# salaries = [30000, 32000, 32000, 33000, 33000, 34000, 34000, 38000, 38000, 38000, 42000,
#             43000, 45000, 45000, 48000, 50000, 55000, 55000, 65000, 110000]
# print(nth_percentile(salaries, 75))
# print(nth_percentile(salaries, 50, 'above'))




