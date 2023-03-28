class Data:
    def __init__(self, data: str, dest_IP: int) -> None:
        self.data = data
        self.dest_IP = dest_IP

class Server:
    def __init__(self) -> None:
        self.IP = id(self)

    def send_data(data):
        """для отправки информационного пакета data(объекта класса Data)
        с указанным IP-адресом получателя(пакет отправляется роутеру и 
        сохраняется в его буфере - локальном свойстве buffer)"""
    def get_data():
        """возвращает список принятых пакетов(если ничего принято не было, 
        то возвращается пустой список) и очищает входной буфер"""
    def get_ip(self):
        return self.IP


class Router:
    routers = {}
    def __init__(self) -> None:
        self.buffer = []
    
    def link(self, server: Server):
        self.routers[server.IP] = server

    def unlink(self, server: Server):
        if self.routers.get(id(server), None):
            self.routers.pop(id(Server))
        
    def send_data(self):
        """для отправки всех пакетов(объектов класса Data) из буфера роутера 
        соответствующим серверам(после отправки буфер должен очищаться)"""
        

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
