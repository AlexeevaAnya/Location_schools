# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Skola(models.Model):
    number = models.TextField(blank=True, null=True)
    commun = models.TextField(blank=True, null=True)
    code = models.IntegerField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    typ_av_huvudman = models.TextField(db_column='Typ av huvudman', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    grund_skola = models.TextField(db_column='Grund-skola', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    förskole_klass = models.TextField(db_column='Förskole-klass', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fritids_hem = models.TextField(db_column='Fritids-hem', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    grund_särskola = models.TextField(db_column='Grund-särskola', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    same_skola = models.TextField(db_column='Same-skola', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gymna_sieskola = models.TextField(db_column='Gymna-sieskola', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gymna_siesär_skola = models.TextField(db_column='Gymna-siesär-skola', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    kommu_nal_vuxenut_bildning = models.TextField(db_column='Kommu-nal vuxenut-bildning', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    svenska_för_invand_rare = models.TextField(db_column='Svenska för invand-rare', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    särskola_för_vuxna = models.TextField(db_column='Särskola för vuxna', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    special_skola = models.TextField(db_column='Special-skola', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    central_insamlings_enhet_för_elever_huvudman = models.TextField(db_column='Central insamlings-enhet för elever / huvudman', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    central_insamlings_enhet_för_personal_huvudman = models.TextField(db_column='Central insamlings-enhet för personal / huvudman', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.


    def __str__(self):
        return self.number +" "+self.commun +" "+self.name

    class Meta:
        managed = False
        db_table = 'skola'
