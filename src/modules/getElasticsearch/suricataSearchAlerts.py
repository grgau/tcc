def SearchAlerts():
    response = client.search (
        index = "suricata-*",
        scroll = '3m', #Tempo de scroll (Tempo maximo que um scroll irá demorar para processar a quantidade de resultados dele)
        size = 10000,
        body = {
            "query": {
                "bool": {
                    "must": [
                        {"exists": {"field": "alert.signature"}},
                        {"range": {"@timestamp": {"from": "now-30m", "to": "now"}}}
                    ]
                }
            },
            "sort": {"@timestamp": {"order": "desc"}}
        }
    )
    return (response)

def SearchAllAlerts():
    hits_total = []
    response = SearchAlerts()
    sid = response['_scroll_id'] #Cada scroll possui uma id, usada para realizar iterações
    scroll_size = response['hits']['total'] #scroll_size recebe total de resultados
    print("Total hits: " + str(scroll_size))
    while(scroll_size > 0):
        hits_total.extend(response['hits']['hits'])
        response = client.scroll(scroll_id = sid, scroll = '3m') #Realiza o scroll de determinada _scroll_id, determianando o tempo de scroll
        sid = response['_scroll_id']
        scroll_size = len(response['hits']['hits']) #Atualiza o tamanho de scroll_size (Quantidade de hits obtidos no scroll corrente)

    #alerts_dict = Counter(item["_source"]["alert"]["signature"] for item in hits_total)
    #pp = pprint.PrettyPrinter(indent=5)
    #pp.pprint(alerts_dict)
    return (hits_total)
