""" Importação das bibliotecas """
import numpy as np
#import matplotlib.pyplot as plt
import leitor_codigo_barra as lb
#import csv
import os
import platform
from time import time
from pdf2image import convert_from_path
from PIL import Image
#from pytesseract import image_to_string

""" Conversor de arquivos em pdf para jpg """
# Entrada: Se entra com o nome do arquivo pdf, seu nome escolhido de saida e os caminhos de onde se encontram(entrada) e para onde seram mandados(Saída)
# Saída: Não possui saida, o seu resultado é um arquivo de imagem na escala cinza, com 300 dpi e no formato jpg

def converte_imagem(nome_pdf, nome_saida_arquivo, caminho_entrada, caminho_saida):
    image = convert_from_path('{}/{}.pdf'.format(caminho_entrada,nome_pdf),dpi = 300,grayscale = True, output_folder = "{}".format(caminho_saida),fmt = 'jpeg', output_file = '{}'.format(nome_saida_arquivo))
    #if platform.system() == "Linux":
    #    img_c = Image.open("{}{}0001-1.jpg".format(caminho_saida,nome_saida_arquivo))
    img_c = Image.open("{}{}-1.jpg".format(caminho_saida,nome_saida_arquivo))
    # elif platform.system() == "Linux":
    #     img_c = Image.open("{}{}-1.jpg".format(caminho_saida,nome_saida_arquivo))
    img_c = img_c.convert('L')
    return np.array(img_c)

""" Função principal """

def main():
    inicio_execucao = time()
    # Variáveis auxiliares
    #path_temp = "./images/temp/"
    subpastas = os.listdir("./images/")
    #print(subpastas)
    # Laço que percorre todo diretorio onde contém os arquivos pdf, e pega o nome de todos esses arquivos.
    # Convertendo então, em imagens temporárias e pegando seu código de barras e os valores das alternativas.
    #for pasta in subpastas:
    for pasta in os.listdir("./images/"):
        diretorio_imagem = "./images/{}".format(pasta)
        path_temp = "./images/{}/temp/".format(pasta)
        for _,_,lista_arquivos in os.walk(diretorio_imagem):
            print(diretorio_imagem)
            os.mkdir(path_temp)
            for arquivo in lista_arquivos:
                try:
                    # print(arquivo)
                    if (arquivo.count(".PDF") == 1) or (arquivo.count("DS") == 1) or (arquivo.count("_EPS") == 1 or (arquivo.count("_Pages"))):
                        continue
                    # print("Lendo arquivo: {}".format(arquivo[:len(arquivo) - 4]))
                    imagem_temporaria = converte_imagem(arquivo[:len(arquivo) - 4],arquivo[:len(arquivo) - 4],diretorio_imagem,path_temp)
                    # print("Conversão: OK")
                        
                    codigo = lb.decode(imagem_temporaria)
                    print("Código: {}".format(codigo))
                    #if codigo == "Nenhum":
                     #   codigo_sem_tratamento = imagem_temporaria[620:720,1950:2200]
                      # if len(codigo) == 9:
                        #    codigo = codigo[1:]
                        # print("Código: {}".format(codigo))
                        # dia_prova = int(input("Insira o dia da prova: "))
                    
                    # print("Arquivo concluído")    
                    del imagem_temporaria, codigo
                    if platform.system() == "Linux":
                        os.remove("{}{}-1.jpg".format(path_temp,arquivo[:len(arquivo) - 4]))
                    # elif platform.system() == "Linux":
                    #     os.remove("{}{}-1.jpg".format(path_temp,arquivo[:len(arquivo) - 4]))
                except ValueError:
                    os.remove("{}{}-1.jpg".format(path_temp,arquivo[:len(arquivo) - 4]))
                    # elif platform.system() == "Linux":
                    #     os.remove("{}{}-1.jpg".format(path_temp,arquivo[:len(arquivo) - 4]))
        os.rmdir(path_temp)
                    
    print("Tempo de execução: {} segundos".format(time() - inicio_execucao))
    
main()