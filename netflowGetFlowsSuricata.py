import pandas as pd
from .suricataGetAlerts import GetAlerts
from .netflowSearchFlows import SearchAllFlows

def GetFlows():
    ssh_scan, gpl_scan, p2p_bittorrentping, p2p_clientutorrent, mssql_badtraffic = GetAlerts()
    ssh_scan_flow = []
    gpl_scan_flow = []
    p2p_bittorrentping_flow = []
    p2p_clientutorrent_flow = []
    mssql_badtraffic_flow = []

    for scan in ssh_scan:
        lte = pd.to_datetime(scan[0]) + pd.DateOffset(minutes=1) # valor maximo
        gte = pd.to_datetime(scan[0]) - pd.DateOffset(minutes=1) # valor minimo
        ssh_scan_flow.append(SearchAllFlows(scan[1], scan[2], scan[3], scan[4], scan[5], gte, lte))

    for scan in gpl_scan:
        lte = pd.to_datetime(scan[0]) + pd.DateOffset(minutes=1) # valor maximo
        gte = pd.to_datetime(scan[0]) - pd.DateOffset(minutes=1) # valor minimo
        gpl_scan_flow.append(SearchAllFlows(scan[1], '.*', scan[2], '.*', scan[3], gte, lte))

    for scan in p2p_bittorrentping:
        lte = pd.to_datetime(scan[0]) + pd.DateOffset(minutes=1) # valor maximo
        gte = pd.to_datetime(scan[0]) - pd.DateOffset(minutes=1) # valor minimo
        p2p_bittorrentping_flow.append(SearchAllFlows(scan[1], scan[2], scan[3], scan[4], scan[5], gte, lte))

    for scan in p2p_clientutorrent:
        lte = pd.to_datetime(scan[0]) + pd.DateOffset(minutes=1) # valor maximo
        gte = pd.to_datetime(scan[0]) - pd.DateOffset(minutes=1) # valor minimo
        p2p_clientutorrent_flow.append(SearchAllFlows(scan[1], scan[2], scan[3], scan[4], scan[5], gte, lte))

    for scan in mssql_badtraffic:
        lte = pd.to_datetime(scan[0]) + pd.DateOffset(minutes=1) # valor maximo
        gte = pd.to_datetime(scan[0]) - pd.DateOffset(minutes=1) # valor minimo
        mssql_badtraffic_flow.append(SearchAllFlows(scan[1], scan[2], scan[3], scan[4], scan[5], gte, lte))

    return (ssh_scan_flow, gpl_scan_flow, p2p_bittorrentping_flow, p2p_clientutorrent_flow, mssql_badtraffic_flow)
