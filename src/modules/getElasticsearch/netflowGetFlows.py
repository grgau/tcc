#!/usr/bin/python3

import time
import pandas as pd
from .suricataGetAlerts import GetAlerts
from .broGetNotes import GetNotes
from .netflowSearchFlows import SearchAllFlows
from itertools import groupby

def GetFlows():
    from ..dates import (start_time, end_time)

    a_scan, p_scan, s_passguess, f_storm = GetNotes()
    ssh_scan, gpl_scan, p2p_bittorrentping, p2p_clientutorrent, mssql_badtraffic, dos_ntp = GetAlerts()

    # Verifica listas vazias, se não há alertas na janela de tempo, não busca fluxos legitmos
    if not ssh_scan and not gpl_scan and not p2p_bittorrentping and not p2p_clientutorrent and not mssql_badtraffic and not dos_ntp:
        None
    else:
        all_flows = SearchAllFlows('.*', '.*', '.*', '.*', '.*', start_time, end_time)

    address_scan_flow = []
    port_scan_flow = []
    ssh_passguess_flow = []
    fin_storm_flow = []
    ssh_scan_flow = []
    gpl_scan_flow = []
    p2p_bittorrentping_flow = []
    p2p_clientutorrent_flow = []
    mssql_badtraffic_flow = []
    dos_ntp_flow = []
    all_traffic_flow = []

    for scan in a_scan:
        if scan[1] == '200.145.216.136' or scan[2] == '200.145.216.136':
            # t_ini,src,dst,port_dst,t_fim,proto
            None
        else:
            lte = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(int(scan[0])+600))
            gte = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(int(scan[0]) - int(scan[4])))
            address_scan_flow.append(SearchAllFlows(scan[1], '.*', '.*', scan[3], scan[5], gte, lte))

    for scan in p_scan:
        if scan[1] == '200.145.216.136' or scan[2] == '200.145.216.136':
            # t_ini,src,dst,t_fim,proto
            None
        else:
            lte = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(int(scan[0])+600))
            gte = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(int(scan[0])-int(scan[3])-600))
            port_scan_flow.append(SearchAllFlows(scan[1], '.*', scan[2], '.*', '.*', gte, lte))

    for scan in s_passguess:
        if scan[1] == '200.145.216.136' or '200.145.216.136' in scan[2]:
            # t_ini,src,port_dst,dst(list),proto
            None
        else:
            lte = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(int(scan[0])+600))
            gte = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(int(scan[0])-600))
            for i in range(len(scan[3])):
                ssh_passguess_flow.append(SearchAllFlows(scan[1], '.*', scan[3][i], scan[2], scan[4], gte, lte))

    for scan in f_storm:
        if scan[1] == '200.145.216.136' or scan[3] == '200.145.216.136':
            # t_ini,src,port_src,dst,port_dst,proto
            None
        else:
            lte = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(int(scan[0])+600))
            gte = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(int(scan[0])-600))
            fin_storm_flow.append(SearchAllFlows(scan[1], scan[2], scan[3], scan[4], scan[5], gte, lte))


    for scan in ssh_scan:
        if scan[1] == '200.145.216.136' or scan[3] == '200.145.216.136':
            # t_ini,src,port_src,dst,port_dst,proto
            None
        else:
            lte = pd.to_datetime(scan[0]) + pd.DateOffset(minutes=10) # valor maximo
            gte = pd.to_datetime(scan[0]) - pd.DateOffset(minutes=10) # valor minimo
            ssh_scan_flow.append(SearchAllFlows(scan[1], scan[2], scan[3], scan[4], scan[5], gte, lte))

    for scan in gpl_scan:
        if scan[1] == '200.145.216.136' or scan[2] == '200.145.216.136':
            # t_ini,src,dst,proto
            None
        else:
            lte = pd.to_datetime(scan[0]) + pd.DateOffset(minutes=10) # valor maximo
            gte = pd.to_datetime(scan[0]) - pd.DateOffset(minutes=10) # valor minimo
            gpl_scan_flow.append(SearchAllFlows(scan[1], '.*', scan[2], '.*', scan[3], gte, lte))

    for scan in p2p_bittorrentping:
        if scan[1] == '200.145.216.136' or scan[3] == '200.145.216.136':
            # t_ini,src,port_src,dst,port_dst,proto
            None
        else:
            lte = pd.to_datetime(scan[0]) + pd.DateOffset(minutes=10) # valor maximo
            gte = pd.to_datetime(scan[0]) - pd.DateOffset(minutes=10) # valor minimo
            p2p_bittorrentping_flow.append(SearchAllFlows(scan[1], scan[2], scan[3], scan[4], scan[5], gte, lte))

    for scan in p2p_clientutorrent:
        if scan[1] == '200.145.216.136' or scan[3] == '200.145.216.136':
            # t_ini,src,port_src,dst,port_dst,proto
            None
        else:
            lte = pd.to_datetime(scan[0]) + pd.DateOffset(minutes=10) # valor maximo
            gte = pd.to_datetime(scan[0]) - pd.DateOffset(minutes=10) # valor minimo
            p2p_clientutorrent_flow.append(SearchAllFlows(scan[1], scan[2], scan[3], scan[4], scan[5], gte, lte))

    for scan in mssql_badtraffic:
        if scan[1] == '200.145.216.136' or scan[3] == '200.145.216.136':
            # t_ini,src,port_src,dst,port_dst,proto
            None
        else:
            lte = pd.to_datetime(scan[0]) + pd.DateOffset(minutes=1) # valor maximo
            gte = pd.to_datetime(scan[0]) - pd.DateOffset(minutes=1) # valor minimo
            mssql_badtraffic_flow.append(SearchAllFlows(scan[1], scan[2], scan[3], scan[4], scan[5], gte, lte))

    for scan in dos_ntp:
        if scan[1] == '200.145.216.136' or scan[3] == '200.145.216.136':
            # t_ini,src,port_src,dst,port_dst,proto
            None
        else:
            lte = pd.to_datetime(scan[0]) + pd.DateOffset(minutes=1) # valor maximo
            gte = pd.to_datetime(scan[0]) - pd.DateOffset(minutes=1) # valor minimo
            dos_ntp_flow.append(SearchAllFlows(scan[1], scan[2], '.*', scan[4], scan[5], gte, lte))


    all_traffic_flow = groupFlows(10)

    return (address_scan_flow, port_scan_flow, ssh_passguess_flow, fin_storm_flow, ssh_scan_flow, gpl_scan_flow, p2p_bittorrentping_flow, p2p_clientutorrent_flow, mssql_badtraffic_flow, dos_ntp_flow, all_traffic_flow)

def groupFlows(window):
    from ..dates import (start_time, end_time)
    allflows = []
    start_time = pd.to_datetime(start_time)
    end_time = pd.to_datetime(end_time)
    start_interval = start_time
    end_interval = pd.to_datetime(start_interval) + pd.DateOffset(minutes=window)
    end_interval = pd.to_datetime(end_interval) - pd.DateOffset(seconds=1)

    while (end_interval <= end_time):
        all_flows = list(SearchAllFlows('.*', '.*', '.*', '.*', '.*', start_interval, end_interval))
        print(start_interval, end_interval)

        for flow in all_flows[:]:
            if flow['_source']['netflow']['src_addr'] == '200.145.216.136' or flow['_source']['netflow']['dst_addr'] == '200.145.216.136':
                all_flows.remove(flow)

        try:
            for key, items in groupby(sorted(all_flows, key=lambda item: (item["_source"]["netflow"]["src_addr"], str(item["_source"]["netflow"]["src_port"]), str(item["_source"]["netflow"]["protocol"]))), \
            key=lambda item: (item["_source"]["netflow"]["src_addr"], str(item["_source"]["netflow"]["src_port"]), str(item["_source"]["netflow"]["protocol"]))):
                allflows.append(list(items))
        except TypeError as e:
            print (e)

        start_interval = pd.to_datetime(start_interval) + pd.DateOffset(minutes=window)
        end_interval = pd.to_datetime(end_interval) + pd.DateOffset(minutes=window)

    return allflows
