import numpy as np
import threading as th
import time

np.random.seed(27)

tempo_corote = 1    #if = 1
tempo_agua = 2      #if = 2
tempo_gummy = 2     #if = 3
tempo_cerveja = 3   #if = 4
tempo_vodka = 5     #if = 5

sem1 = th.Semaphore() #Geladeira para o Corote, Agua, Gummy
sem2 = th.Semaphore() #Geladeira para a Cerveja e Vodka

class Bebida:
    #Funções para pegar as bebidas
    def corote():
        print("Pegando Corote") #Mensagem de que está pegando a bebida
        time.sleep(tempo_corote) #Tempo que leva para pegar a bebida

    def agua():
        print("Pegando Agua")
        time.sleep(tempo_agua)

    def gummy():
        print("Pegando Gummy")
        time.sleep(tempo_gummy)

    def cerveja():
        print("Pegando Cerveja")
        time.sleep(tempo_cerveja)

    def vodka():
        print("Pegando Vodka")
        time.sleep(tempo_vodka)

#Função FIFO com Semáforo
def FIFO_Semaforo(arr, arr_bebida):

    print(arr)
    print(arr_bebida)
    inicio = time.time()

    for i in range(len(arr)):

        #Esperando chegar os pedidos
        while (time.time()-inicio) < arr[i]:
            print("FIFO:Esperando pedidos")
            time.sleep(1)
        
        #Escolhendo a bebida
        if arr_bebida[i] == 1:
            if sem1._value == 0:
                print("Geladeira bloqueada, aguardando liberação")
            sem1.acquire() #Trava a geladeira
            print("FIFO:")
            Bebida.corote() #Chamando a função bebida
            sem1.release() #Libera a geladeira
            

        elif arr_bebida[i] == 2:
            if sem1._value == 0:
                print("Geladeira bloqueada, aguardando liberação")
            sem1.acquire()
            print("FIFO:")
            Bebida.agua()
            sem1.release()

        elif arr_bebida[i] == 3:
            if sem1._value == 0:
                print("Geladeira bloqueada, aguardando liberação")
            sem1.acquire()
            print("FIFO:")
            Bebida.gummy()
            sem1.release()

        elif arr_bebida[i] == 4:
            if sem2._value == 0:
                print("Geladeira bloqueada, aguardando liberação")
            sem2.acquire()
            print("FIFO:")
            Bebida.cerveja()
            sem2.release()
            

        elif arr_bebida[i] == 5:
            if sem2._value == 0:
                print("Geladeira bloqueada, aguardando liberação")
            sem2.acquire()
            print("FIFO:")
            Bebida.vodka()
            sem2.release()

    final = time.time()        
    print("Tempo médio FIFO: ", (final - inicio)/10.0)

#Função SJF com Semáforo
def SJF_Semaforo(array):
    print(array)
    inicio = time.time()
    fila = [] #Fila de bebidas

    # Transpõe o array
    transposed_array = array.T

    # Faz a ordenação do array pela primeira coluna
    sorted_transposed_array = transposed_array[transposed_array[:, 0].argsort()]

    # Transpõe de volta para a orientação original
    sorted_array = sorted_transposed_array.T
    
    i = 0
    while(i < 10):
        for j in range(len(sorted_array[0])):
            if sorted_array[0][j] <= (time.time()-inicio): 

                fila.append(sorted_array[1][j]) #Adiciona a bebida na fila
                sorted_array[0][j] = 10000 #Muda o valor para não ser pego novamente

                # Transpõe o array
                transposed_array = array.T

                # Faz a ordenação do array pela primeira coluna
                sorted_transposed_array = transposed_array[transposed_array[:, 0].argsort()]

                # Transpõe de volta para a orientação original
                sorted_array = sorted_transposed_array.T

            elif sorted_array[0][j] > (time.time()-inicio):
                break

        if(len(fila) == 0):
            print("SJF: Esperando pedidos")
            time.sleep(1) #Esperando o tempo
            continue

        fila.sort() #Ordenando a fila 
        bebida = fila[0] #Pegando a primeira bebida da fila

        #Escolhendo a bebida
        if bebida == 1:
            if sem2._value == 0:
                print("Geladeira bloqueada, aguardando liberação")
            sem1.acquire()
            print("SJF:")
            Bebida.corote() #Chamando a função bebida
            sem1.release()
            

        elif bebida == 2:
            if sem2._value == 0:
                print("Geladeira bloqueada, aguardando liberação")
            sem1.acquire()
            print("SJF:")
            Bebida.agua()
            sem1.release()
            

        elif bebida == 3:
            if sem2._value == 0:
                print("Geladeira bloqueada, aguardando liberação")
            sem1.acquire()
            print("SJF:")
            Bebida.gummy()
            sem1.release()
            

        elif bebida == 4:
            if sem2._value == 0:
                print("Geladeira bloqueada, aguardando liberação")
            sem2.acquire()
            print("SJF:")
            Bebida.cerveja()
            sem2.release()
            
            
        elif bebida == 5:
            if sem2._value == 0:
                print("Geladeira bloqueada, aguardando liberação")
            sem2.acquire()
            print("SJF:")
            Bebida.vodka()
            sem2.release()

        fila.pop(0) #Removendo a bebida da fila
        i += 1 #Incrementando o contador

    final = time.time()
    print('Tempo Médio SJF:',(final - inicio)/10.0)

#Aleatoriamente pegando o tempo de chegada
arr = np.array(np.random.randint(1, 10, 10)) 

#Aleatoriamente pegando a bebida escolhida
arr_bebida = np.array(np.random.randint(1, 5, 10))

#Criando uma matriz com os dois arrays
arr2 = np.array([arr,arr_bebida])
print(arr2)

#Criando as threads
thread1 = th.Thread(target = FIFO_Semaforo, args=[arr, arr_bebida])
thread2 = th.Thread(target = SJF_Semaforo, args=[arr2])

thread1.start()
thread2.start()