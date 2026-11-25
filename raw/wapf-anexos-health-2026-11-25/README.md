# Registro público compacto — cinco anexos WAPF

Pacote pronto para copiar à camada `raw`, sem modificação da wiki. Publica cobertura e localizadores, **não** os textos dos slides/notas ou as medidas culinárias completas. Não contém caminhos absolutos ou nomes de pacientes.

|Arquivo|Conteúdo|Registros|
|---|---|---:|
|`registro-anexos.json`|Registro canônico com método, cobertura e limites|5 fontes,32 itens,21 localizadores de medidas|
|`registro-anexos.schema.json`|JSON Schema Draft2020-12|1|
|`anexos.tsv`|URLs reais, hashes originais, páginas/slides/notas, visual/EMF/OLE|5|
|`itens-culinarios.tsv`|Títulos e ordinais dos preparos; relações com as medidas privadas|32|
|`medidas-localizadores.tsv`|Ordinais, relações e hashes por linha do TSV privado de medidas|21|
|`comprovantes-privados.tsv`|Hashes/tamanhos de ledgers, manifestos e outros comprovantes privados|15|
|`manifesto-publico-sha256.json`|Hashes dos arquivos públicos; não inclui o próprio manifesto|7 arquivos|

## Schema e índices

`sources` contém uma entrada por URL: `unit` distingue slide/página; `units` é a contagem física; `notes_available`/`notes_read` contam partes disponíveis, inclusive notas curtas. I eII são os seminários; O é Oiling; M é Milk; F é Flyer.

`text_read_ranges` e `visual_overview_ranges` usam pares inclusivos. `visual_expanded_ordinals` enumera os slides/páginas lidos individualmente em tamanho ampliado. O panorama de607 slides não equivale a leitura integral das letras miúdas das imagens. Os32 visuais ampliados são **slides**; as2 páginas PDF são contadas separadamente.

`emf_main_graphs_recovered_read` identifica os13 gráficos recuperados e examinados visualmente; `emf_main_graphs_unresolved` está vazio. Duas partes auxiliares deI:176 têm área inválida e não receberam conteúdo presumido. `ole_count`/`ole_ordinals` inventariam objetos que **não** foram executados. Relações externas não foram seguidas; a conversão de PPT legado pode perder recursos.

`culinary_items` usa IDs `CUL-001`–`CUL-032`. `measure_ids` referencia `MED-001`–`MED-021`; lista vazia significa ausência de registro quantitativo separado, não falta de leitura. Os quatro métodos de caldo/redução são `CUL-015`–`CUL-018`.

`measure_locators` não publica as medidas. Cada entrada aponta para os ordinais de slides/notas e para uma linha do arquivo privado `quantidades-culinarias.tsv`, identificado também em `private_evidence_proofs`. `private_row_1based` começa em1 na primeira linha de dados, excluindo o cabeçalho; `private_row_sha256` é o SHA-256 do JSON canônico da linha TSV parseada como objeto, em UTF-8, com chaves ordenadas, sem espaços e sem escapes ASCII forçados.21 entradas não significa21 valores numéricos distintos: o TSV privado também registra tempos/rendimentos e ausências explícitas.

Nos TSV, arrays são células JSON; separador tabulação e codificação UTF-8. Comprovantes privados são identificados somente por chave relativa, tamanho e hash; sua íntegra não acompanha o pacote público.

## Conferência e limites

Cobertura:5 fontes,607 slides,589 notas disponíveis lidas,607 panoramas,32 slides ampliados,13 gráficos EMF recuperados,2 páginas PDF e4 objetos OLE não executados. Unidades/macros/rendimentos não foram inferidos de fotografias. Low carb não foi quantificado. Referências citadas não receberam leitura primária nem validação clínica; conteúdo infantil não virou fórmula prática ou recomendação clínica.
