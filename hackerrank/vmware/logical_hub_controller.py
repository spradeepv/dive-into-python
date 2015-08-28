hosts_dict = {}
hub_id_dict = {}
hosts = []

def get_input():
    inp = raw_input()
    while inp:
        l = inp.split()
        hub_ids = l[1:]
        hosts_dict.update({l[0]: hub_ids})
        try:
            inp = raw_input()
        except EOFError:
            break

def get_mappings():
    hosts.extend(hosts_dict.keys())
    hubs = []
    for host in hosts:
        hubs.extend(hosts_dict.get(host))
    hubs = list(set(hubs))
    for hub_id in hubs:
        for host in hosts:
            hub_list = hosts_dict.get(host)
            if hub_list.count(hub_id) > 0:
                if hub_id_dict.has_key(hub_id):
                    l = hub_id_dict.get(hub_id)
                    l.append(host)
                else:
                    hub_id_dict.update({hub_id: [host]})
    #print hubs
    #print hub_id_dict

def port_to_port(host, indices):
    length = len(indices)
    for i in indices:
        s = "PORT_TO_PORT " + host
        for j in indices:
            if i != j:
                print s, i, j

def port_to_tunnel(src_host, src_port, dest_host, dest_port):
    if dest_port:
        s = "PORT_TO_TUNNEL"
        if len(dest_port) > 1:
            l = []
            for port in dest_port:
                if port not in l:
                    print s, src_host, src_port, dest_host, port
                    l.append(port)
        else:
            print s, src_host, src_port, dest_host, dest_port[0]

def tunnel_to_port(host, hub, port):
    s = "TUNNEL_TO_PORT"
    print s, host, hub, port

def get_command():
    for host in hosts:
        hubs = hosts_dict.get(host)
        for hub in list(set(hubs)):
            indices = [i for i, x in enumerate(hubs) if x == hub]
            if len(indices) > 1:
                port_to_port(host, indices)
        index = 0
        for src_hub in hubs:
            dest_hosts = hub_id_dict.get(src_hub)
            for dest_host in dest_hosts:
                if host != dest_host:
                    dest_hubs = hosts_dict.get(dest_host)
                    indices = [x for i, x in enumerate(dest_hubs) if x == src_hub]
                    port_to_tunnel(host, index, dest_host, indices)
            if len(dest_hosts) > 1:
                tunnel_to_port(host, src_hub, index)
            index += 1

get_input()
get_mappings()
get_command()