

       #----Recursive ve Loop Secenegi----


#   ------Loop Fibonacci---------
def fibonacci_loop(n):
  a,b=0,1
  for i in range(n-1):
    a,b=b,a+b
  return a
sonuc=fibonacci_loop(5)
print(sonuc)


#    --------Recursive Fibonacci----------

def fibonacci_recursive(n):
  if(n<=3):
    return 1
  else:
    return fibonacci_recursive(n-1)+fibonacci_recursive(n-2)

sonuc=fibonacci_recursive(9)
print(sonuc)



#   ---------Recursive Factorial------

def factorial_recursive(n):
  if(n==1):
    return 1
  else:
    return n*factorial_recursive(n-1)

sonuc=factorial_recursive(6)
print(sonuc)



 #---------Loop Factorial---------

def loop_factorial(n):
    s=1
    for i in range(1,n+1):
        s=s*i
    return s

sonuc=loop_factorial(5)
print(sonuc)



# ----- Recursive Power---------

def power_recursive(m,n):
  if(n==0):
    return 1
  elif(n==1):
    return m
  elif(n%2==0):
    return power_recursive(m*m,n//2)
  elif(n%2!=0):
    return power_recursive(m*m,n//2)*m

sonuc=power_recursive(2,4)
print(sonuc)


#  ----------Loop Power----------

def power_loop(m,n):
  s=1
  for i in range(n):
    s=s*m
  return s

sonuc=power_loop(5,3)
print(sonuc)