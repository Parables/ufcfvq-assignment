
from utils import data
from fr1 import arithmetic_mean
from fr2 import standard_deviation
from fr3 import min_max_count
from fr4 import percentile, nthPercentile, percentage_below, percentage_above, percentage_between


# Tests
# FR1: Arithmetic Mean
print("\n\nTesting Arithmetic Mean")
print("Using data: ", data)
print("Arithmetic Mean: ", arithmetic_mean(data))


# FR2: Standard Deviation
print("\n\nTesting Standard Deviation")
print("Using data: ", data)
print("Population Standard Deviation: ", standard_deviation(data))
print("Sample Standard Deviation: ", standard_deviation(data[0:10], True))



# FR3: Min Max Count
print("\n\nTesting Min Max Count")
print("Using data: ", data)
print("Min Max Count: ", min_max_count(data))


# FR4: Percentile

print("\n\nTesting Percentile")
# using list from FR1
data.sort()
print("Using data: ", data)
p25 =percentile(data, 25)
p50 =percentile(data, 50)
p75 =percentile(data, 75)
print("25th percentile: ", p25 )
print("50th percentile: ", p50)
print("75th percentile: ", p75)