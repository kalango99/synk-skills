# Ferramentas do MCP Buzzy

Levantado em 19/10/2026, primeira sessão autenticada (`claude mcp add --transport http --scope user buzzy https://mcp.buzzy.now/mcp`, login via `/mcp`).

## Geração simples (imagem ou vídeo avulso)

| Ferramenta | Para quê | Parâmetros |
|---|---|---|
| `list_model` | Lista modelos com resoluções, aspect ratios, durações e limites. **Chamar antes de gerar** e copiar os valores literalmente. | nenhum |
| `GenerateImage` | Gera imagem (assíncrono, devolve `task_id`). | `prompt` (até 8192, mas respeite o `max_text_length` do modelo), `model`, `resolution`, `aspect_ratio` (obrigatórios), `image_urls[]` (refs públicas, até `max_images`), `project_id` |
| `GenerateVideo` | Gera vídeo (assíncrono). | idem + `duration`, `video_urls`, `audio_urls` |
| `get_task` | Consulta a tarefa até `TASK_STATE_SUCCEEDED`; devolve `node_id` e as URLs. **Nunca reenviar a geração, cobra duas vezes.** | `task_id` |
| `createProject` | Cria projeto (canvas) com nome. Reusar o id em tudo. | `name` |

## Upload de referência local (Claude Code)

1. `UploadFile` com `files[]` (`filename`, `content_length` em bytes, `content_type`). Devolve `upload_url` (pré-assinada, 15 min) e `url` (CDN).
2. `curl -X PUT -H 'If-None-Match: *' -H 'Content-Type: image/png' --upload-file "<caminho>" '<upload_url>'` → precisa dar 200. Use `--upload-file`, nunca `--data-binary`.
3. `ConfirmFileUpload` com `urls[]`. Só depois a URL vale em `image_urls`.

`UploadResource` é widget de navegador (Apps); no Claude Code use o caminho acima.

## Workflows (peças com várias etapas)

`load_workflow` (sem argumento = catálogo de skills do Buzzy; com nome = instruções), `load_workflow_bundle_file`, `ExecutePromptWorkflow`, `DirectorStoryboardWorkflow`, `VideoGenerationWorkflow`, `VideoMergeWorkflow`, `ModifyStoryWorkflow`, `VariationStoryWorkflow`, `RegenerateBGMWorkflow`, `AssetImageGenerationWorkflow`, `SkillAssetChoice`, `ParseProductInfo`, `DisplayProductInfo`, `CreateCanvasDisplayNode`. Regra do servidor: para anúncio, UGC, explainer, série ou drama, chamar `load_workflow` antes e `createProject` antes do primeiro passo. Portões de confirmação usam o AskUserQuestion do host.

## Modelos de imagem (19/10/2026)

| id | Resoluções | Aspect ratios | Máx. refs | Máx. prompt |
|---|---|---|---|---|
| `Nano Banana Pro` | 1K, 2K, 4K | 1:1, 2:3, 3:2, 3:4, 4:3, 4:5, 5:4, 9:16, 16:9, 21:9 | 14 | 2000 |
| `Nano Banana 2.1` / `Nano Banana 2` | 1K, 2K, 4K | idem | 14 | 2000 |
| `doubao-seedream-5-0-260128` | 2K, 3K, 4K | 1:1, 4:3, 3:4, 16:9, 9:16, 3:2, 2:3, 21:9 (sem 4:5) | 14 | 2000 |
| `gpt-image-2`, `gpt-image-2.5-flare`, `gpt-image-2.5-sunburst` | 1k, 2k, 4k | sem 4:5 | 16 | 2000 |
| `grok-imagine-image` | 1k, 2k | vários + auto | 8 | n/d |
| `recraftv4_1` | n/d | muitos, inclui 4:5 | 1 | 10000 |
| `mj_v7`, `mj_v8.2` | 1K | sem 4:5 | 5 | n/d |

## Modelos de vídeo (19/10/2026)

| id | Resoluções | Duração | Primeiro/último quadro | Refs (img/vídeo/áudio) |
|---|---|---|---|---|
| `Seedance 2.5` | 480p, 720p, 1080p | 4 a 30 s | não | 30 / 10 / 10 |
| `dreamina-seedance-2-0-260128` | até 4k | 4 a 15 s | sim | 9 / 3 / 3 |
| `Kling 4.0` | 720p, 1080p | 4 a 30 s | não | 10 / 5 / 0 |
| `Kling 3.0` | até 4k | 4 a 15 s | sim | 4 / 1 / 0 |
| `kling-motion-control` | 720p, 1080p | n/d | n/d | 1 / 1 (copiar movimento de um vídeo) |
| `Veo 3.1` / `Veo 3.1 Fast` | até 4k / 1080p | 4, 6, 8 s | sim | 2 / 0 / 0 |
| `MiniMax-H3` | 480p, 768p, 2k | 4 a 15 s | sim | 9 / 3 / 3 |
| `wan3.0-video` | até 1080p | 2 a 30 s | sim | 10 / 5 / 0 |
| `gen4.5` (Runway) | 720p | 4 a 12 s | sim | 1 / 1 |
| `Flux3`, `grok-imagine`, `gemini-omni-*` | ver `list_model` | | | |

Áudio: `suno`, `music_v2`, `music-2.6`, `mureka` (música), `eleven_multilingual_v2`, `eleven_turbo_v2_5`, `speech-2.8-hd/turbo` (voz), `eleven_text_to_sound_v2` (efeito).

## Custo

O MCP **não expõe saldo nem custo por geração**. Confirmar sempre com o Marcos antes, e conferir o saldo no painel do buzzy.now.
