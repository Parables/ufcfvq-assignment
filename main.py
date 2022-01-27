
from utils import data
from fr1 import arithmetic_mean
from fr2 import standard_deviation
from fr3 import min_max_count


# Tests
print(data)

# FR1: Arithmetic Mean
print(arithmetic_mean(data))


# FR2: Standard Deviation
populationTestData = [9, 2, 5, 4, 12, 7, 8,
                      11, 9, 3, 7, 4, 12, 5, 4, 10, 9, 6, 9, 4]
sampleTestData = [9, 2, 5, 4, 12, 7]
print(standard_deviation(populationTestData))
# print(standard_deviation(sampleTestData, True));


# FR3: Min Max Count
print(min_max_count(data))


# FR4: Percentile