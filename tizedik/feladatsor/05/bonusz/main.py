def morse_to_text(morse_code):
    global abc_list
    sentence = ''
    words = morse_code.strip().split('       ')
    for word in words:
        letter_codes = word.split('   ')
        text = ''
        for code in letter_codes:
            letter = [k[0] for k in abc_list if k[1] == code][0]
            text += letter
        sentence += text + ' '
    return sentence.strip()

with open('abc.txt', encoding='utf-8') as f:
  abc_list = [line.strip().split('\t') for line in f.readlines()[1:]]

print(f'3. morse table has {len(abc_list)} characters')

char_input = input('4.  Please enter a character: ').strip().upper()[0]
char_info = [k for k in abc_list if k[0] == char_input]
if len(char_info) == 0:
    print('not found')
else:
    print(f'\t{char_input}: {char_info[0][1]}')


with open('morze.txt', encoding='utf-8') as f:
  quotes = [line.strip().split(';') for line in f]

print(f'7.  first quote author: {morse_to_text(quotes[0][0])}')

longest = sorted(quotes, key=lambda x: len(morse_to_text(x[1])), reverse=True)[0]
print(f'8.  longest: {morse_to_text(longest[0])}: {morse_to_text(longest[1])}')

aristotle = [quote for quote in quotes if morse_to_text(quote[0]) == 'ARISZTOTELÉSZ']
print('9.  ar quotes:')
[print(f'\t- {morse_to_text(quote[1])}') for quote in aristotle]

with open('out.txt', 'w', encoding='utf-8') as output:
    [print(f'{morse_to_text(quote[0])}: {morse_to_text(quote[1])}', file=output) for quote in quotes]
