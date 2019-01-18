
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
	  
    var ctx = document.getElementById("myChart");
    var myChart = new Chart(ctx, {
        //type: 'bar',
        type: 'horizontalBar',
        data: {
            labels: sites,
            datasets: [{
                label: 'Relevancia',
                data: relevancias,
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero:true
                    }
                }]
            }
        }
    });
    
    var ctx = document.getElementById("category_timeline");
    var category_timeline = new Chart(ctx, {
    	//type: 'line',
    	type: 'bar',
        data: {
            labels: ['19-12-2018', '20-12-2018', '21-12-2018', '22-12-2018', '23-12-2018', '24-12-2018', '25-12-2018', '26-12-2018', '27-12-2018', '28-12-2018', '29-12-2018', '30-12-2018', '31-12-2018', '01-01-2019', '02-01-2019', '03-01-2019', '04-01-2019', '05-01-2019', '06-01-2019', '07-01-2019', '08-01-2019', '09-01-2019', '10-01-2019', '11-01-2019', '12-01-2019', '13-01-2019', '14-01-2019', '15-01-2019', '16-01-2019', '17-01-2019', '18-01-2019'],
            datasets: [{
                label: 'Timeline',
                data: [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero:true
                    }
                }]
            }
        }
    });
    
    var ctx = document.getElementById("category_relation");
    var category_relation = new Chart(ctx, {
    	//type: 'line',
    	type: 'horizontalBar',
        data: {
//        	dict_keys(['bolsonaro', 'onyx lorenzoni', 'paulo guedes', 'augusto heleno', 'marcos pontes', 'sérgio moro', 'hamilton mourão', 'joaquim levy', 'mansueto almeida', 'fernando azevedo e silva', 'ernesto araújo', 'roberto campos neto', 'tereza cristina', 'andré luiz de almeida mendonça', 'carlos von doellinger', 'érika marena', 'luiz mandetta', 'maurício valeixo', 'pedro guimarães', 'ricardo vélez rodríguez', 'roberto castello branco', 'rubem novaes', 'wagner rosário', 'bento costa lima leite de albuquerque junior', 'marcelo álvaro antônio', 'osmar terra', 'gustavo henrique rigodanzo canuto', 'tarcísio gomes de freitas', 'carlos alberto dos santos cruz', 'gustavo bebianno', 'jungmann', 'haddad', 'ac', 'al', 'ap', 'am', 'ba', 'ce', 'df', 'es', 'go', 'ma', 'mt', 'ms', 'mg', 'pa', 'pb', 'pr', 'pe', 'pi', 'rj', 'rn', 'rs', 'ro', 'rr', 'sc', 'sp', 'se', 'to'])
//        	dict_values([87.8345498783455, 29.44038929440389, 31.630170316301705, 6.81265206812652, 7.0559610705596105, 32.11678832116788, 7.542579075425791, 0.9732360097323601, 0.48661800486618007, 4.37956204379562, 5.839416058394161, 3.64963503649635, 15.085158150851582, 1.70316301703163, 0.24330900243309003, 0.24330900243309003, 1.4598540145985401, 0.9732360097323601, 1.70316301703163, 4.37956204379562, 0.9732360097323601, 0.9732360097323601, 6.81265206812652, 0.48661800486618007, 3.8929440389294405, 99.7566909975669, 0.48661800486618007, 8.02919708029197, 3.8929440389294405, 7.2992700729927, 0.0, 0.0, 2.67639902676399, 0.7299270072992701, 0.24330900243309003, 1.4598540145985401, 3.40632603406326, 1.70316301703163, 36.982968369829685, 14.111922141119221, 5.35279805352798, 1.2165450121654502, 3.1630170316301705, 7.542579075425791, 6.326034063260341, 1.4598540145985401, 1.4598540145985401, 26.520681265206814, 1.4598540145985401, 0.7299270072992701, 17.0316301703163, 3.64963503649635, 37.469586374695865, 0.0, 4.37956204379562, 2.4330900243309004, 31.143552311435524, 0.24330900243309003, 0.7299270072992701])

            labels: ['bolsonaro', 'onyx lorenzoni', 'paulo guedes', 'augusto heleno', 'marcos pontes', 'sérgio moro', 'hamilton mourão', 'joaquim levy', 'mansueto almeida', 'fernando azevedo e silva', 'ernesto araújo', 'roberto campos neto', 'tereza cristina', 'andré luiz de almeida mendonça', 'carlos von doellinger', 'érika marena', 'luiz mandetta', 'maurício valeixo', 'pedro guimarães', 'ricardo vélez rodríguez', 'roberto castello branco', 'rubem novaes', 'wagner rosário', 'bento costa lima leite de albuquerque junior', 'marcelo álvaro antônio', 'gustavo henrique rigodanzo canuto', 'tarcísio gomes de freitas', 'carlos alberto dos santos cruz', 'gustavo bebianno', 'ac', 'al', 'ap', 'am', 'ba', 'ce', 'df', 'es', 'go', 'ma', 'mt', 'ms', 'mg', 'pa', 'pb', 'pr', 'pe', 'pi', 'rj', 'rn', 'rs', 'ro', 'rr', 'sc', 'sp', 'se', 'to'],

//            labels: ['10-01','11-01','12-01','13-01','14-01'],
            datasets: [{
                label: 'Relacionamento entre categorias (Porcentagem de noticias que contem a categoria Osmar Terra e a categoria relacionada)',
//                data: [87.8345498783455, 29.44038929440389, 31.630170316301705, 6.81265206812652, 7.0559610705596105, 32.11678832116788, 7.542579075425791, 0.9732360097323601, 0.48661800486618007, 4.37956204379562, 5.839416058394161, 3.64963503649635, 15.085158150851582, 1.70316301703163, 0.24330900243309003, 0.24330900243309003, 1.4598540145985401, 0.9732360097323601, 1.70316301703163, 4.37956204379562, 0.9732360097323601, 0.9732360097323601, 6.81265206812652, 0.48661800486618007, 3.8929440389294405, 99.7566909975669, 0.48661800486618007, 8.02919708029197, 3.8929440389294405, 7.2992700729927, 0.0, 0.0, 2.67639902676399, 0.7299270072992701, 0.24330900243309003, 1.4598540145985401, 3.40632603406326, 1.70316301703163, 36.982968369829685, 14.111922141119221, 5.35279805352798, 1.2165450121654502, 3.1630170316301705, 7.542579075425791, 6.326034063260341, 1.4598540145985401, 1.4598540145985401, 26.520681265206814, 1.4598540145985401, 0.7299270072992701, 17.0316301703163, 3.64963503649635, 37.469586374695865, 0.0, 4.37956204379562, 2.4330900243309004, 31.143552311435524, 0.24330900243309003, 0.7299270072992701],
                data: ['87.83', '29.44', '31.63', '6.81', '7.06', '32.12', '7.54', '0.97', '0.49', '4.38', '5.84', '3.65', '15.09', '1.70', '0.24', '0.24', '1.46', '0.97', '1.70', '4.38', '0.97', '0.97', '6.81', '0.49', '3.89', '0.49', '8.03', '3.89', '7.30', '2.68', '0.73', '0.24', '1.46', '3.41', '1.70', '36.98', '14.11', '5.35', '1.22', '3.16', '7.54', '6.33', '1.46', '1.46', '26.52', '1.46', '0.73', '17.03', '3.65', '37.47', '0.00', '4.38', '2.43', '31.14', '0.24', '0.73'],

//                data: [10, 20, 30, 40, 50],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero:true
                    }
                }]
            }
        }
    });
    
    var ctx = document.getElementById("category_sites");
    var category_sites = new Chart(ctx, {
    	//type: 'line',
    	type: 'horizontalBar',
        data: {
            labels: ['agazetadoacre', 'jornalatribuna', 'jornalopiniao', 'oaltoacre', 'oestadoacre', 'oriobranco', 'pagina20', 'anoticia', 'cadaminuto', 'correiodopovo', 'gazetaweb', 'novoextra', 'primeiraedicao', 'tribunahoje', 'tribunauniao', 'aquiamapa', 'diariodoamapa', 'acritica.com', 'ojornaldailha', 'osolimoes', 'aregiao', 'atarde', 'correiodooeste', 'folharegionalbahia', 'folhasertaneja', 'istoenoticia', 'jornalalerta', 'sertaohoje', 'jornalfolhadoestado', 'jornalimpacto', 'jornalnovafronteira', 'novoeste', 'oecojornal', 'diariobahia', 'tribunafeirense', 'anoticiadoceara', 'oestadoce', 'opovo', 'tribunadoceara', 'camara', 'folhacentrooeste', 'jornaldebrasilia', 'jornalregional', 'estacaonews', 'senado', 'aquinoticias', 'correiodoestadoonline', 'estadocapixaba', 'gazetaonline', 'jornalcorreiocapixaba', 'noticiaagora', 'folhaonline', 'tribunaonline', 'diariodeaparecida', 'diariodoestadogo', 'jornalaguaslindas', 'jornalopcao', 'jornalestadodegoias', 'oanapolis', 'ohoje', 'opopular', 'tribunadoplanalto', 'atosefatos', 'imirante', 'oquartopoder', 'circuitomt', 'copopular', 'folhadoestado', 'gazetadigital', 'acritica.net', 'atribunanews', 'correiodoestado', 'jd1noticias', 'midiamax', 'www.em.com.br', 'folhamg', 'hojeemdia', 'correiodaparaiba', 'jornaldaparaiba', 'bemparana', 'diarioinduscom', 'impactopr', 'jornaldoonibusdecuritiba', 'tribunapr', 'correiodepernambuco', 'diariodepernambuco', 'folhape', 'jconline', 'destakjornal', 'www.jb.com.br', 'monitordigital', 'odia.ig.com.br', 'globo', 'agorarn', 'tribunadenoticias', 'tribunadonorte', 'www.osul.com.br', 'correiodenoticia', 'diariodaamazonia', 'folhabv', 'jornalroraimahoje', 'clicrbs', 'ndonline', 'nsctotal', 'brasildefato', 'www.dci.com.br', 'diariodenoticias', 'estadao', 'folha.uol', 'gazetasp', 'horadopovo', 'jornalestacao', 'meioemensagem', 'metronews', 'www.valor.com.br', 'cinform', 'jornaldesergipe', 'jornaldodiase', 'agora-to', 'conexaoto', 'jornaldotocantins', 'ogirassol', 'portalstylo', 'agenciabrasil', 'bastidoresdopoder', 'bbc', 'cartacapital', 'correio24horas', 'diariodocentrodomundo', 'diariodonordeste', 'dinheirorural', 'elpais', 'exame.abril', 'gauchazh', 'gazetadopovo', 'infomoney', 'istoedinheiro', 'jornalestadodeminas', 'jovempan', 'www.justificando.com', 'marceloauler', 'ne10', 'oantagonista', 'r7.com', 'www.terra.com.br', 'tnh1', 'tribunadosertao', 'veja.abril', 'noticias.uol', 'abert.org.br', 'abi.org.br', 'www.administradores.com.br', 'adrenaline', 'ancine', 'apublica', 'avozeavezdajuventude', 'b9.com.br', 'balaiodokotscho', 'blastingnews', 'blogdafloresta', 'blogdoataide', 'blogdoluciosorge', 'revistaforum', 'blogdomello', 'altamiroborges', 'blogdoneylopes', 'blogdopaulinho', 'blogdopaulonunes', 'blogdoprimo', 'blogdoriella', 'blogdoskarlack', 'blogmarcosfrahm', 'buzzfeed', 'cartamaior', 'ceticismopolitico', 'cinegnose', 'comunicadores.info', 'congressoemfoco', 'convergenciadigital', 'correiodobrasil', 'diplomatique', 'domingoscosta', 'www.eb.mil.br', 'ebc.com.br', 'elielbezerra', 'esporteemidia', 'fabiocampana', 'falandoverdades', 'piaui.folha', 'gospelprime', 'grandesnomesdapropaganda', 'huffpostbrasil', 'imprensaviva', 'istoe.com.br', 'jaderbarbalho', 'jornaisvirtuais', 'jornaldocomercio', 'jornalivre', 'jota.info', 'lulacerda', 'marcossilverio', 'migalhas', 'moneytimes', 'mundodomarketing', 'natelinha', 'nocaute.blog.br', 'noticiasdatv', 'oab.org.br', 'observatoriodatelevisao', 'ocafezinho', 'ocombatente', 'operamundi', 'osamigosdopresidentelula', 'osdivergentes', 'outraspalavras', 'papelpop', 'politicanarede', 'poncheverde', 'portaldapropaganda', 'ptnacamara', 'revistapress', 'rufandobombo', 'saibamais.jor.br', 'sputniknews', 'telepadi', 'telesintese.com.br', 'tijolaco', 'www.torcedores.com', 'tribunadainternet', 'tribunadajustica', 'vermelho.org.br', 'viomundo', 'rss_multiplos'],
            datasets: [{
                label: 'Quantidade de noticias relacionadas a categoria Osmar Terra obtidas do site',
//                data: ['0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.24', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.73', '0.24', '0.00', '0.24', '0.00', '0.24', '0.00', '0.00', '0.24', '0.00', '0.00', '0.00', '0.24', '0.00', '0.00', '0.00', '0.24', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.24', '0.00', '0.49', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.49', '0.00', '0.24', '0.00', '0.00', '0.49', '0.00', '0.00', '0.24', '0.00', '0.00', '0.00', '0.00', '0.00', '0.49', '0.00', '0.00', '0.73', '0.73', '0.49', '0.24', '2.19', '0.00', '0.00', '0.73', '1.22', '0.24', '0.49', '0.00', '0.00', '0.24', '0.00', '0.00', '0.00', '0.24', '0.00', '1.46', '4.38', '0.00', '0.00', '0.00', '0.00', '0.00', '1.70', '0.00', '0.00', '0.97', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.49', '0.00', '0.49', '0.00', '0.00', '0.00', '0.00', '0.00', '0.49', '1.22', '0.00', '1.22', '0.00', '0.00', '0.49', '0.24', '0.24', '3.16', '0.24', '0.00', '0.00', '0.97', '0.00', '0.49', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.97', '0.00', '0.00', '0.24', '0.00', '0.00', '0.24', '0.49', '0.00', '0.97', '0.00', '0.00', '0.00', '0.00', '0.00', '1.22', '0.00', '0.00', '0.00', '0.00', '0.00', '1.46', '0.00', '0.00', '0.73', '0.00', '0.00', '0.24', '0.00', '0.24', '0.00', '0.00', '0.00', '0.24', '0.24', '0.00', '0.00', '0.00', '0.00', '0.00', '0.24', '0.00', '0.00', '0.24', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.24', '0.00', '0.00', '0.00', '0.00', '0.00', '0.49', '0.00', '0.00', '0.00', '0.24', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00'],
                data: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 1, 0, 0, 2, 0, 0, 1, 0, 0, 0, 0, 0, 2, 0, 0, 3, 3, 2, 1, 9, 0, 0, 3, 5, 1, 2, 0, 0, 1, 0, 0, 0, 1, 0, 6, 18, 0, 0, 0, 0, 0, 7, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 2, 5, 0, 5, 0, 0, 2, 1, 1, 13, 1, 0, 0, 4, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 1, 0, 0, 1, 2, 0, 4, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 6, 0, 0, 3, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero:true
                    }
                }]
            }
        }
    });
    
    var ctx = document.getElementById("category_set");
    var category_relation = new Chart(ctx, {
    	//type: 'line',
    	type: 'horizontalBar',
        data: {
//        	dict_keys(['bolsonaro', 'onyx lorenzoni', 'paulo guedes', 'augusto heleno', 'marcos pontes', 'sérgio moro', 'hamilton mourão', 'joaquim levy', 'mansueto almeida', 'fernando azevedo e silva', 'ernesto araújo', 'roberto campos neto', 'tereza cristina', 'andré luiz de almeida mendonça', 'carlos von doellinger', 'érika marena', 'luiz mandetta', 'maurício valeixo', 'pedro guimarães', 'ricardo vélez rodríguez', 'roberto castello branco', 'rubem novaes', 'wagner rosário', 'bento costa lima leite de albuquerque junior', 'marcelo álvaro antônio', 'osmar terra', 'gustavo henrique rigodanzo canuto', 'tarcísio gomes de freitas', 'carlos alberto dos santos cruz', 'gustavo bebianno', 'ac', 'al', 'ap', 'am', 'ba', 'ce', 'df', 'es', 'go', 'ma', 'mt', 'ms', 'mg', 'pa', 'pb', 'pr', 'pe', 'pi', 'rj', 'rn', 'rs', 'ro', 'rr', 'sc', 'sp', 'se', 'to'])
//        	dict_values([1013, 104, 80, 25, 11, 133, 28, 1, 0, 14, 10, 2, 7, 0, 0, 0, 0, 0, 0, 3, 0, 1, 2, 0, 0, 13, 0, 2, 5, 7, 37, 16, 9, 26, 37, 52, 311, 61, 19, 13, 26, 40, 56, 14, 25, 167, 34, 15, 222, 21, 123, 8, 24, 28, 311, 13, 2])

            labels: ['bolsonaro', 'onyx lorenzoni', 'paulo guedes', 'augusto heleno', 'marcos pontes', 'sérgio moro', 'hamilton mourão', 'joaquim levy', 'mansueto almeida', 'fernando azevedo e silva', 'ernesto araújo', 'roberto campos neto', 'tereza cristina', 'andré luiz de almeida mendonça', 'carlos von doellinger', 'érika marena', 'luiz mandetta', 'maurício valeixo', 'pedro guimarães', 'ricardo vélez rodríguez', 'roberto castello branco', 'rubem novaes', 'wagner rosário', 'bento costa lima leite de albuquerque junior', 'marcelo álvaro antônio', 'osmar terra', 'gustavo henrique rigodanzo canuto', 'tarcísio gomes de freitas', 'carlos alberto dos santos cruz', 'gustavo bebianno', 'ac', 'al', 'ap', 'am', 'ba', 'ce', 'df', 'es', 'go', 'ma', 'mt', 'ms', 'mg', 'pa', 'pb', 'pr', 'pe', 'pi', 'rj', 'rn', 'rs', 'ro', 'rr', 'sc', 'sp', 'se', 'to'],

            datasets: [{
                label: 'Quantidade de noticias obtidas do site www.terra.com.br relacionadas a categoria',
                data: [1013, 104, 80, 25, 11, 133, 28, 1, 0, 14, 10, 2, 7, 0, 0, 0, 0, 0, 0, 3, 0, 1, 2, 0, 0, 13, 0, 2, 5, 7, 37, 16, 9, 26, 37, 52, 311, 61, 19, 13, 26, 40, 56, 14, 25, 167, 34, 15, 222, 21, 123, 8, 24, 28, 311, 13, 2],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero:true
                    }
                }]
            }
        }
    });
    
    
  } else {
    const errorMessage = document.createElement('marquee');
    errorMessage.textContent = 'Not working!';
  }
}

request.send();