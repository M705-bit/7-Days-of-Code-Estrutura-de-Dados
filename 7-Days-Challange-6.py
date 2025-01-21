'''
#7DaysOfCode 
O desafio para o dia de hoje é implementar um sistema de pontuação para
jogos online usando uma técnica de hashmap na sua linguagem preferida. 
Cada jogador terá um nome de usuário e um número de pontos associado, e 
o sistema deve permitir adicionar novos jogadores, atualizar a pontuação
de jogadores existentes, remover jogadores e listar todos os jogadores 
em ordem decrescente de pontos, além de determinar qual jogador é o
vencedor.

'''
#essa vai ser a primeira vez que lido com HashMaps, desculpe se houver algum erro no código abaixo
class Game:
    def __init__(self, size):
        self.size = size
        self.data = [[] for _ in range(size)] #isso é uma vetor de listas

    def _hash(self, key):
        return hash(key) % self.size
        #essa função calcula o resto da chave, esse resto será o índice onde eu o nome da pessoa será armazendado 
     
    def addPlayer(self, key, value):
        index = self._hash(key)
        for lista in self.data[index]: # eu vejo se tem a lista tal no meu vetor de listas 
            if lista[0] == key:
                lista[1] = value
                return
        self.data[index].append([key, value])

    def get(self, key):
        index = self._hash(key)
        for kv in self.data[index]:
            if kv[0] == key:
                return kv[1]
        return "Data Not Found"
        
    def deletePlayer(self, key):
        index = self._hash(key)
        for i, kv in enumerate(self.data[index]):
            if kv[0] == key:
                self.data[index].pop(i)
                return

    def __str__(self):
        #tenho que mostrar os dados em ordem 
        return str(self.data)

num = input("São quantos jogadores? ")
hash_map = Game(int(num))
while True: 
    print("1. Para adicionar jogadores" , "2.Para retirar jogadores", "3.Para mostrar jogadores", "4.Para sair", sep = "\n")
    num_selecionado = input("Digite sua opção: ")
    match num_selecionado:
        case '1': 
            print("\n Qual o nome do jogador? \n")
            nome = input(str())
            print("\n Quantos pontos esse jogador tem? \n")
            pontos = input(int())
            hash_map.addPlayer(nome, pontos)
            print(hash_map.get(nome)) # Output: 123
        case '2':
            print("\n Qual o nome do jogador? \n")
            nome = input(str())
            hash_map.deletePlayer(nome)
        case '3':
            print(hash_map)
        case '4':
            print("Saindo...")
            break 
    
        

