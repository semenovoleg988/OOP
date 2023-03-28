class Application:
    def __init__(self, name) -> None:
        self.name = name
        self.blocked = False


class AppStore:
    def __init__(self) -> None:
        self.applications = {}
    
    def add_application(self, app: Application):
        self.applications[id(app)] = app 

    def remove_applicarion(self, app: Application):
        self.applications.pop(id(app))

    def block_application(self, app: Application):
        obj = self.applications.get(id(app), False)
        if not obj:
            return False
        obj.blocked = True
        return True

    def total_apps(self):
        return len(self.applications)

store = AppStore()
appYoutube = Application("YouTube")
print(store.total_apps())
store.add_application(appYoutube)
print(store.total_apps())
store.block_application(appYoutube)
store.remove_applicarion(appYoutube)
print(store.total_apps())