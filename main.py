import telebot 
from config import token
import requests
from logic import Pokemon
bot = telebot.TeleBot(token) 

@bot.message_handler(commands=['go'])
def go(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        pokemon = Pokemon(message.from_user.username)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())
    else:
        bot.reply_to(message, "Ты уже создал себе покемона")
def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"
bot.infinity_polling(none_stop=True)
@bot.message_handler(commands=['attack'])
def go(message):
        if message.reply_to_message:
            pokemon_1 = Pokemon(message.from_user.username)
            pokemon_2 = Pokemon(message.reply_from_message.from_user.username)
            pokemon_1.attack(pokemon_2)
            result = pokemon_1.sttack(pokemon_2)
            bot.set_message(message.chat.id,result)
        else:
             bot.reply_to(message, "Выбери противника")
@bot.message_handler(commands=['info'])
def go(message):
        if message.from_user.username in Pokemon.pokemons.keys():
            pok = Pokemon.pokemons[message.from_user.username]
            bot.send_message(message.chat.id, pok.info())
