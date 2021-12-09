import discord
from keep_alive import keep_alive


client = discord.Client()

@client.event
async def on_ready():
  print ('We have logged in as Jerrys BOT'.format(client))

@client.event
async def on_message (message):
  if message.author == client.user:
    return
    
  if message.content.startswith('/Hello'):
    await message.channel.send('Hello!')

  if message.content.startswith('so sicko mode'):
    await message.channel.send('Its lit!')
    
  if message.content.startswith('/paypal'):
    await message.channel.send('Paypal: if your paying with PayPal please open this link to send the money (https://www.paypal.com/paypalme/Betbotme) MAKE SURE YOU SEND AS FNF AND PUT YOUR DEV ID IN THE NOTES ALONG WITH YOUR DISCORD TAG. After please send the crypto address')

  if message.content.startswith('/Paypal'):
    await message.channel.send('Paypal: if your paying with PayPal please open this link to send the money (https://www.paypal.com/paypalme/Betbotme) MAKE SURE YOU SEND AS FNF AND PUT YOUR DEV ID IN THE NOTES ALONG WITH YOUR DISCORD TAG. After please send the crypto address')

  if message.content.startswith('/PayPal'):
    await message.channel.send('Paypal: if your paying with PayPal please open this link to send the money (https://www.paypal.com/paypalme/Betbotme) MAKE SURE YOU SEND AS FNF AND PUT YOUR DEV ID IN THE NOTES ALONG WITH YOUR DISCORD TAG. After please send the crypto address')

  if message.content.startswith('/Pay'):
    await message.channel.send('Paypal: if your paying with PayPal please open this link to send the money (https://www.paypal.com/paypalme/Betbotme) MAKE SURE YOU SEND AS FNF AND PUT YOUR DEV ID IN THE NOTES ALONG WITH YOUR DISCORD TAG. After please send the crypto address')

  if message.content.startswith('/pay'):
    await message.channel.send('Paypal: if your paying with PayPal please open this link to send the money (https://www.paypal.com/paypalme/Betbotme) MAKE SURE YOU SEND AS FNF AND PUT YOUR DEV ID IN THE NOTES ALONG WITH YOUR DISCORD TAG. After please send the crypto address')

  if message.content.startswith('rules'):
    await message.channel.send('look at the channel that says rules')


keep_alive()    
client.run('OTE3ODQyNzgzOTIwODgxNzY0.Ya-ltA.5LrQkJ_QWEPHL2iMVUzzDzTSgjY')
