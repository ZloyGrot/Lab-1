import re

DIGITS = {'0': 'ноль', '1': 'один', '2': 'два', '3': 'три'}

def to_words(n):
    return ' '.join(DIGITS[d] for d in n)

def process(f):
    with open(f) as file:
        txt = file.read()
    pattern = re.findall(r'\b[0-3]{4,}\b', txt)
    valid = [x for x in pattern if x[0] in '13' and x[-1] in '02']
    for x in valid:
        print(x)
    print('Количество подходящих чисел:', len(valid))
    if valid:
        max_num = max(valid, key=lambda x: int(x, 4))
        print('Максимальное число прописью:', to_words(max_num))
    else:
        print('Подходящих чисел не найдено')

process("1lab.txt")
