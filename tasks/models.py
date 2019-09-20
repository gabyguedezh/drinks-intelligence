from django.db import models
from django.contrib.auth.models import User


# Models for the database of the pieces users can request
class Piece(models.Model):
	#Defining the options for the status multiple choice field:
	status_choices = (
		('To do', 'To do'),
		('Doing', 'Doing'),
		('Customer review', 'Customer review'),
		('Done', 'Done'),
	)
	
	piece_type_choices = (
		('Bespoke Content', 'Bespoke Content'),
		('Tastings and Events', 'Tastings and Events'),
		('Other', 'Other')
	)

	price_point = (
		('€150', '€150'),
		('€250', '€250'),
		('€500', '€500'),
		('Email', 'Email'),
	)
	
	requested_by = models.ForeignKey(User)
	subject = models.CharField(max_length=100)
	description = models.TextField(max_length=500)
	status = models.CharField(max_length=15, choices=status_choices)
	piece_type = models.CharField(max_length=20, choices=piece_type_choices)
	price_point = models.CharField(max_length=10, choices=price_point)
	
	def __str__(self):
		return 'Subject: ' + str(self.subject) + '. Requested by: ' + str(self.requested_by) + '. Type: ' + str(self.piece_type)