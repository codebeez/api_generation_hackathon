import inspect
import sys

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def handle(self, *args, **options):
        # TODO: param
        models_path = "api.models"
        models_ = []
        with open(f"{models_path.split('.')[0]}/serializers.py", "w+") as f:
            for name, obj in inspect.getmembers(sys.modules[models_path]):
                if inspect.isclass(obj):
                    models_.append(obj.__name__)
            f.write("from rest_framework.serializers import ModelSerializer")
            f.write(f"\nfrom {models_path} import {', '.join(models_)}")
            for model in models_:
                f.write(
                    f"\n\nclass {model}Serializer(ModelSerializer):\n    class Meta:\n        model = {model}\n        fields = '__all__'"
                )
