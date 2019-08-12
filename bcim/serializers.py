from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import *

class EdifPubMilitarSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = EdifPubMilitar
        geo_field = 'geom'
        auto_bbox = True
        id_field = 'gid'
        fields = ['gid', 'nome', 'nomeabrev', 'tipoedifmi', 'tipousoedi', 'situacaofi', 'operaciona', 'matconstr', 'id_produto', 'id_element', 'nr_insum_1']

class AdmEdifPubMilitarPSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = AdmEdifPubMilitarP
        geo_field = 'geom'
        auto_bbox = True
        id_field = 'gid'
        fields = ['gid', 'nome', 'nomeabrev', 'tipoedifmi', 'tipousoedi', 'situacaofi', 'operaciona', 'matconstr', 'id_produto', 'id_element', 'nr_insum_1']

class PostoFiscalSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = PostoFiscal
        geo_field = 'geom'
        auto_bbox = True
        id_field = 'gid'
        fields = ['gid', 'nome', 'nomeabrev', 'operaciona', 'situacaofi', 'tipopostof', 'id_produto', 'id_element', 'nr_insum_1']

class EdifAgropecExtVegetalPescaSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = EdifAgropecExtVegetalPesca
        geo_field = 'geom'
        auto_bbox = True
        id_field = 'gid'
        fields = ['gid', 'nome', 'nomeabrev', 'operaciona', 'situacaofi', 'tipoedifag', 'matconstr', 'id_produto', 'id_element', 'nr_insum_1']

class ExtMineralASerializer(GeoFeatureModelSerializer):
    class Meta:
        model = ExtMineralA
        geo_field = 'geom'
        auto_bbox = True
        id_field = 'gid'
        fields = ['gid', 'nome', 'nomeabrev', 'tiposecaoc', 'operaciona', 'situacaofi', 'tipoextmin', 'tipoprodut', 'tipopocomi', 'procextrac', 'formaextra', 'atividade', 'id_produto', 'id_element', 'nr_insum_1']

class ExtMineralPSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = ExtMineralP
        geo_field = 'geom'
        auto_bbox = True
        id_field = 'gid'
        fields = ['gid', 'nome', 'nomeabrev', 'tiposecaoc', 'operaciona', 'situacaofi', 'tipoextmin', 'tipoprodut', 'tipopocomi', 'procextrac', 'formaextra', 'atividade', 'id_produto', 'id_element', 'nr_insum_1']

class EstGeradEnergiaEletricaSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = EstGeradEnergiaEletrica
        geo_field = 'geom'
        auto_bbox = True
        id_field = 'gid'
        fields = ['gid', 'nome', 'nomeabrev', 'codigoesta', 'potenciaou', 'potenciafi', 'operaciona', 'situacaofi', 'tipoestger', 'destenerge', 'id_produto', 'id_element', 'nr_insum_1']

class HidreletricaSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Hidreletrica
        geo_field = 'geom'
        auto_bbox = True
        id_field = 'gid'
        fields = ['gid', 'nome', 'nomeabrev', 'potenciaou', 'potenciafi', 'codigohidr', 'operaciona', 'situacaofi', 'id_produto', 'id_element', 'nr_insum_1']

class TermeletricaSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Termeletrica
        geo_field = 'geom'
        auto_bbox = True
        id_field = 'gid'
        fields = ['gid', 'nome', 'nomeabrev', 'potenciaou', 'potenciafi', 'combrenova', 'tipomaqter', 'geracao', 'tipocombus', 'operaciona', 'situacaofi', 'id_produto', 'id_element', 'nr_insum_1']

class BancoAreiaSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = BancoAreia
        geo_field = 'geom'
        auto_bbox = True
        id_field = 'gid'
        fields = ['gid', 'nome', 'nomeabrev', 'tipobanco', 'situacaoem', 'materialpr', 'id_produto', 'id_element', 'nr_insum_1']

class BarragemLSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = BarragemL
        geo_field = 'geom'
        auto_bbox = True
        id_field = 'gid'
        fields = ['gid', 'nome', 'nomeabrev', 'matconstr', 'usoprincip', 'operaciona', 'situacaofi', 'id_produto', 'id_element', 'nr_insum_1']

class BarragemPSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = BarragemP
        geo_field = 'geom'
        auto_bbox = True
        id_field = 'gid'
        fields = ['gid', 'nome', 'nomeabrev', 'matconstr', 'usoprincip', 'operaciona', 'situacaofi', 'id_produto', 'id_element', 'nr_insum_1']

class CorredeiraLSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = CorredeiraL
        geo_field = 'geom'
        auto_bbox = True
        id_field = 'gid'
        fields = ['gid', 'nome', 'nomeabrev', 'id_produto', 'id_element', 'nr_insum_1']

class CorredeiraPSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = CorredeiraP
        geo_field = 'geom'
        auto_bbox = True
        id_field = 'gid'
        fields = ['gid', 'nome', 'nomeabrev', 'id_produto', 'id_element', 'nr_insum_1']

class IlhaSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Ilha
        geo_field = 'geom'
        auto_bbox = True
        id_field = 'gid'
        fields = ['gid', 'nome', 'nomeabrev', 'tipoilha', 'id_produto', 'id_element', 'nr_insum_1']

class MassaDaguaSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = MassaDagua
        geo_field = 'geom'
        auto_bbox = True
        id_field = 'gid'
        fields = ['gid', 'nome', 'nomeabrev', 'tipomassad', 'salinidade', 'regime', 'id_produto', 'id_element', 'nr_insum_1']

class QuedaDaguaSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = QuedaDagua
        geo_field = 'geom'
        auto_bbox = True
        id_field = 'gid'
        fields = ['gid', 'nome', 'nomeabrev', 'altura', 'tipoqueda', 'id_produto', 'id_element', 'nr_insum_1']

class RecifeSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Recife
        geo_field = 'geom'
        auto_bbox = True
        id_field = 'gid'
        fields = ['gid', 'nome', 'nomeabrev', 'tiporecife', 'situamare', 'situacaoco', 'id_produto', 'id_element', 'nr_insum_1']

class RochaEmAguaSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = RochaEmAgua
        geo_field = 'geom'
        auto_bbox = True
        id_field = 'gid'
        fields = ['gid', 'nome', 'nomeabrev', 'alturalami', 'situacaoem', 'id_produto', 'id_element', 'nr_insum_1']

class SumidouroVertedouroSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = SumidouroVertedouro
        geo_field = 'geom'
        auto_bbox = True
        id_field = 'gid'
        fields = ['gid', 'nome', 'nomeabrev', 'causa', 'tiposumver', 'id_produto', 'id_element', 'nr_insum_1']

class TerrenoSujeitoInundacaoSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = TerrenoSujeitoInundacao
        geo_field = 'geom'
        auto_bbox = True
        id_field = 'gid'
        fields = ['gid', 'nome', 'nomeabrev', 'periodicid', 'id_produto', 'id_element', 'nr_insum_1']

class TrechoDrenagemSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = TrechoDrenagem
        geo_field = 'geom'
        auto_bbox = True
        id_field = 'gid'
        fields = ['gid', 'nome', 'nomeabrev', 'dentrodepo', 'compartilh', 'eixoprinci', 'caladomax', 'larguramed', 'velocidade', 'profundida', 'coincideco', 'navegabili', 'regime', 'id_produto', 'id_element', 'nr_insum_1']

class TrechoMassaDaguaSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = TrechoMassaDagua
        geo_field = 'geom'
        auto_bbox = True
        id_field = 'gid'
        fields = ['gid', 'nome', 'nomeabrev', 'tipotrecho', 'salinidade', 'regime', 'id_produto', 'id_element', 'nr_insum_1']

class MunicipioSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Municipio
        geo_field = 'geom'
        auto_bbox = True
        id_field = 'gid'
        fields = ['gid', 'nome', 'nomeabrev', 'geocodigo', 'anoderefer', 'id_produto', 'id_element', 'nr_insum_1']

class OutrosLimitesOficiaisSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = OutrosLimitesOficiais
        geo_field = 'geom'
        auto_bbox = True
        id_field = 'gid'
        fields = ['gid', 'nome', 'nomeabrev', 'coincideco', 'extensao', 'obssituaca', 'tipooutlim', 'id_produto', 'id_element', 'nr_insum_1']

class PaisSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Pais
        geo_field = 'geom'
        auto_bbox = True
        id_field = 'gid'
        fields = ['gid', 'nome', 'nomeabrev', 'sigla', 'codiso3166', 'id_produto', 'id_element', 'nr_insum_1']

class TerraIndigenaASerializer(GeoFeatureModelSerializer):
    class Meta:
        model = TerraIndigenaA
        geo_field = 'geom'
        auto_bbox = True
        id_field = 'gid'
        fields = ['gid', 'nome', 'nomeabrev', 'perimetroo', 'areaoficia', 'grupoetnic', 'datasituac', 'situacaoju', 'nometi', 'id_produto', 'id_element', 'codigofuna', 'nr_insum_1']

class TerraIndigenaPSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = TerraIndigenaP
        geo_field = 'geom'
        auto_bbox = True
        id_field = 'gid'
        fields = ['gid', 'nome', 'nomeabrev', 'perimetroo', 'areaoficia', 'grupoetnic', 'datasituac', 'situacaoju', 'nometi', 'id_produto', 'id_element', 'codigofuna', 'nr_insum_1']

class UnidadeConservacaoNaoSnucSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = UnidadeConservacaoNaoSnuc
        geo_field = 'geom'
        auto_bbox = True
        id_field = 'gid'
        fields = ['gid', 'nome', 'nomeabrev', 'anocriacao', 'sigla', 'areaoficia', 'administra', 'classifica', 'atolegal', 'id_produto', 'id_element', 'nr_insum_1']

class UnidadeFederacaoSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = UnidadeFederacao
        geo_field = 'geom'
        auto_bbox = True
        id_field = 'gid'
        fields = ['gid', 'nome', 'nomeabrev', 'sigla', 'geocodigo', 'id_produto', 'id_element', 'nr_insum_1']

class UnidadeProtecaoIntegralSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = UnidadeProtecaoIntegral
        geo_field = 'geom'
        auto_bbox = True
        id_field = 'gid'
        fields = ['gid', 'nome', 'nomeabrev', 'anocriacao', 'sigla', 'areaoficia', 'administra', 'atolegal', 'tipounidpr', 'id_produto', 'id_element', 'nr_insum_1']

class UnidadeUsoSustentavelSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = UnidadeUsoSustentavel
        geo_field = 'geom'
        auto_bbox = True
        id_field = 'gid'
        fields = ['gid', 'nome', 'nomeabrev', 'anocriacao', 'sigla', 'areaoficia', 'administra', 'atolegal', 'tipounidus', 'id_produto', 'id_element', 'nr_insum_1']

class AglomeradoRuralIsoladoSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = AglomeradoRuralIsolado
        geo_field = 'geom'
        auto_bbox = True
        id_field = 'gid'
        fields = ['gid', 'nome', 'nomeabrev', 'tipoaglomr', 'id_produto', 'id_element', 'nr_insum_1']

class AldeiaIndigenaSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = AldeiaIndigena
        geo_field = 'geom'
        auto_bbox = True
        id_field = 'gid'
        fields = ['gid', 'nome', 'nomeabrev', 'codigofuna', 'terraindig', 'etnia', 'id_produto', 'id_element', 'nr_insum_1']

class AreaEdificadaSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = AreaEdificada
        geo_field = 'geom'
        auto_bbox = True
        id_field = 'gid'
        fields = ['gid', 'nome', 'nomeabrev', 'geocodigo', 'id_produto', 'id_element', 'nr_insum_1']

class CapitalSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Capital
        geo_field = 'geom'
        auto_bbox = True
        id_field = 'gid'
        fields = ['gid', 'nome', 'nomeabrev', 'tipocapita', 'id_produto', 'id_element', 'nr_insum_1']

class CidadeSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Cidade
        geo_field = 'geom'
        auto_bbox = True
        id_field = 'gid'
        fields = ['gid', 'nome', 'nomeabrev', 'id_produto', 'id_element', 'nr_insum_1']

class VilaSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Vila
        geo_field = 'geom'
        auto_bbox = True
        id_field = 'gid'
        fields = ['gid', 'nome', 'nomeabrev', 'id_produto', 'id_element', 'nr_insum_1']

class CurvaBatimetricaSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = CurvaBatimetrica
        geo_field = 'geom'
        auto_bbox = True
        id_field = 'gid'
        fields = ['gid', 'profundida', 'id_produto', 'id_element', 'nr_insum_1']

class CurvaNivelSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = CurvaNivel
        geo_field = 'geom'
        auto_bbox = True
        id_field = 'gid'
        fields = ['gid', 'cota', 'depressao', 'indice', 'id_produto', 'id_element', 'nr_insum_1']

class DunaSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Duna
        geo_field = 'geom'
        auto_bbox = True
        id_field = 'gid'
        fields = ['gid', 'nome', 'nomeabrev', 'fixa', 'id_produto', 'id_element', 'nr_insum_1']

class ElementoFisiograficoNaturalLSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = ElementoFisiograficoNaturalL
        geo_field = 'geom'
        auto_bbox = True
        id_field = 'gid'
        fields = ['gid', 'nome', 'nomeabrev', 'tipoelemna', 'id_produto', 'id_element', 'nr_insum_1']

class ElementoFisiograficoNaturalPSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = ElementoFisiograficoNaturalP
        geo_field = 'geom'
        auto_bbox = True
        id_field = 'gid'
        fields = ['gid', 'nome', 'nomeabrev', 'tipoelemna', 'id_produto', 'id_element', 'nr_insum_1']

class PicoSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Pico
        geo_field = 'geom'
        auto_bbox = True
        id_field = 'gid'
        fields = ['gid', 'nome', 'nomeabrev', 'id_produto', 'id_element', 'nr_insum_1']

class PontoCotadoAltimetricoSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = PontoCotadoAltimetrico
        geo_field = 'geom'
        auto_bbox = True
        id_field = 'gid'
        fields = ['gid', 'cota', 'cotacompro', 'id_produto', 'id_element', 'nr_insum_1']

class PontoCotadoBatimetricoSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = PontoCotadoBatimetrico
        geo_field = 'geom'
        auto_bbox = True
        id_field = 'gid'
        fields = ['gid', 'profundida', 'id_produto', 'id_element', 'nr_insum_1']

class EclusaSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Eclusa
        geo_field = 'geom'
        auto_bbox = True
        id_field = 'gid'
        fields = ['gid', 'nome', 'nomeabrev', 'desnivel', 'largura', 'extensao', 'calado', 'matconstr', 'operaciona', 'situacaofi', 'id_produto', 'id_element', 'nr_insum_1']

class EdifConstrAeroportuariaSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = EdifConstrAeroportuaria
        geo_field = 'geom'
        auto_bbox = True
        id_field = 'gid'
        fields = ['gid', 'nome', 'nomeabrev', 'operaciona', 'situacaofi', 'administra', 'matconstr', 'tipoedifae', 'id_produto', 'id_element', 'nr_insum_1']

class EdifConstPortuariaSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = EdifConstPortuaria
        geo_field = 'geom'
        auto_bbox = True
        id_field = 'gid'
        fields = ['gid', 'nome', 'nomeabrev', 'tipoedifpo', 'administra', 'matconstr', 'operaciona', 'situacaofi', 'id_produto', 'id_element', 'nr_insum_1']

class EdifMetroFerroviariaSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = EdifMetroFerroviaria
        geo_field = 'geom'
        auto_bbox = True
        id_field = 'gid'
        fields = ['gid', 'nome', 'nomeabrev', 'multimodal', 'funcaoedif', 'operaciona', 'situacaofi', 'administra', 'matconstr', 'id_produto', 'id_element', 'nr_insum_1']

class PistaPontoPousoSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = PistaPontoPouso
        geo_field = 'geom'
        auto_bbox = True
        id_field = 'gid'
        fields = ['gid', 'nome', 'nomeabrev', 'largura', 'extensao', 'operaciona', 'situacaofi', 'homologaca', 'tipopista', 'usopista', 'revestimen', 'id_produto', 'id_element', 'nr_insum_1']

class PonteSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Ponte
        geo_field = 'geom'
        auto_bbox = True
        id_field = 'gid'
        fields = ['gid', 'nome', 'nomeabrev', 'tipoponte', 'modaluso', 'situacaofi', 'operaciona', 'matconstr', 'vaolivreho', 'vaovertica', 'cargasupor', 'nrpistas', 'nrfaixas', 'extensao', 'largura', 'posicaopis', 'id_produto', 'id_element', 'nr_insum_1']

class SinalizacaoSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Sinalizacao
        geo_field = 'geom'
        auto_bbox = True
        id_field = 'gid'
        fields = ['gid', 'nome', 'nomeabrev', 'operaciona', 'situacaofi', 'tiposinal', 'id_produto', 'id_element', 'nr_insum_1']

class TravessiaLSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = TravessiaL
        geo_field = 'geom'
        auto_bbox = True
        id_field = 'gid'
        fields = ['gid', 'nome', 'nomeabrev', 'tipotraves', 'id_produto', 'id_element', 'nr_insum_1']

class TravessiaPSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = TravessiaP
        geo_field = 'geom'
        auto_bbox = True
        id_field = 'gid'
        fields = ['gid', 'nome', 'nomeabrev', 'tipotraves', 'id_produto', 'id_element', 'nr_insum_1']

class TrechoDutoSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = TrechoDuto
        geo_field = 'geom'
        auto_bbox = True
        id_field = 'gid'
        fields = ['gid', 'nome', 'nomeabrev', 'nrdutos', 'tipotrecho', 'mattransp', 'setor', 'posicaorel', 'matconstr', 'situacaoes', 'operaciona', 'situacaofi', 'id_produto', 'id_element', 'nr_insum_1']

class TrechoFerroviarioSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = TrechoFerroviario
        geo_field = 'geom'
        auto_bbox = True
        id_field = 'gid'
        fields = ['gid', 'nome', 'nomeabrev', 'codtrechof', 'posicaorel', 'tipotrecho', 'bitola', 'eletrifica', 'nrlinhas', 'emarruamen', 'jurisdicao', 'administra', 'concession', 'operaciona', 'cargasupor', 'situacaofi', 'id_produto', 'id_element', 'nr_insum_1']

class TrechoHidroviarioSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = TrechoHidroviario
        geo_field = 'geom'
        auto_bbox = True
        id_field = 'gid'
        fields = ['gid', 'nome', 'nomeabrev', 'extensaotr', 'caladomaxs', 'operaciona', 'situacaofi', 'regime', 'id_produto', 'id_element', 'nr_insum_1']

class TrechoRodoviarioSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = TrechoRodoviario
        geo_field = 'geom'
        auto_bbox = True
        id_field = 'gid'
        fields = ['gid', 'codtrechor', 'tipotrecho', 'jurisdicao', 'administra', 'concession', 'revestimen', 'operaciona', 'situacaofi', 'nrpistas', 'nrfaixas', 'trafego', 'capaccarga', 'id_produto', 'id_element', 'canteirodi']

class TunelSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Tunel
        geo_field = 'geom'
        auto_bbox = True
        id_field = 'gid'
        fields = ['gid', 'nome', 'nomeabrev', 'modaluso', 'nrpistas', 'nrfaixas', 'extensao', 'altura', 'largura', 'posicaopis', 'situacaofi', 'operaciona', 'matconstr', 'tipotunel', 'id_produto', 'id_element', 'nr_insum_1']

class BrejoPantanoSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = BrejoPantano
        geo_field = 'geom'
        auto_bbox = True
        id_field = 'gid'
        fields = ['gid', 'nome', 'nomeabrev', 'alturamedi', 'classifica', 'tipobrejop', 'denso', 'antropizad', 'id_produto', 'id_element', 'nr_insum_1']

class MangueSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Mangue
        geo_field = 'geom'
        auto_bbox = True
        id_field = 'gid'
        fields = ['gid', 'nome', 'nomeabrev', 'alturamedi', 'classifica', 'denso', 'antropizad', 'id_produto', 'id_element', 'nr_insum_1']

class VegRestingaSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = VegRestinga
        geo_field = 'geom'
        auto_bbox = True
        id_field = 'gid'
        fields = ['gid', 'nome', 'nomeabrev', 'alturamedi', 'classifica', 'denso', 'antropizad', 'id_produto', 'id_element', 'nr_insum_1']

