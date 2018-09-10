#!/usr/bin/python3

from .searchNotesAlerts import SearchAllNotesAlerts

def GetNotes():
    hits_total = SearchAllNotesAlerts("bro-*", "note")
    address_scan = []
    port_scan = []
    ssh_passguess = []
    fin_storm = []

    if not hits_total:
        return (address_scan, port_scan, ssh_passguess, fin_storm)

    for hit in hits_total:
        if hit['_source']['note'] == 'Scan::Address_Scan':
            time_m, time_s = hit['_source']['msg'].split(' ', 11)[11].split('m', 2)[0] , hit['_source']['msg'].split(' ', 11)[11].split('m', 2)[1].replace("s", "")
            time = (int(time_m) * 60) + int(time_s)
            address_scan.append(tuple((hit['_source']['ts'].split('.',2)[0], hit['_source']['src'], hit['_source']['dst'], hit['_source']['p'], str(time), hit['_source']['proto'].upper())))
        elif hit['_source']['note'] == 'Scan::Port_Scan':
            time_m, time_s = hit['_source']['msg'].split(' ', 11)[11].split('m', 2)[0] , hit['_source']['msg'].split(' ', 11)[11].split('m', 2)[1].replace("s", "")
            time = (int(time_m) * 60) + int(time_s)
            port_scan.append(tuple((hit['_source']['ts'].split('.',2)[0], hit['_source']['src'], hit['_source']['dst'], str(time), hit['_source']['proto'].upper())))
        elif hit['_source']['note'] == 'SSH::Password_Guessing':
            dst_hosts = hit['_source']['sub']
            dst_hosts = dst_hosts.split('  ', 2)[1].split(',',5)
            dst_hosts = [host.replace(" ", "") for host in dst_hosts]
            dst_hosts = list(set(dst_hosts))
            ssh_passguess.append(tuple((hit['_source']['ts'].split('.',2)[0], hit['_source']['src'], '22', dst_hosts, 'TCP')))
        elif hit['_source']['note'] == 'Weird::Activity':
            fin_storm.append(tuple((hit['_source']['ts'].split('.',2)[0], hit['_source']['id.orig_h'], str(hit['_source']['id.orig_p']), hit['_source']['id.resp_h'], str(hit['_source']['id.resp_p']), hit['_source']['proto'].upper())))

    return (address_scan, port_scan, ssh_passguess, fin_storm)
