print("a*b mod m = 1\n")
a = int(input("Please input a string:"))
m = int(input("Please input m string:"))
Om = m # to save the original m
conter = 0
while True:
    if (m + 1)%a != 0:
        m+=Om
        conter+=1
    else:
        b = (m + 1)/a
        print(f"Inverting model = {b} \nto {a}*{b} mod {m} = 1")
        break
