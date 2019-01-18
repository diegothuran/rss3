function getRandomColor() {
	var letters = '0123456789ABCDEF'.split('');
	var color = '#';
	for (var i = 0; i < 6; i++ ) {
	    color += letters[Math.floor(Math.random() * 16)];
	}
return color;
}

var request = new XMLHttpRequest();
request.open('GET', 'http://34.234.188.90:5000/relevancia/', true);
request.onload = function () {

	// Begin accessing JSON data here
	var data = JSON.parse(this.response);
	if (request.status >= 200 && request.status < 400) {
		var sites = []
		var relevancias = []
		data.forEach(element => {
			sites.push(element.site);  
			relevancias.push(element.relevancia);  
    });
		
	var randomColors = [];
	for (var i in relevancias) {
		randomColors.push(getRandomColor());
   }
	  
    var ctx = document.getElementById("myChart");
    var myChart = new Chart(ctx, {
        //type: 'bar',
        type: 'horizontalBar',
        data: {
            labels: sites,
            datasets: [{
//                label: 'Relevancia',
                data: relevancias,
                backgroundColor: randomColors
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero:true
                    },
                    scaleLabel: {
                		display: true,
                		labelString: 'Fonte de informação',
                		fontSize: 14,
                		fontStyle: 'bold'
                			
	                }
                }],
                
                xAxes: [{
                	scaleLabel: {
                		display: true,
                		labelString: 'Relevância',
                		fontSize: 14,
                		fontStyle: 'bold'
                			
	                }
                }]
            },
            
            title: {
	            display: true,
	            text: 'Relevância das fontes de informação.',
//	            text: ['Relevância das fontes de informação',
//	            	'Nosso índice de relevância representa uma média da popularidade das fontes de informações utilizadas e é definido pelo Rank Alexa.', 
//	            	'Na prática quanto mais próximo de 10.00 for a relevãncia, maior o número de usuários que visitaram a fonte de informação. Valores próximos a 0.00 representam um menor número de acessos à informação.'],
	            fontSize: 16
	        },
	        
	        legend: {
	            display: false
	        },
	        
	        tooltips: {
	            callbacks: {
	                label: function(tooltipItem) {
	                    return " A fonte " + tooltipItem.yLabel + " apresenta relevância de " + Number(tooltipItem.xLabel)
	                }
	            }
	        }
        }
    });
    
    // category_timeline
//    dict_keys(['19-12-2018', '20-12-2018', '21-12-2018', '22-12-2018', '23-12-2018', '24-12-2018', '25-12-2018', '26-12-2018', '27-12-2018', '28-12-2018', '29-12-2018', '30-12-2018', '31-12-2018', '01-01-2019', '02-01-2019', '03-01-2019', '04-01-2019', '05-01-2019', '06-01-2019', '07-01-2019', '08-01-2019', '09-01-2019', '10-01-2019', '11-01-2019', '12-01-2019', '13-01-2019', '14-01-2019', '15-01-2019', '16-01-2019', '17-01-2019', '18-01-2019'])
//    dict_values([1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0])

    labels_category_timeline = ['19-12-2018', '20-12-2018', '21-12-2018', '22-12-2018', '23-12-2018', '24-12-2018', '25-12-2018', '26-12-2018', '27-12-2018', '28-12-2018', '29-12-2018', '30-12-2018', '31-12-2018', '01-01-2019', '02-01-2019', '03-01-2019', '04-01-2019', '05-01-2019', '06-01-2019', '07-01-2019', '08-01-2019', '09-01-2019', '10-01-2019', '11-01-2019', '12-01-2019', '13-01-2019', '14-01-2019', '15-01-2019', '16-01-2019', '17-01-2019', '18-01-2019']
    data_category_timeline = [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
    var ctx = document.getElementById("category_timeline");
    var category_timeline = new Chart(ctx, {
    	type: 'line',
//    	type: 'bar',
        data: {
            labels: labels_category_timeline,
            datasets: [{
//                label: 'Timeline',
                data: data_category_timeline,
//                borderWidth: 1
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero:true
                    },  
                    scaleLabel: {
                		display: true,
                		labelString: 'Quantidade',
                		fontSize: 14,
                		fontStyle: 'bold'
                			
	                }
                }],
                
                xAxes: [{
                	scaleLabel: {
                		display: true,
                		labelString: 'Data',
                		fontSize: 14,
                		fontStyle: 'bold'
                			
	                }
                }]
            },
        
	        title: {
	            display: true,
	            text: 'Timeline das notícias relacionadas a categoria: Osmar Terra.',
	            fontSize: 16
	        },
	        
	        legend: {
	            display: false
	        },
	        
	        tooltips: {
	            callbacks: {
	                label: function(tooltipItem) {
	                    return Number(tooltipItem.yLabel) + " notícia(s) obtida(s) na data " + tooltipItem.xLabel + " contêm a categoria Osmar Terra"
	                }
	            }
	        }
        }
    });
    
    // category_relation
//    dict_keys(['bolsonaro', 'onyx lorenzoni', 'paulo guedes', 'augusto heleno', 'marcos pontes', 'sérgio moro', 'hamilton mourão', 'joaquim levy', 'mansueto almeida', 'fernando azevedo e silva', 'ernesto araújo', 'roberto campos neto', 'tereza cristina', 'andré luiz de almeida mendonça', 'carlos von doellinger', 'érika marena', 'luiz mandetta', 'maurício valeixo', 'pedro guimarães', 'ricardo vélez rodríguez', 'roberto castello branco', 'rubem novaes', 'wagner rosário', 'bento costa lima leite de albuquerque junior', 'marcelo álvaro antônio', 'gustavo henrique rigodanzo canuto', 'tarcísio gomes de freitas', 'carlos alberto dos santos cruz', 'gustavo bebianno', 'ac', 'al', 'ap', 'am', 'ba', 'ce', 'df', 'es', 'go', 'ma', 'mt', 'ms', 'mg', 'pa', 'pb', 'pr', 'pe', 'pi', 'rj', 'rn', 'rs', 'ro', 'rr', 'sc', 'sp', 'se', 'to'])
//    dict_values(['85.81', '28.37', '30.47', '6.98', '7.21', '31.63', '7.67', '0.93', '0.47', '6.05', '5.58', '3.72', '14.42', '1.86', '0.23', '0.23', '1.40', '0.93', '1.63', '4.65', '0.93', '0.93', '8.84', '0.47', '3.72', '0.47', '7.91', '3.95', '7.44', '2.56', '0.70', '0.23', '3.02', '3.26', '1.63', '36.74', '13.49', '5.12', '1.16', '3.02', '7.21', '6.05', '1.86', '1.40', '25.35', '1.63', '0.70', '16.28', '3.49', '36.05', '0.00', '7.91', '2.33', '30.00', '0.23', '0.70'])
    
    labels_category_relation = ['bolsonaro', 'onyx lorenzoni', 'paulo guedes', 'augusto heleno', 'marcos pontes', 'sérgio moro', 'hamilton mourão', 'joaquim levy', 'mansueto almeida', 'fernando azevedo e silva', 'ernesto araújo', 'roberto campos neto', 'tereza cristina', 'andré luiz de almeida mendonça', 'carlos von doellinger', 'érika marena', 'luiz mandetta', 'maurício valeixo', 'pedro guimarães', 'ricardo vélez rodríguez', 'roberto castello branco', 'rubem novaes', 'wagner rosário', 'bento costa lima leite de albuquerque junior', 'marcelo álvaro antônio', 'gustavo henrique rigodanzo canuto', 'tarcísio gomes de freitas', 'carlos alberto dos santos cruz', 'gustavo bebianno', 'ac', 'al', 'ap', 'am', 'ba', 'ce', 'df', 'es', 'go', 'ma', 'mt', 'ms', 'mg', 'pa', 'pb', 'pr', 'pe', 'pi', 'rj', 'rn', 'rs', 'ro', 'rr', 'sc', 'sp', 'se', 'to'] 
    data_category_relation = ['85.81', '28.37', '30.47', '6.98', '7.21', '31.63', '7.67', '0.93', '0.47', '6.05', '5.58', '3.72', '14.42', '1.86', '0.23', '0.23', '1.40', '0.93', '1.63', '4.65', '0.93', '0.93', '8.84', '0.47', '3.72', '0.47', '7.91', '3.95', '7.44', '2.56', '0.70', '0.23', '3.02', '3.26', '1.63', '36.74', '13.49', '5.12', '1.16', '3.02', '7.21', '6.05', '1.86', '1.40', '25.35', '1.63', '0.70', '16.28', '3.49', '36.05', '0.00', '7.91', '2.33', '30.00', '0.23', '0.70'] 
    var randomColors = [];
	for (var i in labels_category_relation) {
		randomColors.push(getRandomColor());
	}
    
    var ctx = document.getElementById("category_relation");
    var category_relation = new Chart(ctx, {
    	//type: 'line',
    	type: 'horizontalBar',
        data: {
            labels: labels_category_relation,
            datasets: [{
//                label: 'Relacionamento entre categorias (Porcentagem de noticias que contem a categoria Osmar Terra e a categoria relacionada)',
                data: data_category_relation,
//                borderWidth: 1
                backgroundColor: randomColors
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero:true
                    },
                    scaleLabel: {
                		display: true,
                		labelString: 'Categoria',
                		fontSize: 14,
                		fontStyle: 'bold'
                			
	                }
                }],
                
                xAxes: [{
                	scaleLabel: {
                		display: true,
                		labelString: 'Porcentagem (%)',
                		fontSize: 14,
                		fontStyle: 'bold'
                			
	                }
                }]
            },
            
            title: {
                display: true,
                text: 'Relacionamento entre categorias considerando a categoria base: Osmar Terra.',
                fontSize: 16
            },
            
            legend: {
                display: false
            },
            
            tooltips: {
                callbacks: {
                    label: function(tooltipItem) {
                        return Number(tooltipItem.xLabel) + "% das notícias que contêm a categoria " + "Osmar Terra" + " também contêm a categoria " 
                        + tooltipItem.yLabel
                    }
                }
            }
        }
    });
    
    // Category_sites 
//    dict_keys(['agazetadoacre.com', 'jornalatribuna.com.br', 'jornalopiniao.net', 'oaltoacre.com', 'oestadoacre.com', 'oriobranco.net', 'pagina20.net', 'anoticia.online', 'cadaminuto.com.br', 'correiodopovo.com.br', 'gazetaweb.globo.com/gazetadealagoas', 'gazetaweb.globo.com/portal', 'novoextra.com.br', 'primeiraedicao.com.br', 'tribunahoje.com', 'tribunauniao.com.br', 'aquiamapa.com.br', 'diariodoamapa.com.br', 'acritica.com', 'ojornaldailha.com', 'osolimoes.com.br', 'aregiao.com.br', 'atarde.uol.com.br', 'correiodooeste.com.br', 'folharegionalbahia.com.br', 'folhasertaneja.com.br', 'istoenoticia.com', 'jornalalerta.com.br', 'sertaohoje.com.br', 'jornalfolhadoestado.com', 'jornalimpacto.com.br', 'jornalnovafronteira.com.br', 'novoeste.com', 'oecojornal.com.br', 'diariobahia.com.br', 'tribunafeirense.com.br', 'anoticiadoceara.com.br', 'oestadoce.com.br', 'opovo.com.br', 'tribunadoceara.uol.com.br', 'camara.leg.br', 'folhacentrooeste.blog.br', 'jornaldebrasilia.com.br', 'jornalregional.com.br', 'estacaonews.blog.br', 'senado.leg.br', 'aquinoticias.com', 'correiodoestadoonline.com.br', 'estadocapixaba.com', 'gazetaonline.com.br', 'jornalcorreiocapixaba.com.br', 'noticiaagora.com.br', 'folhaonline.es', 'tribunaonline.com.br', 'diariodeaparecida.com.br', 'diariodoestadogo.com.br', 'jornalaguaslindas.com.br', 'jornalopcao.com.br', 'jornalestadodegoias.com.br', 'oanapolis.com.br', 'ohoje.com.br', 'opopular.com.br', 'tribunadoplanalto.com.br', 'atosefatos.jor.br', 'imirante.com', 'oquartopoder.com', 'circuitomt.com.br', 'copopular.com.br', 'folhadoestado.com.br', 'gazetadigital.com.br', 'acritica.net', 'atribunanews.com.br', 'correiodoestado.com.br', 'jd1noticias.com', 'midiamax.com.br', 'em.com.br', 'folhamg.com', 'hojeemdia.com.br', 'correiodaparaiba.com.br', 'jornaldaparaiba.com.br', 'bemparana.com.br', 'diarioinduscom.com', 'impactopr.com.br', 'jornaldoonibusdecuritiba.com.br', 'tribunapr.com.br', 'correiodepernambuco.com.br', 'diariodepernambuco.com.br', 'folhape.com.br', 'jconline.ne10.uol.com.br', 'destakjornal.com.br', 'jb.com.br', 'monitordigital.com.br', 'odia.ig.com.br', 'oglobo.globo.com', 'agorarn.com.br', 'tribunadenoticias.com.br', 'tribunadonorte.com.br', 'osul.com.br', 'correiodenoticia.com.br', 'diariodaamazonia.com.br', 'folhabv.com.br', 'jornalroraimahoje.com.br', 'anoticia.clicrbs.com.br', 'ndonline.com.br', 'nsctotal.com.br', 'brasildefato.com.br', 'dci.com.br', 'diariodenoticias.com.br', 'estadao.com.br', 'folha.uol.com.br', 'gazetasp.com.br', 'horadopovo.org.br', 'jornalestacao.com.br', 'meioemensagem.com.br', 'metronews.com.br', 'www.valor.com.br', 'cinform.com.br', 'jornaldesergipe.com.br', 'jornaldodiase.com.br', 'agora-to.com.br', 'conexaoto.com.br', 'jornaldotocantins.com.br', 'ogirassol.com.br', 'portalstylo.com.br', 'agenciabrasil.ebc.com.br', 'bastidoresdopoder.com.br', 'bbc.com', 'cartacapital.com.br', 'correio24horas.com.br', 'dc.clicrbs.com.br', 'diariodocentrodomundo.com.br', 'diariodonordeste.verdesmares.com.br', 'dinheirorural.com.br', 'brasil.elpais.com', 'exame.abril.com.br', 'gauchazh.clicrbs.com.br', 'gazetadopovo.com.br', 'g1.globo.com', 'infomoney.com.br', 'istoedinheiro.com.br', 'jovempan.uol.com.br', 'justificando.com', 'marceloauler.com.br', 'ne10.uol.com.br', 'oantagonista.com', 'r7.com', 'terra.com.br', 'tnh1.com.br', 'tribunadosertao.com.br', 'veja.abril.com.br', 'noticias.uol.com.br', 'abert.org.br', 'abi.org.br', 'administradores.com.br', 'adrenaline.uol.com.br', 'ancine.gov.br', 'apublica.org', 'avozeavezdajuventude.blogspot.com', 'b9.com.br', 'balaiodokotscho.com.br', 'br.blastingnews.com', 'blogdafloresta.com.br', 'blogdoataide.com.br', 'blogdoluciosorge.com.br', 'revistaforum.com.br', 'blogdomello.blogspot.com', 'altamiroborges.blogspot.com', 'blogdoneylopes.com.br', 'blogdopaulinho.com.br', 'blogdopaulonunes.com', 'blogdoprimo.com.br', 'blogdoriella.com.br', 'blogdoskarlack.com', 'blogmarcosfrahm.com', 'buzzfeed.com', 'cartamaior.com.br', 'ceticismopolitico.org', 'cinegnose.blogspot.com', 'comunicadores.info', 'congressoemfoco.uol.com.br', 'convergenciadigital.com.br', 'correiodobrasil.com.br', 'diplomatique.org.br', 'domingoscosta.com.br', 'www.eb.mil.br', 'ebc.com.br', 'elielbezerra.blogspot.com', 'esporteemidia.com', 'extra.globo.com', 'fabiocampana.com.br', 'falandoverdades.com.br', 'piaui.folha.uol.com.br', 'noticias.gospelprime.com.br', 'grandesnomesdapropaganda.com.br', 'huffpostbrasil.com', 'imprensaviva.com', 'istoe.com.br', 'jaderbarbalho.com', 'jornaisvirtuais.com.br', 'jornaldocomercio.com', 'jornalivre.com', 'jota.info', 'lulacerda.ig.com.br', 'marcossilverio.blogspot.com', 'migalhas.com.br', 'moneytimes.com.br', 'mundodomarketing.com.br', 'natelinha.uol.com.br', 'nocaute.blog.br', 'noticiasdatv.uol.com.br', 'oab.org.br', 'observatoriodatelevisao.bol.uol.com.br', 'ocafezinho.com', 'ocombatente.com', 'operamundi.uol.com.br', 'osamigosdopresidentelula.blogspot.com', 'osdivergentes.com.br', 'outraspalavras.net', 'papelpop.com', 'politicanarede.com', 'poncheverde.blogspot.com', 'portaldapropaganda.com.br', 'ptnacamara.org.br', 'revistapress.com.br', 'rufandobombo.com.br', 'saibamais.jor.br', 'br.sputniknews.com', 'telepadi.folha.uol.com.br', 'telesintese.com.br', 'tijolaco.com.br', 'torcedores.com', 'tribunadainternet.com.br', 'tribunadajustica.com.br', 'vermelho.org.br', 'viomundo.com.br'])
//    dict_values([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 2, 0, 3, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 8, 1, 0, 0, 0, 3, 0, 0, 1, 2, 0, 2, 8, 4, 0, 0, 6, 0, 0, 0, 2, 0, 0, 1, 1, 2, 0, 3, 0, 0, 0, 0, 0, 0, 0, 3, 0, 1, 5, 0, 3, 0, 0, 5, 0, 0, 0, 0, 0, 2, 2, 0, 9, 10, 3, 3, 5, 0, 0, 5, 14, 1, 2, 9, 1, 0, 1, 0, 2, 1, 0, 8, 31, 1, 0, 1, 0, 0, 9, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 1, 0, 2, 1, 0, 10, 0, 0, 0, 0, 6, 6, 7, 12, 9, 0, 0, 6, 6, 6, 31, 2, 0, 0, 14, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 5, 0, 0, 1, 0, 1, 1, 5, 0, 4, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 11, 0, 0, 1, 7, 1, 0, 1, 0, 3, 0, 3, 0, 1, 3, 0, 0, 0, 0, 1, 2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 0, 0, 1, 4, 0, 2, 0, 0, 0, 0, 1, 0])

    labels_category_sites = ['agazetadoacre.com', 'jornalatribuna.com.br', 'jornalopiniao.net', 'oaltoacre.com', 'oestadoacre.com', 'oriobranco.net', 'pagina20.net', 'anoticia.online', 'cadaminuto.com.br', 'correiodopovo.com.br', 'gazetaweb.globo.com/gazetadealagoas', 'gazetaweb.globo.com/portal', 'novoextra.com.br', 'primeiraedicao.com.br', 'tribunahoje.com', 'tribunauniao.com.br', 'aquiamapa.com.br', 'diariodoamapa.com.br', 'acritica.com', 'ojornaldailha.com', 'osolimoes.com.br', 'aregiao.com.br', 'atarde.uol.com.br', 'correiodooeste.com.br', 'folharegionalbahia.com.br', 'folhasertaneja.com.br', 'istoenoticia.com', 'jornalalerta.com.br', 'sertaohoje.com.br', 'jornalfolhadoestado.com', 'jornalimpacto.com.br', 'jornalnovafronteira.com.br', 'novoeste.com', 'oecojornal.com.br', 'diariobahia.com.br', 'tribunafeirense.com.br', 'anoticiadoceara.com.br', 'oestadoce.com.br', 'opovo.com.br', 'tribunadoceara.uol.com.br', 'camara.leg.br', 'folhacentrooeste.blog.br', 'jornaldebrasilia.com.br', 'jornalregional.com.br', 'estacaonews.blog.br', 'senado.leg.br', 'aquinoticias.com', 'correiodoestadoonline.com.br', 'estadocapixaba.com', 'gazetaonline.com.br', 'jornalcorreiocapixaba.com.br', 'noticiaagora.com.br', 'folhaonline.es', 'tribunaonline.com.br', 'diariodeaparecida.com.br', 'diariodoestadogo.com.br', 'jornalaguaslindas.com.br', 'jornalopcao.com.br', 'jornalestadodegoias.com.br', 'oanapolis.com.br', 'ohoje.com.br', 'opopular.com.br', 'tribunadoplanalto.com.br', 'atosefatos.jor.br', 'imirante.com', 'oquartopoder.com', 'circuitomt.com.br', 'copopular.com.br', 'folhadoestado.com.br', 'gazetadigital.com.br', 'acritica.net', 'atribunanews.com.br', 'correiodoestado.com.br', 'jd1noticias.com', 'midiamax.com.br', 'em.com.br', 'folhamg.com', 'hojeemdia.com.br', 'correiodaparaiba.com.br', 'jornaldaparaiba.com.br', 'bemparana.com.br', 'diarioinduscom.com', 'impactopr.com.br', 'jornaldoonibusdecuritiba.com.br', 'tribunapr.com.br', 'correiodepernambuco.com.br', 'diariodepernambuco.com.br', 'folhape.com.br', 'jconline.ne10.uol.com.br', 'destakjornal.com.br', 'jb.com.br', 'monitordigital.com.br', 'odia.ig.com.br', 'oglobo.globo.com', 'agorarn.com.br', 'tribunadenoticias.com.br', 'tribunadonorte.com.br', 'osul.com.br', 'correiodenoticia.com.br', 'diariodaamazonia.com.br', 'folhabv.com.br', 'jornalroraimahoje.com.br', 'anoticia.clicrbs.com.br', 'ndonline.com.br', 'nsctotal.com.br', 'brasildefato.com.br', 'dci.com.br', 'diariodenoticias.com.br', 'estadao.com.br', 'folha.uol.com.br', 'gazetasp.com.br', 'horadopovo.org.br', 'jornalestacao.com.br', 'meioemensagem.com.br', 'metronews.com.br', 'www.valor.com.br', 'cinform.com.br', 'jornaldesergipe.com.br', 'jornaldodiase.com.br', 'agora-to.com.br', 'conexaoto.com.br', 'jornaldotocantins.com.br', 'ogirassol.com.br', 'portalstylo.com.br', 'agenciabrasil.ebc.com.br', 'bastidoresdopoder.com.br', 'bbc.com', 'cartacapital.com.br', 'correio24horas.com.br', 'dc.clicrbs.com.br', 'diariodocentrodomundo.com.br', 'diariodonordeste.verdesmares.com.br', 'dinheirorural.com.br', 'brasil.elpais.com', 'exame.abril.com.br', 'gauchazh.clicrbs.com.br', 'gazetadopovo.com.br', 'g1.globo.com', 'infomoney.com.br', 'istoedinheiro.com.br', 'jovempan.uol.com.br', 'justificando.com', 'marceloauler.com.br', 'ne10.uol.com.br', 'oantagonista.com', 'r7.com', 'terra.com.br', 'tnh1.com.br', 'tribunadosertao.com.br', 'veja.abril.com.br', 'noticias.uol.com.br', 'abert.org.br', 'abi.org.br', 'administradores.com.br', 'adrenaline.uol.com.br', 'ancine.gov.br', 'apublica.org', 'avozeavezdajuventude.blogspot.com', 'b9.com.br', 'balaiodokotscho.com.br', 'br.blastingnews.com', 'blogdafloresta.com.br', 'blogdoataide.com.br', 'blogdoluciosorge.com.br', 'revistaforum.com.br', 'blogdomello.blogspot.com', 'altamiroborges.blogspot.com', 'blogdoneylopes.com.br', 'blogdopaulinho.com.br', 'blogdopaulonunes.com', 'blogdoprimo.com.br', 'blogdoriella.com.br', 'blogdoskarlack.com', 'blogmarcosfrahm.com', 'buzzfeed.com', 'cartamaior.com.br', 'ceticismopolitico.org', 'cinegnose.blogspot.com', 'comunicadores.info', 'congressoemfoco.uol.com.br', 'convergenciadigital.com.br', 'correiodobrasil.com.br', 'diplomatique.org.br', 'domingoscosta.com.br', 'www.eb.mil.br', 'ebc.com.br', 'elielbezerra.blogspot.com', 'esporteemidia.com', 'extra.globo.com', 'fabiocampana.com.br', 'falandoverdades.com.br', 'piaui.folha.uol.com.br', 'noticias.gospelprime.com.br', 'grandesnomesdapropaganda.com.br', 'huffpostbrasil.com', 'imprensaviva.com', 'istoe.com.br', 'jaderbarbalho.com', 'jornaisvirtuais.com.br', 'jornaldocomercio.com', 'jornalivre.com', 'jota.info', 'lulacerda.ig.com.br', 'marcossilverio.blogspot.com', 'migalhas.com.br', 'moneytimes.com.br', 'mundodomarketing.com.br', 'natelinha.uol.com.br', 'nocaute.blog.br', 'noticiasdatv.uol.com.br', 'oab.org.br', 'observatoriodatelevisao.bol.uol.com.br', 'ocafezinho.com', 'ocombatente.com', 'operamundi.uol.com.br', 'osamigosdopresidentelula.blogspot.com', 'osdivergentes.com.br', 'outraspalavras.net', 'papelpop.com', 'politicanarede.com', 'poncheverde.blogspot.com', 'portaldapropaganda.com.br', 'ptnacamara.org.br', 'revistapress.com.br', 'rufandobombo.com.br', 'saibamais.jor.br', 'br.sputniknews.com', 'telepadi.folha.uol.com.br', 'telesintese.com.br', 'tijolaco.com.br', 'torcedores.com', 'tribunadainternet.com.br', 'tribunadajustica.com.br', 'vermelho.org.br', 'viomundo.com.br']
    data_category_sites = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 2, 0, 3, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 8, 1, 0, 0, 0, 3, 0, 0, 1, 2, 0, 2, 8, 4, 0, 0, 6, 0, 0, 0, 2, 0, 0, 1, 1, 2, 0, 3, 0, 0, 0, 0, 0, 0, 0, 3, 0, 1, 5, 0, 3, 0, 0, 5, 0, 0, 0, 0, 0, 2, 2, 0, 9, 10, 3, 3, 5, 0, 0, 5, 14, 1, 2, 9, 1, 0, 1, 0, 2, 1, 0, 8, 31, 1, 0, 1, 0, 0, 9, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 1, 0, 2, 1, 0, 10, 0, 0, 0, 0, 6, 6, 7, 12, 9, 0, 0, 6, 6, 6, 31, 2, 0, 0, 14, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 5, 0, 0, 1, 0, 1, 1, 5, 0, 4, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 11, 0, 0, 1, 7, 1, 0, 1, 0, 3, 0, 3, 0, 1, 3, 0, 0, 0, 0, 1, 2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 0, 0, 1, 4, 0, 2, 0, 0, 0, 0, 1, 0]
    var randomColors = [];
	for (var i in labels_category_sites) {
		randomColors.push(getRandomColor());
	}
	
    var ctx = document.getElementById("category_sites");
    var category_sites = new Chart(ctx, {
    	//type: 'line',
    	type: 'horizontalBar',
        data: {
            labels: labels_category_sites,
            datasets: [{
//                label: 'Quantidade de noticias relacionadas a categoria Osmar Terra obtidas do site',
                data: data_category_sites,
                backgroundColor: randomColors
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero:true
                    },
                    scaleLabel: {
                		display: true,
                		labelString: 'Fonte de informação',
                		fontSize: 14,
                		fontStyle: 'bold'
                			
	                }
                }],
                
                xAxes: [{
                	scaleLabel: {
                		display: true,
                		labelString: 'Quantidade',
                		fontSize: 14,
                		fontStyle: 'bold'
                			
	                }
                }]
            },
            
            title: {
                display: true,
                text: 'Segmentação das fontes de informação considerando a categoria: Osmar Terra.',
                fontSize: 16
            },
            
            legend: {
                display: false
            },
            
            tooltips: {
                callbacks: {
                    label: function(tooltipItem) {
                        return Number(tooltipItem.xLabel) + " notícias que contêm a categoria " + "Osmar Terra" + " foram obtidas do site " 
                        + tooltipItem.yLabel
                    }
                }
            }
            
        }
    });
    
    // category_set
//    dict_keys(['bolsonaro', 'onyx lorenzoni', 'paulo guedes', 'augusto heleno', 'marcos pontes', 'sérgio moro', 'hamilton mourão', 'joaquim levy', 'mansueto almeida', 'fernando azevedo e silva', 'ernesto araújo', 'roberto campos neto', 'tereza cristina', 'andré luiz de almeida mendonça', 'carlos von doellinger', 'érika marena', 'luiz mandetta', 'maurício valeixo', 'pedro guimarães', 'ricardo vélez rodríguez', 'roberto castello branco', 'rubem novaes', 'wagner rosário', 'bento costa lima leite de albuquerque junior', 'marcelo álvaro antônio', 'osmar terra', 'gustavo henrique rigodanzo canuto', 'tarcísio gomes de freitas', 'carlos alberto dos santos cruz', 'gustavo bebianno', 'ac', 'al', 'ap', 'am', 'ba', 'ce', 'df', 'es', 'go', 'ma', 'mt', 'ms', 'mg', 'pa', 'pb', 'pr', 'pe', 'pi', 'rj', 'rn', 'rs', 'ro', 'rr', 'sc', 'sp', 'se', 'to'])
//    dict_values([1859, 216, 171, 76, 17, 266, 75, 6, 1, 44, 87, 3, 26, 0, 0, 0, 3, 0, 7, 8, 2, 15, 7, 1, 5, 31, 0, 8, 28, 25, 65, 44, 19, 42, 53, 122, 572, 74, 60, 24, 38, 73, 90, 31, 31, 245, 73, 27, 441, 45, 180, 13, 49, 42, 555, 26, 4])

    
    labels_category_set = ['bolsonaro', 'onyx lorenzoni', 'paulo guedes', 'augusto heleno', 'marcos pontes', 'sérgio moro', 'hamilton mourão', 'joaquim levy', 'mansueto almeida', 'fernando azevedo e silva', 'ernesto araújo', 'roberto campos neto', 'tereza cristina', 'andré luiz de almeida mendonça', 'carlos von doellinger', 'érika marena', 'luiz mandetta', 'maurício valeixo', 'pedro guimarães', 'ricardo vélez rodríguez', 'roberto castello branco', 'rubem novaes', 'wagner rosário', 'bento costa lima leite de albuquerque junior', 'marcelo álvaro antônio', 'osmar terra', 'gustavo henrique rigodanzo canuto', 'tarcísio gomes de freitas', 'carlos alberto dos santos cruz', 'gustavo bebianno', 'ac', 'al', 'ap', 'am', 'ba', 'ce', 'df', 'es', 'go', 'ma', 'mt', 'ms', 'mg', 'pa', 'pb', 'pr', 'pe', 'pi', 'rj', 'rn', 'rs', 'ro', 'rr', 'sc', 'sp', 'se', 'to']
    data_category_set = [1859, 216, 171, 76, 17, 266, 75, 6, 1, 44, 87, 3, 26, 0, 0, 0, 3, 0, 7, 8, 2, 15, 7, 1, 5, 31, 0, 8, 28, 25, 65, 44, 19, 42, 53, 122, 572, 74, 60, 24, 38, 73, 90, 31, 31, 245, 73, 27, 441, 45, 180, 13, 49, 42, 555, 26, 4]
    
    var randomColors = [];
	for (var i in labels_category_set) {
		randomColors.push(getRandomColor());
	}
    
    var ctx = document.getElementById("category_set");
    var category_relation = new Chart(ctx, {
    	//type: 'line',
    	type: 'horizontalBar',
        data: {
            labels: labels_category_set,

            datasets: [{
//                label: 'Quantidade de noticias obtidas do site www.terra.com.br relacionadas a categoria',
                data: data_category_set,
//                borderWidth: 1
                backgroundColor: randomColors
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero:true
                    },
                    
                    scaleLabel: {
                		display: true,
                		labelString: 'Categoria',
                		fontSize: 14,
                		fontStyle: 'bold'
	                }
                }],
                
                xAxes: [{
                	scaleLabel: {
                		display: true,
                		labelString: 'Quantidade',
                		fontSize: 14,
                		fontStyle: 'bold'
	                }
                }]
            },
            
            title: {
                display: true,
                text: 'Segmentação das categorias considerando a fonte: terra.com.br',
                fontSize: 16
//                	O gráfico exibe as fontes de notícias e o número de artigos resultantes que cada um deles escreveu.
            },
            
            legend: {
                display: false
            },
            
            tooltips: {
                callbacks: {
                    label: function(tooltipItem) {
                        return Number(tooltipItem.xLabel) + " notícias contêm a categoria " + tooltipItem.yLabel + 
                        	" e têm o site " + "terra.com.br" + " como fonte.";
                    }
                }
            }
        }
    });
    
    
  } else {
    const errorMessage = document.createElement('marquee');
    errorMessage.textContent = 'Not working!';
  }
}

request.send();