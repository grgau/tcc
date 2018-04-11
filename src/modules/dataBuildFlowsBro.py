from .getElasticsearch.netflowGetFlowsBro import GetFlows
from .utils import *
from .csvCreate import createCsv

def BuildFlows():
    ascan_raw, pscan_raw, spass_raw = GetFlows()
    ascan_raw = [x for x in ascan_raw if x is not None] # Removendo valores None


    sec_incident = []  # O lindissimo, falou tudo. O maravilhoso usado para classificar
                        # Seus campos maravilhosos:
    # duracao(last.switched-first.switched), qtd_fluxos, unique_dst_port, protocol,
    # in_pkts_min, in_pkts_max, in_pkts_mean, in_pkts_std, in_pkts_total,
    # in_bytes_min, in_bytes_max, in_bytes_mean, in_bytes_std, in_bytes_total,
    # qtd_urg, qtd_ack, qtd_psh, qtd_rst, qtd_syn, qtd_fin
    # input_snmp, output_snmp (nao implementado, porem easy de implementar)
    # tag (1 = address_scan, 2 = port_scan, 3 = ssh_passguess)


    duration_list = [] # Lista de first.switched de cada fluxo de um pacote de atividade
    bytes_list = [] # Lista de quantidade de bytes de cada fluxo em um pacote de atividade
    pkts_list = [] # Lista de quantidade de pkts em cada fluxo em um pacote de atividade
    dst_ports_list = []
    tcp_flags_list = []

    # Append de atividades de address_scan
    for i in range (0,len(ascan_raw)):
        for flow_raw in ascan_raw[i]: #Para cada um dos flows
            duration_list.append(flow_raw['_source']['netflow']['first_switched'])
            pkts_list.append(flow_raw['_source']['netflow']['in_pkts'])
            bytes_list.append(flow_raw['_source']['netflow']['in_bytes'])
            dst_ports_list.append(flow_raw['_source']['netflow']['dst_port'])
            tcp_flags_list.append(flow_raw['_source']['netflow']['tcp_flags'])

        protocol_name = ascan_raw[i][0]['_source']['netflow']['protocol']
        urg, ack, psh, rst, syn, fin = countTCPFlags(tcp_flags_list)


        sec_incident.append(tuple((calcDuration(duration_list), len(ascan_raw), len(set(dst_ports_list)), translateProtocol(protocol_name),
                    getMinPkts(pkts_list), getMaxPkts(pkts_list), getMeanPkts(pkts_list), getStdPkts(pkts_list), getTotalPkts(pkts_list),
                    getMinBytes(bytes_list), getMaxBytes(bytes_list), getMeanBytes(bytes_list), getStdBytes(bytes_list), getTotalBytes(bytes_list),
                    urg, ack, psh, rst, syn, fin, 1)))

        del duration_list[:]
        del bytes_list[:]
        del pkts_list[:]
        del dst_ports_list[:]
        del tcp_flags_list[:]


    # Append de atividades de port_scan
    for i in range (0,len(pscan_raw)):
        for flow_raw in pscan_raw[i]: #Para cada um dos flows
            duration_list.append(flow_raw['_source']['netflow']['first_switched'])
            pkts_list.append(flow_raw['_source']['netflow']['in_pkts'])
            bytes_list.append(flow_raw['_source']['netflow']['in_bytes'])
            dst_ports_list.append(flow_raw['_source']['netflow']['dst_port'])
            tcp_flags_list.append(flow_raw['_source']['netflow']['tcp_flags'])

        protocol_name = pscan_raw[i][0]['_source']['netflow']['protocol']
        urg, ack, psh, rst, syn, fin = countTCPFlags(tcp_flags_list)


        sec_incident.append(tuple((calcDuration(duration_list), len(pscan_raw), len(set(dst_ports_list)), translateProtocol(protocol_name),
                    getMinPkts(pkts_list), getMaxPkts(pkts_list), getMeanPkts(pkts_list), getStdPkts(pkts_list), getTotalPkts(pkts_list),
                    getMinBytes(bytes_list), getMaxBytes(bytes_list), getMeanBytes(bytes_list), getStdBytes(bytes_list), getTotalBytes(bytes_list),
                    urg, ack, psh, rst, syn, fin, 2)))

        del duration_list[:]
        del bytes_list[:]
        del pkts_list[:]
        del dst_ports_list[:]
        del tcp_flags_list[:]

    # Append de atividades de ssh_passguess
    for i in range (0,len(spass_raw)):
        for flow_raw in spass_raw[i]: #Para cada um dos flows
            duration_list.append(flow_raw['_source']['netflow']['first_switched'])
            pkts_list.append(flow_raw['_source']['netflow']['in_pkts'])
            bytes_list.append(flow_raw['_source']['netflow']['in_bytes'])
            dst_ports_list.append(flow_raw['_source']['netflow']['dst_port'])
            tcp_flags_list.append(flow_raw['_source']['netflow']['tcp_flags'])

        protocol_name = spass_raw[i][0]['_source']['netflow']['protocol']
        urg, ack, psh, rst, syn, fin = countTCPFlags(tcp_flags_list)


        sec_incident.append(tuple((calcDuration(duration_list), len(spass_raw), len(set(dst_ports_list)), translateProtocol(protocol_name),
                    getMinPkts(pkts_list), getMaxPkts(pkts_list), getMeanPkts(pkts_list), getStdPkts(pkts_list), getTotalPkts(pkts_list),
                    getMinBytes(bytes_list), getMaxBytes(bytes_list), getMeanBytes(bytes_list), getStdBytes(bytes_list), getTotalBytes(bytes_list),
                    urg, ack, psh, rst, syn, fin, 3)))

        del duration_list[:]
        del bytes_list[:]
        del pkts_list[:]
        del dst_ports_list[:]
        del tcp_flags_list[:]


    del sec_incident[1::2]
    
    return sec_incident
