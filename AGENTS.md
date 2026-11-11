# Manutenção da LLMWiki sobre caldo de ossos

A estrutura segue [a proposta de LLM Wiki de Andrej Karpathy](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

## Camadas

- `raw/` guarda originais quando a cópia é permitida e acessível, ou registros de acesso que indicam o localizador, a versão/data, a parte consultada e restrições. Preserve o original e registre novas versões em arquivos próprios. Consulte [o guia da camada bruta](raw/README.md).
- `wiki/fontes/` guarda notas por fonte. `wiki/temas/` contém a síntese que incorpora essas notas. O [índice](index.md) enumera páginas e o [mapa de proveniência](wiki/proveniencia.md) liga afirmações centrais às fontes.
- Este arquivo define as convenções. O [log](log.md) registra ingestões, consultas incorporadas e revisões em ordem cronológica.

## Ingestão

As páginas públicas apontam para as fontes externas. Cópias de trabalho e seu manifesto ficam no acervo local.

1. Comece pelo [índice](index.md) e localize as páginas afetadas. Verifique título, autores, ano, identificador, versão e acesso. Leia métodos, resultados, tabelas e declarações de financiamento antes de incorporar números. Registre correções, retratações e limites de acesso. Ao citar só o resumo, identifique-o.
2. Arquive original permitido ou registro de acesso e abra uma nota em `wiki/fontes/`. Registre o objeto estudado, o desenho, comparador, tamanho amostral, unidade, achados, limites e páginas relacionadas. Identifique as tabelas ou seções relevantes. Fontes culinárias sustentam métodos, enquanto orientações sanitárias dependem de autoridades e protocolos aplicáveis.
3. Atualize a síntese nas páginas existentes, preserve divergências explicadas e vincule cada afirmação verificável à nota. Use as classes da [proveniência](wiki/proveniencia.md). Ao cruzar estudos, separe líquidos prontos, concentrados e pós. Declare conversões e preserve unidades de origem.
4. Atualize índice, proveniência e log. Use cabeçalhos de log no formato `## [AAAA-MM-DD] ingestão | assunto`. Execute `python3 scripts/verificar-links.py`.
5. Transcreva a gravação inteira, independentemente da duração. Se o transcritor exigir trechos menores, divida a faixa em blocos e remonte a transcrição com os tempos da gravação original. Confira a cobertura até o último bloco e registre problemas de acesso à mídia ou trechos inaudíveis no inventário.

## Consulta

Comece pelo índice, siga os links para as notas e consulte o original quando houver ambiguidade. Em questões de saúde, separe composição, biomarcadores, desfechos clínicos e validade externa. Registre uma síntese nova na wiki quando ela preencher uma lacuna durável. Para segurança alimentar, revalide a fonte e o contexto de aplicação antes de atualizar um limite.

## Revisão

Faça uma checagem estrutural com o verificador e uma leitura editorial. Procure fontes órfãs, duplicações, divergências de unidade, extrapolações, avisos desatualizados e contradições entre as páginas de preparo e conservação. Desafie as afirmações de ausência de evidência com busca por termos alternativos e registros de ensaios. Registre perguntas, achados, correções e lacunas no log. Para reavaliar as conclusões clínicas, confira as datas e as estratégias de busca registradas na página de saúde.
