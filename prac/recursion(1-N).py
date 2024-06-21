class Solution:
    def printTillN(self, N):
        if N>0:
            self.printTillN(N-1)
            print(N,end=" ")
if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ob.printTillN(N)
        print()