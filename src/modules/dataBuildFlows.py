# Imnprimir bro_incidents, alltraffic_raw, total_incidents e verificar ligitmidade dos resultados

from .getElasticsearch.netflowGetFlows import GetFlows
from .utils import *
from .csvCreate import createCsv

def BuildFlows():
    ascan_raw, pscan_raw, spass_raw, sshscan_raw, fstorm_raw, gplscan_raw, p2pbittorrentping_raw, p2pclientutorrent_raw, mssqlbadtraffic_raw, legittraffic = GetFlowsLabel()

    total_flows = list(itertools.chain(ascan_raw, pscan_raw, spass_raw, sshscan_raw, fstorm_raw, gplscan_raw, p2pbittorrentping_raw, p2pclientutorrent_raw, mssqlbadtraffic_raw, legittraffic))
    total_flows = [x for x in total_flows if x is not None]
    # Removendo de alltraffic_raw os mesmos fluxos que existem em total_incidents

    """import pprint
    pp = pprint.PrettyPrinter(depth=4)
    pp.pprint(total_flows)


    for i in range (0,len(total_flows)):
        for j in range(0, len(total_flows[i])-1): #Para cada um dos flows
            print(len(total_flows[i]))
    """

    sec_incident = []  # O lindissimo, falou tudo. O maravilhoso usado para classificar
                        # Seus campos maravilhosos:
    #duracao(last.switched-first.switched), qtd_fluxos, unique_dst_port, protocol,
    #in_pkts_min, in_pkts_max, in_pkts_mean, in_pkts_std, in_pkts_total,
    #in_bytes_min, in_bytes_max, in_bytes_mean, in_bytes_std, in_bytes_total,
    #qtd_urg, qtd_ack, qtd_psh, qtd_rst, qtd_syn, qtd_fin
    # input_snmp, output_snmp (nao implementado, porem easy de implementar)
    #tag (1 = address_scan, 2 = port_scan, 3 = ssh_passguess)

    duration_list = [] # Lista de first.switched de cada fluxo de um pacote de atividade
    bytes_list = [] # Lista de quantidade de bytes de cada fluxo em um pacote de atividade
    pkts_list = [] # Lista de quantidade de pkts em cada fluxo em um pacote de atividade
    dst_ports_list = []
    tcp_flags_list = []

    # Append de atividades de address_scan
    for i in range (0,len(total_flows)):
        for j in range(0, len(total_flows[i])-1): #Para cada um dos flows
            duration_list.append(total_flows[i][j]['_source']['netflow']['first_switched'])
            pkts_list.append(total_flows[i][j]['_source']['netflow']['in_pkts'])
            bytes_list.append(total_flows[i][j]['_source']['netflow']['in_bytes'])
            dst_ports_list.append(total_flows[i][j]['_source']['netflow']['dst_port'])
            tcp_flags_list.append(total_flows[i][j]['_source']['netflow']['tcp_flags'])

        protocol_name = total_flows[i][0]['_source']['netflow']['protocol']
        urg, ack, psh, rst, syn, fin = countTCPFlags(tcp_flags_list)


        sec_incident.append(tuple((calcDuration(duration_list), len(total_flows[i]), len(set(dst_ports_list)), translateProtocol(protocol_name),
                   getMinPkts(pkts_list), getMaxPkts(pkts_list), getMeanPkts(pkts_list), getStdPkts(pkts_list), getTotalPkts(pkts_list),
                   getMinBytes(bytes_list), getMaxBytes(bytes_list), getMeanBytes(bytes_list), getStdBytes(bytes_list), getTotalBytes(bytes_list),
                   urg, ack, psh, rst, syn, fin, total_flows[i][-1])))

        del duration_list[:]
        del bytes_list[:]
        del pkts_list[:]
        del dst_ports_list[:]
        del tcp_flags_list[:]

    return sec_incident
