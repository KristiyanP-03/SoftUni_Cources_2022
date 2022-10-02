list_of_numbers = input().split(", ")
def polindrome_checker(list_of_nums):
   for num in list_of_nums:
       if num == num[::-1]:
           print("True")
       else:
           print("False")
polindrome_checker(list_of_numbers)