# WAPF: inventário e aquisição de249 páginas das demais classes

Em26/11/2026, a aquisição do catálogo fixo887 alcançou **todos os249 alvos** das classes restantes. O revisor conferiu **498 hashes físicos**, identidades, contagens e flags de texto não branco. Foram249 respostasHTTP200, com **237 TXT não brancos e12 lacunas de extração**. Isso é aquisição, **sem acrescentar leituras semânticas ou fontes clínicas**. [Inventário completo porURL, acesso, hashes e lacunas](../../raw/wapf-classes-restantes-aquisicao249-2026-11-26.json)

**Atualização posterior:** os [12 textos estáticos principais foram recuperados e lidos](wapf-direct-index-main12.md), com escopo `main#genesis-content` e versões estritas originais preservadas. Isso resolve a lacuna do texto principal salvo, sem declarar destinos, paginação ou mídia lidos. As contagens abaixo continuam sendo as da aquisição estrita inicial.

O [primeiro lote de50 resenhas](wapf-book-review50.md) também tem leitura integral própria. Essa cobertura está ligada às provas posteriores, sem converter a aquisição inicial em leitura nem inferir os livros completos.

| Classe original | URLs | TXT estritos não brancos | Objeto e limite |
|---|---:|---:|---|
| Podcast |124|124|Páginas textuais; ler o texto não significa ter ouvido a gravação.|
| Book-review |78|78|Resenhas; não representam leitura integral dos livros.|
| Direct-index |34|22|Índices/arquivos; extração estrita não cobre automaticamente listagem inteira, paginação ou destinos.|
| Gallery |13|13|Corpos textuais; imagens/galeria visual não foram examinadas pela aquisição.|

O material soma18.317 linhas/4.789.442 caracteres nosTXT preservados, incluindo os12 arquivos cujo conteúdo é apenas uma quebra de linha. Foram congelados sete lotes: resenhas50/28, podcasts50/50/24, índices34 e galerias13. A leitura desses novos cortes terá registro próprio; o processamento automático não altera as contagens lidas de health/other.

## Alvo, identidade e extração

Os índices locais de tipos próprios permitiram identificar216 URLs;33 índices diretos ficaram com rótulos locais explícitos, sem inventar IDs de WordPress. As respostas permitem verificar215 WPIDs estruturais. Em uma resenha, **ID indexado18670 versus WPIDHTTP20783** na mesma URL/canonical `eat-right-nick-barnard` são preservados separadamente, sem atribuir causa à divergência.

Em arquivos como `/blog/`, o título/autor/data recuperados podem corresponder ao **primeiro artigo listado**, não ao arquivoBlog. O alvo continua sendo a URL e classe catalogadas. Não se substituiu o índice por esse artigo.

As12 extrações brancas são todas de índices diretos. O modelo original considerou espaços/quebras como conteúdo válido em dois casos; a auditoria exige texto físico não branco e preserva ambas as flags. A lista completa dessasURLs e os respectivos hashes estão no registro. **HTTP200 com TXT branco não é leitura concluída nem prova de página globalmente vazia/inacessível.** A [extração posterior do main estático](wapf-direct-index-main12.md) recuperou esses textos, mantendo a paginação e os destinos separados.

## Cobertura que permanece fora desta aquisição

Imagens, mídia, comentários, livros completos, destinos e estudos externos não foram consultados por causa do download. Alegações históricas de leitura do catálogo não substituem prova individual por hash/faixas. As páginas foram obtidas porHTTPS com certificado validado e sem cookies; não houve corte de tamanho do corpo ou ASR. [Cobertura geral](../cobertura.md) · [Proveniência](../proveniencia.md)

A leitura dos [12 índices recuperados](wapf-direct-index-main12.md) e dos [22 complementares](wapf-direct-index-main22.md) fecha34/34 textos principais estáticos; preserva versões estritas e não abre destinos/páginas seguintes por inferência. As [78 resenhas](wapf-book-review28.md) têm fechamento próprio como resenhas, sem leitura dos livros.

Os [textos das13 galerias](wapf-gallery13.md) foram lidos integralmente como legendas/navegação, com prova própria e sem ver as imagens. Relatos sobrepostos não viraram indivíduos ou coortes independentes, e nomes individuais de crianças não foram reproduzidos no registro público de sobreposição.
