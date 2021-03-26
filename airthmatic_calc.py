# addition
def sum ():
    n = float(input("Enter first number: "))
    t = 0 # Total inputs to be used in finding average
    ans = 0
    while n != 0:
        ans = ans + n
        t+=1
        n = float(input("Enter another number (When done, Press 0 instead of =): "))
    return [ans,t]
# multiplication
def product ():
    print("Multiplication")
    n = float(input("Enter first number: "))
    ans = 1
    while n != 1:
        ans = ans * n
        n = float(input("Enter another number (When done, Press 1 instead of =): "))
    return [ans]
# Division
def division ():
    print("Division")
    n = float(input("Enter numerator: "))
    d = float(input("Enter denominator: "))
    ans = n/d
    return [ans]
# average
def average():
    avg = []
    avg = sum()
    t = avg[1]
    a = avg[0]
    ans = a / t
    return [ans,t]

while True:
    list = []
    print(" Enter 'a' for addition")
    print(" Enter 'm' for multiplication")
    print(" Enter 'd' for division")
    print(" Enter 'v' for average")
    print(" Enter 't' for tips")
    print(" Enter 'q' for quit")
    c = input(" ")
    if c != 'q':
        if c == 'a':
            print("Addition")
            list = sum()
            print("Ans = ", list[0])
        elif c == 'm':
            list = product()
            print("Ans = ", list[0])
        elif c == 'd':
            list = division()
            print("Ans = ",list[0])
        elif c == 'v':
            list = average()
            print("Ans = ", list[0])
        elif c == 't':
            print()
            print("**TIP 1**")
            print("For subtraction you can do simple addition by pressing 'a' ")
            print("And then input number with a minus(-) sign")
            print("")
        elif c == '0':
            print(""" YAY! Your Found The Hidden Easter Egg Menu 
            Press any letter from a,b,c,d """)
            v = input()
            if v == 'a' :
                print("""░░░░░░░▄▄████▄▄▄░░░░░░▄▄██████▄▄
░░░░░██▓▓▓▓▓▓▒▓▓██░░▓█▓▓▓▓▒░▒▒▓▓██
░░░██▓▓▓▓▓▓▓▓▓▒░▓▓███▓▓▓▓▓▒▒▒░░▒▓▓█
░░██▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓█▓▓▓▓▓▓▓▓▓▓▒░░▓▓█
░▒█▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓██▓▓▓▓▓▓▓▓▓▒░░▓▓█
░█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░▒▓█
░█▓▓▓▓▓▓▓▓▓▓▓▓████░████▓▓▓▓▓▓▓▓▓▒░░▓██
█▓▓▓▓▓▓▓▓▓▓▓▓██░░░░░░░██▓▓▓▓▓▓▓▓▓░░▓▓█
█▓▓▓▓▓▓▓▓▓▓▓▓▓░░█░░░█░░▓▓▓▓▓▓▓▓▓▓▒░▓▓█▒
█▓▓▓▓▓▓▓▓▓▓▓▓▓░█▒█░█▒█░▓▓▓▓▓▓▓▓▓▓▒▒▓▓█▒
█▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▒▒▓██▒
█▓▓▓▓▓▓▓▓▓▓▓▓▓▓░▒██░░░▓▓▓▓▓▓▓▓▓▓▓▒▓▓█▓▒
░█▓▓▓▓▓▓▓▓▓▓▓▓▓▓████▓▓▓▓▓▓▓▓▓▓▓▓▓▒▓▓█▓▒
░█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▒
░░█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▒
░░█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███▓▓▓▓▓▓▓▓▓▓█▓▒
░░░█▓▓▓▓▓▓▓▓▓██▓▓▓▓█████▓▓▓▓▓▓▓▓▓▓█▓▒
░░░░█▓▓▓▓▓▓▓▓██████████▓▓▓▓▓▓▓▓▓▓██▓▒
░░░░▓█▓▓▓▓▓▓▓▓██▒▒▓▒▒█▓▓▓▓▓▓▓▓▓▓██▓▒
░░░░░░█▓▓▓▓▓▓▓▓██▒▒▒█▓▓▓▓▓▓▓▓▓▓██▓▒
░░░░░░░██▓▓▓▓▓▓▓▓███▓▓▓▓▓▓▓▓▓▓██▓▒
░░░░░░░░██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▒
░░░░░░░░░░█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▒
░░░░░░░░░░░██▓▓▓▓▓▓▓▓▓▓▓▓██▓▒
░░░░░░░░░░░░░██▓▓▓▓▓▓▓▓▓█▓▒
░░░░░░░░░░░░░░░██▓▓▓▓▓██▓▒
░░░░░░░░░░░░░░░░░█▓▓██▓▒
░░░░░░░░░░░░░░░░░░░█▓▒
""")
            elif v == 'b' :
                print("""────(♥)(♥)(♥)────(♥)(♥)(♥) __ ɪƒ ƴσυ'ʀє αʟσηє,
──(♥)██████(♥)(♥)██████(♥) ɪ'ʟʟ ɓє ƴσυʀ ѕɧα∂σѡ.
─(♥)████████(♥)████████(♥) ɪƒ ƴσυ ѡαηт тσ cʀƴ,
─(♥)██████████████████(♥) ɪ'ʟʟ ɓє ƴσυʀ ѕɧσυʟ∂єʀ.
──(♥)████████████████(♥) ɪƒ ƴσυ ѡαηт α ɧυɢ,
────(♥)████████████(♥) __ ɪ'ʟʟ ɓє ƴσυʀ ρɪʟʟσѡ.
──────(♥)████████(♥) ɪƒ ƴσυ ηєє∂ тσ ɓє ɧαρρƴ,
────────(♥)████(♥) __ ɪ'ʟʟ ɓє ƴσυʀ ѕɱɪʟє.
─────────(♥)██(♥) ɓυт αηƴтɪɱє ƴσυ ηєє∂ α ƒʀɪєη∂,
───────────(♥) __ ɪ'ʟʟ ʝυѕт ɓє ɱє.
""")
            elif v == 'c' :
                print("..... (¯`v´¯)♥
.......•.¸.•´
....¸.•´
... (
☻/
/▌♥♥
/ \ ♥♥
")
            elif v == 'd' :
                print("_░▒███████
░██▓▒░░▒▓██
██▓▒░__░▒▓██___██████
██▓▒░____░▓███▓__░▒▓██
██▓▒░___░▓██▓_____░▒▓██
██▓▒░_______________░▒▓██
_██▓▒░______________░▒▓██
__██▓▒░____________░▒▓██
___██▓▒░__________░▒▓██
____██▓▒░________░▒▓██
_____██▓▒░_____░▒▓██
______██▓▒░__░▒▓██
_______█▓▒░░▒▓██
_________░▒▓██
_______░▒▓██
_____░▒▓██
")
            else :
                print("Smarty Pants!")
        else:
            print("Please choose from given options.")
    else:
        break