import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib.patches as mpatches



def question_1():
    # Lista de idades, a função range gera uma lista que vai de 0 a 9. (o 10 é não inclusivo)
    ages = range(0, 10)
    weights = [3.6, 4.4, 5.2, 6, 6.6, 7.2,
               7.8, 8.4, 8.8, 9.2]  # Lista de pesos

    # título
    plt.title("The relationship between age and weight in a growing infant")

    axes = plt.gca()
    axes.set_xlim([-0.5, 9.5])  # limites no eixo x
    axes.set_ylim([1.5, 10.5])  # limites no eixo y

    plt.xlabel("Age (months)")  # legenda no eixo x
    plt.ylabel("Weight (kg)")  # legenta no eixo y

    plt.yticks([2, 4, 6, 8, 10])  # marcadore do eixo y

    """ 
    Plotagem do gráfico:
      marker recebe o formato do ponto, nesse caso um circulo
      color define a cor da linha
      markerfacecolor define a cor da parte interna do ponto
    """
    plt.plot(ages, weights, marker='o', color='black', markerfacecolor='white')
    plt.show()


def question_2():

    feature_count = [79049, 50770, 32029, 26248, 13840, 5195, 1638,
                     1602, 1431, 491, 474, 341]  # Valor de contagem para cada barra
    y_coords = range(12)  # Lista com as coordenadas y das barras

    # Nome associado a cada contagem para serem colocados no eixo y
    labels = ['Messenger RNA', 'Coding Sequences', 'Genes', 'Transfer RNAs', 'CpG islands', 'Pseudogenes', 'Micro-RNAs',
              'Small nucleolar RNAs', 'Small nuclear RNAs', 'Miscellaneous RNA', 'Immunoglobulin Segments', 'Ribossomal RNAs']

    # Plotagem de uma barra horizontal, color define a cor da barra e edgecolor define a cor do contorno.
    plt.barh(y_coords, feature_count, color='lightgrey', edgecolor='grey')

    # Legenda no eixo x
    plt.xlabel('Number of features')

    # Modificando os valores para marcador nos eixos
    plt.yticks(y_coords, labels) # Associando cada valor de y com o nome dado no arquivo
    plt.xticks([0,20000,40000,60000]) # Colocando os mesmos marcadores do gráfico de exemplo

    plt.tight_layout() # Ajusta o gráfico para a tela, evitando cortar as legendas.
    plt.show()

def question_3():
  norm_std = np.random.normal(0, 1.0, 10000) # Gerando uma lista com 10 mil elementos seguindo a normal padrão(mu=0, sigma=1)
  norm_plus4 = np.random.normal(4, 1.0,10000) # Gerando uma lista com 10 mil elementos seguindo a normal padrão com deslocamento de 4(mu = 4, sigma=1)

  res = np.concatenate([norm_std,norm_plus4]) # Concatenando as duas listas

  plt.hist(res, 110, color='white', edgecolor='black') # Gerando o histograma com 110 barras, cor das barras branca e contorno preto
  plt.xlabel("Values") # legenda do eixo x
  plt.ylabel("Frequencies") # legenda do eixo y

  plt.title("Mixed distribution histogram")

  plt.show()

def question_4():
  # valores dados no dataset, que determinam a altura da barra
  values = [2,1,2,3,3,6,5,10,9,18] 

  # valores dados no dataset(marcadores do eixo x)
  labels = ["D1 Male", "D1 Female", "D2 Male", "D2 Female", "D3 Male", "D3 Female", "D4 Male", "D4 Female", "D5 Male", "D5 Female"]

  # cor para cada barra 
  colors = ['red','orange','palegreen', 'lime', 'limegreen', 'aqua', 'royalblue', 'mediumblue', 'blueviolet', 'magenta']

  # coordenadas do eixo x, de 0 a 9 já que tem 10 barras
  x_coords = range(10)

  # plotando o grafico de barras
  plt.bar(x_coords, values, color=colors)
  
  # modificando os marcadores dos eixos e o tamanho da fonte no eixo x para evitar sobreposição
  plt.xticks(x_coords, labels, fontsize=6)
  plt.yticks([0,5,10,15])
  
  # mostrando o grafico
  plt.show()

# função que retorna a cor de acordo com o estado dado para a questão 5
def map_color(state):
    if state == 'up':
        return 'red'
    if state == 'down':
        return 'blue'
    return 'lightgray'

def question_5():
  # lendo o dataset via csv através do pandas
  data = pd.read_csv('up_down_expression.csv', sep="\t")

  # pegando os dados do eixo x, condition 1
  x = data['Condition1']
  # dados do eixo y, condition 2
  y = data['Condition2']

  # Atribuindo a cor para cada ponto, de acordo com o estado
  # Através de list comprehension, será criado um valor na lista mapeado atravéz da função map_color() para cada linha do dataset
  color = [map_color(i) for i in data['State']]

  # Plotando o gráfico com os dados capturados acima
  plt.scatter(x,y,marker='.',c=color)

  # Modificando os marcadores nos eixos
  plt.xticks([0,5,10])
  plt.yticks([0,5,10])

  # Modificando os limites dos eixos
  axes = plt.gca()
  axes.set_xlim([-4,14])
  axes.set_ylim([-4,14])

  # Definindo as legendas dos eixos
  plt.xlabel('Condition 1')
  plt.ylabel('Condition 2')

  plt.show()

def question_6():
  # Leitura do dataset
  data = pd.read_csv('chromosome_position_data.csv', sep="\t")

  # Recuperando os dados do dataset(valores do eixo y)
  mut1 = data['Mut1']
  mut2 = data['Mut2']
  wt = data['WT']

  # Valores do eixo x
  postitions = data['Position']

  # Plotando as linhas, com width=1 para melhor visualização
  plt.plot(postitions,mut1,color='red', linewidth=1)
  plt.plot(postitions,mut2,color='green', linewidth=1)
  plt.plot(postitions,wt,color='royalblue', linewidth=1)

  # Adicionando as legendas, basta relacionar a cor com o nome do conjunto
  red_patch = mpatches.Patch(color='red', label='Mut1')
  blue_patch = mpatches.Patch(color='royalblue', label='Mut2')
  green_patch = mpatches.Patch(color='green', label='WT')
  plt.legend(handles=[red_patch,blue_patch,green_patch])

  # Legenda dos eixos
  plt.xlabel('Position with chromosome')
  plt.ylabel('Value')

  # Configuração para o gráfico mostrar os valores completos nos marcadores do eixo x, sem isso seria mostrado em notação científica
  plt.ticklabel_format(useOffset=False, style='plain')

  plt.show()

def question_7():
  pass


op = int(input("Digite o número da questão para visualizar o gráfico (de 1 a 7):"))

if(op == 1):
  question_1()
elif(op == 2):
  question_2()
elif(op == 3):
  question_3()
elif(op == 4):
  question_4()
elif(op == 5):
  question_5()
elif(op == 6):
  question_6()
elif(op == 7):
  question_7()

