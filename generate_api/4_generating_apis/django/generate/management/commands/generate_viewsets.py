import inspect
import sys

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def handle(self, *args, **options):
        # TODO: param
        models_path = "api.models"
        module = models_path.split(".")[0]
        models_ = []
        with open(f"{module}/views.py", "w+") as f:
            for name, obj in inspect.getmembers(sys.modules[models_path]):
                if inspect.isclass(obj):
                    models_.append(obj.__name__)
            f.write("from rest_framework.viewsets import ModelViewSet")
            f.write(f"\nfrom {models_path} import {', '.join(models_)}")
            f.write(
                f"\nfrom {module}.serializers import {'Serializer, '.join(models_)}Serializer"
            )
            for model in models_:
                f.write(
                    f"\n\nclass {model}ViewSet(ModelViewSet):\n    queryset = {model}.objects.all()\n    serializer_class = {model}Serializer"
                )

        with open(f"{module}/urls.py", "w+") as f:
            f.write("from rest_framework import routers\n")
            f.write(f"from {module}.views import {'ViewSet, '.join(models_)}ViewSet")
            f.write(f"\n\nrouter = routers.SimpleRouter()")
            for model in models_:
                f.write(f"\nrouter.register(r'{model.lower()}', {model}ViewSet)")

            f.write(f"\n\nurlpatterns = router.urls")
