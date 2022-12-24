from rest_framework import serializers

class OtpVerifyRequest(serializers.Serializer):
    otp = serializers.IntegerField()
    email = serializers.CharField(max_length = 100)