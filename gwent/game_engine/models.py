from django.db import models

# Create your models here.
class Cards(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=1000)
	type = models.CharField(max_length=25)
	faction_id = models.ForeignKey('Factions', to_field='id', db_column='faction_id')
	atk = models.IntegerField(null=False, blank=False)
	effect_id = models.ForeignKey('Effects', to_field='id', db_column='effect_id')
	class Meta:
		db_table = u'Cards'

class Decks(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=100)
	faction_id = models.ForeignKey('Factions', to_field='id', db_column='faction_id')
	card_list = models.CommaSeparatedIntegerField(max_length=100)
	user_id = models.ForeignKey('Users', to_field='id', db_column='user_id')
	class Meta:
		db_table = u'Decks'
	def __unicode__(self):
		return self.name

class Effects(models.Model):
	id = models.AutoField(primary_key=True)
	type = models.CharField(max_length=1000)
	class Meta:
		db_table = u'Effects'
	def __unicode__(self):
		return self.type

class Factions(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=1000)
	class Meta:
		db_table = u'Factions'
	def __unicode__(self):
		return self.name

class SessionManager(models.Model):
	id = models.AutoField(primary_key=True)
	player1_id = models.ForeignKey('Users', to_field='id', db_column='player1_id')
	player1_deck_id = models.ForeignKey('Decks', to_field='id', db_column='player1_deck_id')
	player1_siege = models.CommaSeparatedIntegerField(max_length=100)
	player1_range = models.CommaSeparatedIntegerField(max_length=100)
	player1_infantry = models.CommaSeparatedIntegerField(max_length=100)
	player1_round1 = models.IntegerField(null=False, blank=False)
	player1_round2 = models.IntegerField(null=False, blank=False)
	player1_round3 = models.IntegerField(null=False, blank=False)
	player2_id = models.ForeignKey('Users', to_field='id', db_column='player2_id')
	player2_deck_id = models.ForeignKey('Decks', to_field='id', db_column='player2_deck_id')
	player2_siege = models.CommaSeparatedIntegerField(max_length=100)
	player2_range = models.CommaSeparatedIntegerField(max_length=100)
	player2_infantry = models.CommaSeparatedIntegerField(max_length=100)
	player2_round1 = models.IntegerField(null=False, blank=False)
	player2_round2 = models.IntegerField(null=False, blank=False)
	player2_round3 = models.IntegerField(null=False, blank=False)
	class Meta:
		db_table = u'SessionManager'

class Users(models.Model):
	id = models.AutoField(primary_key=True)
	username = models.CharField(max_length=100)
	password = models.CharField(max_length=100)
	class Meta:
		db_table = u'Users'
	def __unicode__(self):
		return self.username
