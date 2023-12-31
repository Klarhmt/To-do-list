from django.apps import AppConfig


class ToDoListConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'to_do_list'

    def ready(self) -> None:
        import to_do_list.signals