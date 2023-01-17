# finding nth palindrome number
# n=int(input("Enter the nth number:- "))  #enter the nth value to find palindrome 
n=1
def check_prime(num):
  """This function will check if the given number is prime or not"""
  if num>1:
      for i in range(2,num//2+1):
          if num%i==0:
              return False
  return True
def check_palindrome(num):
  """This function will check if the given number is palindrome or not
  A palindrome is a number.
  A palindromic number (also known as a numeral palindrome or a numeric palindrome) is a number (such as 16461) that remains the same when its digits are reversed. """
  if str(num)[::-1]!=str(num):
      return False
  return True

if _name_ == '_main_':
  count=0 
  num=2   
  while True:
      if check_prime(num) and check_palindrome(num):
          if count==n:
              print(f"The {count} prime palindrome is {num}")
              break
          count+=1
      num+=1
#Coded by Abhishek Bharti