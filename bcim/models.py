# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib.gis.db import models


class EdifPubMilitar(models.Model):
    gid = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaa = models.CharField(max_length=4, blank=True, null=True)
    tipoedifmi = models.CharField(max_length=26, blank=True, null=True)
    tipousoedi = models.CharField(max_length=21, blank=True, null=True)
    situacaofi = models.CharField(max_length=80, blank=True, null=True)
    operaciona = models.CharField(max_length=12, blank=True, null=True)
    matconstr = models.CharField(max_length=18, blank=True, null=True)
    id_produto = models.IntegerField(blank=True, null=True)
    id_element = models.IntegerField(blank=True, null=True)
    cd_insumo_field = models.IntegerField(db_column='cd_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insumo_field = models.IntegerField(db_column='nr_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insum_1 = models.IntegerField(blank=True, null=True)
    tx_insumo_field = models.CharField(db_column='tx_insumo_', max_length=60, blank=True, null=True)  # Field renamed because it ended with '_'.
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'adm_edif_pub_militar_a'


class AdmEdifPubMilitarP(models.Model):
    gid = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaa = models.CharField(max_length=4, blank=True, null=True)
    tipoedifmi = models.CharField(max_length=26, blank=True, null=True)
    tipousoedi = models.CharField(max_length=21, blank=True, null=True)
    situacaofi = models.CharField(max_length=80, blank=True, null=True)
    operaciona = models.CharField(max_length=12, blank=True, null=True)
    matconstr = models.CharField(max_length=18, blank=True, null=True)
    id_produto = models.IntegerField(blank=True, null=True)
    id_element = models.IntegerField(blank=True, null=True)
    cd_insumo_field = models.IntegerField(db_column='cd_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insumo_field = models.IntegerField(db_column='nr_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insum_1 = models.IntegerField(blank=True, null=True)
    tx_insumo_field = models.CharField(db_column='tx_insumo_', max_length=60, blank=True, null=True)  # Field renamed because it ended with '_'.
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'adm_edif_pub_militar_p'


class PostoFiscal(models.Model):
    gid = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaa = models.CharField(max_length=4, blank=True, null=True)
    operaciona = models.CharField(max_length=12, blank=True, null=True)
    situacaofi = models.CharField(max_length=80, blank=True, null=True)
    tipopostof = models.CharField(max_length=22, blank=True, null=True)
    id_produto = models.IntegerField(blank=True, null=True)
    id_element = models.IntegerField(blank=True, null=True)
    cd_insumo_field = models.IntegerField(db_column='cd_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insumo_field = models.IntegerField(db_column='nr_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insum_1 = models.IntegerField(blank=True, null=True)
    tx_insumo_field = models.CharField(db_column='tx_insumo_', max_length=60, blank=True, null=True)  # Field renamed because it ended with '_'.
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'adm_posto_fiscal_p'


class EdifAgropecExtVegetalPesca(models.Model):
    gid = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaa = models.CharField(max_length=4, blank=True, null=True)
    operaciona = models.CharField(max_length=12, blank=True, null=True)
    situacaofi = models.CharField(max_length=80, blank=True, null=True)
    tipoedifag = models.CharField(max_length=50, blank=True, null=True)
    matconstr = models.CharField(max_length=18, blank=True, null=True)
    id_produto = models.IntegerField(blank=True, null=True)
    id_element = models.IntegerField(blank=True, null=True)
    cd_insumo_field = models.IntegerField(db_column='cd_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insumo_field = models.IntegerField(db_column='nr_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insum_1 = models.IntegerField(blank=True, null=True)
    tx_insumo_field = models.CharField(db_column='tx_insumo_', max_length=60, blank=True, null=True)  # Field renamed because it ended with '_'.
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eco_edif_agropec_ext_vegetal_pesca_p'


class ExtMineralA(models.Model):
    gid = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaa = models.CharField(max_length=3, blank=True, null=True)
    tiposecaoc = models.CharField(max_length=50, blank=True, null=True)
    operaciona = models.CharField(max_length=12, blank=True, null=True)
    situacaofi = models.CharField(max_length=80, blank=True, null=True)
    tipoextmin = models.CharField(max_length=20, blank=True, null=True)
    tipoprodut = models.CharField(max_length=40, blank=True, null=True)
    tipopocomi = models.CharField(max_length=15, blank=True, null=True)
    procextrac = models.CharField(max_length=12, blank=True, null=True)
    formaextra = models.CharField(max_length=12, blank=True, null=True)
    atividade = models.CharField(max_length=12, blank=True, null=True)
    id_produto = models.IntegerField(blank=True, null=True)
    id_element = models.IntegerField(blank=True, null=True)
    cd_insumo_field = models.IntegerField(db_column='cd_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insumo_field = models.IntegerField(db_column='nr_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insum_1 = models.IntegerField(blank=True, null=True)
    tx_insumo_field = models.CharField(db_column='tx_insumo_', max_length=60, blank=True, null=True)  # Field renamed because it ended with '_'.
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eco_ext_mineral_a'


class ExtMineralP(models.Model):
    gid = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaa = models.CharField(max_length=4, blank=True, null=True)
    tiposecaoc = models.CharField(max_length=50, blank=True, null=True)
    operaciona = models.CharField(max_length=12, blank=True, null=True)
    situacaofi = models.CharField(max_length=80, blank=True, null=True)
    tipoextmin = models.CharField(max_length=20, blank=True, null=True)
    tipoprodut = models.CharField(max_length=40, blank=True, null=True)
    tipopocomi = models.CharField(max_length=15, blank=True, null=True)
    procextrac = models.CharField(max_length=12, blank=True, null=True)
    formaextra = models.CharField(max_length=12, blank=True, null=True)
    atividade = models.CharField(max_length=12, blank=True, null=True)
    id_produto = models.IntegerField(blank=True, null=True)
    id_element = models.IntegerField(blank=True, null=True)
    cd_insumo_field = models.IntegerField(db_column='cd_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insumo_field = models.IntegerField(db_column='nr_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insum_1 = models.IntegerField(blank=True, null=True)
    tx_insumo_field = models.CharField(db_column='tx_insumo_', max_length=60, blank=True, null=True)  # Field renamed because it ended with '_'.
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eco_ext_mineral_p'


class EstGeradEnergiaEletrica(models.Model):
    gid = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaa = models.CharField(max_length=4, blank=True, null=True)
    codigoesta = models.CharField(max_length=30, blank=True, null=True)
    potenciaou = models.IntegerField(blank=True, null=True)
    potenciafi = models.IntegerField(blank=True, null=True)
    operaciona = models.CharField(max_length=12, blank=True, null=True)
    situacaofi = models.CharField(max_length=80, blank=True, null=True)
    tipoestger = models.CharField(max_length=15, blank=True, null=True)
    destenerge = models.CharField(max_length=56, blank=True, null=True)
    id_produto = models.IntegerField(blank=True, null=True)
    id_element = models.IntegerField(blank=True, null=True)
    cd_insumo_field = models.IntegerField(db_column='cd_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insumo_field = models.IntegerField(db_column='nr_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insum_1 = models.IntegerField(blank=True, null=True)
    tx_insumo_field = models.CharField(db_column='tx_insumo_', max_length=60, blank=True, null=True)  # Field renamed because it ended with '_'.
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enc_est_gerad_energia_eletrica_p'


class Hidreletrica(models.Model):
    gid = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaa = models.CharField(max_length=4, blank=True, null=True)
    potenciaou = models.IntegerField(blank=True, null=True)
    potenciafi = models.IntegerField(blank=True, null=True)
    codigohidr = models.CharField(max_length=30, blank=True, null=True)
    operaciona = models.CharField(max_length=12, blank=True, null=True)
    situacaofi = models.CharField(max_length=80, blank=True, null=True)
    id_produto = models.IntegerField(blank=True, null=True)
    id_element = models.IntegerField(blank=True, null=True)
    cd_insumo_field = models.IntegerField(db_column='cd_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insumo_field = models.IntegerField(db_column='nr_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insum_1 = models.IntegerField(blank=True, null=True)
    tx_insumo_field = models.CharField(db_column='tx_insumo_', max_length=60, blank=True, null=True)  # Field renamed because it ended with '_'.
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enc_hidreletrica_p'


class Termeletrica(models.Model):
    gid = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaa = models.CharField(max_length=3, blank=True, null=True)
    potenciaou = models.IntegerField(blank=True, null=True)
    potenciafi = models.IntegerField(blank=True, null=True)
    combrenova = models.CharField(max_length=3, blank=True, null=True)
    tipomaqter = models.CharField(max_length=33, blank=True, null=True)
    geracao = models.CharField(max_length=20, blank=True, null=True)
    tipocombus = models.CharField(max_length=17, blank=True, null=True)
    operaciona = models.CharField(max_length=12, blank=True, null=True)
    situacaofi = models.CharField(max_length=80, blank=True, null=True)
    id_produto = models.IntegerField(blank=True, null=True)
    id_element = models.IntegerField(blank=True, null=True)
    cd_insumo_field = models.IntegerField(db_column='cd_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insumo_field = models.IntegerField(db_column='nr_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insum_1 = models.IntegerField(blank=True, null=True)
    tx_insumo_field = models.CharField(db_column='tx_insumo_', max_length=60, blank=True, null=True)  # Field renamed because it ended with '_'.
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enc_termeletrica_p'


class BancoAreia(models.Model):
    gid = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaa = models.CharField(max_length=4, blank=True, null=True)
    tipobanco = models.CharField(max_length=15, blank=True, null=True)
    situacaoem = models.CharField(max_length=17, blank=True, null=True)
    materialpr = models.CharField(max_length=27, blank=True, null=True)
    id_produto = models.IntegerField(blank=True, null=True)
    id_element = models.IntegerField(blank=True, null=True)
    cd_insumo_field = models.IntegerField(db_column='cd_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insumo_field = models.IntegerField(db_column='nr_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insum_1 = models.IntegerField(blank=True, null=True)
    tx_insumo_field = models.CharField(db_column='tx_insumo_', max_length=60, blank=True, null=True)  # Field renamed because it ended with '_'.
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hid_banco_areia_a'


class BarragemL(models.Model):
    gid = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaa = models.CharField(max_length=4, blank=True, null=True)
    matconstr = models.CharField(max_length=18, blank=True, null=True)
    usoprincip = models.CharField(max_length=15, blank=True, null=True)
    operaciona = models.CharField(max_length=12, blank=True, null=True)
    situacaofi = models.CharField(max_length=80, blank=True, null=True)
    id_produto = models.IntegerField(blank=True, null=True)
    id_element = models.IntegerField(blank=True, null=True)
    cd_insumo_field = models.IntegerField(db_column='cd_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insumo_field = models.IntegerField(db_column='nr_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insum_1 = models.IntegerField(blank=True, null=True)
    tx_insumo_field = models.CharField(db_column='tx_insumo_', max_length=60, blank=True, null=True)  # Field renamed because it ended with '_'.
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hid_barragem_l'


class BarragemP(models.Model):
    gid = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaa = models.CharField(max_length=3, blank=True, null=True)
    matconstr = models.CharField(max_length=18, blank=True, null=True)
    usoprincip = models.CharField(max_length=15, blank=True, null=True)
    operaciona = models.CharField(max_length=12, blank=True, null=True)
    situacaofi = models.CharField(max_length=80, blank=True, null=True)
    id_produto = models.IntegerField(blank=True, null=True)
    id_element = models.IntegerField(blank=True, null=True)
    cd_insumo_field = models.IntegerField(db_column='cd_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insumo_field = models.IntegerField(db_column='nr_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insum_1 = models.IntegerField(blank=True, null=True)
    tx_insumo_field = models.CharField(db_column='tx_insumo_', max_length=60, blank=True, null=True)  # Field renamed because it ended with '_'.
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hid_barragem_p'


class CorredeiraL(models.Model):
    gid = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaa = models.CharField(max_length=4, blank=True, null=True)
    id_produto = models.IntegerField(blank=True, null=True)
    id_element = models.IntegerField(blank=True, null=True)
    cd_insumo_field = models.IntegerField(db_column='cd_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insumo_field = models.IntegerField(db_column='nr_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insum_1 = models.IntegerField(blank=True, null=True)
    tx_insumo_field = models.CharField(db_column='tx_insumo_', max_length=60, blank=True, null=True)  # Field renamed because it ended with '_'.
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hid_corredeira_l'


class CorredeiraP(models.Model):
    gid = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaa = models.CharField(max_length=4, blank=True, null=True)
    id_produto = models.IntegerField(blank=True, null=True)
    id_element = models.IntegerField(blank=True, null=True)
    cd_insumo_field = models.IntegerField(db_column='cd_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insumo_field = models.IntegerField(db_column='nr_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insum_1 = models.IntegerField(blank=True, null=True)
    tx_insumo_field = models.CharField(db_column='tx_insumo_', max_length=60, blank=True, null=True)  # Field renamed because it ended with '_'.
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hid_corredeira_p'


class Ilha(models.Model):
    gid = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaa = models.CharField(max_length=4, blank=True, null=True)
    tipoilha = models.CharField(max_length=9, blank=True, null=True)
    id_produto = models.IntegerField(blank=True, null=True)
    id_element = models.IntegerField(blank=True, null=True)
    cd_insumo_field = models.IntegerField(db_column='cd_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insumo_field = models.IntegerField(db_column='nr_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insum_1 = models.IntegerField(blank=True, null=True)
    tx_insumo_field = models.CharField(db_column='tx_insumo_', max_length=60, blank=True, null=True)  # Field renamed because it ended with '_'.
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hid_ilha_a'


class MassaDagua(models.Model):
    gid = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaa = models.CharField(max_length=4, blank=True, null=True)
    tipomassad = models.CharField(max_length=18, blank=True, null=True)
    salinidade = models.CharField(max_length=16, blank=True, null=True)
    regime = models.CharField(max_length=31, blank=True, null=True)
    id_produto = models.IntegerField(blank=True, null=True)
    id_element = models.IntegerField(blank=True, null=True)
    cd_insumo_field = models.IntegerField(db_column='cd_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insumo_field = models.IntegerField(db_column='nr_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insum_1 = models.IntegerField(blank=True, null=True)
    tx_insumo_field = models.CharField(db_column='tx_insumo_', max_length=60, blank=True, null=True)  # Field renamed because it ended with '_'.
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hid_massa_dagua_a'


class QuedaDagua(models.Model):
    gid = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaa = models.CharField(max_length=4, blank=True, null=True)
    altura = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    tipoqueda = models.CharField(max_length=15, blank=True, null=True)
    id_produto = models.IntegerField(blank=True, null=True)
    id_element = models.IntegerField(blank=True, null=True)
    cd_insumo_field = models.IntegerField(db_column='cd_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insumo_field = models.IntegerField(db_column='nr_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insum_1 = models.IntegerField(blank=True, null=True)
    tx_insumo_field = models.CharField(db_column='tx_insumo_', max_length=60, blank=True, null=True)  # Field renamed because it ended with '_'.
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hid_queda_dagua_l'


class Recife(models.Model):
    gid = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaa = models.CharField(max_length=4, blank=True, null=True)
    tiporecife = models.CharField(max_length=16, blank=True, null=True)
    situamare = models.CharField(max_length=35, blank=True, null=True)
    situacaoco = models.CharField(max_length=12, blank=True, null=True)
    id_produto = models.IntegerField(blank=True, null=True)
    id_element = models.IntegerField(blank=True, null=True)
    cd_insumo_field = models.IntegerField(db_column='cd_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insumo_field = models.IntegerField(db_column='nr_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insum_1 = models.IntegerField(blank=True, null=True)
    tx_insumo_field = models.CharField(db_column='tx_insumo_', max_length=60, blank=True, null=True)  # Field renamed because it ended with '_'.
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hid_recife_a'


class RochaEmAgua(models.Model):
    gid = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaa = models.CharField(max_length=4, blank=True, null=True)
    alturalami = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    situacaoem = models.CharField(max_length=17, blank=True, null=True)
    id_produto = models.IntegerField(blank=True, null=True)
    id_element = models.IntegerField(blank=True, null=True)
    cd_insumo_field = models.IntegerField(db_column='cd_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insumo_field = models.IntegerField(db_column='nr_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insum_1 = models.IntegerField(blank=True, null=True)
    tx_insumo_field = models.CharField(db_column='tx_insumo_', max_length=60, blank=True, null=True)  # Field renamed because it ended with '_'.
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hid_rocha_em_agua_a'


class SumidouroVertedouro(models.Model):
    gid = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaa = models.CharField(max_length=4, blank=True, null=True)
    causa = models.CharField(max_length=25, blank=True, null=True)
    tiposumver = models.CharField(max_length=12, blank=True, null=True)
    id_produto = models.IntegerField(blank=True, null=True)
    id_element = models.IntegerField(blank=True, null=True)
    cd_insumo_field = models.IntegerField(db_column='cd_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insumo_field = models.IntegerField(db_column='nr_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insum_1 = models.IntegerField(blank=True, null=True)
    tx_insumo_field = models.CharField(db_column='tx_insumo_', max_length=60, blank=True, null=True)  # Field renamed because it ended with '_'.
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hid_sumidouro_vertedouro_p'


class TerrenoSujeitoInundacao(models.Model):
    gid = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaa = models.CharField(max_length=4, blank=True, null=True)
    periodicid = models.CharField(max_length=20, blank=True, null=True)
    id_produto = models.IntegerField(blank=True, null=True)
    id_element = models.IntegerField(blank=True, null=True)
    cd_insumo_field = models.IntegerField(db_column='cd_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insumo_field = models.IntegerField(db_column='nr_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insum_1 = models.IntegerField(blank=True, null=True)
    tx_insumo_field = models.CharField(db_column='tx_insumo_', max_length=60, blank=True, null=True)  # Field renamed because it ended with '_'.
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hid_terreno_sujeito_inundacao_a'


class TrechoDrenagem(models.Model):
    gid = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaa = models.CharField(max_length=4, blank=True, null=True)
    dentrodepo = models.CharField(max_length=4, blank=True, null=True)
    compartilh = models.CharField(max_length=4, blank=True, null=True)
    eixoprinci = models.CharField(max_length=4, blank=True, null=True)
    caladomax = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    larguramed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    velocidade = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    profundida = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    coincideco = models.CharField(max_length=35, blank=True, null=True)
    navegabili = models.CharField(max_length=16, blank=True, null=True)
    regime = models.CharField(max_length=31, blank=True, null=True)
    id_produto = models.IntegerField(blank=True, null=True)
    id_element = models.IntegerField(blank=True, null=True)
    cd_insumo_field = models.IntegerField(db_column='cd_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insumo_field = models.IntegerField(db_column='nr_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insum_1 = models.IntegerField(blank=True, null=True)
    tx_insumo_field = models.CharField(db_column='tx_insumo_', max_length=60, blank=True, null=True)  # Field renamed because it ended with '_'.
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hid_trecho_drenagem_l'


class TrechoMassaDagua(models.Model):
    gid = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaa = models.CharField(max_length=4, blank=True, null=True)
    tipotrecho = models.CharField(max_length=14, blank=True, null=True)
    salinidade = models.CharField(max_length=16, blank=True, null=True)
    regime = models.CharField(max_length=31, blank=True, null=True)
    id_produto = models.IntegerField(blank=True, null=True)
    id_element = models.IntegerField(blank=True, null=True)
    cd_insumo_field = models.IntegerField(db_column='cd_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insumo_field = models.IntegerField(db_column='nr_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insum_1 = models.IntegerField(blank=True, null=True)
    tx_insumo_field = models.CharField(db_column='tx_insumo_', max_length=60, blank=True, null=True)  # Field renamed because it ended with '_'.
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hid_trecho_massa_dagua_a'


class Municipio(models.Model):
    gid = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaa = models.CharField(max_length=3, blank=True, null=True)
    geocodigo = models.CharField(max_length=15, blank=True, null=True)
    anoderefer = models.IntegerField(blank=True, null=True)
    id_produto = models.IntegerField(blank=True, null=True)
    id_element = models.IntegerField(blank=True, null=True)
    cd_insumo_field = models.IntegerField(db_column='cd_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insumo_field = models.IntegerField(db_column='nr_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insum_1 = models.IntegerField(blank=True, null=True)
    tx_insumo_field = models.CharField(db_column='tx_insumo_', max_length=60, blank=True, null=True)  # Field renamed because it ended with '_'.
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lim_municipio_a'


class OutrosLimitesOficiais(models.Model):
    gid = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaa = models.CharField(max_length=4, blank=True, null=True)
    coincideco = models.CharField(max_length=50, blank=True, null=True)
    extensao = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    obssituaca = models.CharField(max_length=100, blank=True, null=True)
    tipooutlim = models.CharField(max_length=50, blank=True, null=True)
    id_produto = models.IntegerField(blank=True, null=True)
    id_element = models.IntegerField(blank=True, null=True)
    cd_insumo_field = models.IntegerField(db_column='cd_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insumo_field = models.IntegerField(db_column='nr_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insum_1 = models.IntegerField(blank=True, null=True)
    tx_insumo_field = models.CharField(db_column='tx_insumo_', max_length=60, blank=True, null=True)  # Field renamed because it ended with '_'.
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lim_outros_limites_oficiais_l'


class Pais(models.Model):
    gid = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaa = models.CharField(max_length=4, blank=True, null=True)
    sigla = models.CharField(max_length=3, blank=True, null=True)
    codiso3166 = models.CharField(max_length=3, blank=True, null=True)
    id_produto = models.IntegerField(blank=True, null=True)
    id_element = models.IntegerField(blank=True, null=True)
    cd_insumo_field = models.IntegerField(db_column='cd_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insumo_field = models.IntegerField(db_column='nr_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insum_1 = models.IntegerField(blank=True, null=True)
    tx_insumo_field = models.CharField(db_column='tx_insumo_', max_length=60, blank=True, null=True)  # Field renamed because it ended with '_'.
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lim_pais_a'


class TerraIndigenaA(models.Model):
    gid = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaa = models.CharField(max_length=4, blank=True, null=True)
    perimetroo = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    areaoficia = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    grupoetnic = models.CharField(max_length=100, blank=True, null=True)
    datasituac = models.CharField(max_length=20, blank=True, null=True)
    situacaoju = models.CharField(max_length=23, blank=True, null=True)
    nometi = models.CharField(max_length=100, blank=True, null=True)
    id_produto = models.IntegerField(blank=True, null=True)
    id_element = models.IntegerField(blank=True, null=True)
    codigofuna = models.IntegerField(blank=True, null=True)
    cd_insumo_field = models.IntegerField(db_column='cd_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insumo_field = models.IntegerField(db_column='nr_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insum_1 = models.IntegerField(blank=True, null=True)
    tx_insumo_field = models.CharField(db_column='tx_insumo_', max_length=60, blank=True, null=True)  # Field renamed because it ended with '_'.
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lim_terra_indigena_a'


class TerraIndigenaP(models.Model):
    gid = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaa = models.CharField(max_length=4, blank=True, null=True)
    perimetroo = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    areaoficia = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    grupoetnic = models.CharField(max_length=100, blank=True, null=True)
    datasituac = models.CharField(max_length=20, blank=True, null=True)
    situacaoju = models.CharField(max_length=23, blank=True, null=True)
    nometi = models.CharField(max_length=100, blank=True, null=True)
    id_produto = models.IntegerField(blank=True, null=True)
    id_element = models.IntegerField(blank=True, null=True)
    codigofuna = models.IntegerField(blank=True, null=True)
    cd_insumo_field = models.IntegerField(db_column='cd_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insumo_field = models.IntegerField(db_column='nr_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insum_1 = models.IntegerField(blank=True, null=True)
    tx_insumo_field = models.CharField(db_column='tx_insumo_', max_length=60, blank=True, null=True)  # Field renamed because it ended with '_'.
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lim_terra_indigena_p'


class UnidadeConservacaoNaoSnuc(models.Model):
    gid = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaa = models.CharField(max_length=4, blank=True, null=True)
    anocriacao = models.IntegerField(blank=True, null=True)
    sigla = models.CharField(max_length=6, blank=True, null=True)
    areaoficia = models.CharField(max_length=15, blank=True, null=True)
    administra = models.CharField(max_length=80, blank=True, null=True)
    classifica = models.CharField(max_length=100, blank=True, null=True)
    atolegal = models.CharField(max_length=100, blank=True, null=True)
    id_produto = models.IntegerField(blank=True, null=True)
    id_element = models.IntegerField(blank=True, null=True)
    cd_insumo_field = models.IntegerField(db_column='cd_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insumo_field = models.IntegerField(db_column='nr_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insum_1 = models.IntegerField(blank=True, null=True)
    tx_insumo_field = models.CharField(db_column='tx_insumo_', max_length=60, blank=True, null=True)  # Field renamed because it ended with '_'.
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lim_unidade_conservacao_nao_snuc_a'


class UnidadeFederacao(models.Model):
    gid = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaa = models.CharField(max_length=3, blank=True, null=True)
    sigla = models.CharField(max_length=3, blank=True, null=True)
    geocodigo = models.CharField(max_length=15, blank=True, null=True)
    id_produto = models.IntegerField(blank=True, null=True)
    id_element = models.IntegerField(blank=True, null=True)
    cd_insumo_field = models.IntegerField(db_column='cd_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insumo_field = models.IntegerField(db_column='nr_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insum_1 = models.IntegerField(blank=True, null=True)
    tx_insumo_field = models.CharField(db_column='tx_insumo_', max_length=60, blank=True, null=True)  # Field renamed because it ended with '_'.
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lim_unidade_federacao_a'


class UnidadeProtecaoIntegral(models.Model):
    gid = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaa = models.CharField(max_length=4, blank=True, null=True)
    anocriacao = models.IntegerField(blank=True, null=True)
    sigla = models.CharField(max_length=6, blank=True, null=True)
    areaoficia = models.CharField(max_length=15, blank=True, null=True)
    administra = models.CharField(max_length=80, blank=True, null=True)
    atolegal = models.CharField(max_length=100, blank=True, null=True)
    tipounidpr = models.CharField(max_length=100, blank=True, null=True)
    id_produto = models.IntegerField(blank=True, null=True)
    id_element = models.IntegerField(blank=True, null=True)
    cd_insumo_field = models.IntegerField(db_column='cd_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insumo_field = models.IntegerField(db_column='nr_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insum_1 = models.IntegerField(blank=True, null=True)
    tx_insumo_field = models.CharField(db_column='tx_insumo_', max_length=60, blank=True, null=True)  # Field renamed because it ended with '_'.
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lim_unidade_protecao_integral_a'


class UnidadeUsoSustentavel(models.Model):
    gid = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaa = models.CharField(max_length=4, blank=True, null=True)
    anocriacao = models.IntegerField(blank=True, null=True)
    sigla = models.CharField(max_length=6, blank=True, null=True)
    areaoficia = models.CharField(max_length=15, blank=True, null=True)
    administra = models.CharField(max_length=80, blank=True, null=True)
    atolegal = models.CharField(max_length=100, blank=True, null=True)
    tipounidus = models.CharField(max_length=100, blank=True, null=True)
    id_produto = models.IntegerField(blank=True, null=True)
    id_element = models.IntegerField(blank=True, null=True)
    cd_insumo_field = models.IntegerField(db_column='cd_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insumo_field = models.IntegerField(db_column='nr_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insum_1 = models.IntegerField(blank=True, null=True)
    tx_insumo_field = models.CharField(db_column='tx_insumo_', max_length=60, blank=True, null=True)  # Field renamed because it ended with '_'.
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lim_unidade_uso_sustentavel_a'


class AglomeradoRuralIsolado(models.Model):
    gid = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaa = models.CharField(max_length=4, blank=True, null=True)
    tipoaglomr = models.CharField(max_length=35, blank=True, null=True)
    id_produto = models.IntegerField(blank=True, null=True)
    id_element = models.IntegerField(blank=True, null=True)
    cd_insumo_field = models.IntegerField(db_column='cd_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insumo_field = models.IntegerField(db_column='nr_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insum_1 = models.IntegerField(blank=True, null=True)
    tx_insumo_field = models.CharField(db_column='tx_insumo_', max_length=60, blank=True, null=True)  # Field renamed because it ended with '_'.
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'loc_aglomerado_rural_isolado_p'

# Identificador de metadados: fa86e58d-eb04-47f9-8f46-54406a0ca432
# http://www.metadados.geo.ibge.gov.br/geonetwork_ibge/srv/por/metadata.show?id=21723&currTab=simple
# ET-EDGV http://www.geoportal.eb.mil.br/images/PDF/EDGV_DEFESA_F_Ter_2a_Edicao_2016_Aprovada_Publicada_BE_7_16.pdf
class AldeiaIndigena(models.Model):
    gid = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaa = models.CharField(max_length=4, blank=True, null=True)
    codigofuna = models.CharField(max_length=15, blank=True, null=True)
    terraindig = models.CharField(max_length=100, blank=True, null=True)
    etnia = models.CharField(max_length=100, blank=True, null=True)
    id_produto = models.IntegerField(blank=True, null=True)
    id_element = models.IntegerField(blank=True, null=True)
    cd_insumo_field = models.IntegerField(db_column='cd_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insumo_field = models.IntegerField(db_column='nr_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insum_1 = models.IntegerField(blank=True, null=True)
    tx_insumo_field = models.CharField(db_column='tx_insumo_', max_length=60, blank=True, null=True)  # Field renamed because it ended with '_'.
    geom = models.PointField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'loc_aldeia_indigena_p'


class AreaEdificada(models.Model):
    gid = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaa = models.CharField(max_length=4, blank=True, null=True)
    geocodigo = models.CharField(max_length=15, blank=True, null=True)
    id_produto = models.IntegerField(blank=True, null=True)
    id_element = models.IntegerField(blank=True, null=True)
    cd_insumo_field = models.IntegerField(db_column='cd_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insumo_field = models.IntegerField(db_column='nr_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insum_1 = models.IntegerField(blank=True, null=True)
    tx_insumo_field = models.CharField(db_column='tx_insumo_', max_length=60, blank=True, null=True)  # Field renamed because it ended with '_'.
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'loc_area_edificada_a'


class Capital(models.Model):
    gid = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaa = models.CharField(max_length=3, blank=True, null=True)
    tipocapita = models.CharField(max_length=20, blank=True, null=True)
    id_produto = models.IntegerField(blank=True, null=True)
    id_element = models.IntegerField(blank=True, null=True)
    cd_insumo_field = models.IntegerField(db_column='cd_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insumo_field = models.IntegerField(db_column='nr_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insum_1 = models.IntegerField(blank=True, null=True)
    tx_insumo_field = models.CharField(db_column='tx_insumo_', max_length=60, blank=True, null=True)  # Field renamed because it ended with '_'.
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'loc_capital_p'


class Cidade(models.Model):
    gid = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaa = models.CharField(max_length=4, blank=True, null=True)
    id_produto = models.IntegerField(blank=True, null=True)
    id_element = models.IntegerField(blank=True, null=True)
    cd_insumo_field = models.IntegerField(db_column='cd_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insumo_field = models.IntegerField(db_column='nr_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insum_1 = models.IntegerField(blank=True, null=True)
    tx_insumo_field = models.CharField(db_column='tx_insumo_', max_length=60, blank=True, null=True)  # Field renamed because it ended with '_'.
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'loc_cidade_p'


class Vila(models.Model):
    gid = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaa = models.CharField(max_length=4, blank=True, null=True)
    id_produto = models.IntegerField(blank=True, null=True)
    id_element = models.IntegerField(blank=True, null=True)
    cd_insumo_field = models.IntegerField(db_column='cd_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insumo_field = models.IntegerField(db_column='nr_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insum_1 = models.IntegerField(blank=True, null=True)
    tx_insumo_field = models.CharField(db_column='tx_insumo_', max_length=60, blank=True, null=True)  # Field renamed because it ended with '_'.
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'loc_vila_p'


class CurvaBatimetrica(models.Model):
    gid = models.AutoField(primary_key=True)
    profundida = models.IntegerField(blank=True, null=True)
    id_produto = models.IntegerField(blank=True, null=True)
    id_element = models.IntegerField(blank=True, null=True)
    cd_insumo_field = models.IntegerField(db_column='cd_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insumo_field = models.IntegerField(db_column='nr_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insum_1 = models.IntegerField(blank=True, null=True)
    tx_insumo_field = models.CharField(db_column='tx_insumo_', max_length=60, blank=True, null=True)  # Field renamed because it ended with '_'.
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rel_curva_batimetrica_l'


class CurvaNivel(models.Model):
    gid = models.AutoField(primary_key=True)
    cota = models.IntegerField(blank=True, null=True)
    depressao = models.CharField(max_length=3, blank=True, null=True)
    geometriaa = models.CharField(max_length=4, blank=True, null=True)
    indice = models.CharField(max_length=16, blank=True, null=True)
    id_produto = models.IntegerField(blank=True, null=True)
    id_element = models.IntegerField(blank=True, null=True)
    cd_insumo_field = models.IntegerField(db_column='cd_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insumo_field = models.IntegerField(db_column='nr_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insum_1 = models.IntegerField(blank=True, null=True)
    tx_insumo_field = models.CharField(db_column='tx_insumo_', max_length=60, blank=True, null=True)  # Field renamed because it ended with '_'.
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rel_curva_nivel_l'


class Duna(models.Model):
    gid = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaa = models.CharField(max_length=3, blank=True, null=True)
    fixa = models.CharField(max_length=4, blank=True, null=True)
    id_produto = models.IntegerField(blank=True, null=True)
    id_element = models.IntegerField(blank=True, null=True)
    cd_insumo_field = models.IntegerField(db_column='cd_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insumo_field = models.IntegerField(db_column='nr_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insum_1 = models.IntegerField(blank=True, null=True)
    tx_insumo_field = models.CharField(db_column='tx_insumo_', max_length=60, blank=True, null=True)  # Field renamed because it ended with '_'.
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rel_duna_a'


class ElementoFisiograficoNaturalL(models.Model):
    gid = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaa = models.CharField(max_length=3, blank=True, null=True)
    tipoelemna = models.CharField(max_length=12, blank=True, null=True)
    id_produto = models.IntegerField(blank=True, null=True)
    id_element = models.IntegerField(blank=True, null=True)
    cd_insumo_field = models.IntegerField(db_column='cd_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insumo_field = models.IntegerField(db_column='nr_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insum_1 = models.IntegerField(blank=True, null=True)
    tx_insumo_field = models.CharField(db_column='tx_insumo_', max_length=60, blank=True, null=True)  # Field renamed because it ended with '_'.
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rel_elemento_fisiografico_natural_l'


class ElementoFisiograficoNaturalP(models.Model):
    gid = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaa = models.CharField(max_length=3, blank=True, null=True)
    tipoelemna = models.CharField(max_length=12, blank=True, null=True)
    id_produto = models.IntegerField(blank=True, null=True)
    id_element = models.IntegerField(blank=True, null=True)
    cd_insumo_field = models.IntegerField(db_column='cd_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insumo_field = models.IntegerField(db_column='nr_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insum_1 = models.IntegerField(blank=True, null=True)
    tx_insumo_field = models.CharField(db_column='tx_insumo_', max_length=60, blank=True, null=True)  # Field renamed because it ended with '_'.
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rel_elemento_fisiografico_natural_p'


class Pico(models.Model):
    gid = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaa = models.CharField(max_length=3, blank=True, null=True)
    id_produto = models.IntegerField(blank=True, null=True)
    id_element = models.IntegerField(blank=True, null=True)
    cd_insumo_field = models.IntegerField(db_column='cd_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insumo_field = models.IntegerField(db_column='nr_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insum_1 = models.IntegerField(blank=True, null=True)
    tx_insumo_field = models.CharField(db_column='tx_insumo_', max_length=60, blank=True, null=True)  # Field renamed because it ended with '_'.
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rel_pico_p'


class PontoCotadoAltimetrico(models.Model):
    gid = models.AutoField(primary_key=True)
    geometriaa = models.CharField(max_length=4, blank=True, null=True)
    cota = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cotacompro = models.CharField(max_length=3, blank=True, null=True)
    id_produto = models.IntegerField(blank=True, null=True)
    id_element = models.IntegerField(blank=True, null=True)
    cd_insumo_field = models.IntegerField(db_column='cd_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insumo_field = models.IntegerField(db_column='nr_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insum_1 = models.IntegerField(blank=True, null=True)
    tx_insumo_field = models.CharField(db_column='tx_insumo_', max_length=60, blank=True, null=True)  # Field renamed because it ended with '_'.
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rel_ponto_cotado_altimetrico_p'


class PontoCotadoBatimetrico(models.Model):
    gid = models.AutoField(primary_key=True)
    profundida = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_produto = models.IntegerField(blank=True, null=True)
    id_element = models.IntegerField(blank=True, null=True)
    cd_insumo_field = models.IntegerField(db_column='cd_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insumo_field = models.IntegerField(db_column='nr_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insum_1 = models.IntegerField(blank=True, null=True)
    tx_insumo_field = models.CharField(db_column='tx_insumo_', max_length=60, blank=True, null=True)  # Field renamed because it ended with '_'.
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rel_ponto_cotado_batimetrico_p'


class Eclusa(models.Model):
    gid = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaa = models.CharField(max_length=4, blank=True, null=True)
    desnivel = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    largura = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    extensao = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    calado = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    matconstr = models.CharField(max_length=18, blank=True, null=True)
    operaciona = models.CharField(max_length=12, blank=True, null=True)
    situacaofi = models.CharField(max_length=80, blank=True, null=True)
    id_produto = models.IntegerField(blank=True, null=True)
    id_element = models.IntegerField(blank=True, null=True)
    cd_insumo_field = models.IntegerField(db_column='cd_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insumo_field = models.IntegerField(db_column='nr_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insum_1 = models.IntegerField(blank=True, null=True)
    tx_insumo_field = models.CharField(db_column='tx_insumo_', max_length=60, blank=True, null=True)  # Field renamed because it ended with '_'.
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tra_eclusa_l'


class EdifConstrAeroportuaria(models.Model):
    gid = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaa = models.CharField(max_length=4, blank=True, null=True)
    operaciona = models.CharField(max_length=12, blank=True, null=True)
    situacaofi = models.CharField(max_length=80, blank=True, null=True)
    administra = models.CharField(max_length=80, blank=True, null=True)
    matconstr = models.CharField(max_length=18, blank=True, null=True)
    tipoedifae = models.CharField(max_length=23, blank=True, null=True)
    id_produto = models.IntegerField(blank=True, null=True)
    id_element = models.IntegerField(blank=True, null=True)
    cd_insumo_field = models.IntegerField(db_column='cd_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insumo_field = models.IntegerField(db_column='nr_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insum_1 = models.IntegerField(blank=True, null=True)
    tx_insumo_field = models.CharField(db_column='tx_insumo_', max_length=60, blank=True, null=True)  # Field renamed because it ended with '_'.
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tra_edif_const_aeroportuaria_p'


class EdifConstPortuaria(models.Model):
    gid = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaa = models.CharField(max_length=4, blank=True, null=True)
    tipoedifpo = models.CharField(max_length=23, blank=True, null=True)
    administra = models.CharField(max_length=80, blank=True, null=True)
    matconstr = models.CharField(max_length=18, blank=True, null=True)
    operaciona = models.CharField(max_length=12, blank=True, null=True)
    situacaofi = models.CharField(max_length=80, blank=True, null=True)
    id_produto = models.IntegerField(blank=True, null=True)
    id_element = models.IntegerField(blank=True, null=True)
    cd_insumo_field = models.IntegerField(db_column='cd_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insumo_field = models.IntegerField(db_column='nr_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insum_1 = models.IntegerField(blank=True, null=True)
    tx_insumo_field = models.CharField(db_column='tx_insumo_', max_length=60, blank=True, null=True)  # Field renamed because it ended with '_'.
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tra_edif_const_portuaria_p'


class EdifMetroFerroviaria(models.Model):
    gid = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaa = models.CharField(max_length=4, blank=True, null=True)
    multimodal = models.CharField(max_length=12, blank=True, null=True)
    funcaoedif = models.CharField(max_length=44, blank=True, null=True)
    operaciona = models.CharField(max_length=12, blank=True, null=True)
    situacaofi = models.CharField(max_length=80, blank=True, null=True)
    administra = models.CharField(max_length=80, blank=True, null=True)
    matconstr = models.CharField(max_length=18, blank=True, null=True)
    id_produto = models.IntegerField(blank=True, null=True)
    id_element = models.IntegerField(blank=True, null=True)
    cd_insumo_field = models.IntegerField(db_column='cd_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insumo_field = models.IntegerField(db_column='nr_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insum_1 = models.IntegerField(blank=True, null=True)
    tx_insumo_field = models.CharField(db_column='tx_insumo_', max_length=60, blank=True, null=True)  # Field renamed because it ended with '_'.
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tra_edif_metro_ferroviaria_p'


class PistaPontoPouso(models.Model):
    gid = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    geometriaa = models.CharField(max_length=4, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    largura = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    extensao = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    operaciona = models.CharField(max_length=12, blank=True, null=True)
    situacaofi = models.CharField(max_length=80, blank=True, null=True)
    homologaca = models.CharField(max_length=12, blank=True, null=True)
    tipopista = models.CharField(max_length=14, blank=True, null=True)
    usopista = models.CharField(max_length=15, blank=True, null=True)
    revestimen = models.CharField(max_length=80, blank=True, null=True)
    id_produto = models.IntegerField(blank=True, null=True)
    id_element = models.IntegerField(blank=True, null=True)
    cd_insumo_field = models.IntegerField(db_column='cd_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insumo_field = models.IntegerField(db_column='nr_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insum_1 = models.IntegerField(blank=True, null=True)
    tx_insumo_field = models.CharField(db_column='tx_insumo_', max_length=60, blank=True, null=True)  # Field renamed because it ended with '_'.
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tra_pista_ponto_pouso_p'


class Ponte(models.Model):
    gid = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    geometriaa = models.CharField(max_length=4, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    tipoponte = models.CharField(max_length=12, blank=True, null=True)
    modaluso = models.CharField(max_length=16, blank=True, null=True)
    situacaofi = models.CharField(max_length=80, blank=True, null=True)
    operaciona = models.CharField(max_length=12, blank=True, null=True)
    matconstr = models.CharField(max_length=18, blank=True, null=True)
    vaolivreho = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    vaovertica = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cargasupor = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    nrpistas = models.IntegerField(blank=True, null=True)
    nrfaixas = models.IntegerField(blank=True, null=True)
    extensao = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    largura = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    posicaopis = models.CharField(max_length=15, blank=True, null=True)
    id_produto = models.IntegerField(blank=True, null=True)
    id_element = models.IntegerField(blank=True, null=True)
    cd_insumo_field = models.IntegerField(db_column='cd_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insumo_field = models.IntegerField(db_column='nr_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insum_1 = models.IntegerField(blank=True, null=True)
    tx_insumo_field = models.CharField(db_column='tx_insumo_', max_length=60, blank=True, null=True)  # Field renamed because it ended with '_'.
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tra_ponte_l'


class Sinalizacao(models.Model):
    gid = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaa = models.CharField(max_length=4, blank=True, null=True)
    operaciona = models.CharField(max_length=12, blank=True, null=True)
    situacaofi = models.CharField(max_length=80, blank=True, null=True)
    tiposinal = models.CharField(max_length=21, blank=True, null=True)
    id_produto = models.IntegerField(blank=True, null=True)
    id_element = models.IntegerField(blank=True, null=True)
    cd_insumo_field = models.IntegerField(db_column='cd_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insumo_field = models.IntegerField(db_column='nr_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insum_1 = models.IntegerField(blank=True, null=True)
    tx_insumo_field = models.CharField(db_column='tx_insumo_', max_length=60, blank=True, null=True)  # Field renamed because it ended with '_'.
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tra_sinalizacao_p'


class TravessiaL(models.Model):
    gid = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    geometriaa = models.CharField(max_length=4, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    tipotraves = models.CharField(max_length=18, blank=True, null=True)
    id_produto = models.IntegerField(blank=True, null=True)
    id_element = models.IntegerField(blank=True, null=True)
    cd_insumo_field = models.IntegerField(db_column='cd_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insumo_field = models.IntegerField(db_column='nr_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insum_1 = models.IntegerField(blank=True, null=True)
    tx_insumo_field = models.CharField(db_column='tx_insumo_', max_length=60, blank=True, null=True)  # Field renamed because it ended with '_'.
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tra_travessia_l'


class TravessiaP(models.Model):
    gid = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    geometriaa = models.CharField(max_length=4, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    tipotraves = models.CharField(max_length=18, blank=True, null=True)
    id_produto = models.IntegerField(blank=True, null=True)
    id_element = models.IntegerField(blank=True, null=True)
    cd_insumo_field = models.IntegerField(db_column='cd_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insumo_field = models.IntegerField(db_column='nr_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insum_1 = models.IntegerField(blank=True, null=True)
    tx_insumo_field = models.CharField(db_column='tx_insumo_', max_length=60, blank=True, null=True)  # Field renamed because it ended with '_'.
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tra_travessia_p'


class TrechoDuto(models.Model):
    gid = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaa = models.CharField(max_length=3, blank=True, null=True)
    nrdutos = models.IntegerField(blank=True, null=True)
    tipotrecho = models.CharField(max_length=22, blank=True, null=True)
    mattransp = models.CharField(max_length=12, blank=True, null=True)
    setor = models.CharField(max_length=21, blank=True, null=True)
    posicaorel = models.CharField(max_length=15, blank=True, null=True)
    matconstr = models.CharField(max_length=18, blank=True, null=True)
    situacaoes = models.CharField(max_length=11, blank=True, null=True)
    operaciona = models.CharField(max_length=12, blank=True, null=True)
    situacaofi = models.CharField(max_length=80, blank=True, null=True)
    id_produto = models.IntegerField(blank=True, null=True)
    id_element = models.IntegerField(blank=True, null=True)
    cd_insumo_field = models.IntegerField(db_column='cd_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insumo_field = models.IntegerField(db_column='nr_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insum_1 = models.IntegerField(blank=True, null=True)
    tx_insumo_field = models.CharField(db_column='tx_insumo_', max_length=60, blank=True, null=True)  # Field renamed because it ended with '_'.
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tra_trecho_duto_l'


class TrechoFerroviario(models.Model):
    gid = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaa = models.CharField(max_length=4, blank=True, null=True)
    codtrechof = models.CharField(max_length=25, blank=True, null=True)
    posicaorel = models.CharField(max_length=15, blank=True, null=True)
    tipotrecho = models.CharField(max_length=12, blank=True, null=True)
    bitola = models.CharField(max_length=27, blank=True, null=True)
    eletrifica = models.CharField(max_length=12, blank=True, null=True)
    nrlinhas = models.CharField(max_length=12, blank=True, null=True)
    emarruamen = models.CharField(max_length=12, blank=True, null=True)
    jurisdicao = models.CharField(max_length=80, blank=True, null=True)
    administra = models.CharField(max_length=80, blank=True, null=True)
    concession = models.CharField(max_length=100, blank=True, null=True)
    operaciona = models.CharField(max_length=12, blank=True, null=True)
    cargasupor = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    situacaofi = models.CharField(max_length=80, blank=True, null=True)
    id_produto = models.IntegerField(blank=True, null=True)
    id_element = models.IntegerField(blank=True, null=True)
    cd_insumo_field = models.IntegerField(db_column='cd_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insumo_field = models.IntegerField(db_column='nr_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insum_1 = models.IntegerField(blank=True, null=True)
    tx_insumo_field = models.CharField(db_column='tx_insumo_', max_length=60, blank=True, null=True)  # Field renamed because it ended with '_'.
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tra_trecho_ferroviario_l'


class TrechoHidroviario(models.Model):
    gid = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaa = models.CharField(max_length=4, blank=True, null=True)
    extensaotr = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    caladomaxs = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    operaciona = models.CharField(max_length=12, blank=True, null=True)
    situacaofi = models.CharField(max_length=80, blank=True, null=True)
    regime = models.CharField(max_length=31, blank=True, null=True)
    id_produto = models.IntegerField(blank=True, null=True)
    id_element = models.IntegerField(blank=True, null=True)
    cd_insumo_field = models.IntegerField(db_column='cd_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insumo_field = models.IntegerField(db_column='nr_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insum_1 = models.IntegerField(blank=True, null=True)
    tx_insumo_field = models.CharField(db_column='tx_insumo_', max_length=60, blank=True, null=True)  # Field renamed because it ended with '_'.
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tra_trecho_hidroviario_l'


class TrechoRodoviario(models.Model):
    gid = models.AutoField(primary_key=True)
    codtrechor = models.CharField(max_length=25, blank=True, null=True)
    tipotrecho = models.CharField(max_length=80, blank=True, null=True)
    jurisdicao = models.CharField(max_length=80, blank=True, null=True)
    administra = models.CharField(max_length=80, blank=True, null=True)
    concession = models.CharField(max_length=100, blank=True, null=True)
    revestimen = models.CharField(max_length=80, blank=True, null=True)
    operaciona = models.CharField(max_length=12, blank=True, null=True)
    situacaofi = models.CharField(max_length=80, blank=True, null=True)
    nrpistas = models.IntegerField(blank=True, null=True)
    nrfaixas = models.IntegerField(blank=True, null=True)
    trafego = models.CharField(max_length=80, blank=True, null=True)
    capaccarga = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_produto = models.IntegerField(blank=True, null=True)
    id_element = models.IntegerField(blank=True, null=True)
    geometriaa = models.CharField(max_length=4, blank=True, null=True)
    canteirodi = models.CharField(max_length=4, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tra_trecho_rodoviario_l'


class Tunel(models.Model):
    gid = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    geometriaa = models.CharField(max_length=4, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    modaluso = models.CharField(max_length=15, blank=True, null=True)
    nrpistas = models.IntegerField(blank=True, null=True)
    nrfaixas = models.IntegerField(blank=True, null=True)
    extensao = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    altura = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    largura = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    posicaopis = models.CharField(max_length=13, blank=True, null=True)
    situacaofi = models.CharField(max_length=80, blank=True, null=True)
    operaciona = models.CharField(max_length=12, blank=True, null=True)
    matconstr = models.CharField(max_length=18, blank=True, null=True)
    tipotunel = models.CharField(max_length=28, blank=True, null=True)
    id_produto = models.IntegerField(blank=True, null=True)
    id_element = models.IntegerField(blank=True, null=True)
    cd_insumo_field = models.IntegerField(db_column='cd_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insumo_field = models.IntegerField(db_column='nr_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insum_1 = models.IntegerField(blank=True, null=True)
    tx_insumo_field = models.CharField(db_column='tx_insumo_', max_length=60, blank=True, null=True)  # Field renamed because it ended with '_'.
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tra_tunel_l'


class BrejoPantano(models.Model):
    gid = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaa = models.CharField(max_length=3, blank=True, null=True)
    alturamedi = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    classifica = models.CharField(max_length=12, blank=True, null=True)
    tipobrejop = models.CharField(max_length=27, blank=True, null=True)
    denso = models.CharField(max_length=12, blank=True, null=True)
    antropizad = models.CharField(max_length=23, blank=True, null=True)
    id_produto = models.IntegerField(blank=True, null=True)
    id_element = models.IntegerField(blank=True, null=True)
    cd_insumo_field = models.IntegerField(db_column='cd_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insumo_field = models.IntegerField(db_column='nr_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insum_1 = models.IntegerField(blank=True, null=True)
    tx_insumo_field = models.CharField(db_column='tx_insumo_', max_length=60, blank=True, null=True)  # Field renamed because it ended with '_'.
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'veg_brejo_pantano_a'


class Mangue(models.Model):
    gid = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaa = models.CharField(max_length=3, blank=True, null=True)
    alturamedi = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    classifica = models.CharField(max_length=12, blank=True, null=True)
    denso = models.CharField(max_length=12, blank=True, null=True)
    antropizad = models.CharField(max_length=23, blank=True, null=True)
    id_produto = models.IntegerField(blank=True, null=True)
    id_element = models.IntegerField(blank=True, null=True)
    cd_insumo_field = models.IntegerField(db_column='cd_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insumo_field = models.IntegerField(db_column='nr_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insum_1 = models.IntegerField(blank=True, null=True)
    tx_insumo_field = models.CharField(db_column='tx_insumo_', max_length=60, blank=True, null=True)  # Field renamed because it ended with '_'.
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'veg_mangue_a'


class VegRestinga(models.Model):
    gid = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    nomeabrev = models.CharField(max_length=50, blank=True, null=True)
    geometriaa = models.CharField(max_length=3, blank=True, null=True)
    alturamedi = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    classifica = models.CharField(max_length=12, blank=True, null=True)
    denso = models.CharField(max_length=12, blank=True, null=True)
    antropizad = models.CharField(max_length=23, blank=True, null=True)
    id_produto = models.IntegerField(blank=True, null=True)
    id_element = models.IntegerField(blank=True, null=True)
    cd_insumo_field = models.IntegerField(db_column='cd_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insumo_field = models.IntegerField(db_column='nr_insumo_', blank=True, null=True)  # Field renamed because it ended with '_'.
    nr_insum_1 = models.IntegerField(blank=True, null=True)
    tx_insumo_field = models.CharField(db_column='tx_insumo_', max_length=60, blank=True, null=True)  # Field renamed because it ended with '_'.
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'veg_veg_restinga_a'
