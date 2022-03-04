import secrets


class Conta:
    def __init__(self, Cpf, Nome, Senha, Saldo):
        self.Token = secrets.token_bytes(16)
        self.cpf = Cpf
        self.senha = Senha
        self.nome = Nome
        self.saldo = Saldo
        self.historico = ()

    def deposito(self, valor):
        self.saldo = self.saldo + valor
        self.historico.append("+ {}".format(valor))

    def saque(self, valor):
        if self.saldo > valor:
            self.saldo = self.saldo - valor
            self.historico.append("- {}".format(valor))
        else:
            print("Saldo Insuficiente")

    def extrato(self):
        print("Seu Saldo é de:", self.saldo, "\n")
        print(self.historico)

    def transfer(self, destino, valor):
        if self.saldo > valor:
            self.saldo = self.saldo - valor
            destino.saldo = destino.saldo + valor
            self.historico.append("Transferencia para {destino}: - {valor}")
            destino.historico.append("Transferencia recebido {self}: + {valor}")


class Cartao(Conta):
    a = 0


class Premium(Conta):
    a = 0
