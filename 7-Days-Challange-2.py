"""
O desafio para o dia de hoje é implementar um sistema de gerenciamento de pacientes em um hospital usando listas 
simplesmente encadeadas.

Cada paciente deve ter um nome, um número de identificação e o estado de saúde atual do paciente, como “estável”, 
“em tratamento intensivo”, “em estado crítico”, entre outros.

O sistema deve permitir adicionar novos pacientes, remover pacientes e listar todos os pacientes em ordem de chegada.
"""
class Paciente:
    def __init__(self):
        self.prev = None
        self.next = None

class novoPaciente(Paciente):  # novoPaciente herda de Paciente
    # criando o construtor
    def __init__(self, nome, num, estado):
        super().__init__()  # Chama o construtor da classe base Paciente
        self.name = nome
        self.number = num
        self.state = estado

class ListadePacientes:
    def __init__(self):
        self.head = None  # Início da lista encadeada

    def adiciona_paciente(self, name, num, state):
        # Cria um novo nó do tipo novoPaciente
        newnode = novoPaciente(name, num, state)

        # Verifica se a lista está vazia
        if self.head is None:
            self.head = newnode  # Define o novo nó como o head
            return  # Sai da função, pois o nó foi adicionado

        # Percorre a lista até o final
        current = self.head
        while current.next is not None:
            current = current.next

        # Adiciona o novo nó no final da lista
        current.next = newnode
        newnode.prev = current

    def retira_paciente(self, alvo):
        atual = self.head
        while atual:
            if atual.name == alvo: 
                # Se for o primeiro produto da lista
                if atual.prev is None:
                    self.head = atual.next
                    if self.head:  # Se houver um próximo nó, atualiza seu prev
                        self.head.prev = None
                else:
                    atual.prev.next = atual.next
                # Se for o último produto da lista
                    
                if atual.next:
                    atual.next.prev = atual.prev
                    
                return  # Sai da função após remover o produto
                
            atual = atual.next
        print("Nome ou número de registro não encontrado.")  # Se o produto não for encontrado
# como eu preciso exibir os pacientes em ordem dechegada, o último da lista deve ser exebido primeiro e assim sucessivamente 
    def mostra_lista(self):
        atual = self.head
        while atual:
            print(f"paciente: {atual.name} número de registro: {atual.number} estado: {atual.state}")
            atual = atual.next

def menu():
    lista_de_pacientes = ListadePacientes()  # Criação da lista de compras
    while True:
        print("\nEscolha uma opção:")
        print("1. Adicionar paciente")
        print("2. Remover paciente")
        print("3. Mostrar lista de pacientes")
        print("4. Sair")
        
        escolha = input("Digite o número da opção desejada: ")

        match escolha:
            case '1':
                print("Você escolheu a opção 1.")
                try:
                    entrada = input("Digite o nome do paciente, seu número de registro e seu estado separados por vírgula: ")  
                    nome, num, estado  = entrada.split(",")  # Separa a string em dois valores
                    lista_de_pacientes.adiciona_paciente(nome.strip(), int(num.strip()), estado)  
                except ValueError:
                    print("Entrada inválida. Certifique-se de usar o formato correto: nome, quantidade")
            case '2':
                print("Você escolheu a opção 2.")
                entrada = input("Digite o nome do produto a ser removido: ")  
                lista_de_pacientes.retira_paciente(entrada.strip())
            case '3':
                print("Você escolheu a opção 3.")
                lista_de_pacientes.mostra_lista()
            case '4':
                print("Saindo...")
                break  # Sai do loop quando o usuário escolhe a opção 4

menu()
