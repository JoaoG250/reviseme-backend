from rest_framework import serializers

from topic.models import Topic, TopicFile, TopicRevision


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = "__all__"


class TopicFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopicFile
        fields = "__all__"


class TopicRevisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopicRevision
        fields = "__all__"
