def numerals_converter(z):
     if z == "I":
          z = 1
     if z == "V":
          z = 5
     if z == "X":
          z = 10
     if z == "L":
          z = 50
     if z == "C":
          z = 100
     if z == "D":
          z = 500
     if z == "M":
          z = 1000
     return z

#check if the numebrs are in descending order in which case we just add 
def descending_order_check(x):
     i = 1
     flag = 0
     while i < len(x):
         if (x[i] >= x[i-1]):
               flag = 1
               i = i + 1
     if (not flag):
          return print(True) 
     return print(False)

def roman_convert(s):
     x = [letter for letter in s ]
     nums = []
     for i in x:
          b = numerals_converter(i)
          nums.append(b)
     print(nums, 'got here')
     if descending_order_check(nums) == True:
          return print(nums)


roman_convert("LVIII")




