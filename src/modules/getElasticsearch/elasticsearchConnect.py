#!/usr/bin/python3

from requests import get
from elasticsearch import Elasticsearch

def esConn():
    try:
        client = Elasticsearch('localhost:9200')
    except:
        client = Elasticsearch('127.0.0.1:9200')

    return client
