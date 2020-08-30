country = input ("輸入你的國家 : ")
age = int(input("輸入你的年齡 : "))

if country == "台灣" :
    if age >= 18 :
        print("你可以考駕照")
    else :
        print("你還不能考駕照")
elif country == "美國" :
    if  age >= 16 :
        print("你可以考駕照")
    else : 
        print("你不能考駕照")
else :
    print("你只可以輸入 台灣/美國")
    
    #
