import socket
import json


def add_server(name, server_type, ip_address):
    new_server = Server(name, server_type, ip_address)
    ServerManager.servers.append(new_server)


def write_to_json():
    current_list = []
    for i in ServerManager.servers:
        current_list.append(str(i))
    json_string = json.dumps(current_list)
    with open('server_list.json', 'w') as json_file:
        json.dump(json_string, json_file)


class Server:

    def __init__(self, name, server_type, ip_address):
        self.name = name
        self.server_type = server_type
        self.ip_address = ip_address
        self.checkip()

    def checkip(self):
        try:
            socket.inet_aton(self.ip_address)
        except socket.error:
            raise ValueError('The given IP address is not valid!')

    def __str__(self):
        return f"The server's name: {self.name} / server's type: {self.server_type} / IP address: {self.ip_address}"


class ServerManager(Server):
    servers = []

    def __init__(self):
        super().__init__(self.name, self.server_type, self.ip_address)

    def listing(self):
        for i in self.servers:
            print(i)

    def find_server(self, anydata):
        for i in self.servers:
            if anydata in str(i):
                print(i)

    def load_servers_list(self, opt_path=None):
        with open(opt_path, 'r') as json_file:
            r = json.load(json_file)
        r_mod = r.split(',')
        for i in r_mod:
            print(i)


add_server('this', 'big', '148.122.10.11')
add_server('that', 'small', '147.10.11.14')
# ServerManager.find_server(ServerManager, 'this')
write_to_json()
ServerManager.load_servers_list(ServerManager, 'server_list.json')
