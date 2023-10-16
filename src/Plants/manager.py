from django.db.models.manager import Manager

class UsersManager(Manager):
    
    def get_list(self):
        client_list = []
        clients = self.all()
        for client in clients:
            client_list.append(self.create_schema(client))
        return 200, client_list
