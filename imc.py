
def calcular_imc(alt, pes):
    return pes / alt ** 2

while True:
    print("=== MENU ===")
    print("1. Calcular IMC")
    print("2. Sair")
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        alt = float(input("Digite sua altura: "))
        pes = float(input("Digite seu peso: "))
        res = calcular_imc(alt, pes)
        print("Seu IMC é:", res)
        if res < 18.5:
            print("Abaixo do peso")
        elif res <= 24.9:
            print("Peso normal")
        elif res <= 29.9:
            print("Excesso de peso")
        elif res <= 34.9:
            print("Obesidade I")
        elif res <= 39.9:
            print("Obesidade II")
        else:
            print("Obesidade suprema")
    elif escolha == "2":
        break
    else:
        print("Opção inválida. Tente novamente.")
