from elasticsearch import Elasticsearch
import hits_all_hits_netflow

try:
    client = Elasticsearch('200.145.216.220:9200')
except:
    client = Elasticsearch('200.145.216.220:9200')

def GetNote():
    response = client.search (
        index = "bro-*",
        body = {
            "query": {
                "bool": {
                    "must": [
                        {"exists": {"field": "note"}},
                        {"range": {"@timestamp": {"from": "now-1h", "to": "now"}}}
                    ]
                }
            },
            "size": 1,
            "sort": {"@timestamp": {"order": "desc"}}
        }
    )
    return (response)

recent = ()

while(True):
    alerts = GetNote()
    alert_note = alerts['hits']['hits'][0]['_source']['note']
    alert_msg = alerts['hits']['hits'][0]['_source']['msg']
    if (alert_note == 'Scan::Address_Scan'):
        last = (alert_note.split('::')[0], alert_note.split('::')[1] , alert_msg.split(' ')[0], alert_msg.split(' ')[4], alert_msg.split(' ')[6], alert_msg.split(' ')[9].split('/')[0], alert_msg.split(' ')[9].split('/')[1], str(int(alert_msg.split(' ')[11].split('m')[0])*60 + int(alert_msg.split(' ')[11].split('m')[1].split('s')[0]) + 10)+'s')
        if (recent != last):
            recent = last
            print (last)
            hits_all_hits_netflow.Get_All_Hits('netflow-*', str(last[2]), '200\.145\..*', str(last[5]), str(last[6]).upper(), 'now-'+str(last[7]), 'now')

    #elif (alert_note == 'SSL::Invalid_Server_Cert'):

    #elif (alert_note == 'Intel::Notice'):

#alerts = GetNote()
#alert_note = alerts['hits']['hits'][0]['_source']['note']
#alert_msg = alerts['hits']['hits'][0]['_source']['msg']
#last = (alert_note.split('::')[0], alert_note.split('::')[1] , alert_msg.split(' ')[0], alert_msg.split(' ')[4], alert_msg.split(' ')[6], alert_msg.split(' ')[9].split('/')[0], alert_msg.split(' ')[9].split('/')[1], str(int(alert_msg.split(' ')[11].split('m')[0])*60 + int(alert_msg.split(' ')[11].split('m')[1].split('s')[0]))+'s')
