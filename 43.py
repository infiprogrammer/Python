"""Python function frequnecy (list) that takes as input a list of integers & returns a pair (minfreqlist, maxfreqlsit) where minfreqlist in a list of a number with maximum frequancy in list is sorted in assending orders"""

def frequency(s):
    d={}
    for i in s:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    print(d)
    minfreq = [k for (k,v) in d.items() if v==min(d.values())]
    maxfreq = [k for (k,v) in d.items() if v==max(d.values())]
    print(minfreq,maxfreq)
    return((sorted(minfreq)),sorted(maxfreq))
print(frequency([13,12,11,13,14,13,13,7,14,11,13,14,12,14,7,11,14]))   