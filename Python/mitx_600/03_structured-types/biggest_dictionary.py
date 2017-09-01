animals = {'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')


def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    result = None
    maxCount = 0
    for key in aDict.keys():
        if len(aDict[key]) >= maxCount:
            result = key 
            maxCount = len(aDict[key])
             
    return result
        

print(biggest(animals))
print(biggest({'b': [1, 7, 5, 4, 3, 18, 10, 0], 'a': []}))
