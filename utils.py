from models import Events, Subjects

def insere_evento(nome, data):
    evento = Events(name=nome, date=data)
    evento.save()

def consulta_eventos():
    eventos = Events.query.all()
    print(eventos)

def insere_disciplina(nome, periodo, prof, creditos, carga, site):
    subject = Subjects(
        name = nome,
        period = periodo,
        professor = prof,
        credits = creditos,
        workload = carga,
        url = site
    )
    subject.save()

def consulta_disciplinas():
    disciplinas = Subjects.query.all()
    print(disciplinas)

if __name__ == "__main__":
    insere_disciplina(
        'Calculo',
        2,
        'Rafael Saraiva',
        5,
        90,
        'https://www.sites.google.com/site/cefetsaraiva2/home/calculo-a-uma-variavel'
    )
    insere_disciplina(
        'AEDsI',
        3,
        'Jurair rosa',
        4,
        70,
        'https://sites.google.com/site/jurairr/home/cefet/aeds-i?authuser=0'
    )
    consulta_disciplinas()
