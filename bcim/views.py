from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.reverse import reverse
from hyper_resource.resources.AbstractResource import AbstractResource, CONTENT_TYPE_JSONLD, JSON_CONTENT_TYPE, \
    RequiredObject
from hyper_resource.resources.FeatureCollectionResource import FeatureCollectionResource
from hyper_resource.resources.FeatureResource import FeatureResource
from .serializers import *

# ============================ Hyper Resource Classes ============================


#  ============================ BCIM Resource Classes  ============================

class APIRoot(AbstractResource):

    def add_entry_point_link_header(self, request, response):
        entry_point_uri = request.build_absolute_uri()[:-1]
        link_content = '<' + entry_point_uri + '>; rel="https://schema.org/EntryPoint", '
        link_content += '<' + entry_point_uri + '.jsonld>; rel="http://www.w3.org/ns/json-ld#context"; type="application/ld+json"'
        response["Link"] = link_content

    def get_entry_point_data(self, request, *args, **kwargs):
        return {
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
            'veg-restinga': reverse('bcim:VegRestinga_list', args=args, kwargs=kwargs, request=request),
            #'marker-icon.png': reverse('bcim:Icon_detail', args=args, kwargs=kwargs, request=request),
        }

    def get(self, request, *args, **kwargs):
        data = self.get_entry_point_data(request, *args, **kwargs)
        response = Response(data, status=status.HTTP_200_OK, content_type=JSON_CONTENT_TYPE)
        self.add_entry_point_link_header(request, response)
        return response

    # todo: maybe this content make more sanse in contexts.py
    def options(self, request, *args, **kwargs):
        entry_point_keys = self.get_entry_point_data(request, *args, **kwargs).keys()
        context = {"@context": {"hydra": "https://www.w3.org/ns/hydra/core#"}}
        for key in entry_point_keys:
            context["@context"].update({
                key: {
                    "@id": "https://purl.org/geojson/vocab#FeatureCollection",
                    "@type": "@id"
                }
            })

        context["hydra:supportedProperty"] = []

        for key in entry_point_keys:
            context["hydra:supportedProperty"].append({
                "hydra:property": key,
                "hydra:writable": False,
                "hydra:readable": True,
                "hydra:required": False
            })

        response = Response(context, status=status.HTTP_200_OK, content_type=CONTENT_TYPE_JSONLD)
        self.add_entry_point_link_header(request, response)
        return response
        #return Response(context, status=status.HTTP_200_OK, content_type=CONTENT_TYPE_JSONLD)

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

    def __init__(self):
        super().__init__()
        self.metadata_uri = "http://www.metadados.geo.ibge.gov.br/geonetwork_ibge/srv/por/csw?request=GetRecordById&service=CSW&version=2.0.2&elementSetName=full&id=ff2d4215-9843-4137-bad9-c15f2a8caa9e"
        #self.metadata_uri = "http://www.metadados.inde.gov.br/geonetwork/srv/en/resources.get?request=GetRecordById&service=CSW&version=2.0.2&elementSetName=full&id=425971af-1be0-4f32-81c4-a2d78bb01a85"
        self.style_uri = "http://localhost:8000/api/restful-ide/bcim/unidade-federativa.sld"

class UnidadesFederativasDetail(FeatureResource):
    serializer_class = UnidadeFederacaoSerializer

    def __init__(self):
        super().__init__()
        self.metadata_uri = "http://www.metadados.geo.ibge.gov.br/geonetwork_ibge/srv/por/csw?request=GetRecordById&service=CSW&version=2.0.2&elementSetName=full&id=ff2d4215-9843-4137-bad9-c15f2a8caa9e"
        self.style_uri = "http://localhost:8000/api/restful-ide/bcim/unidade-federativa.sld"

    def basic_get(self, request, *args, **kwargs):
        query_dict = {}

        try:
            query_dict["sigla"] = kwargs["sigla"]
        except KeyError:
            return super().basic_get(request, *args, **kwargs)

        object = get_object_or_404(self.serializer_class.Meta.model, **query_dict)

        if "operation" in kwargs:
            return self.required_object_for_operation(request, object, *args, **kwargs)

        contype_accept = self.feature_utils.content_type_by_accept(request, *args, kwargs)
        serialize_data = self.serialize_object(request, object, contype_accept)
        return RequiredObject(serialize_data, contype_accept, 200)

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

"""
class IconDetail(AbstractResource):
    def get(self, reqest, *args, **kwargs):
        with open("marker-icon.png", "rb") as icon:
            content = icon.read()
        return HttpResponse(
            content,
            status=200,
            content_type="image/png"
        )
"""