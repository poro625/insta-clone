from django.contrib import admin
from .models import TweetComment, Feed
# Register your models here.


admin.site.register(Feed)
admin.site.register(TweetComment)