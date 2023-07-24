from p_10 import *

try:
    num=get_phonenumber()
except(IphoneNumberlengthError,IphoneNumbernotdigitError) as e:
    #IphoneNumbernotdigitError='电话号码位数不正确'
    print(e)
else:
    print(num)

