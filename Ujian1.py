# Soal nomor 1

# notel = input('masukkan nomer telpon:')
# import re
# if notel.isnumeric():
#     print('(%s) %s-%s' % tuple(re.findall(r'\d{4}$|\d{3}', notel)))
# elif notel.isalpha():
#     print('Invalid Input. No Alphabet.')
# elif notel.isascii():
#     print('Invalid Input. No Symbols')
# else :
#     print('Digits must be in length of 10, not more or less')



# Soal nomor 2

# def moveZeros(list):
#     newList = []
#     zero = 0
#     for i in list:
#         if i != 0 or type(i) == type(False) :
#             newList.append(i)
#         else :
#             zero += 1
#     for i in range(zero):
#         newList.append(0)
#     return newList
# print(moveZeros([False,1,0,1,2,0,1,3,'a']))
# print(moveZeros([0,0,0,'Test',0,3,'a','True','False']))
# print(moveZeros([0,'True','True','False','a','b',1,1,1]))


# Soal nomor 3

# import statistics as st
# angka = ([1, 2, 3, 4, 5, 'a'])
# m1=st.mean(angka)
# m2=st.median(angka)
# m3=st.mode(angka)
# m4=st.std(angka)

# print(m1,m2,m3,m4)



