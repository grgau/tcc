#!/usr/bin/python3

from .searchNotesAlerts import SearchAllNotesAlerts

def GetAlerts():
    hits_total = SearchAllNotesAlerts("suricata-*", "alert.signature")
    ssh_scan = []
    gpl_scan = []
    p2p_bittorrentping = []
    p2p_clientutorrent = []
    mssql_badtraffic = []

    if not hits_total:
        return (ssh_scan, gpl_scan, p2p_bittorrentping, p2p_clientutorrent, mssql_badtraffic)

    for hit in hits_total:
        if hit['_source']['alert']['signature'] == 'ET SCAN Potential SSH Scan':
            ssh_scan.append(tuple((hit['_source']['timestamp'], hit['_source']['src_ip'], hit['_source']['src_port'], hit['_source']['dest_ip'], hit['_source']['dest_port'], hit['_source']['proto'])))
        elif hit['_source']['alert']['signature'] == 'GPL SCAN superscan echo':
            gpl_scan.append(tuple((hit['_source']['timestamp'], hit['_source']['src_ip'], hit['_source']['dest_ip'], hit['_source']['proto'])))
        elif hit['_source']['alert']['signature'] == 'ET P2P BitTorrent DHT ping request':
            p2p_bittorrentping.append(tuple((hit['_source']['timestamp'], hit['_source']['src_ip'], hit['_source']['src_port'], hit['_source']['dest_ip'], hit['_source']['dest_port'], hit['_source']['proto'])))
        elif hit['_source']['alert']['signature'] == 'ET P2P BTWebClient UA uTorrent in use':
            p2p_clientutorrent.append(tuple((hit['_source']['timestamp'], hit['_source']['src_ip'], hit['_source']['src_port'], hit['_source']['dest_ip'], hit['_source']['dest_port'], hit['_source']['proto'])))
        elif hit['_source']['alert']['signature'] == 'ET POLICY Suspicious inbound to MSSQL port 1433':
            mssql_badtraffic.append(tuple((hit['_source']['timestamp'], hit['_source']['src_ip'], hit['_source']['src_port'], hit['_source']['dest_ip'], hit['_source']['dest_port'], hit['_source']['proto'])))
        #else:
            #pp.pprint(hit['_source']['alert'])
    return (ssh_scan, gpl_scan, p2p_bittorrentping, p2p_clientutorrent, mssql_badtraffic)
