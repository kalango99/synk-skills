"""Junta as telas de um carrossel numa folha só, para ver repetição de uma vez.

Uso: python folha_de_contato.py pasta-com-as-telas/ folha.jpg [--colunas 5]
As telas entram em ordem alfabética do nome do arquivo, numeradas embaixo.
"""
import argparse
from pathlib import Path
from PIL import Image, ImageDraw

EXTENSOES = {".png", ".jpg", ".jpeg", ".webp"}


def montar(pasta, saida, colunas, largura_tela=360):
    arquivos = sorted(p for p in Path(pasta).iterdir() if p.suffix.lower() in EXTENSOES)
    if not arquivos:
        raise SystemExit("Nenhuma imagem encontrada na pasta.")
    altura_tela = int(largura_tela * 1350 / 1080)
    espaco, legenda = 16, 28
    linhas = -(-len(arquivos) // colunas)
    folha = Image.new("RGB", (colunas * (largura_tela + espaco) + espaco,
                              linhas * (altura_tela + legenda + espaco) + espaco), (18, 18, 20))
    desenho = ImageDraw.Draw(folha)
    for indice, arquivo in enumerate(arquivos):
        tela = Image.open(arquivo).convert("RGB")
        tela.thumbnail((largura_tela, altura_tela))
        x = espaco + (indice % colunas) * (largura_tela + espaco)
        y = espaco + (indice // colunas) * (altura_tela + legenda + espaco)
        folha.paste(tela, (x, y))
        desenho.text((x, y + altura_tela + 6), f"{indice + 1}  {arquivo.name}", fill=(190, 190, 196))
    folha.save(saida, quality=90)
    print(f"Folha com {len(arquivos)} telas salva em {saida}")


if __name__ == "__main__":
    argumentos = argparse.ArgumentParser()
    argumentos.add_argument("pasta")
    argumentos.add_argument("saida")
    argumentos.add_argument("--colunas", type=int, default=5)
    lidos = argumentos.parse_args()
    montar(lidos.pasta, lidos.saida, lidos.colunas)
