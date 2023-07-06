from model import *
from view import *

def clicked(event):
    get_entries()
    getdetails()


def getdetails():
    name = get_entries()[0]
    password = get_entries()[1]
    saved = savedetails(name, password)
    if saved:
        print('Details saved')


def get_entries(*args):
    print(args)
    return list(args)