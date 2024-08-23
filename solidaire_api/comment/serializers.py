from rest_framework import serializers
from solidaire_content.models import Comment
from solidaire_api.user.serializers import UserPublicSerializer

class CommentSerializer(serializers.ModelSerializer):
    
    owner = UserPublicSerializer(read_only=True)
    
    