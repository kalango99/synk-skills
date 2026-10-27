---
name: synk-posts
description: "Método de diagramação da Synk Lab para carrossel, post e story no Figma, para qualquer marca. Mede as peças que o cliente já aprovou, monta cada tela com um modelo diferente, lê a foto antes de pôr o texto, tira o elemento visual do que o texto diz e confere os erros grosseiros e os vícios de máquina antes de mostrar. Usar sempre que for montar, refazer, variar ou conferir peças de Instagram ou LinkedIn: carrossel, capa, tela final, post único, story, lote de peças, ou quando um carrossel ficou 'tudo igual', 'repetitivo' ou 'com cara de IA'. Não escreve o texto das peças: o texto chega pronto e aprovado."
---

# Synk-posts

> Método da Synk Lab · versão 1 · outubro de 2026 · Breno e Marcos.
> Material da mentoria Synk Lab. Cada regra daqui saiu de uma peça real que foi aprovada ou reprovada.

A Synk Lab trabalha mostrando o processo. A diagramação segue a mesma ideia: **cada tela mostra uma coisa só, e essa coisa é real.** Uma cena, uma tela de trabalho, uma frase, um objeto que representa uma etapa. Nada entra na peça só por ser bonito.

O problema que o método resolve: quando uma fórmula funciona, a tendência é repeti-la em todas as telas. O carrossel fica com cara de modelo pronto e o cliente diz "ficou tudo igual". Aqui, cada tela é montada de um jeito, e o lote inteiro é conferido de uma vez antes de o cliente ver.

## Antes de começar: de onde vêm as regras da marca

Esta skill não traz cor, fonte nem tamanho de nenhuma marca. Ela tira tudo isso do projeto em que está rodando, nesta ordem de quem manda:

1. **O manual da marca do cliente**, se existir no projeto (DNA, guia de marca, brandbook, `DESIGN.md`).
2. **O arquivo `estilo-dos-posts.md` do projeto.** É o registro vivo do que o cliente aprovou, com valores medidos. Se não existir, criar a partir de `references/estilo-dos-posts-modelo.md` na primeira montagem e ir preenchendo.
3. **As peças já aprovadas no Figma.**
4. Este método.

Se o projeto não tiver nenhum dos três primeiros, perguntar ao usuário qual é a marca, pedir 2 ou 3 referências que ele aprove e só então começar. Referência escolhida pela IA não serve de régua.

O texto não é decidido aqui. Ele chega pronto e aprovado. Se a diagramação pedir texto mais curto, devolver o pedido a quem escreveu, sem reescrever por conta própria.

Para ver o método aplicado numa marca de verdade, ler `references/caso-synk-lab.md`.

## O que precisa estar instalado

- **Figma** conectado ao Claude (conector oficial do Figma). Se houver a skill `figma-use`, carregar antes de qualquer `use_figma`.
- **Python 3** com Pillow e numpy, para os programas da pasta `scripts/`. Conferir com `python3 -c "import PIL, numpy"`. Se faltar, avisar o usuário e sugerir `python3 -m pip install pillow numpy`.
- Opcional: um gerador de imagem (Magnific, Higgsfield ou outro) para cenas e objetos.

Nos comandos abaixo, `SKILL_DIR` é a pasta onde este arquivo está.

## Etapa 1. Medir antes de montar

Abrir as peças aprovadas com `get_metadata` ou `use_figma` e anotar os valores reais no `estilo-dos-posts.md`: fonte, tamanho, entrelinha, espaço entre letras, cor em hex ou variável, posição do logo, margem, cantos, opacidades, desfoques.

Nunca estimar pelo print. Um título que parece ter 110 px pode ter 142, e um número errado quebra a palavra em duas linhas, que é o erro que derruba a peça inteira.

Se o arquivo usa variáveis de cor no Figma, ligar as cores novas a elas em vez de colar o hex.

## Etapa 2. Os modelos de tela

Cada tela usa um modelo. **O mesmo modelo nunca aparece em duas telas vizinhas**, e o fundo alterna entre claro, foto e escuro.

| Modelo | O que a tela mostra | Onde fica o texto | Fundo |
|---|---|---|---|
| **Frame de filme** | Uma cena inteira, com contexto, escurecida onde vai o texto | Título na base | Foto |
| **Vidro sobre a cena** | A cena desfocada e um cartão de interface nítido por cima, mostrando o que acontece por dentro (uma mensagem, um botão, um resultado) | Topo ou base, oposto ao cartão | Foto |
| **Frase grande** | Só tipografia, uma palavra na cor de destaque | Terço de baixo ou centro | Claro ou escuro |
| **Capa em índice** | Palavras empilhadas, as opções na cor de destaque e a palavra de ligação em tom neutro | Ocupa a tela | Claro |
| **Close** | Um detalhe em tela cheia: textura, mão, objeto | Curto, na faixa calma | Foto |
| **Objeto da etapa** | Um objeto sobre fundo escuro, com um único ponto de luz na cor de destaque onde acontece a ação | Oposto ao objeto | Escuro |
| **Tela de trabalho** | Um site, sistema ou resultado real numa janela, sangrando pela borda | Topo | Escuro |
| **Lista para marcar** | Os itens do post em linhas, com um círculo para marcar | Topo | Escuro ou claro |

**Logo só na capa e no fechamento.** Selo, logo e barra de progresso repetidos em toda tela deixam o carrossel com moldura de modelo pronto.

**O fechamento reveza** entre formatos, nunca o mesmo em dois posts seguidos:

1. Palavra gigante com as cenas do post em miniatura.
2. Resumo para salvar, com a lista do post.
3. Os passos para contratar ou entrar em contato.
4. Mandar para alguém: uma pergunta que faz a pessoa lembrar de alguém.

**Uma palavra em destaque por título**, no máximo (ou um nome composto). Cor de destaque sólida, nunca transparente. Texto sobre a cor de destaque sempre no tom mais claro da marca.

## Etapa 3. Ler a foto antes de pôr o texto

Toda foto tem uma área que chama o olho e uma faixa calma. O texto vai na faixa calma, do lado oposto ao assunto.

```bash
python3 -I "$SKILL_DIR/scripts/ler_a_cena.py" caminho/da/foto.jpg            # carrossel 4:5
python3 -I "$SKILL_DIR/scripts/ler_a_cena.py" caminho/da/foto.jpg --formato 9:16   # story
```

Ele divide a imagem em 9 partes e devolve onde está o assunto, qual faixa é a mais calma, o lado indicado para o texto, se vale espelhar a foto e se o topo é claro demais para o logo.

Quando o assunto e o texto brigam, três saídas, nesta ordem:

1. Levar o texto para a faixa calma.
2. Espelhar a foto (o assunto troca de lado e o texto fica onde precisa).
3. Subir ou descer a foto dentro da tela até o assunto sair de baixo do escurecimento.

O escurecimento nunca engole o assunto. O objeto principal nunca fica atrás do título. Quando o logo cai sobre área clara, escurecer o topo.

A foto é sempre maior que a tela e deslocada, para nenhuma emenda aparecer. Conferir se o gerador deixou borda branca.

## Etapa 4. O elemento sai do texto

Ler a tela e perguntar o que ela mostra. Uma floricultura pede pétalas. Uma mensagem sem resposta às 22:47 pede o celular na mesa, à noite. Trânsito pede semáforo. O elemento sai do conteúdo, nunca de um catálogo.

O elemento é uma de três coisas:

1. **Uma cena com contexto**, gerada por IA de imagem. A série inteira vive no mesmo mundo (mesmo tipo de lugar, mesma luz, mesmo tratamento de cor, mesmo grão), com ângulo diferente em cada tela. Cada tela tem a sua cena; a mesma foto só se repete quando é a mesma cena em outro momento.
2. **Uma tela real de trabalho:** site no ar, conversa, resultado medido.
3. **Um objeto que representa uma etapa.** Gerado e recortado, **nunca desenhado à mão em vetor**, que sai amador. Alternar 3D e 2D chapado para o recurso não virar maneirismo. Pedido que funciona para o 2D: *flat 2D vector illustration, bold clean outlines, simple geometric shapes, editorial sticker style, palette of <cores da marca>, isolated on plain pure white background, no text, no shadow*.

Regras:

- **Menos da metade das telas leva objeto.** O resto vive de cena, de tela real e de tipografia.
- O objeto fica do lado oposto ao texto, sangrando pela borda. Se não cabe sem competir com o texto, sai.
- Para tirar o fundo branco de um objeto gerado:
  ```bash
  python3 -I "$SKILL_DIR/scripts/recortar_fundo_branco.py" entrada.png saida.png
  ```
  Ele só apaga o branco ligado à borda, então os brancos de dentro do objeto ficam intactos, e corta a imagem no tamanho do objeto.

Evitar o visual genérico de IA: roxo brilhante, robô, cérebro, mão robótica tocando mão humana, fitas abstratas sem significado, painel de dashboard genérico, ícone de biblioteca comum, quadradinho colorido atrás do ícone, mancha de luz difusa como fundo de tela clara. Luz difusa só como brilho atrás de um objeto em fundo escuro.

## Etapa 5. Montar em lote e olhar o lote inteiro

- Duplicar a seção no Figma para cada versão nova (V2, V3...). A versão aprovada nunca é mexida.
- Montar o carrossel inteiro, tirar o `get_screenshot` de cada tela, salvar numa pasta e juntar numa folha só:
  ```bash
  python3 -I "$SKILL_DIR/scripts/folha_de_contato.py" pasta-com-as-telas/ folha.jpg
  ```
- Na folha se vê o que não aparece tela por tela: dois modelos iguais vizinhos, duas telas claras seguidas, a mesma foto, o título sempre no mesmo lugar.

## Quebra de linha harmônica (regra do Breno, 15/10/2026)

"corrigir um pouco a quebra de linha pra ficar um texto harmônico... não ficar viúva tipográfica em uma linha com apenas uma ou duas palavras, quero que sejam linhas harmônicas que facilitem a leitura." Vale para todo texto de todo post: título, apoio, legenda dentro da tela, texto de papel, post do X.

- **Linhas do mesmo tamanho, ou quase.** Num bloco de duas ou três linhas, a última tem pelo menos uns 60% da maior. Nunca uma ou duas palavras sozinhas na última linha.
- **Como ele faz (e como fazer):** não forçar quebra com Enter no meio do apoio. Estreitar a caixa do texto até as linhas se equilibrarem, sem aumentar o número de linhas. No CREDITO V5 ele levou as caixas de 900 para 790, 769, 580, 536 px.
- **Título** pode ter quebra manual, escolhida pelo sentido (cada linha uma ideia), e também sem viúva.
- **Texto centralizado** continua centralizado depois de estreitar (recalcular o x pelo centro).
- **Na conferência (Etapa 6):** olhar a última linha de cada bloco. Uma ou duas palavras sozinhas é erro grosseiro.

Equilíbrio automático no Figma (texto com altura automática): busca binária da menor largura que mantém a mesma altura, depois recentraliza se o alinhamento for centro.

```js
function equilibrar(t){ if(t.textAutoResize!=='HEIGHT') return; const h0=t.height, w0=t.width, cx=t.x+w0/2;
  let lo=w0*0.5, hi=w0; for(let i=0;i<14;i++){ const m=(lo+hi)/2; t.resize(m,t.height); t.textAutoResize='HEIGHT'; if(t.height>h0+1) lo=m; else hi=m; }
  t.resize(Math.ceil(hi)+2,t.height); t.textAutoResize='HEIGHT'; if(t.textAlignHorizontal==='CENTER') t.x=cx-t.width/2; }
```

## Chamada pra arrastar (regra do Breno, 15/10/2026)

"eu ainda sinto que faltam nos carros um CTAzinho desde o primeiro slide para ir arrastar para o lado." Todo carrossel leva um "arrasta pro lado" pequeno e parado no canto de baixo à direita, da tela 1 até a penúltima (a última não leva). Discreto, nunca disputa com o conteúdo, nunca anima nem pula (seta pulando continua proibida).

- Fundo escuro (objetos com física, área de trabalho): "arrasta pro lado" em Geist Medium 26, cor de apoio, com uma seta curta em Pulso.
- Conversa anotada: escrito à mão em Caveat, Pulso, levemente inclinado.
- Post do X: Geist Medium 26 em cinza, com "→".
- Conferir que não encosta em nada: a faixa de baixo à direita fica livre.

## Etapa 6. Conferir antes de mostrar

O cliente olha em duas camadas. Se houver um erro grosseiro, o resto nem é avaliado.

**Erro grosseiro**

- Elemento, fio ou cartão em cima do texto
- Fonte fora do manual da marca
- Emenda ou borda branca da foto aparecendo
- Logo fora do eixo do texto
- Palavra quebrada no meio, ou uma ou duas palavras sozinhas na última linha (ver "Quebra de linha harmônica")
- Texto sem contraste contra a foto
- Tela vazia ou faltando camada
- Número que ninguém mediu nem aprovou

**Vícios de máquina**

- Travessão no texto
- Traço decorativo antes de rótulo ou título
- Cor de destaque transparente ou em mais de uma palavra por título
- Contador subindo de zero, "arraste para o lado" com seta pulando
- Os três clichês juntos: número grande no centro, numeração 01/02/03 e rótulo em caixa alta espaçada (um deles passa; os três juntos entregam a peça)
- Moldura repetida em toda tela
- Mesma foto em telas diferentes

**Conferência automática:** contar as camadas de cada tela contra o esperado, procurar imagens repetidas entre telas, confirmar que a sequência está completa e em ordem.

**O teste da troca de logo:** trocar o logo da marca pelo de um concorrente. Se a tela continuar servindo, está genérica. Refazer essa tela.

## Etapa 7. Quando o cliente mexe, vira régua

- O cliente decide na tela pronta, nunca na descrição. Mostrar a peça, não explicar a peça.
- Pedido de estética (premium, elegante, sofisticado): pedir 2 ou 3 referências dele antes de gerar.
- Referência é para tirar a lógica, nunca a cara.
- Quando o usuário disser que mexeu no Figma, comparar camada por camada com o que foi montado (cor, borda, opacidade, tamanho, posição), não só pelo print. Registrar a diferença no `estilo-dos-posts.md`, com a data e a frase dele. É assim que a régua da marca cresce a cada post.
- Exportar só quando o usuário pedir.

## Eixo e edição ao mesmo tempo

- **Eixo:** se o texto está à direita, o logo, o selo e qualquer fio vão para a direita também. Nada fica solto, flutuando sem alinhamento.
- **Arquivo aberto:** se o usuário está com o Figma aberto, o que foi criado pode sumir por um desfazer dele, e camadas podem ser agrupadas. Reler o estado real antes de qualquer correção em lote e nunca apagar o que não foi criado nesta sessão.
