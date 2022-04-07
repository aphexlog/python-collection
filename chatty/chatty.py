import chatterbot
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
from argparse import ArgumentParser

args = ArgumentParser()

args.add_argument("-a", "--arg", help="Argument to feed the bot")

bot = ChatBot("Chatty")

trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")
trainer.train("chatterbot.corpus.english.greetings")
trainer.train("chatterbot.corpus.english.conversations")



arg = args.parse_args().arg

response = bot.get_response(args.parse_args().arg)

print(response)
