ERRO_DIV_ZERO = "ERRO_DIV_ZERO"


def obter_numero(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")


def obter_operacao():
    while True:
        operacao = input("Escolha sua operação (+ - * /): ").strip()
        if operacao in ["+", "-", "*", "/"]:
            return operacao
        print("Operação inválida. Tente novamente.")


def calcular(n1, n2, operacao):
    if operacao == "+":
        return n1 + n2
    elif operacao == "-":
        return n1 - n2
    elif operacao == "*":
        return n1 * n2
    elif operacao == "/":
        if n2 == 0:
            return ERRO_DIV_ZERO
        return n1 / n2


continuar = "s"

while continuar == "s":
    n1 = obter_numero("Digite o primeiro número: ")
    n2 = obter_numero("Digite o segundo número: ")
    operacao = obter_operacao()

    resultado = calcular(n1, n2, operacao)

    if resultado == ERRO_DIV_ZERO:
        print("Erro: divisão por zero não é permitida.")
    else:
        print("Resultado:", resultado)

    continuar = input("Deseja continuar? (s/n): ").strip().lower()[0]