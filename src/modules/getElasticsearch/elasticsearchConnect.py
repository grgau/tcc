#!/usr/bin/python3

from requests import get
from elasticsearch import Elasticsearch

def esConn():
    try:
        client = Elasticsearch('200.145.216.220:9200')
        test = requests.get("http://www.wildfire.acmesecurity.org:9200")
    except:
        client = Elasticsearch('200.145.216.220:9200')

    return client
