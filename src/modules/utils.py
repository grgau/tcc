#!/usr/bin/python3

import numpy
from datetime import datetime
from .getElasticsearch.netflowGetFlows import GetFlows
import itertools
from copy import deepcopy


def calcDuration(duration_list): # Calcula a duração entre o fluxo mais antigo e o mais recente

    utc_time = datetime.strptime(sorted(duration_list)[-1], "%Y-%m-%dT%H:%M:%S.%fZ")
    d1 = (utc_time - datetime(1970, 1, 1)).total_seconds()

    utc_time = datetime.strptime(sorted(duration_list)[0], "%Y-%m-%dT%H:%M:%S.%fZ")
    d2 = (utc_time - datetime(1970, 1, 1)).total_seconds()

    difference = d1 - d2
    return difference

def translateProtocol(protocol_name):
    if protocol_name == 'ICMP':
        return 1
    elif protocol_name == 'TCP':
        return 6
    elif protocol_name == 'UDP':
        return 17
    else:
        return 0

def getMinPkts(pkts_list):
    return (sorted(pkts_list)[0])

def getMaxPkts(pkts_list):
    return (sorted(pkts_list)[-1])

def getMeanPkts(pkts_list):
    return numpy.mean(pkts_list)

def getStdPkts(pkts_list):
    return numpy.std(pkts_list)

def getTotalPkts(pkts_list):
    return sum(pkts_list)

def getMinBytes(bytes_list):
    return (sorted(bytes_list)[0])

def getMaxBytes(bytes_list):
    return (sorted(bytes_list)[-1])

def getMeanBytes(bytes_list):
    return numpy.mean(bytes_list)

def getStdBytes(bytes_list):
    return numpy.std(bytes_list)

def getTotalBytes(bytes_list):
    return sum(bytes_list)

def convertTCPFlags(tcp_flag):
    flag = format(tcp_flag, '06b')

    if flag[5] == '1':
        fin = 1
    else:
        fin = 0

    if flag[4] == '1':
        syn = 1
    else:
        syn = 0

    if flag[3] == '1':
        rst = 1
    else:
        rst = 0

    if flag[2] == '1':
        psh = 1
    else:
        psh = 0

    if flag[1] == '1':
        ack = 1
    else:
        ack = 0

    if flag[0] == '1':
        urg = 1
    else:
        urg = 0

    return (urg, ack, psh, rst, syn, fin)

def countTCPFlags(tcp_flags_list):
    fin = syn = rst = psh = ack = urg = 0
    for flag in tcp_flags_list:
        fin += convertTCPFlags(flag)[5]
        syn += convertTCPFlags(flag)[4]
        rst += convertTCPFlags(flag)[3]
        psh += convertTCPFlags(flag)[2]
        ack += convertTCPFlags(flag)[1]
        urg += convertTCPFlags(flag)[0]
    return urg, ack, psh, rst, syn, fin

def GetFlowsLabel():
    ascan_raw, pscan_raw, spass_raw, fstorm_raw, sshscan_raw, gplscan_raw, p2pbittorrentping_raw, p2pclientutorrent_raw, mssqlbadtraffic_raw, all_traffic_raw = GetFlows()

    ascan_raw = [x for x in ascan_raw if x is not None] # Removendo valores None
    pscan_raw = [x for x in pscan_raw if x is not None] # Removendo valores None
    spass_raw = [x for x in spass_raw if x is not None] # Removendo valores None
    fstorm_raw = [x for x in fstorm_raw if x is not None] # Removendo valores None
    sshscan_raw = [x for x in sshscan_raw if x is not None] # Removendo valores None
    gplscan_raw = [x for x in gplscan_raw if x is not None] # Removendo valores None
    p2pbittorrentping_raw = [x for x in p2pbittorrentping_raw if x is not None] # Removendo valores None
    p2pclientutorrent_raw = [x for x in p2pclientutorrent_raw if x is not None] # Removendo valores None
    mssqlbadtraffic_raw = [x for x in mssqlbadtraffic_raw if x is not None] # Removendo valores None
    all_traffic_raw = [x for x in all_traffic_raw if x is not None] # Removendo valores None

    del ascan_raw[1::2] # Removendo valores de bro notes duplicados
    del pscan_raw[1::2] # Removendo valores de bro notes duplicados
    del spass_raw[1::2] # Removendo valores de bro notes duplicados
    del fstorm_raw[1::2] # Removendo valores de bro notes duplicados

    total_incidents = list(itertools.chain(ascan_raw, pscan_raw, spass_raw, fstorm_raw, sshscan_raw, gplscan_raw, p2pbittorrentping_raw, p2pclientutorrent_raw, mssqlbadtraffic_raw))
    legittraffic = removeIncidents(all_traffic_raw, total_incidents)

    for index in ascan_raw:
        if index is not None:
            index.insert(len(index), 1)

    for index in pscan_raw:
        if index is not None:
            index.insert(len(index), 2)

    for index in spass_raw:
        if index is not None:
            index.insert(len(index), 3)

    for index in fstorm_raw:
        if index is not None:
            index.insert(len(index), 4)

    for index in sshscan_raw:
        if index is not None:
            index.insert(len(index), 5)

    for index in gplscan_raw:
        if index is not None:
            index.insert(len(index), 6)

    for index in p2pbittorrentping_raw:
        if index is not None:
            index.insert(len(index), 7)

    for index in p2pclientutorrent_raw:
        if index is not None:
            index.insert(len(index), 8)

    for index in mssqlbadtraffic_raw:
        if index is not None:
            index.insert(len(index), 9)

    for index in legittraffic:
        if index is not None:
            index.insert(len(index), 10)

    return (ascan_raw, pscan_raw, spass_raw, fstorm_raw, sshscan_raw, gplscan_raw, p2pbittorrentping_raw, p2pclientutorrent_raw, mssqlbadtraffic_raw, legittraffic)

def removeIncidents(alltraffic_raw, total_incidents):
    legittraffic = deepcopy(alltraffic_raw)
    for listam2 in total_incidents:
        for listam1 in legittraffic:
            for i in range (len(listam1)):
                value = [item for item in listam2 if item['_id'] == listam1[i]['_id']]
                if value :
                    listam1[i]['_id'] = ''

    for lista in legittraffic:
        lista[:] = [d for d in lista if d.get('_id') != '']

    legittraffic = [x for x in legittraffic if x != []]

    return legittraffic
