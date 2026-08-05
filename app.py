import os
import sqlite3
from flask import Flask, g
from utils import BASE_DIR, get_db

app = Flask(__name__)  # creates the flask app object

