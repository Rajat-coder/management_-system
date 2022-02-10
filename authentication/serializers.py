from rest_framework import serializers
from authentication.models import AssociatesMasterModel


class AssociatesMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssociatesMasterModel
        fields = "__all__"