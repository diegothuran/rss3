# coding: utf-8

import sys
sys.path.insert(0, '../../src')

' import pages by state '
from pages.acre import agazetadoacre, jornalatribuna, jornalopiniao, jornalopiniao_economia, jornalopiniao_policia, jornalopiniao_politica, oaltoacre,\
oestadoacre, oriobranco_geral, oriobranco_policial, oriobranco_politica, pagina20, pagina20_economia, pagina20_policia, pagina20_politica

from pages.alagoas import anoticia, cadaminuto, correiodopovo, gazetadealagoas, gazetaweb, novoextra, primeiraedicao, tribunahoje, tribunauniao

from pages.amapa import aquiamapa, diariodoamapa

from pages.amazonas import diariodoamazonas, ojornaldailha, osolimoes

from pages.bahia import aregiao, atarde, correiodooeste, folharegionalbahia, folhasertaneja, istoenoticia, jornalalerta, jornalanossavoz, jornalfolhadoestado,\
jornalimpacto, jornalnovafronteira, novoeste, oecojornal, rss_diariobahia, tribunafeirense

from pages.ceara import anoticiadoceara, folhadosertaoce, oestadoce, opovo, tribunadoceara

from pages.distrito_federal import camara, correiobraziliense, diariodeceilandia, folhacentrooeste, jornaldebrasilia, jornalregional, rss_estacaonews, rss_senado

from pages.espirito_santo import aquinoticias, correiodoestadoonline, estadocapixaba, gazetaonline, jornalcorreiocapixaba, noticiaagora, rss_folhaonline, tribunaonline

from pages.goias import diariodeaparecida, diariodoestadogo, jornalaguaslindas, jornaldiariodonorte, jornalestadodegoias, oanapolis, ohoje, opopular, \
rss_jornalopcao, tribunadoplanalto

from pages.maranhao import atosefatos, oestadoma, oimparcial, oquartopoder

' import Gabriel pages '
from pages.gabriel import agenciabrasil, apublica, avozeavezdajuventude, b9, balaiodokotscho, blastingnews, blogdafloresta, blogdoataide, blogdoluciosorge,\
blogdomaringoni, blogdomello, blogdomiro, blogdopaulonunes, blogdoprimo, blogdoriella, blogdorovai, blogdoskarlack, blogmarcosfrahm, buzzfeed_news_br,\
carta_maior, cartamaior, ceticismopolitico, cinegnose, comunicadores, congressoemfoco, correiodobrasil, diariodocentrodomundo, diplomatique, domingoscosta,\
ebc, elielbezerra, estadao, extra_globo, fabiocampana, falandoverdades, folha_piaui, folha_sp, gospelprime, grandesnomesdapropaganda, huffpostbrasil, \
imprensaviva, istoe, jaderbarbalho, jornais_virtuais, jornaldocomercio, jornallivre, jota, justificando, marcossilverio, migalhas, moneytimes,\
mundodomarketing, natelinha, observatoriodatelevisao, ocafezinho, ocombatente, operamundi, osamigosdopresidentelula, osdivergentes, otvfoco, outraspalavras, \
papelpop, polibiobraga, politicanarede, poncheverde, portaldapropaganda, ptnacamara, revistaforum, revistapress, rss_multiplos, rufandobombo, saibamais, \
sputniknews, telepadi, telesintese, tijolaco, tribunadainternet, tribunadajustiça, veja, viomundo

' import general pages '
from pages import agenciabrasil_ebc, bastidoresdopoder, bbc, cartacapital, correio24horas, diariocatarinense, diariodocentrodomundo, \
diariodocentrodomundo_mundo, diariodonordeste, dinheirorural, elpais, exame, gauchazh, gazetadopovo, globo_eleicoes, infomoney, istoedinheiro, jornalestadodeminas, \
jovempan, justificando_artigos, justificando, marceloauler, ne10, oantagonista, r7, rss_globo, terra_noticias, tnh1, tribunadosertao, veja_ultimas

""" List of pages """
PAGES = [# page from the states
         agazetadoacre, jornalatribuna, jornalopiniao, jornalopiniao_economia, jornalopiniao_policia, jornalopiniao_politica, oaltoacre,
         oestadoacre, oriobranco_geral, oriobranco_policial, oriobranco_politica, pagina20, pagina20_economia, pagina20_policia, pagina20_politica,
         anoticia, cadaminuto, correiodopovo, gazetadealagoas, gazetaweb, novoextra, primeiraedicao, tribunahoje, tribunauniao,
         aquiamapa, diariodoamapa, diariodoamazonas, ojornaldailha, osolimoes, aregiao, atarde, correiodooeste, folharegionalbahia, folhasertaneja, 
         istoenoticia, jornalalerta, jornalanossavoz, jornalfolhadoestado, jornalimpacto, jornalnovafronteira, novoeste, oecojornal, rss_diariobahia, tribunafeirense,
         anoticiadoceara, folhadosertaoce, oestadoce, opovo, tribunadoceara, camara, correiobraziliense, diariodeceilandia, folhacentrooeste, jornaldebrasilia, 
         jornalregional, rss_estacaonews, rss_senado, aquinoticias, correiodoestadoonline, estadocapixaba, gazetaonline, jornalcorreiocapixaba, noticiaagora, 
         rss_folhaonline, tribunaonline, diariodeaparecida, diariodoestadogo, jornalaguaslindas, jornaldiariodonorte, jornalestadodegoias, oanapolis, ohoje, 
         opopular, rss_jornalopcao, tribunadoplanalto, atosefatos, oestadoma, oimparcial, oquartopoder,
         # pages ate o maranhao
         agenciabrasil, apublica, avozeavezdajuventude, b9, balaiodokotscho, blastingnews, blogdafloresta, blogdoataide, blogdoluciosorge, blogdomaringoni, 
         blogdomello, blogdomiro, blogdopaulonunes, blogdoprimo, blogdoriella, blogdorovai, blogdoskarlack, blogmarcosfrahm, buzzfeed_news_br, carta_maior, 
         cartamaior, ceticismopolitico, cinegnose, comunicadores, congressoemfoco, correiodobrasil, diariodocentrodomundo, diplomatique, domingoscosta,
         ebc, elielbezerra, estadao, extra_globo, fabiocampana, falandoverdades, folha_piaui, folha_sp, gospelprime, grandesnomesdapropaganda, huffpostbrasil, 
         imprensaviva, istoe, jaderbarbalho, jornais_virtuais, jornaldocomercio, jornallivre, jota, justificando, marcossilverio, migalhas, moneytimes,
         mundodomarketing, natelinha, observatoriodatelevisao, ocafezinho, ocombatente, osamigosdopresidentelula, osdivergentes, outraspalavras, 
         papelpop, politicanarede, poncheverde, portaldapropaganda, ptnacamara, revistaforum, revistapress, rss_multiplos, rufandobombo, saibamais, 
         sputniknews, telepadi, telesintese, tijolaco, tribunadainternet, tribunadajustiça, veja, viomundo,
         
         agenciabrasil_ebc, bastidoresdopoder, bbc, cartacapital, correio24horas, diariocatarinense, diariodocentrodomundo, diariodocentrodomundo_mundo,
         diariodonordeste, dinheirorural, elpais, exame, gauchazh, gazetadopovo, globo_eleicoes, infomoney, istoedinheiro, jornalestadodeminas, jovempan, 
         justificando_artigos, justificando, marceloauler, ne10, oantagonista, r7, rss_globo, terra_noticias, tnh1, tribunadosertao, veja_ultimas]