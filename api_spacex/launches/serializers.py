from rest_framework import serializers

class FirstStageSerializer(serializers.Serializer):
    rocket_name = serializers.CharField()
    is_reused = serializers.BooleanField(allow_null=True)
    land_success = serializers.BooleanField(allow_null=True)
    landing_intent = serializers.BooleanField(allow_null=True)

class SecondStageSerializer(serializers.Serializer):
    costumers = serializers.ListField()
    nationality = serializers.CharField()
    manufacturer = serializers.CharField()

class RocketSerializer(serializers.Serializer):
    first_stage = FirstStageSerializer()
    second_stage = SecondStageSerializer()

class APISerializer(serializers.Serializer):
    mission_name = serializers.CharField()
    flight_number = serializers.IntegerField()
    launch_year = serializers.IntegerField()
    launch_date_utc = serializers.DateTimeField()
    rocket = RocketSerializer()
    launch_success = serializers.BooleanField(allow_null=True)
    launch_site = serializers.CharField()
    imgs = serializers.ListField()
    img_mission_patch = serializers.CharField(allow_null=True)
    video_link = serializers.CharField(allow_null=True)
    reddit_link = serializers.CharField(allow_null=True)
    details = serializers.CharField()
