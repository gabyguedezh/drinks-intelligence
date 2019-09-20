from django.contrib import admin
from .models import Piece


@admin.register(Piece)
class ProductAdmin(admin.ModelAdmin):
		list_display = (
		    'requested_by',
		    'subject',
		    'piece_type',
			'status',
			'id'
		)
		list_select_related = (
			'requested_by',
		)