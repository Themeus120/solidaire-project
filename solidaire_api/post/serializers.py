from rest_framework import serializers
from solidaire_content.models import Post
from solidaire_api.user.serializers import UserPublicSerializer

class PostSerilizer(serializers.ModelSerializer):
    
    owner = UserPublicSerializer()
    
    class Meta:
        model = Post
        fields = [
            "id",
            "uuid",
            "title",
            "owner",
            "body",
            "status",
            "created_at",
        ]
        
        read_only_fields = [
            "id",
            "uuid",
            "owner",
            "created_at",
        ]