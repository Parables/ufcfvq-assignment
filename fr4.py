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
    """ Calculates the percentile using nearest-rank

    Args:
        iterable (list): the list of data to be used
        pthPercentile (number): The nth Percentile. 
        E.g: 25th percentile = 25, 80th percentile = 80

    Returns:
        [type]:  The p-th percentile for a set of numbers 
    """
    return _percentile_value(iterable, _ordinal_rank(iterable, pthPercentile));

def nthPercentile(iterable, item, option='below', itemEnd=None, orEqual=False):
    """Given the nthPercentile, this functions finds the percentile score at that nthPercentile
    
    p = (n/N) * 100
    
    Args:
        iterable ([type]): [description]
        item ([type]): [description]
        option: 'below', 'above', 'between'
    """
    # loop through the iterable and find `element` where `item` is `option` `element`
    if(option == 'below'):
        result = percentage_below(iterable, item)
        return "{0}% of the items are {1} {2}".format(result, option, item)
    elif (option == 'above'):
       result = percentage_above(iterable, item)
       return "{0}% of the items are {1} {2}".format(result, option, item)
    elif (option == 'between' and itemEnd is not None):
        result = percentage_between(iterable, item, itemEnd)
        return "{0}% of the items are {1} {2} and {3}".format(result, option, item, itemEnd)
        
def percentage_below(iterable, item, OrEqual=False):
    # sort the iterable
    iterable.sort()
    if (item in iterable):
        indexOfPreviousItem = iterable.index(item)
    else:
        itemsBelow = list(filter(lambda x:item>x and item<=iterable[(iterable.index(x)+1)], iterable ))
        print("itemsBelow: ", itemsBelow)
        indexOfPreviousItem = iterable.index(itemsBelow[0])
    n = indexOfPreviousItem+1-OrEqual 
    # +1 to get the next value where all the values are below it 
    # -OrEqual to include item in the calculation
    
    N = len(iterable)
    return int((n/N) * 100);

def percentage_above(iterable, item, OrEqual=False):
    # sort the iterable
    iterable.sort()
    if (item in iterable):
        n = len(iterable)- (iterable.index(item)+1)
    else:
        itemsAbove = list(filter(lambda x:x>item, iterable ))
        print("itemsAbove: ",item , itemsAbove)
        indexOfNextItem = iterable.index(itemsAbove[0])
        n=indexOfNextItem+1#-OrEqual
    N = len(iterable)
    return int((n/N) * 100);

def percentage_between(iterable, item, itemEnd, OrEqual=False):
    return percentage_below(iterable, itemEnd, OrEqual)-percentage_above(iterable, item, OrEqual)  

