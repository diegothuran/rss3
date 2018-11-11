# coding: utf-8

import sys
sys.path.insert(0, '../../src')

' import pages by state '
from pages.acre import agazetadoacre, jornalatribuna, jornalopiniao, jornalopiniao_economia, jornalopiniao_policia, jornalopiniao_politica, oaltoacre,\
oestadoacre, oriobranco_geral, oriobranco_policial, oriobranco_politica, pagina20, pagina20_economia, pagina20_policia, pagina20_politica

from pages.alagoas import anoticia, cadaminuto, correiodopovo, gazetadealagoas, gazetaweb, novoextra, primeiraedicao, tribunahoje, tribunauniao

from pages.amapa import aquiamapa, diariodoamapa

from pages.amazonas import acritica_am, ojornaldailha, osolimoes

from pages.bahia import aregiao, atarde, correiodooeste, folharegionalbahia, folhasertaneja, istoenoticia, jornalalerta, jornalanossavoz, jornalfolhadoestado,\
jornalimpacto, jornalnovafronteira, novoeste, oecojornal, rss_diariobahia, tribunafeirense

from pages.ceara import anoticiadoceara, oestadoce, opovo, tribunadoceara

from pages.distrito_federal import camara, correiobraziliense, folhacentrooeste, jornaldebrasilia, jornalregional, rss_estacaonews, rss_senado

from pages.espirito_santo import aquinoticias, correiodoestadoonline, estadocapixaba, gazetaonline, jornalcorreiocapixaba, noticiaagora, \
rss_folhaonline, tribunaonline

from pages.goias import diariodeaparecida, diariodoestadogo, jornalaguaslindas, jornalopcao, jornalestadodegoias, oanapolis, ohoje, opopular, \
rss_jornalopcao, tribunadoplanalto

from pages.maranhao import atosefatos, oestadoma, oquartopoder

' import Gabriel pages '
from pages.gabriel import abert, abi, administradores, adrenaline, agenciabrasil, ancine, apublica, avozeavezdajuventude, b9, balaiodokotscho, \
blastingnews, blogdafloresta, blogdoataide, blogdoluciosorge, blogdomaringoni, blogdomello, blogdomiro, blogdoneylopes, blogdopaulinho, \
blogdopaulonunes, blogdoprimo, blogdoriella, blogdorovai, blogdoskarlack, blogmarcosfrahm, brasildefato, buzzfeed_news_br, camara, \
carta_maior, cartamaior, ceticismopolitico, cinegnose, comunicadores, congressoemfoco, convergenciadigital, correiodobrasil, diariodocentrodomundo, \
diplomatique, domingoscosta, eb, ebc, elielbezerra, esporteemidia, estadao, extra_globo, fabiocampana, falandoverdades, folha_piaui, folha_sp, \
gospelprime, grandesnomesdapropaganda, huffpostbrasil, imprensaviva, istoe, jaderbarbalho, jornaisvirtuais, jornaldocomercio, jornallivre, jota, \
justificando, lulacerda, marcossilverio, migalhas, moneytimes, mundodomarketing, natelinha, nocaute, noticiasdatv, oab, observatoriodatelevisao, \
ocafezinho, ocombatente, operamundi, osamigosdopresidentelula, osdivergentes, otvfoco, outraspalavras, papelpop, polibiobraga, politicanarede, \
poncheverde, portaldapropaganda, ptnacamara, revistaforum, revistapress, rss_multiplos, rufandobombo, saibamais, sputniknews, telepadi, \
telesintese, tijolaco, torcedores, tribunadainternet, tribunadajustiça, valor, veja, vermelho, viomundo

' import general pages '
from pages import agenciabrasil_ebc, bastidoresdopoder, bbc, cartacapital, correio24horas, diariocatarinense, diariodocentrodomundo, \
diariodocentrodomundo_mundo, diariodonordeste, dinheirorural, elpais, exame, gauchazh, gazetadopovo, globo_eleicoes, infomoney, istoedinheiro, jornalestadodeminas, \
jovempan, justificando_artigos, justificando, marceloauler, ne10, oantagonista, r7, rss_globo, terra_noticias, tnh1, tribunadosertao, veja_ultimas

""" List of pages """
PAGES = [# page from the states
         agazetadoacre, jornalatribuna, jornalopiniao, jornalopiniao_economia, jornalopiniao_policia, jornalopiniao_politica, oaltoacre,
         oestadoacre, oriobranco_geral, oriobranco_policial, oriobranco_politica, pagina20, pagina20_economia, pagina20_policia, pagina20_politica,
         anoticia, cadaminuto, correiodopovo, gazetadealagoas, gazetaweb, novoextra, primeiraedicao, tribunahoje, tribunauniao,
         aquiamapa, diariodoamapa, acritica_am, ojornaldailha, osolimoes, aregiao, atarde, correiodooeste, folharegionalbahia, folhasertaneja, 
         istoenoticia, jornalalerta, jornalanossavoz, jornalfolhadoestado, jornalimpacto, jornalnovafronteira, novoeste, oecojornal, rss_diariobahia, 
         tribunafeirense, anoticiadoceara, oestadoce, opovo, tribunadoceara, camara, correiobraziliense, folhacentrooeste, jornaldebrasilia, jornalregional, 
         rss_estacaonews, rss_senado, aquinoticias, correiodoestadoonline, estadocapixaba, gazetaonline, jornalcorreiocapixaba, noticiaagora, 
         rss_folhaonline, tribunaonline, diariodeaparecida, diariodoestadogo, jornalaguaslindas, jornalopcao, jornalestadodegoias, oanapolis, ohoje, 
         opopular, rss_jornalopcao, tribunadoplanalto, atosefatos, oestadoma, oquartopoder, 
         # pages ate o maranhao
         
         #paginas diversas
         agenciabrasil_ebc, bastidoresdopoder, bbc, cartacapital, correio24horas, diariocatarinense, diariodocentrodomundo, diariodocentrodomundo_mundo, 
         diariodonordeste, dinheirorural, elpais, exame, gauchazh, gazetadopovo, globo_eleicoes, infomoney, istoedinheiro, jornalestadodeminas, jovempan, 
         justificando_artigos, justificando, marceloauler, ne10, oantagonista, r7, rss_globo, terra_noticias, tnh1, tribunadosertao, veja_ultimas,

         # paginas gabriel
         abert, abi, administradores, adrenaline, agenciabrasil, ancine, apublica, avozeavezdajuventude, b9, balaiodokotscho, 
        blastingnews, blogdafloresta, blogdoataide, blogdoluciosorge, blogdomaringoni, blogdomello, blogdomiro, blogdoneylopes, blogdopaulinho, 
        blogdopaulonunes, blogdoprimo, blogdoriella, blogdorovai, blogdoskarlack, blogmarcosfrahm, brasildefato, buzzfeed_news_br, camara, 
        carta_maior, cartamaior, ceticismopolitico, cinegnose, comunicadores, congressoemfoco, convergenciadigital, correiodobrasil, diariodocentrodomundo, 
        diplomatique, domingoscosta, eb, ebc, elielbezerra, esporteemidia, estadao, extra_globo, fabiocampana, falandoverdades, folha_piaui, folha_sp, 
        gospelprime, grandesnomesdapropaganda, huffpostbrasil, imprensaviva, istoe, jaderbarbalho, jornaisvirtuais, jornaldocomercio, jornallivre, jota, 
        justificando, lulacerda, marcossilverio, migalhas, moneytimes, mundodomarketing, natelinha, nocaute, noticiasdatv, oab, observatoriodatelevisao, 
        ocafezinho, ocombatente, operamundi, osamigosdopresidentelula, osdivergentes, outraspalavras, papelpop, politicanarede, 
        poncheverde, portaldapropaganda, ptnacamara, revistaforum, revistapress, rufandobombo, saibamais, sputniknews, telepadi, 
        telesintese, tijolaco, torcedores, tribunadainternet, tribunadajustiça, valor, veja, vermelho, viomundo, rss_multiplos
]