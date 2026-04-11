# Code developed by Emily 04/09

def median_calculation(ratings):
    """
    Calculate the median of the ratings (a list of integers)
    Input: a list of integer
    Output: the median value of the list (0 if the list is empty)
    """

    # test for blank list
    if not ratings:
        return 0
    
    # save the sorted list of ratings into sorted_ratings. 
    # this won't change the original list of ratings
    sorted_ratings = sorted(ratings) 
    count = len(sorted_ratings) # get the number of ratings

    # finding the median
    if count % 2 == 1:
        return sorted_ratings[count // 2] # odd number of datas
    else:
        middle1 = sorted_ratings[(count // 2) - 1]
        middle2 = sorted_ratings[count // 2]
        return (middle1 + middle2) / 2 # even number of datas



def histogram_calc(ratings):
    """
    Calculate the histogram of the ratings (a list of integers)
    Input: a list of integer
    Output: the dictionary of histogram of ratings
    """

    # using dictionary to store the histogram
    histogram_dict = {
        "1 star": ratings.count(1), 
        "2 stars": ratings.count(2),
        "3 stars": ratings.count(3),
        "4 stars": ratings.count(4),
        "5 stars": ratings.count(5)
    }
    return histogram_dict




def bayesian_average_calc(ratings):
    """
    Calculate the bayesian average of a list of integers.
    Input: the list of ratings
    Output: the bayesian average of the ratings (float)
    Bayesian Average=
    (C⋅m+∑x)/(C+n)
    Where:
    C = weight of the prior (minimum number of ratings an item needs before its own rating starts to matter more than the global average.)
    m = overall average rating (prior mean)
    n = number of ratings
    ∑x = sum of all rating scores
    C = 15 for this program
    m = 3.5 for this program
    """

    C = 15 # minimum number of ratings an item needs before its own rating starts to matter more than the global average.
    counter = len(ratings) # number of ratings
    total = sum(ratings) # sum of the ratings scores
    m = 3.5 # the expacted average rating score

    return (C * m + total) / (C + counter)


#End of code developed by Emily
