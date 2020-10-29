def is_power_of_two(n):
    # Check if the number can be divided by two without a remainder

 n == 0
 while n <= 10:
     n += 1
     if n % 2 == 0 or n / 2 == 1:
          return True

     if n / 2 != 1 and n % 2 != 0:
          return False
     
       
            
print(is_power_of_two(0))  # Should be False
print(is_power_of_two(1))  # Should be True
print(is_power_of_two(9))  # Should be True
print(is_power_of_two(8))  # Should be False
