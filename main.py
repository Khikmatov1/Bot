from googletrans import Translator

translator = Translator()

# result = translator.translate('salom', dest='en').text
# print(result)

while True:
    text = input('Inter text to translate: ')
    to_language = input('Inter language to translate: ')

    result = translator.translate(text, dest='ru').text

    print(result)


