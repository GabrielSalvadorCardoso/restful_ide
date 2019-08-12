from rest_framework.negotiation import BaseContentNegotiation
from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from bcim.contexts import AbstractContextResource, FeatureCollectionContextResource, FeatureContextResource
from .models import *
from .serializers import *

JSON_CONTENT_TYPE = "application/json"
GEOJSON_CONTENT_TYPE = "application/geo+json"
JSONLD_CONTENT_TYPE = "application/ld+json"

CORS_HEADERS = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "GET, HEAD, OPTIONS"
}

class BlankContentNegotiation(BaseContentNegotiation):
    '''
    Class to ignore django rest framework default renders
    '''
    def select_parser(self, request, parsers):
        return parsers[0]

    def select_renderer(self, request, renderers, format_suffix=None):
        return (renderers[0], renderers[0].media_type)

# ============================ Hyper Resource Classes ============================

class RequiredObject(object):
    def __init__(self, representation_object, content_type, status_code, etag=None):
        self.representation_object = representation_object
        self.content_type = content_type
        self.status_code = status_code
        self.etag = etag

class AbstractResource(APIView):
    content_negotiation_class = BlankContentNegotiation
    serializer_class = None
    context_class = AbstractContextResource

    def add_cors_headers(self, response):
        for header, value in CORS_HEADERS.items():
            response[header] = value

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        self.add_cors_headers(response)
        return response

    def basic_get(self, request, *args, **kwargs):
        object = self.serializer_class.Meta.model.objects.get(pk=kwargs['pk'])
        serializer = self.serializer_class(object, context={'request': request})
        return RequiredObject(serializer.data, JSON_CONTENT_TYPE, 200)

    def options(self, request, *args, **kwargs):
        context = self.context_class().create_context_for_fields(self.serializer_class.Meta.model()._meta.fields)
        return Response(context, status=status.HTTP_200_OK, content_type=JSONLD_CONTENT_TYPE)

class AbstractCollectionResource(AbstractResource):

    def basic_get(self, request, *args, **kwargs):
        queryset = self.serializer_class.Meta.model.objects.all()
        serializer = self.serializer_class(queryset, many=True, context={'request': request})
        return RequiredObject(serializer.data, JSON_CONTENT_TYPE, 200)

    def get(self, request, *args, **kwargs):
        required_object = self.basic_get(request, *args, **kwargs)
        return Response(
            required_object.representation_object,
            status=required_object.status_code,
            content_type=required_object.content_type
        )

class FeatureConcentrator(AbstractResource):
    """
    This isn't a Hyper Resource class. The role pf this class is to
    concentrate behavior common to FeatureResource and FeatureCollectionResource
    """
    pass

class FeatureCollectionResource(AbstractCollectionResource):
    context_class = FeatureCollectionContextResource

    def get(self, request, *args, **kwargs):
        required_object = self.basic_get(request, *args, **kwargs)
        return Response(
            required_object.representation_object,
            status=required_object.status_code,
            content_type=GEOJSON_CONTENT_TYPE
        )

class FeatureResource(AbstractResource):
    context_class = FeatureContextResource

    def get(self, request, *args, **kwargs):
        required_object = self.basic_get(request, *args, **kwargs)
        return Response(
            required_object.representation_object,
            status=required_object.status_code,
            content_type=GEOJSON_CONTENT_TYPE
        )

#  ============================ BCIM Resource Classes  ============================

class APIRoot(AbstractResource):

    def get(self, request, *args, **kwargs):
        data = {
            "unidades-federativas": reverse("bcim:UnidadesFederativas_list", args=args, kwargs=kwargs, request=request),
            'edif-pub-militar': reverse('bcim:EdifPubMilitar_list', args=args, kwargs=kwargs, request=request),
            'adm-edif-pub-militar-p': reverse('bcim:AdmEdifPubMilitarP_list', args=args, kwargs=kwargs, request=request),
            'posto-fiscal': reverse('bcim:PostoFiscal_list', args=args, kwargs=kwargs, request=request),
            'edif-agropec-ext-vegetal-pesca': reverse('bcim:EdifAgropecExtVegetalPesca_list', args=args, kwargs=kwargs, request=request),
            'ext-mineral-a': reverse('bcim:ExtMineralA_list', args=args, kwargs=kwargs, request=request),
            'ext-mineral-p': reverse('bcim:ExtMineralP_list', args=args, kwargs=kwargs, request=request),
            'est-gerad-energia-eletrica': reverse('bcim:EstGeradEnergiaEletrica_list', args=args, kwargs=kwargs, request=request),
            'hidreletrica': reverse('bcim:Hidreletrica_list', args=args, kwargs=kwargs, request=request),
            'termeletrica': reverse('bcim:Termeletrica_list', args=args, kwargs=kwargs, request=request),
            'banco-areia': reverse('bcim:BancoAreia_list', args=args, kwargs=kwargs, request=request),
            'barragem-l': reverse('bcim:BarragemL_list', args=args, kwargs=kwargs, request=request),
            'barragem-p': reverse('bcim:BarragemP_list', args=args, kwargs=kwargs, request=request),
            'corredeira-l': reverse('bcim:CorredeiraL_list', args=args, kwargs=kwargs, request=request),
            'corredeira-p': reverse('bcim:CorredeiraP_list', args=args, kwargs=kwargs, request=request),
            'ilha': reverse('bcim:Ilha_list', args=args, kwargs=kwargs, request=request),
            'massa-dagua': reverse('bcim:MassaDagua_list', args=args, kwargs=kwargs, request=request),
            'queda-dagua': reverse('bcim:QuedaDagua_list', args=args, kwargs=kwargs, request=request),
            'recife': reverse('bcim:Recife_list', args=args, kwargs=kwargs, request=request),
            'rocha-em-agua': reverse('bcim:RochaEmAgua_list', args=args, kwargs=kwargs, request=request),
            'sumidouro-vertedouro': reverse('bcim:SumidouroVertedouro_list', args=args, kwargs=kwargs, request=request),
            'terreno-sujeito-inundacao': reverse('bcim:TerrenoSujeitoInundacao_list', args=args, kwargs=kwargs, request=request),
            'trecho-drenagem': reverse('bcim:TrechoDrenagem_list', args=args, kwargs=kwargs, request=request),
            'trecho-massa-dagua': reverse('bcim:TrechoMassaDagua_list', args=args, kwargs=kwargs, request=request),
            'municipio': reverse('bcim:Municipio_list', args=args, kwargs=kwargs, request=request),
            'outros-limites-oficiais': reverse('bcim:OutrosLimitesOficiais_list', args=args, kwargs=kwargs, request=request),
            'pais': reverse('bcim:Pais_list', args=args, kwargs=kwargs, request=request),
            'terra-indigena-a': reverse('bcim:TerraIndigenaA_list', args=args, kwargs=kwargs, request=request),
            'terra-indigena-p': reverse('bcim:TerraIndigenaP_list', args=args, kwargs=kwargs, request=request),
            'unidade-conservacao-nao-snuc': reverse('bcim:UnidadeConservacaoNaoSnuc_list', args=args, kwargs=kwargs, request=request),
            #'unidade-federacao': reverse('bcim:UnidadeFederacao_list', args=args, kwargs=kwargs, request=request),
            'unidade-protecao-integral': reverse('bcim:UnidadeProtecaoIntegral_list', args=args, kwargs=kwargs, request=request),
            'unidade-uso-sustentavel': reverse('bcim:UnidadeUsoSustentavel_list', args=args, kwargs=kwargs, request=request),
            'aglomerado-rural-isolado': reverse('bcim:AglomeradoRuralIsolado_list', args=args, kwargs=kwargs, request=request),
            'aldeia-indigena': reverse('bcim:AldeiaIndigena_list', args=args, kwargs=kwargs, request=request),
            'area-edificada': reverse('bcim:AreaEdificada_list', args=args, kwargs=kwargs, request=request),
            'capital': reverse('bcim:Capital_list', args=args, kwargs=kwargs, request=request),
            'cidade': reverse('bcim:Cidade_list', args=args, kwargs=kwargs, request=request),
            'vila': reverse('bcim:Vila_list', args=args, kwargs=kwargs, request=request),
            'curva-batimetrica': reverse('bcim:CurvaBatimetrica_list', args=args, kwargs=kwargs, request=request),
            'curva-nivel': reverse('bcim:CurvaNivel_list', args=args, kwargs=kwargs, request=request),
            'duna': reverse('bcim:Duna_list', args=args, kwargs=kwargs, request=request),
            'elemento-fisiografico-natural-l': reverse('bcim:ElementoFisiograficoNaturalL_list', args=args, kwargs=kwargs, request=request),
            'elemento-fisiografico-natural-p': reverse('bcim:ElementoFisiograficoNaturalP_list', args=args, kwargs=kwargs, request=request),
            'pico': reverse('bcim:Pico_list', args=args, kwargs=kwargs, request=request),
            'ponto-cotado-altimetrico': reverse('bcim:PontoCotadoAltimetrico_list', args=args, kwargs=kwargs, request=request),
            'ponto-cotado-batimetrico': reverse('bcim:PontoCotadoBatimetrico_list', args=args, kwargs=kwargs, request=request),
            'eclusa': reverse('bcim:Eclusa_list', args=args, kwargs=kwargs, request=request),
            'edif-constr-aeroportuaria': reverse('bcim:EdifConstrAeroportuaria_list', args=args, kwargs=kwargs, request=request),
            'edif-const-portuaria': reverse('bcim:EdifConstPortuaria_list', args=args, kwargs=kwargs, request=request),
            'edif-metro-ferroviaria': reverse('bcim:EdifMetroFerroviaria_list', args=args, kwargs=kwargs, request=request),
            'pista-ponto-pouso': reverse('bcim:PistaPontoPouso_list', args=args, kwargs=kwargs, request=request),
            'ponte': reverse('bcim:Ponte_list', args=args, kwargs=kwargs, request=request),
            'sinalizacao': reverse('bcim:Sinalizacao_list', args=args, kwargs=kwargs, request=request),
            'travessia-l': reverse('bcim:TravessiaL_list', args=args, kwargs=kwargs, request=request),
            'travessia-p': reverse('bcim:TravessiaP_list', args=args, kwargs=kwargs, request=request),
            'trecho-duto': reverse('bcim:TrechoDuto_list', args=args, kwargs=kwargs, request=request),
            'trecho-ferroviario': reverse('bcim:TrechoFerroviario_list', args=args, kwargs=kwargs, request=request),
            'trecho-hidroviario': reverse('bcim:TrechoHidroviario_list', args=args, kwargs=kwargs, request=request),
            'trecho-rodoviario': reverse('bcim:TrechoRodoviario_list', args=args, kwargs=kwargs, request=request),
            'tunel': reverse('bcim:Tunel_list', args=args, kwargs=kwargs, request=request),
            'brejo-pantano': reverse('bcim:BrejoPantano_list', args=args, kwargs=kwargs, request=request),
            'mangue': reverse('bcim:Mangue_list', args=args, kwargs=kwargs, request=request),
            'veg-restinga': reverse('bcim:VegRestinga_list', args=args, kwargs=kwargs, request=request)
        }
        return Response(data, status=status.HTTP_200_OK, content_type=JSON_CONTENT_TYPE)

class EdifPubMilitarList(FeatureCollectionResource):
    serializer_class = EdifPubMilitarSerializer

class EdifPubMilitarDetail(FeatureResource):
    serializer_class = EdifPubMilitarSerializer

class AdmEdifPubMilitarPList(FeatureCollectionResource):
    serializer_class = AdmEdifPubMilitarPSerializer

class AdmEdifPubMilitarPDetail(FeatureResource):
    serializer_class = AdmEdifPubMilitarPSerializer

class PostoFiscalList(FeatureCollectionResource):
    serializer_class = PostoFiscalSerializer

class PostoFiscalDetail(FeatureResource):
    serializer_class = PostoFiscalSerializer

class EdifAgropecExtVegetalPescaList(FeatureCollectionResource):
    serializer_class = EdifAgropecExtVegetalPescaSerializer

class EdifAgropecExtVegetalPescaDetail(FeatureResource):
    serializer_class = EdifAgropecExtVegetalPescaSerializer

class ExtMineralAList(FeatureCollectionResource):
    serializer_class = ExtMineralASerializer

class ExtMineralADetail(FeatureResource):
    serializer_class = ExtMineralASerializer

class ExtMineralPList(FeatureCollectionResource):
    serializer_class = ExtMineralPSerializer

class ExtMineralPDetail(FeatureResource):
    serializer_class = ExtMineralPSerializer

class EstGeradEnergiaEletricaList(FeatureCollectionResource):
    serializer_class = EstGeradEnergiaEletricaSerializer

class EstGeradEnergiaEletricaDetail(FeatureResource):
    serializer_class = EstGeradEnergiaEletricaSerializer

class HidreletricaList(FeatureCollectionResource):
    serializer_class = HidreletricaSerializer

class HidreletricaDetail(FeatureResource):
    serializer_class = HidreletricaSerializer

class TermeletricaList(FeatureCollectionResource):
    serializer_class = TermeletricaSerializer

class TermeletricaDetail(FeatureResource):
    serializer_class = TermeletricaSerializer

class BancoAreiaList(FeatureCollectionResource):
    serializer_class = BancoAreiaSerializer

class BancoAreiaDetail(FeatureResource):
    serializer_class = BancoAreiaSerializer

class BarragemLList(FeatureCollectionResource):
    serializer_class = BarragemLSerializer

class BarragemLDetail(FeatureResource):
    serializer_class = BarragemLSerializer

class BarragemPList(FeatureCollectionResource):
    serializer_class = BarragemPSerializer

class BarragemPDetail(FeatureResource):
    serializer_class = BarragemPSerializer

class CorredeiraLList(FeatureCollectionResource):
    serializer_class = CorredeiraLSerializer

class CorredeiraLDetail(FeatureResource):
    serializer_class = CorredeiraLSerializer

class CorredeiraPList(FeatureCollectionResource):
    serializer_class = CorredeiraPSerializer

class CorredeiraPDetail(FeatureResource):
    serializer_class = CorredeiraPSerializer

class IlhaList(FeatureCollectionResource):
    serializer_class = IlhaSerializer

class IlhaDetail(FeatureResource):
    serializer_class = IlhaSerializer

class MassaDaguaList(FeatureCollectionResource):
    serializer_class = MassaDaguaSerializer

class MassaDaguaDetail(FeatureResource):
    serializer_class = MassaDaguaSerializer

class QuedaDaguaList(FeatureCollectionResource):
    serializer_class = QuedaDaguaSerializer

class QuedaDaguaDetail(FeatureResource):
    serializer_class = QuedaDaguaSerializer

class RecifeList(FeatureCollectionResource):
    serializer_class = RecifeSerializer

class RecifeDetail(FeatureResource):
    serializer_class = RecifeSerializer

class RochaEmAguaList(FeatureCollectionResource):
    serializer_class = RochaEmAguaSerializer

class RochaEmAguaDetail(FeatureResource):
    serializer_class = RochaEmAguaSerializer

class SumidouroVertedouroList(FeatureCollectionResource):
    serializer_class = SumidouroVertedouroSerializer

class SumidouroVertedouroDetail(FeatureResource):
    serializer_class = SumidouroVertedouroSerializer

class TerrenoSujeitoInundacaoList(FeatureCollectionResource):
    serializer_class = TerrenoSujeitoInundacaoSerializer

class TerrenoSujeitoInundacaoDetail(FeatureResource):
    serializer_class = TerrenoSujeitoInundacaoSerializer

class TrechoDrenagemList(FeatureCollectionResource):
    serializer_class = TrechoDrenagemSerializer

class TrechoDrenagemDetail(FeatureResource):
    serializer_class = TrechoDrenagemSerializer

class TrechoMassaDaguaList(FeatureCollectionResource):
    serializer_class = TrechoMassaDaguaSerializer

class TrechoMassaDaguaDetail(FeatureResource):
    serializer_class = TrechoMassaDaguaSerializer

class MunicipioList(FeatureCollectionResource):
    serializer_class = MunicipioSerializer

class MunicipioDetail(FeatureResource):
    serializer_class = MunicipioSerializer

class OutrosLimitesOficiaisList(FeatureCollectionResource):
    serializer_class = OutrosLimitesOficiaisSerializer

class OutrosLimitesOficiaisDetail(FeatureResource):
    serializer_class = OutrosLimitesOficiaisSerializer

class PaisList(FeatureCollectionResource):
    serializer_class = PaisSerializer

class PaisDetail(FeatureResource):
    serializer_class = PaisSerializer

class TerraIndigenaAList(FeatureCollectionResource):
    serializer_class = TerraIndigenaASerializer

class TerraIndigenaADetail(FeatureResource):
    serializer_class = TerraIndigenaASerializer

class TerraIndigenaPList(FeatureCollectionResource):
    serializer_class = TerraIndigenaPSerializer

class TerraIndigenaPDetail(FeatureResource):
    serializer_class = TerraIndigenaPSerializer

class UnidadeConservacaoNaoSnucList(FeatureCollectionResource):
    serializer_class = UnidadeConservacaoNaoSnucSerializer

class UnidadeConservacaoNaoSnucDetail(FeatureResource):
    serializer_class = UnidadeConservacaoNaoSnucSerializer

class UnidadesFederativasList(FeatureCollectionResource):
    serializer_class = UnidadeFederacaoSerializer

class UnidadesFederativasDetail(FeatureResource):
    serializer_class = UnidadeFederacaoSerializer

class UnidadeProtecaoIntegralList(FeatureCollectionResource):
    serializer_class = UnidadeProtecaoIntegralSerializer

class UnidadeProtecaoIntegralDetail(FeatureResource):
    serializer_class = UnidadeProtecaoIntegralSerializer

class UnidadeUsoSustentavelList(FeatureCollectionResource):
    serializer_class = UnidadeUsoSustentavelSerializer

class UnidadeUsoSustentavelDetail(FeatureResource):
    serializer_class = UnidadeUsoSustentavelSerializer

class AglomeradoRuralIsoladoList(FeatureCollectionResource):
    serializer_class = AglomeradoRuralIsoladoSerializer

class AglomeradoRuralIsoladoDetail(FeatureResource):
    serializer_class = AglomeradoRuralIsoladoSerializer

class AldeiaIndigenaList(FeatureCollectionResource):
    serializer_class = AldeiaIndigenaSerializer

class AldeiaIndigenaDetail(FeatureResource):
    serializer_class = AldeiaIndigenaSerializer

class AreaEdificadaList(FeatureCollectionResource):
    serializer_class = AreaEdificadaSerializer

class AreaEdificadaDetail(FeatureResource):
    serializer_class = AreaEdificadaSerializer

class CapitalList(FeatureCollectionResource):
    serializer_class = CapitalSerializer

class CapitalDetail(FeatureResource):
    serializer_class = CapitalSerializer

class CidadeList(FeatureCollectionResource):
    serializer_class = CidadeSerializer

class CidadeDetail(FeatureResource):
    serializer_class = CidadeSerializer

class VilaList(FeatureCollectionResource):
    serializer_class = VilaSerializer

class VilaDetail(FeatureResource):
    serializer_class = VilaSerializer

class CurvaBatimetricaList(FeatureCollectionResource):
    serializer_class = CurvaBatimetricaSerializer

class CurvaBatimetricaDetail(FeatureResource):
    serializer_class = CurvaBatimetricaSerializer

class CurvaNivelList(FeatureCollectionResource):
    serializer_class = CurvaNivelSerializer

class CurvaNivelDetail(FeatureResource):
    serializer_class = CurvaNivelSerializer

class DunaList(FeatureCollectionResource):
    serializer_class = DunaSerializer

class DunaDetail(FeatureResource):
    serializer_class = DunaSerializer

class ElementoFisiograficoNaturalLList(FeatureCollectionResource):
    serializer_class = ElementoFisiograficoNaturalLSerializer

class ElementoFisiograficoNaturalLDetail(FeatureResource):
    serializer_class = ElementoFisiograficoNaturalLSerializer

class ElementoFisiograficoNaturalPList(FeatureCollectionResource):
    serializer_class = ElementoFisiograficoNaturalPSerializer

class ElementoFisiograficoNaturalPDetail(FeatureResource):
    serializer_class = ElementoFisiograficoNaturalPSerializer

class PicoList(FeatureCollectionResource):
    serializer_class = PicoSerializer

class PicoDetail(FeatureResource):
    serializer_class = PicoSerializer

class PontoCotadoAltimetricoList(FeatureCollectionResource):
    serializer_class = PontoCotadoAltimetricoSerializer

class PontoCotadoAltimetricoDetail(FeatureResource):
    serializer_class = PontoCotadoAltimetricoSerializer

class PontoCotadoBatimetricoList(FeatureCollectionResource):
    serializer_class = PontoCotadoBatimetricoSerializer

class PontoCotadoBatimetricoDetail(FeatureResource):
    serializer_class = PontoCotadoBatimetricoSerializer

class EclusaList(FeatureCollectionResource):
    serializer_class = EclusaSerializer

class EclusaDetail(FeatureResource):
    serializer_class = EclusaSerializer

class EdifConstrAeroportuariaList(FeatureCollectionResource):
    serializer_class = EdifConstrAeroportuariaSerializer

class EdifConstrAeroportuariaDetail(FeatureResource):
    serializer_class = EdifConstrAeroportuariaSerializer

class EdifConstPortuariaList(FeatureCollectionResource):
    serializer_class = EdifConstPortuariaSerializer

class EdifConstPortuariaDetail(FeatureResource):
    serializer_class = EdifConstPortuariaSerializer

class EdifMetroFerroviariaList(FeatureCollectionResource):
    serializer_class = EdifMetroFerroviariaSerializer

class EdifMetroFerroviariaDetail(FeatureResource):
    serializer_class = EdifMetroFerroviariaSerializer

class PistaPontoPousoList(FeatureCollectionResource):
    serializer_class = PistaPontoPousoSerializer

class PistaPontoPousoDetail(FeatureResource):
    serializer_class = PistaPontoPousoSerializer

class PonteList(FeatureCollectionResource):
    serializer_class = PonteSerializer

class PonteDetail(FeatureResource):
    serializer_class = PonteSerializer

class SinalizacaoList(FeatureCollectionResource):
    serializer_class = SinalizacaoSerializer

class SinalizacaoDetail(FeatureResource):
    serializer_class = SinalizacaoSerializer

class TravessiaLList(FeatureCollectionResource):
    serializer_class = TravessiaLSerializer

class TravessiaLDetail(FeatureResource):
    serializer_class = TravessiaLSerializer

class TravessiaPList(FeatureCollectionResource):
    serializer_class = TravessiaPSerializer

class TravessiaPDetail(FeatureResource):
    serializer_class = TravessiaPSerializer

class TrechoDutoList(FeatureCollectionResource):
    serializer_class = TrechoDutoSerializer

class TrechoDutoDetail(FeatureResource):
    serializer_class = TrechoDutoSerializer

class TrechoFerroviarioList(FeatureCollectionResource):
    serializer_class = TrechoFerroviarioSerializer

class TrechoFerroviarioDetail(FeatureResource):
    serializer_class = TrechoFerroviarioSerializer

class TrechoHidroviarioList(FeatureCollectionResource):
    serializer_class = TrechoHidroviarioSerializer

class TrechoHidroviarioDetail(FeatureResource):
    serializer_class = TrechoHidroviarioSerializer

class TrechoRodoviarioList(FeatureCollectionResource):
    serializer_class = TrechoRodoviarioSerializer

class TrechoRodoviarioDetail(FeatureResource):
    serializer_class = TrechoRodoviarioSerializer

class TunelList(FeatureCollectionResource):
    serializer_class = TunelSerializer

class TunelDetail(FeatureResource):
    serializer_class = TunelSerializer

class BrejoPantanoList(FeatureCollectionResource):
    serializer_class = BrejoPantanoSerializer

class BrejoPantanoDetail(FeatureResource):
    serializer_class = BrejoPantanoSerializer

class MangueList(FeatureCollectionResource):
    serializer_class = MangueSerializer

class MangueDetail(FeatureResource):
    serializer_class = MangueSerializer

class VegRestingaList(FeatureCollectionResource):
    serializer_class = VegRestingaSerializer

class VegRestingaDetail(FeatureResource):
    serializer_class = VegRestingaSerializer