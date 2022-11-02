from django.contrib import admin
from article.models  import Article, Comment
from django_summernote.admin import SummernoteModelAdmin

class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('body',)

admin.site.register(Article, PostAdmin)
admin.site.register(Comment)



