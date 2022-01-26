
# FR1: Alternative
def simple_arithmetic_mean(list):
    if(len(list)==0): return None;
    sum = 0
    for x in list:
        sum += x;
    result = sum/len(list);
    print(result)
    return result;
