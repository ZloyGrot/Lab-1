DIGITS = {'0': 'ноль', '1': 'один', '2': 'два', '3': 'три'}
def to_words(n): return ' '.join(DIGITS[d] for d in n)
def process(f):
    with open(f) as file: txt = file.read()
    valid = [x for x in txt.split() if len(x)>3 and all(c in '0123' for c in x) and x[0] in '13' and x[-1] in '02']
    for x in valid: print(x)
    print('Количество подходящих чисел:', len(valid))
    print('Максимальное число прописью:', to_words(max(valid, key=lambda x: int(x,4)))) if valid else print('Подходящих чисел не найдено')
process("1lab.txt")
