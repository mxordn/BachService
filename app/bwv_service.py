from dataclasses import dataclass
import re
from .models import BWVEntry, ChoralEntry
from flask import Blueprint, jsonify, request
from flask_cors import cross_origin
from .models import db

bwvNum = re.compile('[1-9]..')

'''@dataclass
class BwvData():
    titel: str = ''
    bwvNumber: str = ''
    bwvNumberZusatz: str = ''
    kategorie1: str = ''
    kategorie2: str = ''
    kategorie3: str = ''
    werkgruppe: str = ''
    platziertNach: int = -1
    besetzung: str = ''
    BWV: int = -1
    kantaten: str = ''
    Sonntag: str = ''
    anzahl_gesamt: str = ''
    alternativen: str = ''

    def getClassValues(self):
        return {'bwvNumber': self.bwvNumber, 'alternativen': self.alternativen, 'titel': self.titel }'''

bwv_service = Blueprint('bwv', __name__, url_prefix='/bwv-service')

@bwv_service.route('/', methods=['GET'])
@cross_origin()
def status():
    be = BWVEntry.query.filter_by(titel='Allein zu dir, Herr Jesu Christ').first()
    print(be)
    return be.getJson()
    #make_response("<!DOCTYPE html><head></head><body>Service is running!</body></html>", 200)

@bwv_service.route('/chorales', methods=['GET', 'POST'])
@cross_origin()
def queryBWVChorales():
    if request.method == 'GET':
        try:
            bwvString = request.args['bwv']
        except:
            return jsonify({'status:': 'No query was given',
                            'results': 0,
                            'data': []
                            })

        bwvElements = re.findall('[0-9.]', bwvString)
        bwv = ''

        if '.' in bwvElements:
            i = bwvElements.index('.')
            bwv = ''.join([s for s in bwvElements[0:i+1]])  + '%'
        else:
            bwv = ''.join([s for s in bwvElements])  + '%'
        #print("QueryString: ", bwv, bwvString)
        res = db.session.query(ChoralEntry).filter(ChoralEntry.bwv.like(bwv)).first()
        print(res)
        if res:
            return jsonify({'status:': 'Ok',
                            'results': 1,
                            'data': [res.getEntry()]
                            })
        else:
            return jsonify({'status:': 'Ok',
                            'results': 0,
                            'data': []
                            })
        '''dbCon = sqlite3.connect('bwv.sqlite')
        wildcard = ''
        if bwv:
            if '.' in bwv:
                i = bwv.index('.')
                bwv = ''.join([s for s in bwv[0:i+1]])
                print('bwv: ', bwv)
                wildcard = '%'
                query = f"SELECT * from BWV WHERE BWV LIKE '{bwv}{wildcard}'"
            else:
                bwv = ''.join(bwv)
                print('bwv: ', bwv)
                wildcard = '%'
                query = f"SELECT * from BWV WHERE BWV LIKE '{bwv}{wildcard}'"
        #data = __setBWVData()

            data = pd.read_sql(query, dbCon)
            if len(data) > 1:
                data = data.head(1)#[0]
            #response = data.to_dict(orient='records'), 200)
            #response.headers['Content-Type'] = 'application/json'
            print('Resp: ', {'resp': data.to_dict(orient='records')})
            return jsonify({'resp': data.to_dict(orient='records')})
        else:
            return make_response('GET Request done.', 200)
    else:
        return make_response('Alles erledigt!', 200)'''



@bwv_service.route('/works', methods=['GET'])
@cross_origin()
def queryBWVWorks():
    if request.method == 'GET':
        filterArgs = []
        '''for a in request.args.keys():
            print(a, request.args[a])
            if hasattr(BWVEntry, a):
                print(a)'''
        if 'bwv' in request.args.keys():
            filterArgs.append(BWVEntry.bwv.like(request.args['bwv']))
        if 'titel' in request.args.keys():
            filterArgs.append(BWVEntry.titel.like('%' + request.args['titel'] + '%'))
            #be.query.filter

        res = db.session.query(BWVEntry).filter(
            *filterArgs
        ).all()
        #print(res)
        #bwv = request.args['bwv']
        #be = BWVEntry.query.filter(BWVEntry.bwv.like(bwv)).first()
        if res != []:
            #be = res[0]
            return jsonify({'status': 'Index out of range',
                            'results': len(res),
                            'data': [entry.getEntry() for entry in res]})
        else:
            return jsonify({'status': 'Index out of range',
                            'results': 0,
                            'data': []
                            })