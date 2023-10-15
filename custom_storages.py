from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage

class StaticStorage(S3Boto3Storage):
    # Directs the location for static files storage 
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    # Directs the location for media files storage
    location = settings.MEDIAFILES_LOCATION