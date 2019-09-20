from django.contrib import admin
from .models import BlogPost


@admin.register(BlogPost)
class ProductAdmin(admin.ModelAdmin):
		list_display = (
		    'title',
		    'created_date',
		    'published_date',
			'id'
		)