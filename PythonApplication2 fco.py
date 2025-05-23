def fibonacci(n): 
   if n <= 0:
         return []
   elif n == 1:
         return [0]
   elif n == 2:
         return [0,1]
   else:
    fib_sequence = [0,1]
    for i in range(2, n):
       fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    return fib_sequence

def main():
    n = 5
    fib_sequence = fibonacci(n)
    print("los primeros", n, "numros de la serie de fibonacci son:", fib_sequence)
    
if __name__ == "__main__":
    main()
