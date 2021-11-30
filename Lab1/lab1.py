from collections import Counter

def make_new_alpha(s,word,code):
    line =''
    for i in s:
        if i not in word:
            line = line + i
    alpha_caesar = line[-code:] + word + line[:-code]
    new_alpha = {}
    for i,val in enumerate(s,start=1):
        new_alpha[val]=alpha_caesar[i-1]
        new_alpha[val.upper()]=alpha_caesar[i-1].upper()
    return new_alpha

def encrypt(text, alpha):
    text_encrypt = ''
    for i in text:
        if(i in alpha.keys()):
            text_encrypt = text_encrypt + alpha[i]
        else:
            text_encrypt = text_encrypt + i
    return text_encrypt

def frequency(text, alphabet):
    counter = Counter(text)
    list_frequency = []
    for i in range(len(counter)):
        if counter.most_common()[i][0] in alphabet:
            list_frequency.append(counter.most_common(len(counter))[i][0])
    return list_frequency

def decrypt(text, frequency,frequency_alphabet):
    text_decrypted = []
    d = dict(zip(frequency,frequency_alphabet))
    for i in text:
        if i in frequency_alphabet:
            text_decrypted.append(d.get(i))
        else:
            text_decrypted.append(i)
    return ''.join(text_decrypted)


alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
frequency_alphabet = ['о', 'а', 'е', 'и', 'т', 'н', 'л',
                           'р', 'с', 'в', 'к', 'м', 'д', 'у', 'п',
                           'б', 'г', 'ы', 'ч', 'ь', 'з', 'я', 'й',
                           'х', 'ж', 'ш', 'ю', 'ф', 'э', 'щ',
                           'ё', 'ц', 'ъ']
code = 5
key_word = 'стол'
new_alphabet = make_new_alpha(alphabet,key_word,code)
print(new_alphabet)
with open('chapter.txt') as f:
    chapter = f.read()

text_encrypted = encrypt(chapter, new_alphabet)
print(text_encrypted)
freq = frequency(text_encrypted,alphabet)
print(freq)
print(decrypt(text_encrypted,freq,frequency_alphabet))
