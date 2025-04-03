import random

syllables = [
    'ма', 'мо', 'му', 'ме', 'ми', 'ба', 'бо', 'бу', 'бе', 'би',
    'ра', 'ро', 'ру', 'ре', 'ри', 'ла', 'ло', 'лу', 'ле', 'ли',
    'ка', 'ко', 'ку', 'ке', 'ки', 'на', 'но', 'ну', 'не', 'ни',
    'та', 'то', 'ту', 'те', 'ти', 'да', 'до', 'ду', 'де', 'ди',
    'са', 'со', 'су', 'се', 'си', 'ва', 'во', 'ву', 'ве', 'ви',
    'га', 'го', 'гу', 'ге', 'ги', 'па', 'по', 'пу', 'пе', 'пи',
    'жа', 'жо', 'жу', 'же', 'жи', 'ша', 'шо', 'шу', 'ше', 'ши',
    'ча', 'чо', 'чу', 'че', 'чи', 'ца', 'цо', 'цу', 'це', 'ци'
]

def generate_syllable_word(syllable_count):
    return ''.join(random.choice(syllables) for _ in range(syllable_count))

def create_directs(amount):
    st = set()
    while len(st) < amount:
        l = random.randint(3, 6)
        w = generate_syllable_word(l)  # Например: "малицу"
        st.add(w)
    t = [(str(i+1), e) for i,e in enumerate(st)]

    headers = ['idDirect', 'nameDirect']
    with open('./_directs.csv', 'w', encoding='utf8') as f:
        f.write(';'.join(headers) + '\n')
        for e in t:
            f.write(';'.join(e) + '\n')

def create_hobby(amountH, amountD):
    stH = set()
    while len(stH) < amountH:
        l = random.randint(3, 6)
        w = generate_syllable_word(l)
        stH.add(w)
    lst_H = list(stH)

    stI = set()
    while len(stI) < amountH:
        i = random.randint(1_000_000, 9_999_999)
        stI.add(i)
    lst_I = list(stI)

    headers = ['idHobby', 'nameHobby', 'idDirect']
    with open('./_hobby.csv', 'w', encoding='utf8') as f:
        f.write(';'.join(headers) + '\n')
        for i in range(amountH):
            e = [str(lst_I[i]), lst_H[i], str(random.randint(1, amountDirect))]
            f.write(';'.join(e) + '\n')

amountDirect = 100
create_directs(amountDirect)
amountHobby = 200_000
create_hobby(amountHobby, amountDirect)
