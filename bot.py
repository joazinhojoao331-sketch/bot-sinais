from telegram import Bot
import schedule
import time
from datetime import datetime, timedelta

TOKEN = "7755383653:AAFzXMaH2RYwury6DOYRtBYZoXKSqgqDvkY"
CHAT_ID = "-1002628031072"

bot = Bot(token=TOKEN)

def hora_brasil(hora_str):
    hora = datetime.strptime(hora_str, "%H:%M")
    hora = hora + timedelta(hours=3)
    return hora.strftime("%H:%M")

sinais = [
    {"hora": "10:10", "par": "EURUSD", "direcao": "PUT"},
    {"hora": "10:35", "par": "EURUSD", "direcao": "CALL"},
    {"hora": "11:00", "par": "EURUSD", "direcao": "PUT"},
]

def enviar_sinal(sinal):
    mensagem = f"""
📊 SINAL - {sinal['par']} M5

🕐 Horário: {sinal['hora']}
📈 Direção: {sinal['direcao']}

⚠️ 1 Gale permitido
"""
    bot.send_message(chat_id=CHAT_ID, text=mensagem)

def agendar():
    for sinal in sinais:
        horario = hora_brasil(sinal["hora"])
        schedule.every().day.at(horario).do(enviar_sinal, sinal=sinal)

agendar()

while True:
    schedule.run_pending()
    time.sleep(1)
