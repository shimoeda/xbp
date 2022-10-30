import random
from re import I
from tkinter import Y



counter=0

print("99を超えないように限界まで挑戦してください。")
print("現在の数字は０です。")
while counter<=99:
    a  =   random.randint(1,30)
    question=input("まだ足しますか。")
    if question=="yes":
        counter=counter+a
        print("現在の合計は",counter,"です。")
    elif counter==99:
        print("おめでとうございます。99ぴったりです。")    
        break
    elif question=="no":
        print("ハイスコアは",counter,"です。")
        break


    else:
        print("99を超えました。失敗です。")
        
