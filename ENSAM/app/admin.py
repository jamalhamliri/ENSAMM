from django.contrib import admin

from .models import *

admin.site.register(ArticleType)
admin.site.register(Article)
admin.site.register(Slide)
admin.site.register(Photo)
admin.site.register(Gallery)


