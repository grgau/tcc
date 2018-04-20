from .elasticsearchConnect import *

def SearchNotes(client):
    from ..dates import (start_time, end_time)
    response = client.search (
        index = "bro-*",
        scroll = '20m', #Tempo de scroll (Tempo maximo que um scroll irá demorar para processar a quantidade de resultados dele)
        size = 10000,
        request_timeout = 180,
        body = {
            "query": {
                "bool": {
                    "must": [
                        {"exists": {"field": "note"}},
                        {"range": {"@timestamp": {"from": start_time, "to": end_time}}}
                    ]
                }
            },
            "sort": {"@timestamp": {"order": "desc"}}
        }
    )
    return (response)

def SearchAllNotes():
    client = esConn()
    hits_total = []
    response = SearchNotes(client)
    sid = response['_scroll_id'] #Cada scroll possui uma id, usada para realizar iterações
    scroll_size = response['hits']['total'] #scroll_size recebe total de resultados
    #print("Total hits: " + str(scroll_size))
    while(scroll_size > 0):
        hits_total.extend(response['hits']['hits'])
        response = client.scroll(scroll_id = sid, scroll = '3m') #Realiza o scroll de determinada _scroll_id, determianando o tempo de scroll
        sid = response['_scroll_id']
        scroll_size = len(response['hits']['hits']) #Atualiza o tamanho de scroll_size (Quantidade de hits obtidos no scroll corrente)

    #notes_dict = Counter(item["_source"]["note"] for item in hits_total)
    #pp.pprint(notes_dict)
    if len(hits_total) != 0:
        return (hits_total)
