path('edif-pub-militar/<int:pk>', EdifPubMilitarDetail.as_view(), name='EdifPubMilitar_detail'),
path('edif-pub-militar', EdifPubMilitarList.as_view(), name='EdifPubMilitar_list'),

path('adm-edif-pub-militar-p/<int:pk>', AdmEdifPubMilitarPDetail.as_view(), name='AdmEdifPubMilitarP_detail'),
path('adm-edif-pub-militar-p', AdmEdifPubMilitarPList.as_view(), name='AdmEdifPubMilitarP_list'),

path('posto-fiscal/<int:pk>', PostoFiscalDetail.as_view(), name='PostoFiscal_detail'),
path('posto-fiscal', PostoFiscalList.as_view(), name='PostoFiscal_list'),

path('edif-agropec-ext-vegetal-pesca/<int:pk>', EdifAgropecExtVegetalPescaDetail.as_view(), name='EdifAgropecExtVegetalPesca_detail'),
path('edif-agropec-ext-vegetal-pesca', EdifAgropecExtVegetalPescaList.as_view(), name='EdifAgropecExtVegetalPesca_list'),

path('ext-mineral-a/<int:pk>', ExtMineralADetail.as_view(), name='ExtMineralA_detail'),
path('ext-mineral-a', ExtMineralAList.as_view(), name='ExtMineralA_list'),

path('ext-mineral-p/<int:pk>', ExtMineralPDetail.as_view(), name='ExtMineralP_detail'),
path('ext-mineral-p', ExtMineralPList.as_view(), name='ExtMineralP_list'),

path('est-gerad-energia-eletrica/<int:pk>', EstGeradEnergiaEletricaDetail.as_view(), name='EstGeradEnergiaEletrica_detail'),
path('est-gerad-energia-eletrica', EstGeradEnergiaEletricaList.as_view(), name='EstGeradEnergiaEletrica_list'),

path('hidreletrica/<int:pk>', HidreletricaDetail.as_view(), name='Hidreletrica_detail'),
path('hidreletrica', HidreletricaList.as_view(), name='Hidreletrica_list'),

path('termeletrica/<int:pk>', TermeletricaDetail.as_view(), name='Termeletrica_detail'),
path('termeletrica', TermeletricaList.as_view(), name='Termeletrica_list'),

path('banco-areia/<int:pk>', BancoAreiaDetail.as_view(), name='BancoAreia_detail'),
path('banco-areia', BancoAreiaList.as_view(), name='BancoAreia_list'),

path('barragem-l/<int:pk>', BarragemLDetail.as_view(), name='BarragemL_detail'),
path('barragem-l', BarragemLList.as_view(), name='BarragemL_list'),

path('barragem-p/<int:pk>', BarragemPDetail.as_view(), name='BarragemP_detail'),
path('barragem-p', BarragemPList.as_view(), name='BarragemP_list'),

path('corredeira-l/<int:pk>', CorredeiraLDetail.as_view(), name='CorredeiraL_detail'),
path('corredeira-l', CorredeiraLList.as_view(), name='CorredeiraL_list'),

path('corredeira-p/<int:pk>', CorredeiraPDetail.as_view(), name='CorredeiraP_detail'),
path('corredeira-p', CorredeiraPList.as_view(), name='CorredeiraP_list'),

path('ilha/<int:pk>', IlhaDetail.as_view(), name='Ilha_detail'),
path('ilha', IlhaList.as_view(), name='Ilha_list'),

path('massa-dagua/<int:pk>', MassaDaguaDetail.as_view(), name='MassaDagua_detail'),
path('massa-dagua', MassaDaguaList.as_view(), name='MassaDagua_list'),

path('queda-dagua/<int:pk>', QuedaDaguaDetail.as_view(), name='QuedaDagua_detail'),
path('queda-dagua', QuedaDaguaList.as_view(), name='QuedaDagua_list'),

path('recife/<int:pk>', RecifeDetail.as_view(), name='Recife_detail'),
path('recife', RecifeList.as_view(), name='Recife_list'),

path('rocha-em-agua/<int:pk>', RochaEmAguaDetail.as_view(), name='RochaEmAgua_detail'),
path('rocha-em-agua', RochaEmAguaList.as_view(), name='RochaEmAgua_list'),

path('sumidouro-vertedouro/<int:pk>', SumidouroVertedouroDetail.as_view(), name='SumidouroVertedouro_detail'),
path('sumidouro-vertedouro', SumidouroVertedouroList.as_view(), name='SumidouroVertedouro_list'),

path('terreno-sujeito-inundacao/<int:pk>', TerrenoSujeitoInundacaoDetail.as_view(), name='TerrenoSujeitoInundacao_detail'),
path('terreno-sujeito-inundacao', TerrenoSujeitoInundacaoList.as_view(), name='TerrenoSujeitoInundacao_list'),

path('trecho-drenagem/<int:pk>', TrechoDrenagemDetail.as_view(), name='TrechoDrenagem_detail'),
path('trecho-drenagem', TrechoDrenagemList.as_view(), name='TrechoDrenagem_list'),

path('trecho-massa-dagua/<int:pk>', TrechoMassaDaguaDetail.as_view(), name='TrechoMassaDagua_detail'),
path('trecho-massa-dagua', TrechoMassaDaguaList.as_view(), name='TrechoMassaDagua_list'),

path('municipio/<int:pk>', MunicipioDetail.as_view(), name='Municipio_detail'),
path('municipio', MunicipioList.as_view(), name='Municipio_list'),

path('outros-limites-oficiais/<int:pk>', OutrosLimitesOficiaisDetail.as_view(), name='OutrosLimitesOficiais_detail'),
path('outros-limites-oficiais', OutrosLimitesOficiaisList.as_view(), name='OutrosLimitesOficiais_list'),

path('pais/<int:pk>', PaisDetail.as_view(), name='Pais_detail'),
path('pais', PaisList.as_view(), name='Pais_list'),

path('terra-indigena-a/<int:pk>', TerraIndigenaADetail.as_view(), name='TerraIndigenaA_detail'),
path('terra-indigena-a', TerraIndigenaAList.as_view(), name='TerraIndigenaA_list'),

path('terra-indigena-p/<int:pk>', TerraIndigenaPDetail.as_view(), name='TerraIndigenaP_detail'),
path('terra-indigena-p', TerraIndigenaPList.as_view(), name='TerraIndigenaP_list'),

path('unidade-conservacao-nao-snuc/<int:pk>', UnidadeConservacaoNaoSnucDetail.as_view(), name='UnidadeConservacaoNaoSnuc_detail'),
path('unidade-conservacao-nao-snuc', UnidadeConservacaoNaoSnucList.as_view(), name='UnidadeConservacaoNaoSnuc_list'),

path('unidade-federacao/<int:pk>', UnidadeFederacaoDetail.as_view(), name='UnidadeFederacao_detail'),
path('unidade-federacao', UnidadeFederacaoList.as_view(), name='UnidadeFederacao_list'),

path('unidade-protecao-integral/<int:pk>', UnidadeProtecaoIntegralDetail.as_view(), name='UnidadeProtecaoIntegral_detail'),
path('unidade-protecao-integral', UnidadeProtecaoIntegralList.as_view(), name='UnidadeProtecaoIntegral_list'),

path('unidade-uso-sustentavel/<int:pk>', UnidadeUsoSustentavelDetail.as_view(), name='UnidadeUsoSustentavel_detail'),
path('unidade-uso-sustentavel', UnidadeUsoSustentavelList.as_view(), name='UnidadeUsoSustentavel_list'),

path('aglomerado-rural-isolado/<int:pk>', AglomeradoRuralIsoladoDetail.as_view(), name='AglomeradoRuralIsolado_detail'),
path('aglomerado-rural-isolado', AglomeradoRuralIsoladoList.as_view(), name='AglomeradoRuralIsolado_list'),

path('aldeia-indigena/<int:pk>', AldeiaIndigenaDetail.as_view(), name='AldeiaIndigena_detail'),
path('aldeia-indigena', AldeiaIndigenaList.as_view(), name='AldeiaIndigena_list'),

path('area-edificada/<int:pk>', AreaEdificadaDetail.as_view(), name='AreaEdificada_detail'),
path('area-edificada', AreaEdificadaList.as_view(), name='AreaEdificada_list'),

path('capital/<int:pk>', CapitalDetail.as_view(), name='Capital_detail'),
path('capital', CapitalList.as_view(), name='Capital_list'),

path('cidade/<int:pk>', CidadeDetail.as_view(), name='Cidade_detail'),
path('cidade', CidadeList.as_view(), name='Cidade_list'),

path('vila/<int:pk>', VilaDetail.as_view(), name='Vila_detail'),
path('vila', VilaList.as_view(), name='Vila_list'),

path('curva-batimetrica/<int:pk>', CurvaBatimetricaDetail.as_view(), name='CurvaBatimetrica_detail'),
path('curva-batimetrica', CurvaBatimetricaList.as_view(), name='CurvaBatimetrica_list'),

path('curva-nivel/<int:pk>', CurvaNivelDetail.as_view(), name='CurvaNivel_detail'),
path('curva-nivel', CurvaNivelList.as_view(), name='CurvaNivel_list'),

path('duna/<int:pk>', DunaDetail.as_view(), name='Duna_detail'),
path('duna', DunaList.as_view(), name='Duna_list'),

path('elemento-fisiografico-natural-l/<int:pk>', ElementoFisiograficoNaturalLDetail.as_view(), name='ElementoFisiograficoNaturalL_detail'),
path('elemento-fisiografico-natural-l', ElementoFisiograficoNaturalLList.as_view(), name='ElementoFisiograficoNaturalL_list'),

path('elemento-fisiografico-natural-p/<int:pk>', ElementoFisiograficoNaturalPDetail.as_view(), name='ElementoFisiograficoNaturalP_detail'),
path('elemento-fisiografico-natural-p', ElementoFisiograficoNaturalPList.as_view(), name='ElementoFisiograficoNaturalP_list'),

path('pico/<int:pk>', PicoDetail.as_view(), name='Pico_detail'),
path('pico', PicoList.as_view(), name='Pico_list'),

path('ponto-cotado-altimetrico/<int:pk>', PontoCotadoAltimetricoDetail.as_view(), name='PontoCotadoAltimetrico_detail'),
path('ponto-cotado-altimetrico', PontoCotadoAltimetricoList.as_view(), name='PontoCotadoAltimetrico_list'),

path('ponto-cotado-batimetrico/<int:pk>', PontoCotadoBatimetricoDetail.as_view(), name='PontoCotadoBatimetrico_detail'),
path('ponto-cotado-batimetrico', PontoCotadoBatimetricoList.as_view(), name='PontoCotadoBatimetrico_list'),

path('eclusa/<int:pk>', EclusaDetail.as_view(), name='Eclusa_detail'),
path('eclusa', EclusaList.as_view(), name='Eclusa_list'),

path('edif-constr-aeroportuaria/<int:pk>', EdifConstrAeroportuariaDetail.as_view(), name='EdifConstrAeroportuaria_detail'),
path('edif-constr-aeroportuaria', EdifConstrAeroportuariaList.as_view(), name='EdifConstrAeroportuaria_list'),

path('edif-const-portuaria/<int:pk>', EdifConstPortuariaDetail.as_view(), name='EdifConstPortuaria_detail'),
path('edif-const-portuaria', EdifConstPortuariaList.as_view(), name='EdifConstPortuaria_list'),

path('edif-metro-ferroviaria/<int:pk>', EdifMetroFerroviariaDetail.as_view(), name='EdifMetroFerroviaria_detail'),
path('edif-metro-ferroviaria', EdifMetroFerroviariaList.as_view(), name='EdifMetroFerroviaria_list'),

path('pista-ponto-pouso/<int:pk>', PistaPontoPousoDetail.as_view(), name='PistaPontoPouso_detail'),
path('pista-ponto-pouso', PistaPontoPousoList.as_view(), name='PistaPontoPouso_list'),

path('ponte/<int:pk>', PonteDetail.as_view(), name='Ponte_detail'),
path('ponte', PonteList.as_view(), name='Ponte_list'),

path('sinalizacao/<int:pk>', SinalizacaoDetail.as_view(), name='Sinalizacao_detail'),
path('sinalizacao', SinalizacaoList.as_view(), name='Sinalizacao_list'),

path('travessia-l/<int:pk>', TravessiaLDetail.as_view(), name='TravessiaL_detail'),
path('travessia-l', TravessiaLList.as_view(), name='TravessiaL_list'),

path('travessia-p/<int:pk>', TravessiaPDetail.as_view(), name='TravessiaP_detail'),
path('travessia-p', TravessiaPList.as_view(), name='TravessiaP_list'),

path('trecho-duto/<int:pk>', TrechoDutoDetail.as_view(), name='TrechoDuto_detail'),
path('trecho-duto', TrechoDutoList.as_view(), name='TrechoDuto_list'),

path('trecho-ferroviario/<int:pk>', TrechoFerroviarioDetail.as_view(), name='TrechoFerroviario_detail'),
path('trecho-ferroviario', TrechoFerroviarioList.as_view(), name='TrechoFerroviario_list'),

path('trecho-hidroviario/<int:pk>', TrechoHidroviarioDetail.as_view(), name='TrechoHidroviario_detail'),
path('trecho-hidroviario', TrechoHidroviarioList.as_view(), name='TrechoHidroviario_list'),

path('trecho-rodoviario/<int:pk>', TrechoRodoviarioDetail.as_view(), name='TrechoRodoviario_detail'),
path('trecho-rodoviario', TrechoRodoviarioList.as_view(), name='TrechoRodoviario_list'),

path('tunel/<int:pk>', TunelDetail.as_view(), name='Tunel_detail'),
path('tunel', TunelList.as_view(), name='Tunel_list'),

path('brejo-pantano/<int:pk>', BrejoPantanoDetail.as_view(), name='BrejoPantano_detail'),
path('brejo-pantano', BrejoPantanoList.as_view(), name='BrejoPantano_list'),

path('mangue/<int:pk>', MangueDetail.as_view(), name='Mangue_detail'),
path('mangue', MangueList.as_view(), name='Mangue_list'),

path('veg-restinga/<int:pk>', VegRestingaDetail.as_view(), name='VegRestinga_detail'),
path('veg-restinga', VegRestingaList.as_view(), name='VegRestinga_list'),

