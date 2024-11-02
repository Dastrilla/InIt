cyrillic_letters = {
    'а':'a',
    'б':'b',
    'в':'v',
    'г':'g',
    'д':'d',
    'е':'e',
    'ё':'e',
    'ж':'zh',
    'з':'z',
    'и':'i',
    'й':'i',
    'к':'k',
    'л':'l',
    'м':'m',
    'н':'n',
    'о':'o',
    'п':'p',
    'р':'r',
    'с':'s',
    'т':'t',
    'у':'u',
    'ф':'f',
    'х':'h',
    'ц':'ts',
    'ч':'ch',
    'ш':'sh',
    'щ':'sch',
    'ъ':'',
    'ы':'y',
    'ь':'',
    'э':'e',
    'ю':'yu',
    'я':'ya',
}


def cyrillic_to_english(text: str):
    text = text.replace(' ', '_').lower()
    fin = []
    for ch in text:
        fin.append(cyrillic_letters.get(ch, ch))
    return ''.join(fin)