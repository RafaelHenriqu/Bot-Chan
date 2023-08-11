import discord
import time
 #import tkinter
import requests
TagsEspecias = {
}
EstadoMental = {
   0: "Normal",
   1: "Mais o menos",
   2: "Feliz",
   3: "Muito Feliz",
   4: "Apaixonada",
   5: "Nivel S De Felicidade"
}
Tags = { # Amigos: 
 "gabriel": "Lindo De +",
 "rafael":"Analfabeto",
 "ariel":"Dono Do Server",
 "ryan": "Famoso: JÉ BADURA",
 "lu":"Bizzaro",
 "nicolas":"Bizzaro de Mais"   

}
Moedas = { #Conversão De Moedas
   "dolar": "USD",
   "euro": "EUR",
   "libra":"GBP",
   "peso":"ARS",
   "bitcoin": "BTC",
   "litecoin":"LTC",
   "iene":"JPY",
   "franco":"CHF",
   "yuan":"CNY",
   "ethereum":"ETH",
   "xrp":"XRP",

}
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))  
        Msg = message.content 
        if  Msg.lower() in Tags:
         await message.channel.send(Tags[Msg.lower()]) 
        if  Msg.lower() in TagsEspecias: 
         await message.channel.send(TagsEspecias[Msg.lower()]) 
        if Msg.lower() in Moedas: # Conversão de Moedas
           print(Moedas)
           response = requests.get(f'https://economia.awesomeapi.com.br/last/{Moedas[Msg.lower()]}')
           data = response.json()
           Moeda = Moedas[Msg.lower()] + 'BRL'
           await message.channel.send(data[Moeda]['ask'])
        
          




 
intents = discord.Intents.default()
intents.message_content = True


client = MyClient(intents=intents)
client.change_presence(activity=discord.Game(name="Nada"))
client.run('MTEzOTIyNTg5MzQ2NjgwMDEzOA.GJZXrm.OxRzgEhrOcWJxpN3kTvdibon77FcOUCuy5hljE')



