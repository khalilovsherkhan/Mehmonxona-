d = {
    "sherxon": ["15", "standart"],
    "asqar": ["12", "standart"]
}

def check(data, key, value):
    for i in data.values():
        try:
            if (i[key] == value): return True

        except:
            pass
    return False

def plus():
    name = input("Ismi:  ")
    while name in d.keys():
        print("Bunday ismi mehmon mavjud")
        name = input("Ismi:")
    number = input("Xona raqaini  kiriting:  ")
    while check(d, 0, number):
        print(" Kechirasiz  bu xona band, iltimos boshqa xona tanlang😢😢😢 ")
        number = input("Bu yerga xona raqamini kirting:  ")

    def Type():
        try:
            type = input("Xona turini quydagi belgilar bilan tanlamg: \n e - ekanom  \n s - standart \n l - lyuks \n")

            if type == 'e':
                turi = 'ekanom'
            elif type == 's':
                turi = 'standart'
            elif type == 'l':
                turi = 'lyuks'
            d[name] = [number, turi]
            print(f"{name} ro'yxatga qo'shildi😎 \n \n")
        except Exception:
            print("Xato belgi kiritild")
            Type()

    Type()


def minus():
    x = input("Qaysing ketmoqchiqasan mehmonxonadan 🤬")
    if x in  d.keys():
        d.pop(x)
        print(x, " yo'q boldi 😂")

    else:
        print("Bu odam mehmonxonamz umuman mavjud emasss \n \n")


def show():
    print("{:>18} {:>25} {:>20}".format('Ismi', 'Xonasi', 'Xona turi', ), "\n")
    for k, v  in  d.items():
        v1, v2 = v 
        print("{:>18} {:>25} {:>20}".format(k, v1, v2  ))

    print("\n \n")


while True:
    option = input(
        "       Xush kelmabsz!!!\n Buyruqni tanlang: \n 1 - mehmon qoshish \n 2 - mehmonni ro'yxatdan chiqarish  \n 3 - mehmonla ro'yxati       \n 0 - dasturdan chiqish    \n")
    

    if option == "1":
        plus()
    elif option == "2":
        minus()

    elif option == "3":
        show()
        break
