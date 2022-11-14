import qrcode
import validators


def validate(title):
    title_safe = True
    for i in ["\\", "/", ":", "*", "?", "\"", "<", ">", "|"]:
        title_safe = False if i in title else True
    if title[0] == ' ' or title[len(title) - 1] == ' ' or title == '.' or title == 'NUL' or ',' in title:
        title_safe = False

    return title_safe


while True:
    link = input('URL or Code : ')
    title = input('QRCode title : ')

    if validate(title):
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(link)
        qr.make(fit=True)

        img = qr.make_image(fill='black', back_color='white')
        img.save(f'{title}.png')
    else:
        print('Invalid title')

    if input('quit?(y for yes) : ').lower() == 'y':
        break
