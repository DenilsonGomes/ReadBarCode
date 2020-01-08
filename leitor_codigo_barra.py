""" Importação das bibliotecas """
import pyzbar.pyzbar as pyzbar

""" Detector de código de barras """
# Entrada: Um arquivo de imagem
# Saída: Uma string contendo o valor do código de barra o erro que não 
#        foi encontrado nenhum código de barra.

def decode(im):
    try:
        objeto_decodificado = pyzbar.decode(im)
        codigo_barra = []
        for objeto in objeto_decodificado:
            codigo_barra.append(int("".join([ numero for numero in str(objeto.data) if numero.isdigit() ])))
            continue
        
        return codigo_barra
    except UnboundLocalError:
        # print("Prova sem código de barras!")
        return "Nenhum"