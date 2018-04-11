#!/usr/bin/python3
import time
from .broGetNotes import GetNotes
from .netflowSearchFlows import SearchAllFlows

def GetFlows():
    a_scan, p_scan, s_passguess, f_storm = GetNotes()
    address_scan_flow = []
    port_scan_flow = []
    ssh_passguess_flow = []
    fin_storm_flow = []

    for scan in a_scan:
        if scan[1] == '200.145.216.136' or scan[3] == '200.145.216.136':
            None
        else:
            lte = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(int(scan[0])+60))
            gte = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(int(scan[0]) - int(scan[3])))
            address_scan_flow.append(SearchAllFlows(scan[1], '.*', '.*', scan[2], scan[4], gte, lte))


    for scan in p_scan:
        if scan[1] == '200.145.216.136' or scan[3] == '200.145.216.136':
            None
        else:
            lte = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(int(scan[0])+60))
            gte = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(int(scan[0])-int(scan[3])-60))
            port_scan_flow.append(SearchAllFlows(scan[1], '.*', scan[2], '.*', '.*', gte, lte))

    for scan in s_passguess:
        if scan[1] == '200.145.216.136' or scan[3] == '200.145.216.136':
            None
        else:
            lte = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(int(scan[0])+60))
            gte = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(int(scan[0])-60))
            for i in range(len(scan[3])):
                ssh_passguess_flow.append(SearchAllFlows(scan[1], '.*', scan[3][i], scan[2], scan[4], gte, lte))

    return (address_scan_flow, port_scan_flow, ssh_passguess_flow)
