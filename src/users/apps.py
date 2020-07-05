from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'src.users'

    # actstream register model
    # def ready(self):
    #     from actstream import registry
    #     registry.register(self.get_model('User'))
