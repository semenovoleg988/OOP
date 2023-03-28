class Data:

    def __init__(self, data: str, dest_IP: int) -> None:
        self.data = data
        self.dest_IP = dest_IP

class Server:

    def __init__(self) -> None:
        self.IP = id(self)
        self.buffer  = []

    def send_data(self, data: Data):
        if hasattr(self, "router"):
            self.router.buffer.append(data)
        else: 
            print("Router not connected!")

    def get_data(self):
        arr = self.buffer
        self.buffer = [] 
        return arr 

    def get_ip(self):
        return self.IP


class Router:

    def __init__(self) -> None:
        self.buffer = []
        self.servers = {}
    
    def link(self, server: Server):
        self.servers[server.get_ip()] = server
        server.router = self

    def unlink(self, server: Server):
        if self.servers.get(server.get_ip(), None):
            self.servers.pop(server.get_ip())
            server.router = None
        
    def send_data(self):
        for data in self.buffer:
            if data.dest_IP in self.servers.keys():
                self.servers[data.dest_IP].buffer.append(data)
        self.buffer = []
        

router = Router()
sv_from = Server()
sv_from2 = Server()

router.link(sv_from)
router.link(sv_from2)

router.link(Server())
router.link(Server())

sv_to = Server()
router.link(sv_to)

sv_from.send_data(Data("Hello", sv_to.get_ip()))
sv_from2.send_data(Data("Hello", sv_to.get_ip()))
sv_to.send_data(Data("Hi", sv_from.get_ip()))
router.send_data()
msg_lst_from = sv_from.get_data()
msg_lst_to = sv_to.get_data()

print(list(map(lambda x: x.data, msg_lst_from)))
print(list(map(lambda x: x.data, msg_lst_to)))
