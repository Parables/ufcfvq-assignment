
from library import (data, reducer, round_up_down, filename,
                     arithmetic_mean,
                     standard_deviation,
                     min_max_count,
                     percentile, nthPercentile, percentage_below, percentage_above, percentage_between,
                     readfile, read_column,
                     read_content, generate_stats)

# Tests
# FR1: Develop a function to find the arithmetic mean
print("\n\nTesting Arithmetic Mean")
print("Using data: ", data)
print("Arithmetic Mean: ", arithmetic_mean(data))


# FR2: Develop a function to find the standard deviation
print("\n\nTesting Standard Deviation")
print("Using data: ", data)
print("Population Standard Deviation: ", standard_deviation(data))
print("Sample Standard Deviation: ", standard_deviation(data[0:10], True))



# FR3: Develop a function to find the minimum, maximum values, and count
print("\n\nTesting Min Max Count")
print("Using data: ", data)
print("Min Max Count: ", min_max_count(data))


# FR4: Develop a function to find the 25th, 50th and 75th percentiles
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


# FR5: Develop a function to read a single specified column of data from a CSV file
print("\n\nColumn record")
print("\nColumn 3: ", read_column(filename, 3))
print("\nColumn -5: ", read_column(filename, -5))
print("\nColumn -1: ", read_column(filename, -1))


# FR6: Develop a function to read CSV data from a file into memory
print("\n\nCSV to memory: ",read_content(filename))

# FR7: Develop a function to generate a set of statistics for a given data file
print("\n\nStats from data: ",generate_stats(filename))

# FR8: Develop a function to print a custom table
