#!/usr/bin/env python3
from Sansa import models
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        models = models.UserProfile
        fields = ('url','email','name','is_staff')


class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        models = models.Asset
        depth = 2
        fields = ('url','sn','asset_type','manufactory','name','create_date')




class ManufactorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        models = models.Manufactory
        fields = ('url','manufactory','support_num','memo')




