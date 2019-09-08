from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'Users'

    def read(self):
        import Users.signals
