# Importa o módulo de expressões regulares
import re

# Função para separar números e texto de uma lista mista
def separar_numeros_e_texto(lista):
    numeros = []  # Lista para armazenar números extraídos
    textos = []   # Lista para armazenar textos extraídos
    
    # Itera sobre cada item na lista fornecida
    for item in lista:
        # Se o item for uma string
        if isinstance(item, str):
            # Extrair números e texto usando expressões regulares
            extrair_numeros = re.findall(r'\d+', item)  # Encontra todas as sequências de dígitos
            extrair_texto = re.findall(r'\D+', item)    # Encontra todas as sequências de caracteres não dígitos
            
            # Se encontrou números na string
            if extrair_numeros:
                # Converte cada sequência de dígitos em um inteiro e adiciona à lista de números
                numeros.extend([int(num) for num in extrair_numeros])
            
            # Se encontrou texto na string
            if extrair_texto:
                # Remove espaços em branco e adiciona à lista de textos
                textos.extend([txt.strip() for txt in extrair_texto])
        
        # Se o item for um número (inteiro ou float)
        elif isinstance(item, (int, float)):
            # Adiciona diretamente à lista de números
            numeros.append(item)
    
    # Retorna as listas de números e textos extraídos
    return numeros, textos

# Função principal
def main():
    # Define uma lista mista de strings e números
    lista_mista = ["abc123", "456def", 789, "ghi 101 jkl", 202, "mno"]
    # Chama a função para separar números e textos da lista mista
    numeros, textos = separar_numeros_e_texto(lista_mista)
    
    # Imprime os números extraídos
    print("Números extraídos:", numeros)
    # Imprime os textos extraídos
    print("Textos extraídos:", textos)

# Executa a função principal se o script for executado diretamente
if __name__ == "__main__":
    main()

