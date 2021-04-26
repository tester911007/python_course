from itertools import permutations

print(*[''.join(t) for t in permutations(input())], sep='\n')


'''
Sample Input 1:

123
Sample Output 1:

123
132
213
231
312
321
'''
