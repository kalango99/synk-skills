"""Lê uma foto antes de pôr o texto: onde está o assunto e onde está a faixa calma.

Uso: python ler_a_cena.py foto.jpg [--formato 4:5]
O formato padrão é o do carrossel da Synk Lab (1080 x 1350, 4:5). Para story use 9:16.
"""
import argparse
from PIL import Image, ImageOps, ImageFilter
import numpy as np

NOMES_LINHA = ["topo", "meio", "base"]
NOMES_COLUNA = ["esquerda", "centro", "direita"]


def recortar_no_formato(imagem, proporcao):
    largura, altura = imagem.size
    if largura / altura > proporcao:
        nova = int(altura * proporcao)
        x = (largura - nova) // 2
        return imagem.crop((x, 0, x + nova, altura))
    nova = int(largura / proporcao)
    y = (altura - nova) // 2
    return imagem.crop((0, y, largura, y + nova))


def ler_a_cena(caminho, proporcao):
    imagem = recortar_no_formato(Image.open(caminho).convert("RGB"), proporcao)
    imagem = imagem.resize((270, int(270 / proporcao)))
    cinza = ImageOps.grayscale(imagem)
    bordas = np.asarray(cinza.filter(ImageFilter.FIND_EDGES), dtype=float)
    tons = np.asarray(cinza, dtype=float)
    energia = bordas + np.abs(tons - tons.mean()) * 0.35

    altura, largura = energia.shape
    grade = np.zeros((3, 3))
    for linha in range(3):
        for coluna in range(3):
            pedaco = energia[linha * altura // 3:(linha + 1) * altura // 3,
                             coluna * largura // 3:(coluna + 1) * largura // 3]
            grade[linha, coluna] = pedaco.mean()
    grade = grade / grade.max() * 100

    linha_assunto, coluna_assunto = np.unravel_index(grade.argmax(), grade.shape)
    faixas = grade.mean(axis=1)
    faixa_calma = int(faixas.argmin())
    colunas = grade.mean(axis=0)
    lado_texto = "esquerda" if colunas[0] < colunas[2] else "direita"
    brilho_por_faixa = [tons[i * altura // 3:(i + 1) * altura // 3].mean() for i in range(3)]

    print("Energia por parte (100 = a mais carregada):")
    print("            " + "  ".join(f"{n:>9}" for n in NOMES_COLUNA))
    for linha in range(3):
        print(f"  {NOMES_LINHA[linha]:>8}  " + "  ".join(f"{grade[linha, c]:9.0f}" for c in range(3)))
    print()
    print(f"Assunto: {NOMES_LINHA[linha_assunto]} {NOMES_COLUNA[coluna_assunto]}")
    print(f"Faixa calma: {NOMES_LINHA[faixa_calma]}")
    print(f"Lado indicado para o texto: {lado_texto}")
    if NOMES_COLUNA[coluna_assunto] == lado_texto:
        print("Atenção: o assunto está no lado do texto. Considere espelhar a foto.")
    if NOMES_COLUNA[coluna_assunto] == "centro":
        print("Assunto no centro: texto na faixa calma, de margem a margem.")
    print("Brilho médio por faixa (0 preto, 255 branco): "
          + ", ".join(f"{NOMES_LINHA[i]} {brilho_por_faixa[i]:.0f}" for i in range(3)))
    if brilho_por_faixa[0] > 150:
        print("Topo claro: escurecer o topo se o logo ou o selo forem ficar ali.")


if __name__ == "__main__":
    argumentos = argparse.ArgumentParser()
    argumentos.add_argument("foto")
    argumentos.add_argument("--formato", default="4:5", help="largura:altura, ex. 4:5 ou 9:16")
    lidos = argumentos.parse_args()
    a, b = (float(x) for x in lidos.formato.split(":"))
    ler_a_cena(lidos.foto, a / b)
