import pyperclip

texto = pyperclip.paste()
print (texto)
try:
    pos = str(texto).index('?')
    substring = texto[0 : pos]

    print (substring)

    pyperclip.copy(substring)

except Exception as eerro:
    print(eerro)

