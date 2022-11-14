import requests
import json
import random

command_list = '`!generate-quotes -> generate a quotes\n' \
               '!rand-num n, m -> generate a random number between n and m\n' \
               '!calc operation -> calculate an operation\n!convert-binary -> convert a decimal number ' \
               'to a binary number' \
               '\n!convert-decimal -> convert a binary to decimal number`'


def get_quotes():
    response = requests.get('https://zenquotes.io/api/random')
    json_data = json.loads(response.text)
    quote = '**\"' + json_data[0]['q'] + '\"**' + "\n*~" + json_data[0]['a'] + "*"
    return quote


def calc(operation):
    return eval(operation)


def rand_num(n, m):
    return random.randint(n, m)


def convert_binary(n: int):
    binary = bin(n)
    return str(binary)[2:]


def convert_decimal(n: int):
    return int(n, 2)


def handle_response(message) -> str:
    msg = message.lower()
    if msg[0] == '!':  # Command : !
        if msg == '!help':
            return f"`I will help you! Here's a list of available command:`\n\n{command_list}"

        # Generate quotes
        elif msg == '!generate-quotes':
            return get_quotes()

        # Calculate
        elif msg[:5] == '!calc':
            if msg == '!calc':
                return f'`Calculation command : \nExample :\n!calc 2*2. The bot will respond \'' \
                       f'Result : 4\'\n** => raise to the power of\n* => multiplication\n+/- => ' \
                       f'addition/subtraction\n% => modulus`'
            return f'**Result :** {calc(msg[6:])}'

        # Random Number
        elif msg[:9] == '!rand-num':
            if msg == '!ra nd-num':
                return f'`Use \'!rand-num\' command to generate random number between n and m Example:' \
                       f'\nrand-num 2, 10. The bot will respond with a random number between 2 and 10`'
            else:
                cmd = [int(i) for i in msg[10:].split(', ')]
                return f'**Random number :** {rand_num(cmd[0], cmd[1])}'

        # Binary Number
        elif msg[:15] == '!convert-binary':
            if msg == '!convert-binary':
                return f'`Use this command to convert n(decimal) to binary Example:\nconvert-binary 9. The' \
                       f'bot will return the binary number of 9`'
            return f'**Binary :** {convert_binary(int(msg[16:]))}'

        elif msg[:16] == '!convert-decimal':
            if msg == '!convert-decimal':
                return f'`Use this command to convert n(binary) to decimal Example:\nconvert-decimal 1001. The' \
                       f' bot will return the decimal number of 1001`'
            return f'**Decimal :** {convert_decimal(msg[17:])}'
        return 'I don\'t recognize your command. Please type \'!help\''
