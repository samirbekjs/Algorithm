s = input()
alfuz = {
    'й':'q',
    'ц':'w',
    'у':'e',
    'к':'r',
    'е':'t',
    'н':'y',
    'г':'u',
    'ш':'i',
    'щ':'o',
    'з':'p',
    'ф':'a',
    'ы':'s',
    'в':'d',
    'а':'f',
    'п':'g',
    'р':'h',
    'о':'j',
    'л':'k',
    'д':'l',
    'я':'z',
    'ч':'x',
    'с':'c',
    'м':'v',
    'и':'b',
    'т':'n',
    'ь':'m',
}
alf = alfuz.copy()
for i,j in alf.items():
    alfuz.update({i.upper():j.upper()})
alfuz.update({'э':"'"})
alfuz.update({'Э':"'"})
new = ''
for i in s:
    if i!=' ':
        new += alfuz[i]
    else:
        new += i
print(new)
