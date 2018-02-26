from elasticsearch import Elasticsearch
__name__ = "hits_all_hits_netflow"

try:
    client = Elasticsearch('200.145.216.220:9200')
except ConnectionTimeout:
    client = Elasticsearch('200.145.216.220:9200')

def GetHits (givenIndex, givenSRCAddr, givenDSTAddr, givenDSTPort, givenProtocol, time_gte, time_lte):
    response = client.search (
        index = givenIndex,
        scroll = '3m', #Tempo de scroll (Tempo maximo que um scroll irá demorar para processar a quantidade de resultados dele)
        size = 10000, #Quantidade de resultados por scroll
        body = {
            "query": {
                "bool": {
                    "must": [
                        {"range": {"@timestamp": {"gte": time_gte, "lte": time_lte}}},
                        {"regexp": {"netflow.ipv4_src_addr": givenSRCAddr}},
                        {"regexp": {"netflow.ipv4_dst_addr": givenDSTAddr}},
                        {"match": {"netflow.l4_dst_port": givenDSTPort}},
                        {"match": {"netflow.protocol": givenProtocol}}
                    ]
                }
            }
        }
    )
    return (response)

def Get_All_Hits(givenIndex, givenSRCAddr, givenDSTAddr, givenDSTPort, givenProtocol, time_gte, time_lte):
    hits_total = []
    response = GetHits(givenIndex, givenSRCAddr, givenDSTAddr, givenDSTPort, givenProtocol, time_gte, time_lte)
    sid = response['_scroll_id'] #Cada scroll possui uma id, usada para realizar iterações
    scroll_size = response['hits']['total'] #scroll_size recebe total de resultados
    print("Total hits: " + str(scroll_size))
    while(scroll_size > 0):
        hits_total.extend(response['hits']['hits'])
        response = client.scroll(scroll_id = sid, scroll = '3m') #Realiza o scroll de determinada _scroll_id, determianando o tempo de scroll
        sid = response['_scroll_id']
        scroll_size = len(response['hits']['hits']) #Atualiza o tamanho de scroll_size (Quantidade de hits obtidos no scroll corrente)

    #print (hits_total[0].get("_index"))
    print ([str(d['_source']['netflow']['ipv4_src_addr'])+":"+str(d['_source']['netflow']['l4_src_port'])+" -> "+str(d['_source']['netflow']['ipv4_dst_addr'])+":"+str(d['_source']['netflow']['l4_dst_port']) for d in hits_total])


"""
Regexp sintaxe:
    .*    -> Tudo depois de determinada string
    \     -> Caractere de escape (por ex: \. faz escape do .)
    ~     -> Negacao do proximo caractere (por ex: ~a retorna tudo que nao possui a)
    <a-b> -> Especifica um intervalo de resultados (por ex: <1-10> encontra numeros de 1 a 10)

Regexp exemplos:
    200\.145\.216\..*        -> Tudo que possui 200.145.216. no campo especificado
    ~(200\.145\.216\..*)     -> Tudo que NÃO possui 200.145.216. no campo especificado
    200\.145\.216\.<1-100>   -> Todos os ips de 200.145.216.1 até 200.145.216.100
"""

Get_All_Hits('netflow-2018.02.26', '222.240.222.92', '200\.145\..*', '2010', 'TCP', 'now-10m', 'now')