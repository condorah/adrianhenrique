import telebot
import time
import random
from datetime import datetime, timedelta, timezone
import pytz

# Configuração do bot
TOKEN = '6201845089:AAEzz7LXAeyKR8jzNcts1EDGuiItQW5q3v4'
chat_id = '-727372835'
bot = telebot.TeleBot(TOKEN)

# Dimensões da malha
num_linhas = 5
num_colunas = 5

# Tempo entre cada mensagem (em segundos)
tempo_entre_mensagens = 30

# Função para gerar uma matriz aleatória com 4 diamantes
def gerar_matriz_aleatoria():
    matriz = [['⬛' for _ in range(num_colunas)] for _ in range(num_linhas)]
    posicoes_diamantes = set()

    # Escolhe 4 posições aleatórias para os diamantes
    while len(posicoes_diamantes) < 4:
        posicao = (random.randint(0, num_linhas - 1), random.randint(0, num_colunas - 1))
        posicoes_diamantes.add(posicao)

    # Preenche as posições escolhidas com diamantes
    for linha, coluna in posicoes_diamantes:
        matriz[linha][coluna] = '💎'  # Representação do diamante com um emoji

    return matriz

# Função para formatar a matriz em uma string
def formatar_matriz(matriz):
    return '\n'.join([' '.join(linha) for linha in matriz])

while True:
    # Obtém o horário atual em UTC
    horario_atual_utc = datetime.now(pytz.utc)

    # Converte o horário atual para o fuso horário de Brasília (America/Sao_Paulo)
    fuso_horario_brasilia = pytz.timezone('America/Sao_Paulo')
    horario_atual_brasilia = horario_atual_utc.astimezone(fuso_horario_brasilia)

    # Adiciona 1 minuto ao horário atual de Brasília (tempo entre cada mensagem)
    horario_validade_brasilia = horario_atual_brasilia + timedelta(minutes=1)

    # Gera a matriz aleatória com 4 diamantes
    matriz_aleatoria = gerar_matriz_aleatoria()

    # Formata a mensagem com o horário de validade e a matriz formatada
    mensagem = f'PADRÃO ENCONTRADO!✅\n\n⚙️ = 3 bombas 💣\n\n{formatar_matriz(matriz_aleatoria)}\n\n⚠️ Válido até as {horario_validade_brasilia.strftime("%H:%M")} (horário de Brasília).'
    bot.send_message(chat_id=chat_id, text=mensagem)

    # Aguarda o tempo determinado
    time.sleep(60)
