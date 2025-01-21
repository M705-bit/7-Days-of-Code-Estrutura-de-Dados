"""
O desafio para o dia é implementar uma fila simples para gerenciar pedidos de um restaurante. 
Cada pedido pode ser representado por uma string com o nome do prato e a mesa em que foi feito. 
O sistema deve permitir adicionar novos pedidos na fila, remover pedidos que já foram entregues 
e listar todos os pedidos na ordem em que foram feitos.

Você pode implementar uma fila de diversas formas, como com arrays ou até mesmo listas encadeadas.
 Para este desafio, eu vou fazer com arrays, mas sinta-se livre em decidir qual abordagem irá seguir.
"""
class Node:
    def __init__(self):
        self.next = None
        self.prev = None
class newNode(Node):
    def __init__(self, nome, num):
        super().__init__()  # Chama o construtor da classe base Paciente
        self.nome_do_prato = nome
        self.mesa = num

class ListaDePedidos:
    def __init__(self):
         self.head = None  # Início da lista encadeada
         self.tail = None
    def InsereNoFinal(self, name,num):
        # Cria um novo nó do tipo novoPaciente
        newnode = newNode(name, num)

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
    
    def RemoveDoInicio(self):
         current = self.head
         if current.next is not None:
            self.head = current.next 
            current.next.prev = None 
         else:
             self.head= None 
    def MostraLista(self):
        current = self.head
        while current:
            print(f"Pedido: {current.nome_do_prato}, Mesa: {current.mesa}")
            current = current.next
        
def main():
    lista_de_pedidos = ListaDePedidos()
    qtd = 0 
    while True: 
        print("1.Para entrar na fila", "2.Para sair da fila", "3.Para mostrar a lista", "4. Para Sair", sep= '\n')
        botao= input("Digite a opção desejada: ")
        match botao:
            case '1':
                try: 
                    pedido = input("Escreva aqui o nome do prato e o da mesa separados por vírgula:")  
                    nome, mesa = pedido.split(',')
                    lista_de_pedidos.InsereNoFinal(nome, mesa)
                    qtd+=1
                except ValueError:
                      print("Entrada inválida. Certifique-se de usar o formato correto: nome do pedido , numero da mesa")
            case '2':
                lista_de_pedidos.RemoveDoInicio(qtd)
            case '3': 
                lista_de_pedidos.MostraLista()
            case '4': 
                print("Saindo...")
                break 
main() 




   
    


