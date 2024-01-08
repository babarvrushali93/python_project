# email validation in python
# (using RegEX -re )

# a - z (isalpha)
# 0-9 (num)
# . _ ( at time 1)
# @ (at time 1)
# . (revsers 2[-2],3[-3] position)

import re
email_condition="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email=input("Enter your Email : ")

if re.search(email_condition,user_email):
    print(" Right email ")
else:
    print(" wrong email ")    