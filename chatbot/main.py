import chatterbot
from chatterbot.trainers import ListTrainer
import re


def chat_to_text(chat_export_file):
    # cleaning the chat
    date_time = r"(\d+\/\d+\/\d+,\s\d+:\d+)"  # 9/16/22, 06:34
    dash_whitespace = r"\s-\s"  # -
    username = r"([\w\s]+)"  # name
    metadata_end = r":\s"  # :
    pattern = date_time + dash_whitespace + username + metadata_end

    with open(chat_export_file, "r", encoding='utf8') as corpus_file:
        content = corpus_file.read()
    cleaned_corpus = re.sub(pattern, "", content)
    return tuple(cleaned_corpus.split("\n"))


def clean_nonmessage(export_text_lines):
    messages = export_text_lines[1:len(export_text_lines) - 1]  # [1:-1]

    filter_out_msgs = ("<Media omitted>",)
    return tuple((msg for msg in messages if msg not in filter_out_msgs))


def clean(chat_export_file):
    message_corpus = chat_to_text(chat_export_file)
    return clean_nonmessage(message_corpus)


bot = chatterbot.ChatBot('Ooga Booga')

trainer = chatterbot.trainers.ListTrainer(bot)

# TRAIN THE BOT
# cleaned = clean('chat.txt')
# trainer.train(cleaned)

trainer.train("chatterbot.corpus.english.greetings")


while True:
    user_chat = input("Me : ")
    if user_chat == ':quit':  # end program
        break

    print(f'{bot.name} : {bot.get_response(user_chat)}')

