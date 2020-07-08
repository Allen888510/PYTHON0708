

h=int(input("請輸入身高:"))
w=int(input("請輸入體重:"))

bmi= w / (h/100)**2
print("bmi=")
print(bmi)

if 18.5<=bmi<24:
    print("正常")
if bmi<18:
    print("過瘦")
if bmi>=24:
    print("過重")