# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def findGaps(N, gaps):

    if len(N)>0:
        first = N.find('1')
        if first == -1:
            return gaps
        N = N[first+1:]
        second = N.find('1')
        if second ==-1:
            return gaps
        gaps.append(second)
        N= N[second:]
        return findGaps(N,gaps)
    else:
        return gaps

def solution(N):
    # write your code in Python 3.6
    if N % 2 == 0:
        return 0
    n_bin = bin(N)[2:]
    if n_bin.count('0') == 0 :
        return 0
    gaps = findGaps(n_bin,[])
    if len(gaps) > 0:
        return max(gaps)
    else:
        return 0

