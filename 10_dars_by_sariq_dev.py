# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 22:31:19 2022

@author: user
"""

# avtolar = ['mustang', 'audi', 'bmw', 'volvo', 'kia', 'hyundai']
# for avto in avtolar:
#     if avto == 'bmw':
#         print(avto.upper())
#     else:
#         print(avto.title())
        
# ism = "Ali"
# ism.lower() == 'ali'

# ism = input('Ismingiz nima\n>>>')
# if ism.lower() != 'ali':
#     print(f'Uzur {ism.title()} biz Alini kutyapmiz!!!')
# else:
#     print('Salom Ali!!!')
        
# javob = float(input("12x6 nechiga teng?\n>>>"))
# if javob != 72:
#     print('Xato javob!')

# yosh = int(input('Yoshingiz nechida?\n>>>'))
# if yosh >= 18:
#     print('Xush kelibsiz!!!')
# else:
#     print('Kirish taqiqlangan!!!🚫🚫🚫')

yil = int(input("Tug'ulgan yilingizni kiriting: "))
if 2022-yil < 18:
    print(f'Yoshingiz {2022-yil}da ekan!')
    print('Sizga kirish taqiqlangan!!!🚫🚫🚫')
else:
    print("Xush kelibsiz!!!")    
