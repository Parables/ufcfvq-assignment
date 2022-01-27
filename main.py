
from utils import data
from fr1 import arithmetic_mean
from fr2 import standard_deviation
from fr3 import min_max_count
from fr4 import percentile, nthPercentile, percentage_below, percentage_above, percentage_between


# Tests
# print("Using data: ", data)

# FR1: Arithmetic Mean
print("\n\nTesting Arithmetic Mean")
print("Using data: ", data)
print("Arithmetic Mean: ", arithmetic_mean(data))


# FR2: Standard Deviation
print("\n\nTesting Standard Deviation")
populationTestData = [9, 2, 5, 4, 12, 7, 8,
                      11, 9, 3, 7, 4, 12, 5, 4, 10, 9, 6, 9, 4]
sampleTestData = [9, 2, 5, 4, 12, 7]
print("Population Standard Deviation: ", standard_deviation(populationTestData))
# print(standard_deviation(sampleTestData, True));


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

# print("nthPercentile for {0} is {1}% ".format( p25, nthPercentile(data, p25)))
# print("nthPercentile for {0} is {1}% ".format( p50, nthPercentile(data, p50)))
# print("nthPercentile for {0} is {1}% ".format( p50, nthPercentile(data, p50, 'above')))
# print("nthPercentile for {0} is {1}% ".format( p75, nthPercentile(data, p75)))

# print("nthPercentile for 38,000: ", nthPercentile(testData, 38000, ))
# print("nthPercentile between 33,500 and 49,000: ", nthPercentile(testData, 33500, 'between', 49000, ))
# below_p25 = percentage_below(data, p25)
# above_p25 = percentage_above(data, p25)
# print("{0}% of the items are {1} {2}".format(below_p25, 'below', p25))
# print("{0}% of the items are {1} {2}".format(above_p25, 'above', p25))


# testData = [15, 20, 35, 40, 50]
# print("\nUsing data: ",testData)
# print("5th percentile: ", percentile(testData, 5))
# print("30th percentile: ", percentile(testData, 30))
# print("40th percentile: ", percentile(testData, 40))
# print("50th percentile: ", percentile(testData, 50))
# print("100th percentile: ", percentile(testData, 100))

# testData = [3, 6, 7, 8, 8, 10, 13, 15, 16, 20]
# print("\nUsing data: ",testData)
# print("25th percentile: ", percentile(testData, 25))
# print("50th percentile: ", percentile(testData, 50))
# print("75th percentile: ", percentile(testData, 75))
# print("100th percentile: ", percentile(testData, 100))


# testData = [3, 6, 7, 8, 8, 9, 10, 13, 15, 16, 20]
# print("\nUsing data: ",testData)
# print("25th percentile: ", percentile(testData, 25))
# print("50th percentile: ", percentile(testData, 50))
# print("75th percentile: ", percentile(testData, 75))
# print("100th percentile: ", percentile(testData, 100))


# testData = [75, 77, 78, 78, 80, 81, 81, 82, 83, 84, 84, 84, 85, 87, 87, 88, 88, 88, 89, 90]
# print("\nUsing data: ",testData)
# print("20th percentile: ", percentile(testData, 20))

# testData = [30000, 32000, 32000, 33000, 33000, 34000, 34000, 38000, 38000, 38000, 42000,
# 43000, 45000, 45000, 48000, 50000, 55000, 55000, 65000, 110000]
# testData.sort()
# print("\nUsing data: ",testData)
# print("75th percentile: ", percentile(testData, 75))

# # print("nthPercentile for 49,000: ", nthPercentile(testData, 49000))