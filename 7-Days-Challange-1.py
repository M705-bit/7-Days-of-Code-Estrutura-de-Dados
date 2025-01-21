'''
O desafio para o dia é implementar uma versão simplificada de uma lista de compras usando arrays. 
A lista deve permitir adicionar novos itens, remover itens e listar todos os itens.

Ao adicionar um novo item, o usuário deve inserir o nome do produto e a quantidade desejada. 
Ao remover um item, o usuário deve especificar o nome do produto. Por fim, ao listar todos os itens, 
a lista deve exibir o nome do produto e a quantidade em um formato legível.

Obs: não é necessário criar nenhuma interface do usuário para esse desafio (a não ser que você queira), 
o objetivo é executar apenas um único arquivo.'''

class Produto:
    def __init__(self, dados):
      # Atribuir os valores da tupla a 'nome' e 'idade'
        self.nome, self.idade = dados
        self.next = None
        self.prev = None

class ListadeCompras: 
    def __init__(self):
        self.head= None 
    def adiciona_produto (self, dados):
        produto = Produto(dados)  # Instancia o produto automaticamente
        produto.next = self.head
        if self.head:
            self.head.prev = produto
        self.head = produto
        produto.prev = None 
  
    def retira_produto(self, alvo):
        atual = self.head
        while atual:
            if atual.nome == alvo:
                # Se for o primeiro produto da lista
                if atual.prev is None:
                    self.head = atual.next
                else:
                    atual.prev.next = atual.next

                # Se for o último produto da lista
                if atual.next:
                    atual.next.prev = atual.prev
                return  # Sai da função após remover o produto
                
            atual = atual.next
        print("Produto não encontrado.")  # Se o produto não for encontrado

    def mostra_lista(self):
        atual = self.head
        while atual:
            print(f"produto: {atual.nome} quantidade: {atual.idade}")
            atual = atual.next

def menu():
    lista_de_compras = ListadeCompras()  # Criação da lista de compras
    while True:
        print("\nEscolha uma opção:")
        print("1. Adicionar produto")
        print("2. Remover produto")
        print("3. Mostrar lista de produtos")
        print("4. Sair")
        
        escolha = input("Digite o número da opção desejada: ")

        match escolha:
            case '1':
                print("Você escolheu a opção 1.")
                try:
                    entrada = input("Digite o produto e a quantidade separados por espaço: ")  
                    nome, quantidade = entrada.split(" ")  # Separa a string em dois valores
                    #produto1[i++] = Produto((nome.strip(), int(quantidade.strip())))  # Cria a tupla e a instância do produto
                    lista_de_compras.adiciona_produto((nome.strip(), int(quantidade.strip())))  # Adiciona o produto à lista
                   
                except ValueError:
                    print("Entrada inválida. Certifique-se de usar o formato correto: nome, quantidade")
            case '2':
                print("Você escolheu a opção 2.")
                entrada = input("Digite o nome do produto a ser removido: ")  
                lista_de_compras.retira_produto(entrada.strip())
            case '3':
                print("Você escolheu a opção 3.")
                lista_de_compras.mostra_lista()
            case '4':
                print("Saindo...")
                break  # Sai do loop quando o usuário escolhe a opção 4

menu()
