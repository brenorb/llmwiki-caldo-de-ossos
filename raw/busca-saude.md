# Registro de acesso e busca — Saúde

Consulta exploratória em 2026-11-11, com busca web, páginas da PubMed/PMC, editoras e registros públicos de ensaios. O objetivo foi localizar primeiro estudos com caldo em humanos, depois confrontar alegações com estudos em animais e estudos clínicos de intervenções relacionadas. As notas de fonte indicam a versão e o nível de acesso. Este registro descreve a consulta inicial e pode ser complementado com novos registros datados de busca.

| Frente | Consultas representativas | Resultado útil |
| --- | --- | --- |
| Estudos diretos | `"bone broth" randomized clinical trial human consumed participant`, `"bone broth" randomized crossover participants`, `site:clinicaltrials.gov "bone broth"`, `site:anzctr.org.au "bone broth"` | Artigo de aminoácidos plasmáticos e registro australiano. Os comparadores são diferentes produtos e as porções têm doses desiguais. |
| Intestino | `"bone broth powder" "intestinal permeability"`, `"Broth & Co Beef Bone Broth Powder" ACTRN`, `ACTRN12620000092998`, `bone broth experimental colitis murine model` | Relatório comercial rastreado pelo link do resumo executivo e checado contra o registro indexado. Dois artigos primários em camundongos. O estudo humano digestivo é de braço único. |
| Peso | `"bone broth diet" weight loss trial`, `"An open-label clinical trial" "bone broth" obesity`, `10.1016/j.nutos.2025.04.009`, `NCT05740670` | Resumo e DOI de ensaio aberto com dieta multicomponente. |
| Articulações e fraturas | `"bone broth" trial joint bone healing`, `"bone broth" osteoarthritis WOMAC`, `骨汤 临床 试验 骨折`, `사골국 섭취 임상시험 골다공증 관절염`, `collagen osteoarthritis meta-analysis`, `König specific collagen peptides bone mineral density` | Suplementos e decocções medicinais de composição diferente foram separados do caldo culinário. Nenhum ensaio humano controlado de caldo para artrose ou fraturas foi localizado nessas consultas. Seki et al. mediram densidade em um modelo de perda óssea em ratas. |
| Desfechos e mecanismos relacionados | `collagen supplements skin aging meta analysis industry funded`, `Shaw vitamin C gelatin exercise`, `Zhou glutamine postinfectious irritable bowel syndrome`, `Rennard chicken soup neutrophil chemotaxis`, `Saketkhoo chicken soup nasal mucus velocity`, `Yamadera glycine sleep` | Suplementos, nutrientes isolados, estudos de marcadores e sopa de galinha em contextos específicos. |

## Acesso e seleção

- A consulta foi orientada por perguntas, com termos em português/inglês e consultas exploratórias em chinês/coreano. Não houve dupla triagem sistemática, extração de todos os ensaios de suplementos ou busca integral em bases proprietárias. “Não localizado” descreve essa busca. Uma consulta complementar da API ClinicalTrials.gov em 2026-11-11 com o termo exato `"bone broth"` retornou um registro, NCT05740670. Esse resultado não cobre outros registros nacionais ou estudos registrados com terminologia distinta.
- O relatório de 11 páginas do NIIM/Broth & Co estava acessível no CDN da marca. O documento se apresenta como versão pública baseada no relatório de 23/06/2021. A ficha individual [ANZCTR ACTRN12620000092998](https://www.anzctr.org.au/Trial/Registration/TrialReview.aspx?ACTRN=12620000092998) abriu por consulta direta após o leitor web falhar. Ela confirma o financiamento comercial, o desenho e os desfechos primários. Não foi localizado artigo revisado por pares com os resultados.
- Doma et al. teve resumo oficial indexado e ficha em AGRIS. Editor e plataforma do periódico retornaram HTTP 403 para HTML integral/PDF. A [API pública de ClinicalTrials.gov](https://clinicaltrials.gov/api/v2/studies/NCT05740670) permitiu ler e [preservar o registro NCT05740670](https://clinicaltrials.gov/api/v2/studies/NCT05740670) após a página HTML abrir apenas a estrutura. O registro fundamenta os dados de protocolo e patrocínio. O resumo publicado fundamenta os resultados.
- Para Liang et al. o resumo e trechos indexados estavam disponíveis. Para Myung e Park e Saketkhoo et al. a nota usa o resumo bibliográfico. Nos demais casos, a nota aponta o texto ou documento consultado.
- Referências foram rastreadas do artigo de aminoácidos de Alcock ao registro, ao estudo de composição e ao ensaio de gelatina. Foram cruzados o relatório do NIIM, seu resumo executivo, a ficha ANZCTR e o material de divulgação. A revisão narrativa de Matar et al. e sua bibliografia levaram ao estudo pré-clínico de enxaqueca. Foi incluído o estudo multicomponente de Konijeti et al., que recomendava caldo sem isolar sua contribuição. Para pele, foram comparados revisão favorável, revisão com análise de financiamento e reanálise de metodologia.

Voltar a [Alegações de saúde](../wiki/temas/alegacoes-saude.md).

## Fontes consultadas e hashes das cópias locais

Arquivos recuperados em 2026-11-11. Os PDFs estão sob CC BY, conforme avisos nas publicações. Para as demais fontes, as notas fornecem links e detalhes de acesso.

| Arquivo | Origem | SHA-256 |
| --- | --- | --- |
| [Alcock et al. (2019)](https://www.frontiersin.org/journals/nutrition/articles/10.3389/fnut.2019.00163/pdf) | [PDF da Frontiers](https://www.frontiersin.org/journals/nutrition/articles/10.3389/fnut.2019.00163/pdf) | `c728ddde8875539076b0bcad710727434ca43c1f677eecc80287fc5071ac2c34` |
| [Mar-Solís et al. (2021)](https://mdpi-res.com/d_attachment/medicina/medicina-57-01138/article_deploy/medicina-57-01138-v2.pdf?version=1634803313) | [PDF da MDPI, versão 2](https://mdpi-res.com/d_attachment/medicina/medicina-57-01138/article_deploy/medicina-57-01138-v2.pdf?version=1634803313) | `0d8651f30ef31fd8865f454234f2e07d3725e8a653c14fabd5e5ac72c07c36ca` |
| [Wang et al. (2022)](https://www.frontiersin.org/journals/nutrition/articles/10.3389/fnut.2022.821404/pdf) | [PDF da Frontiers](https://www.frontiersin.org/journals/nutrition/articles/10.3389/fnut.2022.821404/pdf) | `98c429b3f057e06e4ac9ba4b339b704d814011b07421f194613c04a5c67a78d0` |
| [NCT05740670](https://clinicaltrials.gov/api/v2/studies/NCT05740670) | [API do registro ClinicalTrials.gov](https://clinicaltrials.gov/api/v2/studies/NCT05740670) | `38721e0753ff098b22baea9d0119240a129e8a73023a92cdef2fc6bf18d2bf99` |
