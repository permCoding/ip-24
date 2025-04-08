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

def generate_word(count):
    return ''.join(random.choice(syllables) for _ in range(count))

def create_words(amount, a, b):
    st = set()
    while len(st) < amount:
        st.add(generate_word(random.randint(a, b)).title())
    return list(st)
    
def write_to_csv(fn, t, headers):
    with open(fn, 'w', encoding='utf8') as f:
        f.write(';'.join(headers) + '\n')
        for e in t:
            f.write(';'.join(map(str, e)) + '\n')


groupNames = ['ИС-21','ПИнб-1','ПИб-3','ПИб-4','ИСу-2022','ПИм-1','ПИнб-4']
groups = [(i,g) for i, g in enumerate(groupNames, start=1)]
write_to_csv('./groups.csv', groups, ['idGroup', 'nameGroup'])

amount = 100
lastNames, firstNames = create_words(amount, 3, 5), create_words(amount, 2, 4)
persons = [(i+1,lastNames[i],firstNames[i],random.randint(0,1),random.randint(1,len(groupNames))) for i in range(amount)]
headers = ['idUser', 'lastName', 'firstName', 'gender', 'idGroup']
write_to_csv('./users.csv', persons, headers)


