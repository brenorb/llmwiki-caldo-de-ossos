# Wise Traditions: auditoria das237 entradas da seleção inglesa

**Atualização de26/11/2026:** o episódio181 foi transcrito novamente, em execução isolada, sem limite de duração ou timeout por gravação. O novo log registra **17/17 blocos em ordem, uma conclusão e saída0**. Assim, há versões com prova estrita para os237 GUIDs selecionados:236 da auditoria original e uma nova para181. Os arquivos e a ressalva histórica abaixo permanecem preservados. [Prova da nova execução](../../raw/wapf-audio-en-181-isolado-2026-11-26.json)

Em26/11/2026, a auditoria confirmou **237 conjuntos de mídia/TXT/log/checkpoint,948 arquivos físicos**. Todos os hashes/tamanhos foram reconferidos pelo revisor após a leitura integral do parecer. O alvo é a **seleção fixa de237 GUIDs de páginas curtas**, dentro de um RSS inglês de608 itens; não o canal inteiro. [Inventário porGUID, metadados e provas](../../raw/wapf-audio-en-237-processamento-2026-11-26.json)

| Controle | Resultado |
|---|---|
| Mídia e resultados disponíveis |237 MP3,237 TXT,237 logs e237 checkpoints; nenhum artefato ausente.|
| Duração somada |126h25min25s, segundo metadados ffprobe; sem nova audição ou decodificaçãoPCM integral.|
| Checkpoints |237 declaram verified, com metadados/tamanhos/timestamps conferidos.|
| Logs com sequência final estrita |236, somando3.957 blocos ordenados.|
| Exceção de prova |Episódio181 tem os índices1–17 presentes; no log inteiro1–12 se repetem entre duas execuções.|
| Leitura semântica |Nenhuma nova leitura dos237 TXT foi alegada por esta auditoria.|

## O episódio181

*Food lies exposed*, GUID `da2e32fbccc14c668c989f148171a674`, tem os quatro arquivos e bordas conferidos. O log mistura duas execuções e não associa cada linha inequivocamente ao TXT final. **Isso não demonstra áudio faltante nem exige nova ASR automaticamente.** É uma pendência conservadora de reconciliação da prova; o original permanece preservado. As3.974 declarações totais de blocos incluem os17 desse log, sem fingir que todos passaram pela validação estrita de ordem.


O esclarecimento posterior leu log/checkpoint inteiros: **1–12 aparecem duas vezes no log completo e13–17 uma vez**. O recorte da auditoria inicial, após o segundo anúncio de transcrição, tinha apenas6–12 repetidos porque os primeiros1–5 da outra execução estavam antes desse anúncio. Sob hipótese de dois laços, existe uma subsequência ordenada1–17 e outra1–12, semPID que autentique a atribuição ao TXT final.

O código local atual percorre os blocos em ordem e incorpora resultados, mas não foi comprovado como o mesmo build histórico que gerou181. Mantém-se a pendência de proveniência, sem inferir fala faltante ou reiniciarASR. Os16 entregáveis originais da auditoria continuam congelados; o adendo e seus hashes estão no registro público.

## Nova execução isolada de181

Usou o mesmo MP3 de **31min30,339s**, modelo `parakeet-v3-int8`, saída timestampada com `--text --raw`, sem corte de duração. Foram geradas332 linhas,34.550 caracteres; os inícios vão de00:00:00 a00:31:25, sem recuos e com oito pares de inícios iguais. O último tempo marca o início do segmento, não seu fim. O log inteiro foi conferido e está associado a um único processo da nova execução; os quatro artefatos anteriores mantêm os mesmos hashes.

O novo TXT é uma versão separada. Resolve a atribuição do processamento desta versão, sem modificar o log intercalado anterior nem demonstrar que aquele TXT tinha fala faltante. Foram registrados hashes de mídia, TXT, log, metadados, script e executável; o hash do executável não identifica sozinho todas as dependências/modelos. Não houve nova audição ou leitura semântica integral do texto nesta validação.

## Integralidade e acurácia são controles distintos

O worker existente processa a gravação inteira, sem limite de duração por mídia. Timeout do download, timeout da consulta ffprobe e tolerâncias de timestamps não são cortes da transcrição. Não houve novo download ou reinício nesta auditoria.

Os354 recuos de timestamp são de1s, em185 TXT. Foram enumerados48 intervalos entre inícios acima de55s, em41 TXT, sem inferir silêncio ou fala omitida. O último timestamp também é **início**, não fim do segmento. Checkpoint, hash e blocos completos não garantem reconhecimento de toda palavra ou precisão de nomes/números; não houve escuta ou leitura semântica do corpus nesta checagem.

O [catálogo espanhol de189](wapf-audio-es-processamento189.md) tem auditoria própria. Esses resultados não viraram receitas, estudos ou leituras novas por estarem processados. [Cobertura geral](../cobertura.md)
