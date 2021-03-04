#!/usr/bin/env python #ustawia srodowisko z jakiego bedziemy korzystac

import funkcje #importuje funkcje
import flask
import json

app = flask.Flask(__name__)

# wynik = funkcje.szybkie_losowanie() #tworzy zmienna wynik ktora odpala funkcje losowania

# print(wynik) #printuje zmienna wynik

@app.route('/')
def endpoint1():
    return json.dumps(funkcje.szybkie_losowanie())