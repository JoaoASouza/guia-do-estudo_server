from flask import Flask, jsonify, request
from flask_cors import CORS
from models import Events, Subjects
from random import randint
import json

app = Flask(__name__)
CORS(app)

subjects = [
    {
        'name': 'Calculo',
        'period': 2,
        'professor': 'Rafael Saraiva',
        'credits': 5,
        'workload': 90,
        'url': 'https://www.sites.google.com/site/cefetsaraiva2/home/calculo-a-uma-variavel'
    },
    {
        'name': 'AEDsI',
        'period': 3,
        'professor': 'Jurair rosa',
        'credits': 4,
        'workload': 70,
        'url': 'https://sites.google.com/site/jurairr/home/cefet/aeds-i?authuser=0'
    },
    {
        'name': 'Arquitetura',
        'period': 4,
        'professor': 'Fernanda',
        'credits': 5,
        'workload': 90,
        'url': 'https://sites.google.com/view/fernandaduarteoliveira/disciplinas/arquitetura-de-computadores'
    }
]

event_list = [
    {
        'id': 0,
        'name': 'Prova',
        'date': '2020-09-01'
    },
    {
        'id': 1,
        'name': 'Trabalho',
        'date': '2020-09-02'
    },
    {
        'id': 2,
        'name': 'Reuniao',
        'date': '2020-09-03'
    }
]

@app.route('/')
def index():
    return 'Hello there'

@app.route('/subjectinfo/<subject_name>', methods=['GET'])
def get_subject_info(subject_name):
    subject = Subjects.query.filter_by(name=subject_name).first()
    response = {
        'name': subject.name,
        'period': subject.period,
        'professor': subject.professor,
        'credits': subject.credits,
        'workload': subject.workload,
        'url': subject.url
    }
    return jsonify(response)

@app.route('/subsnames', methods=['GET'])
def get_subjects_names():
    subjects = Subjects.query.all()
    subjects_names = [i.name for i in subjects]
    return jsonify(subjects_names)

@app.route('/events', methods=['GET', 'POST', 'DELETE'])
def events():
    if (request.method == 'GET'):
        events = Events.query.all()
        events_list = [{'name':e.name, 'date':e.date} for e in events]
        return jsonify(events_list)

    elif (request.method == 'POST'):
        new_event = json.loads(request.data)
        event = Events(name=new_event['name'], date=new_event['date'])
        event.save()
        return jsonify(new_event)

    elif (request.method == 'DELETE'):
        event_names = json.loads(request.data)
        
        for event_name in event_names:
            event = Events.query.filter_by(name=event_name).first()
            print(event_name)
            event.delete()

        return jsonify(event_names)


if __name__ == "__main__":
    app.run(port=5000)