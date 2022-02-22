from rest_framework import serializers
from bluehaven.models import Bluehaven


class BluehavenSerailizer(serializers.ModelSerializer):
    class Meta:
        model=Bluehaven
        fields=("company","net_investment","year")