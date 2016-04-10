# cs6065_hw4
MapReduce mincemeat

1. mathstats.py -  Calculated standard deviation by using mincemeat map reduce. Passed chunks of data by dividing them into list of lists. 
2. primes.py - Calculated pallindrome primes. First created a list of 10 million numbers , then passed the data to mincemeat map reduce as chunks of data for parallelism. Checked for pallindromes in ma and passed to reduce for prime checking.
3. passCrack.py - used all combination strings for comparison by using iterator tools(product) . passed all the combinations as chunks into map function. Then passed the input hex and compared in the map function. returned the exact passwords.
