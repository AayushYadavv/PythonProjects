from googletrans import Translator


with open('english.txt',mode='r') as ENGfile:
    text=ENGfile.read()

translator = Translator()
translated = translator.translate(text, dest='hi')

with open('hindi.txt',mode='w') as HIfile:
    HIfile.write(translated.text)
