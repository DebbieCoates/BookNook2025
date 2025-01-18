from django.apps import AppConfig


class MemberConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'member'


class MembersConfig(AppConfig):
    name = 'members'

    def ready(self):
        import members.signals
