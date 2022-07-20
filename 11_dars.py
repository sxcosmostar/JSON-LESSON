# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 11:24:22 2022

@author: user
"""


# yosh = int(input("Yoshingiz nechida?"))
# if yosh <=4:
#     print('Sizga kirish bepul!')
# elif yosh <=12:
#     print('Sizga kirish 5000 so\'m!')
# else:
#     print("Sizga kirish 10000 so'm!")


# kun = input("Bugun qaysi kun?\n>>>")
# if kun.lower() == 'shanba' or kun.lower() == 'yakshanba':
#     print('Bugun dam olish kuni!!!')
# else:
#     print('Bugun ish kuni!!!')

# kun = input("Bugun qaysi kun?\n>>>")
# harorat = float(input('Harorat qanaday?\n>>>'))
# # if kun.lower() == 'yakshanba' and harorat>= 30:
# #     print('Cho\'milishga kettik!!!')
# if (kun.lower() == 'yakshanba' or kun.lower() == 'shanba') and harorat>= 30:
#     print('Cho\'milgani kettik!!!')
# elif (kun.lower() == 'yakshanba' or kun.lower() == 'shanba') and harorat<= 30:
#     print('Uyda dam olaylik!!!')
# else:
#     print('E qoy shanba yo yakshanba kun boramiz')

narx = 15000
choy = True
salat = False

# if choy and salat:
#     narx = narx + 10000
# elif choy or salat:
#     narx = narx +5000

# print(f"Jami {narx} so'm")
# non = True
# kampot = True
# assarti = False
# if choy:
#     print('Mijoz choy sotib oldi.')
#     narx = narx + 3000
    
# if salat:
#     print('Mijoz salat sotib oldi.')
#     narx = narx + 5000
    
# if non:
#     print('Mijoz non sotib oldi.')
#     narx = narx + 2000
    
# if kampot:
#     print('Mijoz kampot sotib oldi.')
#     narx = narx + 5000
    
# if assarti:
#     print('Mijoz assarti sotib oldi.')
#     narx = narx + 15000


menu = ['osh', 'qazonkabob', 'shashlik', 'norin', 'somsa']
buyurtmalar = ['osh', 'somsa', 'manti', 'shashlik']

if buyurtmalar:
    for taom in buyurtmalar:
        if taom in menu:
            print(f"Menuda {taom} bor")
        else:
            print(f"Kechiarsiz, {taom} yo'q")
else:
    print("Savatchangiz bo'sh!")

# for taom in buyurtmalar:
#     if taom in menu:
#         print(f"Menuda {taom} bor")
#     else:
#         print(f"Menuda {taom} yo'q")




# ovqat = input('Nima ovqat yeysiz?\n>>>')
# if ovqat.lower() in menu:
#     print('Buyurtma qabul qilindi!')
# else:
#     print('Bunday ovqat menuda yoq!!!')



# 'manti' in menu
    
    

    



























