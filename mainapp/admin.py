from django.contrib import admin
from .models import Slider, Menu, SubMenu, Language, Context, Question
from .models import Gallery, Images, Personal, ArticleContext

admin.site.register(Slider)
admin.site.register(Menu)
admin.site.register(SubMenu)
admin.site.register(Language)
admin.site.register(Context)
admin.site.register(Question)
admin.site.register(Personal)


class ArticleContextAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('article_lan', 'title', 'title2', 'title3', 'title4')
        }),
        ('For Text', {
            'classes': ('collapse',),
            'fields': ('text1', 'text2', 'text3', 'text4', 'text5'),
        }),
        ('Images', {
            'classes': ('collapse',),
            'fields': ('image1', 'image2', 'image3', 'image4', 'image5',
             'image6', 'image7'),
        }),
    )


class ImageInline(admin.TabularInline):
    model = Images


class GalleryAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]


admin.site.register(ArticleContext, ArticleContextAdmin)
admin.site.register(Gallery, GalleryAdmin)
