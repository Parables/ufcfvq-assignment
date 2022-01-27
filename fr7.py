from library import (data, reducer, round_up_down,statKey, statColumns, 
                     arithmetic_mean,
                     standard_deviation,
                     min_max_count,
                     percentile, nthPercentile, percentage_below, percentage_above, percentage_between,
                     readfile, read_column,
                     read_content)


def generate_stats(filename):
    content = read_content(filename)
    # print(content)

    for field in content:
        data = list(map(lambda x: float(x), content[field]))

        count = len(data)
        mean = float("{0:0.3f}".format(arithmetic_mean(data)))
        sd = float("{0:0.3f}".format(standard_deviation(data)))
        minMaxCount = min_max_count(data)
        min = float("{0:0.3f}".format(minMaxCount["min"]))
        max = float("{0:0.3f}".format(minMaxCount["max"]))
        p25 = float("{0:0.3f}".format(percentile(data, 25)))
        p50 = float("{0:0.3f}".format(percentile(data, 50)))
        p75 = float("{0:0.3f}".format(percentile(data, 75)))
        
        content[field] = [count, mean, sd, min, p25, p50, p75, max, ]

    #  insert the stats header before the new contents
    statData = {statKey: statColumns}
    statData.update(content)
    return statData


