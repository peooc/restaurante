# Paulo elias 12202124

import threading
import queue
import time

# Cria uma fila segura para múltiplas threads (fluxos de execução paralelos dentro do programa)
fila_pedidos = queue.Queue()

TOTAL_PEDIDOS = 5



# THREAD CLIENTE - Funcao do cliente responsavel por gerar pedidos adicionar pedidos na fila

def cliente():

    
    # Laco de repeticao - Cada repetição gera um pedido.
    for i in range(1, TOTAL_PEDIDOS + 1):

        pedido = f"Pedido {i}"

        # put Adiciona pedido na fila First In First Out - Cliente atua como produtor
        fila_pedidos.put(pedido)

        # Exibição do pedido criado
        print(f"Pedido criado: {pedido}")
        # time.sleep simula tempo de preparo e chegada de pedidos faz o cliente esperar 1 segundo antes de criar outro pedido - simula: chegada gradual de clientes tempo real de operação
        time.sleep(1)



# THREAD COZINHA

def cozinha():

    for i in range(TOTAL_PEDIDOS):

       
        # RETIRAR PEDIDO DA FILA - Responsável por retirar pedidos da fila processar pedidos - cozinha atua como consumidor
        
        pedido = fila_pedidos.get()

        print(f"Cozinha retirou da fila: {pedido}")

        
        # PROCESSAR PEDIDO - Simula início do preparo.
        
        print(f"Cozinha preparando: {pedido}")
        # A cozinha demora 2 segundos preparando o pedido.
        time.sleep(2)

        # Simula pedido finalizado
        print(f"Pedido preparado: {pedido}")

        # Marca tarefa como concluída - Informa à fila: O pedido foi concluído
        fila_pedidos.task_done()


# Criação das threads 
thread_cliente = threading.Thread(target=cliente)
thread_cozinha = threading.Thread(target=cozinha)

# Inicia threads - Concorrencia as duas funções executam ao mesmo tempo.
thread_cliente.start()
thread_cozinha.start()

# Aguarda finalização - Espera das threads o programa aguarda: cliente terminar cozinha terminar - antes de encerrar
thread_cliente.join()
thread_cozinha.join()

print("Sistema encerrado.")
