def imc(peso, altura):
    return peso / (altura * altura)

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

print("Seu imc é: ", imc(peso, altura))