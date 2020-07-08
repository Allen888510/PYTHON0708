score=int(input("請輸入成績:"))
if score>100:
    print("請不要亂輸入成績")
elif score>=90 and score>=100:
    print("成績A+ 非常好")
elif score>=80 and score<=90:
    print("成績A 很好")
elif score>=80 and score<=70:
    print("成績B+ 好")
elif score>=70 and score<=60:
    print("成績B 不錯")
else:
    print("成績C 再加油")