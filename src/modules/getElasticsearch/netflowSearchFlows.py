#!/usr/bin/python3

from .elasticsearchConnect import *

def SearchFlows (givenSRCAddr, givenSRCPort, givenDSTAddr, givenDSTPort, givenProtocol, time_gte, time_lte, client):
    response = client.search (
        index = "netflow-*",
        scroll = '20m', #Tempo de scroll (Tempo maximo que um scroll irá demorar para processar a quantidade de resultados dele)
        size = 10000, #Quantidade de resultados por scroll
        request_timeout = 180,
        body = {
            "query": {
                "bool": {
                    "must": [
                        {"range": {"@timestamp": {"gte": time_gte, "lte": time_lte}}},
                        {"regexp": {"netflow.src_addr": givenSRCAddr}},
                        {"regexp": {"netflow.src_port": givenSRCPort}},
                        {"regexp": {"netflow.dst_addr": givenDSTAddr}},
                        {"regexp": {"netflow.dst_port": givenDSTPort}}
                    ],
                    "should": [
                        {"match": {"netflow.protocol": givenProtocol}},
                        {"regexp": {"netflow.protocol": givenProtocol}}
                    ]
                }
            }
        }
    )
    return (response)

def SearchAllFlows(givenSRCAddr, givenSRCPort, givenDSTAddr, givenDSTPort, givenProtocol, time_gte, time_lte):
    client = esConn()
    hits_total = []
    response = SearchFlows(givenSRCAddr, givenSRCPort, givenDSTAddr, givenDSTPort, givenProtocol, time_gte, time_lte, client)
    sid = response['_scroll_id'] #Cada scroll possui uma id, usada para realizar iterações
    scroll_size = response['hits']['total'] #scroll_size recebe total de resultados
    #print("Total hits: " + str(scroll_size))
    while(scroll_size > 0):
        hits_total.extend(response['hits']['hits'])
        response = client.scroll(scroll_id = sid, scroll = '3m') #Realiza o scroll de determinada _scroll_id, determianando o tempo de scroll
        sid = response['_scroll_id']
        scroll_size = len(response['hits']['hits']) #Atualiza o tamanho de scroll_size (Quantidade de hits obtidos no scroll corrente)
    if len(hits_total) != 0:
        return (hits_total)
