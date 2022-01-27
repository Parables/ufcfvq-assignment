from utils import reducer, sum

# FR1:
def arithmetic_mean( iterable,reducerFunction=reducer, sampleVariance =0):
    """Calculates the mean of an iterable

    Args:
        reducerFunction (function( list, fn,)): a function that reduces a list into a single value by applying fn to every element of the list
        iterable (iterable): the iterable to perform the mean calculation on
        sampleVariance: if True returns sum/(n-1), otherwise sum/(n-0)=sum/n

    Returns:
        [type]: Returns None if iterable is None, otherwise the mean of the iterable
    """
    if(len(iterable)==0): return None;
    return reducerFunction(iterable, sum)/(len(iterable)-sampleVariance);
