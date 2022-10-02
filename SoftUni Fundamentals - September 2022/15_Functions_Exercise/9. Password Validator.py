the_password = input()
def password_checker(password):
   i_count = 0
   digit_counter = 0
   errors = 0
   unknow_char = False
   for i in password:
       i_count += 1
       if i.isdigit() == True:
           digit_counter += 1
       elif i.isalpha() == False:
           unknow_char = True
           errors += 1
           break
   if unknow_char == True:
       print("Password must consist only of letters and digits")
       quit()
   if 6 > i_count or i_count > 10:
       print("Password must be between 6 and 10 characters")
       errors += 1
   if digit_counter < 2:
       print("Password must have at least 2 digits")
       errors += 1
   if errors == 0:
       print("Password is valid")
password_checker(the_password)