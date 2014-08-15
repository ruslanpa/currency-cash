__author__ = 'ruslanpa'
__version__ = '0.0.1'

from flask import Flask

app = Flask(__name__)
from app import views
from app import tests