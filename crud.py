from flask import Flask, render_template, request
import sqlite3 as sql

app = Flask(__name__)
conn = sql.connect('database.db')


