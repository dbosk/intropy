# Author: Celina Soori <celinah@kth.se>
# Python program to display the Fibonacci sequence

def fibo(n):
   if n <= 1:
       return n
   else:
       return(fibo(n-1) + fibo(n-2))


n = 10
for i in range(nt):
    print(fibo(i))
