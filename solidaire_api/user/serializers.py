from rest_framework import serializers
from solidaire_auth.models import User

class UserPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "bio",
        ]