nums = [2,6,8,9,10,12,13,15,17,24,55,66,78,77,79]

# checks if number is prime
#returns 1 if composite, returns 0 if prime
def gFactor (number): 
     for i in range (2, number):
          if number % i == 0:
               return 1
     return 0
 

def removePrimes():
     for number in nums:
          if gFactor(number) == 0:
               nums.remove(number)


print(nums)
removePrimes()
print(nums)







    
    
