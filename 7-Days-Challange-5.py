"""
#7DaysOfCode 
O desafio do dia é implementar uma pilha simples para gerenciar os livros da saga “As Crônicas de Gelo e Fogo” (Game of Thrones). 
Cada livro deve ter um nome e o número de páginas. O sistema deve permitir adicionar novos livros na pilha, remover livros, mostrar 
o livro que está no topo e listar todos os livros da pilha.

Você pode implementar uma pilha de diversas formas, como com arrays ou até mesmo listas encadeadas. Para este desafio, eu vou fazer 
com arrays, mas sinta-se livre em decidir qual abordagem irá seguir.
"""
"""
Lista Duplamente Ligada é uma estrutura de dados para armazenar objetos em ordem linear, cada objeto tem um dado e dois ponteiros, 
um para o objeto que o antecede e outro para o qual o sucede.
"""

#criando um nó, que apontará para seu antecessor e sucessor 
class Node: 
    def __init__(self):
        self.prev = None
        self.next = None 
#classe herdeira de Node, faço desse jeito, pois para mimé mais fácil de manipular os atributos do objeto 
class newNode(Node):
    def __init__(self, nome, num):
        super().__init__()  # Chama o construtor da classe base Paciente
        self.nome_do_livro = nome
        self.paginas = num

class ListaLigada:
    def __init__(self):
        self.head = None
        self.tail = None
    @property
    def mostra(self):
         return self.head, self.tail
    
    def FIFO_add(self, nome, num):
            
            #adiciona no início
            newnode = newNode(nome,num)
            if self.head is None:
                self.head = newnode  # Define o novo nó como o head
                return  # Sai da função, pois o nó foi adicionado
            current = self.head
            while current.next is not None:
                current = current.next
            current.next= newnode
            newnode.prev = current
            self.tail = current.next
    def FIFO_delete(self):
            current= self.head
            if current.next is not None:
                 self.head = current.next 
                 current.next.prev = None
                 return 
            else:
                 self.head = None

    def LIFO_add(self, nome,num):
        #chama o FIFO_add, pq é o mesmo algoritimo
        self.FIFO_add(nome, num) 
         
    def LIFO_delete(self):
         if self.head is None:
              return 
         current = self.head 
         while current.next is not None:
              current = current.next       
         if current.prev is None:
              self.head = None  
              return
         else: 
            current = self.tail
            self.tail = current.prev 
            current.prev.next = None 
    def MostraLista(self):
        current = self.head
        while current:
            print(f"Livro: {current.nome_do_livro}, Páginas: {current.paginas}")
            current = current.next
         
def main():
     lista_de_livros= ListaLigada()
     while True: 
        print("1.Formar uma fila", "2.Formar uma pilha", "3.Sair", sep= '\n')
        botao= input("Digite a opção desejada: ")
        match botao:
            case '1':
                print("1.Adicionar a fila", "2.Retirar da Fila", "3.Mostrar a Fila", "4.Sair", sep = '\n')
                botao1 = input("Digite a opção desejada: ")    
                match botao1: 
                     case '1':       
                        try: 
                            livro = input("Escreva aqui o nome do livro e o número de páginas, separa as informações com vírgula:")  
                            titulo, qts = livro.split(',')
                            ListaLigada.FIFO_add(lista_de_livros,titulo, qts)
                            
                        except ValueError:
                            print("Entrada inválida. Certifique-se de usar o formato correto: nome do livro , número de páginas")
                     case '2':
                            ListaLigada.FIFO_delete(lista_de_livros)
                     case '3': 
                             ListaLigada.MostraLista(lista_de_livros)
                     case '4': 
                         print("Saindo...")
                         break 
            case '2':
                print("1.Adicionar à pilha", "2.Retirar da pilha", "3.Mostrar a Pilha", "4.Sair",  sep = '\n')
                botao1 = input("Digite a opção desejada: ")    
                match botao1: 
                     case '1':       
                        try: 
                            livro = input("Escreva aqui o nome do livro e o número de páginas, separa as informações com vírgula:")  
                            titulo, qts = livro.split(',')
                            ListaLigada.LIFO_add(lista_de_livros,titulo, qts)
                            
                        except ValueError:
                            print("Entrada inválida. Certifique-se de usar o formato correto: nome do livro , número de páginas")
                     case '2':
                            ListaLigada.LIFO_delete(lista_de_livros)
                     case '3': 
                             ListaLigada.MostraLista(lista_de_livros)
                     case '4': 
                         print("Saindo...")
                         break 
            case '3':
                print("Saindo...")
                break 
main() 