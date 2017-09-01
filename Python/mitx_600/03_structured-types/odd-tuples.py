def oddTuples(aTup):
    newTuples = ()
    for i in range(len(aTup)):
        if i % 2 == 0:
            newTuples += (aTup[i],)
    return newTuples

print(oddTuples(('I', 'am', 'a', 'test', 'tuple')))
