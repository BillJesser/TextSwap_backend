from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import pymongo as pym

app = Flask(__name__)
client = pym.MongoClient("mongodb://localhost:27017")