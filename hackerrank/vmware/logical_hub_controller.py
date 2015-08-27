hosts_dict = {}
hub_id_dict = {}
hosts = []

def get_input():
    inp = raw_input()
    while inp:
        l = inp.split()
        hub_ids = l[1:]
        hosts_dict.update({l[0]: hub_ids})
        inp = raw_input()

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
    print hubs
    print hub_id_dict

def port_to_port(host, indices):
    length = len(indices)
    for i in indices:
        s = "PORT_TO_PORT " + host
        for j in indices:
            if i != j:
                print s, i, j

def get_command():
    for host in hosts:
        hubs = hosts_dict.get(host)
        l =
        for hub in hubs:
            indices = [i for i, x in enumerate(hubs) if x == hub]
            if len(indices) > 1:
                print indices
                port_to_port(host, indices)

get_input()
get_mappings()
get_command()