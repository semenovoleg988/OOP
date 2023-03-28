# здесь объявляются все необходимые классы
class Graph:
    def __init__(self, data: list) -> None:
        self.data = data[:]
        self.is_show  = True

    def set_data(self, data: list):
        self.data = data[:]
    
    def _get_str_data(self):
        return " ".join(map(str, self.data))

    def _show_is_opened_graph(self) -> bool:
        if self.is_show == False:
            print("Відображення данних закрито!")
            return False
        return True
        
    def show_table(self):
        if self._show_is_opened_graph():
            print(self._get_str_data())

    def show_graph(self):
        if self._show_is_opened_graph():
            print(f"Графічне відображення данних: {self._get_str_data()}")
    
    def show_bar(self):
        if self._show_is_opened_graph():
            print(f"Стовбчата діаграма: {self._get_str_data()}")

    def set_show(self, fl_show: bool):
        self.is_show = fl_show

# считывание списка из входного потока (эту строку не менять)
data_graph = list(map(int, input().split()))

# здесь создаются объекты классов и вызываются нужные методы
gr = Graph(data_graph)

gr.show_graph()
gr.show_bar()
#gr.set_show(False)
gr.show_table()

