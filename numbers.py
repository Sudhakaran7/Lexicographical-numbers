class Solution: 
  def lexicalOrder(self, m,n): 
    my_nums = [str(i) for i in range(m, n+1)] 
    my_nums = list(sorted(my_nums)) 
    return my_nums

val=Solution()
m,n=map(int,input().split())
print(*val.lexicalOrder(m,n))
