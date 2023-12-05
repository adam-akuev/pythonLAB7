k = int(input('Введите количество стран:'))
if k > 0:
    C_C = {}
    for i in range(k):
        country = str(input("Введите название страны:"))
        citys = str(input("Введите название городов через пробел:")).split()
        C_C[country] = citys
    print(C_C)
    Gorod = str(input('!:'))
    for country, citys in C_C.items():
        if Gorod in citys:
            print(f'Город:{Gorod}=Страна:{country}')