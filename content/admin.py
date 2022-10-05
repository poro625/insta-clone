from django.contrib import admin
from .models import TaggedFeed, TweetComment, Feed

admin.site.register(Feed)
admin.site.register(TweetComment)
admin.site.register(TaggedFeed)


# Register your models here.
