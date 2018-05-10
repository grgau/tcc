#!/usr/bin/python3

from .elasticsearchConnect import *

def SearchNotesAlerts(client, idsIndex, fieldIncident):
    from ..dates import (start_time, end_time)
    response = client.search (
        index = idsIndex,
        scroll = '20m', #Tempo de scroll (Tempo maximo que um scroll irá demorar para processar a quantidade de resultados dele)
        size = 10000,
        request_timeout = 180,
        body = {
            "query": {
                "bool": {
                    "must": [
                        {"exists": {"field": fieldIncident}},
                        {"range": {"@timestamp": {"from": start_time, "to": end_time}}}
                    ]
                }
            },
            "sort": {"@timestamp": {"order": "desc"}}
        }
    )
    return (response)

def SearchAllNotesAlerts(idsIndex, fieldIncident):
    client = esConn()
    hits_total = []
    response = SearchNotesAlerts(client, idsIndex, fieldIncident)
    sid = response['_scroll_id'] #Cada scroll possui uma id, usada para realizar iterações
    scroll_size = response['hits']['total'] #scroll_size recebe total de resultados
    #print("Total hits: " + str(scroll_size))
    while(scroll_size > 0):
        hits_total.extend(response['hits']['hits'])
        response = client.scroll(scroll_id = sid, scroll = '3m') #Realiza o scroll de determinada _scroll_id, determianando o tempo de scroll
        sid = response['_scroll_id']
        scroll_size = len(response['hits']['hits']) #Atualiza o tamanho de scroll_size (Quantidade de hits obtidos no scroll corrente)

    #pp = pprint.PrettyPrinter(indent=5)
    #pp.pprint(alerts_dict)
    if len(hits_total) != 0:
        return (hits_total)
