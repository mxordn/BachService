from flask import jsonify
from flask_sqlalchemy import SQLAlchemy

#from .db import db
db = SQLAlchemy()

class BWVEntry(db.Model):
    index = db.Column(db.Integer, primary_key=True)
    titel = db.Column(db.String)
    bwv = db.Column(db.Integer)
    bwv_zusatz = db.Column(db.String)
    kategorieEins = db.Column(db.String)
    kategorieZwei = db.Column(db.String)
    kategorieDrei = db.Column(db.String)
    beschreibung = db.Column(db.String)
    placed_after = db.Column(db.String)
    besetzung = db.Column(db.String)
    bc_num = db.Column(db.String)
    bach_compendium = db.Column(db.String)
    sonntag = db.Column(db.String)
    total_entries = db.Column(db.Integer)
    #possession = db.String(db.String)
    
    def getEntry(self):
        return {
            'index': self.index,
            'titel': self.titel,
            'bwv': self.bwv,
            'bwvZusatz': self.bwv_zusatz,
            'kategorie1': self.kategorieEins,
            'kategorie2': self.kategorieZwei,
            'kategorie3': self.kategorieDrei,
            'beschreibung': self.beschreibung,
            'platziertNach': self.placed_after,
            'besetzung': self.besetzung,
            'bwvKomplett': self.bc_num,
            'bach_compendium': self.bach_compendium,
            'sonntag': self.sonntag
            #anzahl_gesamt: self.total_entries
            #alternativen: str = ''
        }

    def __repr__(self):
        return f"<BWVEntry: {self.titel}, BWV {self.bc_num}>"

class ChoralEntry(db.Model):
    index = db.Column(db.Integer, primary_key=True)
    bwv = db.Column(db.String)
    d = db.Column(db.String)
    b = db.Column(db.String)
    r = db.Column(db.String)
    text = db.Column(db.String)
    textAuthor = db.Column(db.String)
    tune = db.Column(db.String)
    tuneComposer = db.Column(db.String)
    zahn = db.Column(db.String)
    liturgicalOccasion = db.Column(db.String)
    otherSettings = db.Column(db.String)
    
    def getEntry(self):
        return {
            'index': self.index,
            'bwv': self.bwv,
            'd': self.d,
            'b': self.b,
            'r': self.r,
            'text': self.text,
            'textAuthor': self.textAuthor,
            'tune': self.tune,
            'tuneComposer': self.tuneComposer,
            'zahn': self.zahn,
            'liturgicalOccasion': self.liturgicalOccasion,
            'otherSettings': self.otherSettings

        }

    def __repr__(self):
        return f"<ChoralEntry: {self.text}, BWV {self.bwv}>"