from rest_framework import serializers
from main.models import Tweet

class TweetSerializer(serializers.ModelSerializer):

    # user_id = serializers.SerializerMethodField(read_only=True)
    # user_name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Tweet
        fields = ('tweet_id', 'user', 'content', 'created_at')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tweet_id'].read_only = True