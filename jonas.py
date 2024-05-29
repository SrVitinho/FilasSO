import numpy as np
import threading as th
import time

tempo_corote = 1    #if = 1
tempo_agua = 2      #if = 2
tempo_gummy = 2     #if = 3
tempo_cerveja = 3   #if = 4
tempo_vodka = 5     #if = 5

np.random.seed(27)

class Bebida:
    def __init__(self, nome, tempo):
        self.nome = nome
        self.tempo = tempo

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

#Função FIFO
def FIFO(arr, arr_bebida):

    tempo = 0 #Tempo inicial

    for i in range(len(arr)):

        #Esperando chegar os pedidos
        while tempo < arr[i]:
            print("FIFO:Esperando pedidos")
            time.sleep(1)
            tempo += 1
        
        #Escolhendo a bebida
        if arr_bebida[i] == 1:
            print("FIFO:")
            Bebida.corote() #Chamando a função bebida
            tempo += tempo_corote #Adicionando o tempo da bebida
            

        elif arr_bebida[i] == 2:
            print("FIFO:")
            Bebida.agua()
            tempo += tempo_agua
            

        elif arr_bebida[i] == 3:
            print("FIFO:")
            Bebida.gummy()
            tempo += tempo_gummy
            

        elif arr_bebida[i] == 4:
            print("FIFO:")
            Bebida.cerveja()
            tempo += tempo_cerveja
            

        elif arr_bebida[i] == 5:
            print("FIFO:")
            Bebida.vodka()
            tempo += tempo_vodka
            
    print("Tempo médio FIFO: ", tempo/10.0)

#Função SJF
def SJF(array):

    tempo = 0 #Tempo inicial
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
            if sorted_array[0][j] <= tempo: 

                fila.append(sorted_array[1][j]) #Adiciona a bebida na fila
                sorted_array[0][j] = 10000 #Muda o valor para não ser pego novamente

                # Transpõe o array
                transposed_array = array.T

                # Faz a ordenação do array pela primeira coluna
                sorted_transposed_array = transposed_array[transposed_array[:, 0].argsort()]

                # Transpõe de volta para a orientação original
                sorted_array = sorted_transposed_array.T

            elif sorted_array[0][j] > tempo:
                break

        if(len(fila) == 0):
            print("SJF: Esperando pedidos")
            time.sleep(1) #Esperando o tempo
            tempo += 1 #Acrescentando o tempo
            continue

        fila.sort() #Ordenando a fila 
        bebida = fila[0] #Pegando a primeira bebida da fila

        #Escolhendo a bebida
        if bebida == 1:
            print("SJF:")
            Bebida.corote() #Chamando a função bebida
            tempo += tempo_corote #Adicionando o tempo da bebida
            

        elif bebida == 2:
            print("SJF:")
            Bebida.agua()
            tempo += tempo_agua
            

        elif bebida == 3:
            print("SJF:")
            Bebida.gummy()
            tempo += tempo_gummy
            

        elif bebida == 4:
            print("SJF:")
            Bebida.cerveja()
            tempo += tempo_cerveja
            
            
        elif bebida == 5:
            print("SJF:")
            Bebida.vodka()
            tempo += tempo_vodka


        fila.pop(0) #Removendo a bebida da fila
        i += 1 #Incrementando o contador

    
    print('Tempo Médio SJF:',tempo/10.0)
       
#Aleatoriamente pegando o tempo de chegada
arr = np.array(np.random.randint(1, 10, 10)) 

#Aleatoriamente pegando a bebida escolhida
arr_bebida = np.array(np.random.randint(1, 5, 10))

#Criando uma matriz com os dois arrays
arr2 = np.array([arr,arr_bebida])
print(arr2)

#Criando as threads
thread1 = th.Thread(target = FIFO, args=[arr, arr_bebida])
thread2 = th.Thread(target = SJF, args=[arr2])

thread1.start()
thread2.start()
