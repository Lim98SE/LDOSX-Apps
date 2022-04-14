import math

isRunning=True

basic="123456"
bitwise="78abc"
converters="defgl"
intrest="hi"
pyth="j"
mod="k"
funct="m"

while isRunning:
    try:
        choice=input("""1 - Add
2 - Subtract
3 - Multiply
4 - Divide
5 - Exponent
6 - Root
7 - &
8 - |
9 - ^
A - ~
B - <<
C - >>
D - Decimal to Hex
E - Hex to Decimal
F - Decimal to Binary
G - Binary to Decimal
H - Simple Intrest (Prt)
I - Compound Intrest (P(1+r)^t)
J - Pythagorean Theorum(A²+B²=C²)
K - Modulo (Remainder)
L - Base Converstion
M - Average
X - Exit
Choice here: """).lower()
        if choice[0] in basic:
            a=input("Number One? ").lower()
            b=input("Number Two? ").lower()
            if choice=="1":
                print(f"{a} + {b} = {float(a)+float(b)}")
            elif choice=="2":
                print(f"{a} - {b} = {float(a)-float(b)}")
            elif choice=="3":
                print(f"{a} x {b} = {float(a)*float(b)}")
            elif choice=="4":
                print(f"{a} ÷ {b} = {float(a)/float(b)}")
            elif choice=="5":
                print(f"{a} ^ {b} = {pow(float(a),float(b))}")
            elif choice=="6":
                print(f"{a} ^ 1/{b} = {pow(float(a),1/float(b))}")
        elif choice[0] in bitwise:
            a=input("Number One? ").lower()
            b=input("Number Two? ").lower()
            if choice=="7":
                print(f"{int(a)} && {int(b)} = {int(a) & int(b)}")
            if choice=="8":
                print(f"{int(a)} | {int(b)} = {int(a) | int(b)}")
            if choice=="a":
                print(f"{int(a)} ^ {int(b)} = {int(a) ^ int(b)}")
            if choice=="b":
                print(f"{int(a)} << {int(b)} = {int(a) << int(b)}")
            if choice=="c":
                print(f"{int(a)} >> {int(b)} = {int(a) >> int(b)}")
        elif choice[0]=="9":
            a=input("Number? ")
            print(f"~{a} = {~int(a)}")
        elif choice[0] in converters:
            number=input("Number? ")
            if choice=="d":
                print(f"{number} in hex is {hex(int(number))[0:len(hex(int(number)))]}")
            elif choice=="e":
                print(f"{number} in decimal is {int(number,base=16)})")
            elif choice=="f":
                print(f"{number} in binary is {bin(int(number))[0:len(bin(int(number)))]})")
            elif choice=="g":
                print(f"{number} in decimal is {int(number,base=2)})")
            elif choice=="l":
                a=number
                b=int(input("What base? "))%30
                print(f"{a} in base {b} is {int(a,base=b)}")
        elif choice[0] in intrest:
            if choice=="h":
                p=float(input("P: "))
                r=float(input("R: "))
                t=float(input("T: "))
                print(f"{p}x{r}x{t}={p*r*t}")
            elif choice=="i":
                p=float(input("P: "))
                r=float(input("R: "))
                t=float(input("T: "))
                print(f"{p}x(1+{r})^{t}={p*pow((1+r),t)}")
        elif choice[0] in pyth:
            a=float(input("A: "))
            b=float(input("B: "))
            print(f"{a}²+{b}²={pow(a,2)+pow(b,2)}²")
        elif choice[0]=="k":
            a=input("A: ")
            b=input("B: ")
            print(f"{a} mod {b} is {float(a) % int(b)}")
        elif choice[0] in funct:
            error=False
            toAvg=[]
            while not error:
                try:
                    toAvg.append(float(input("Enter a number. Press nothing to end: ")))
                except ValueError:
                    error=True
            sol=0
            for i in toAvg:
                sol+=i
            sol=sol/len(toAvg)
            print(f"The average is {sol}.")
        elif choice[0]=="x":
            break
    except Exception:
        print("error.")
