"""Tira o fundo branco de um objeto gerado, sem furar os brancos de dentro dele.

Uso: python recortar_fundo_branco.py entrada.png saida.png
Só apaga o branco que está ligado à borda da imagem; depois corta no tamanho do objeto.
"""
import sys
from collections import deque
from PIL import Image
import numpy as np


def recortar(entrada, saida):
    imagem = Image.open(entrada).convert("RGBA")
    cores = np.asarray(imagem).copy()
    rgb = cores[..., :3].astype(int)
    quase_branco = (rgb.min(axis=2) > 238) & ((rgb.max(axis=2) - rgb.min(axis=2)) < 14)

    altura, largura = quase_branco.shape
    fundo = np.zeros_like(quase_branco)
    fila = deque()
    for x in range(largura):
        for y in (0, altura - 1):
            if quase_branco[y, x] and not fundo[y, x]:
                fundo[y, x] = True
                fila.append((y, x))
    for y in range(altura):
        for x in (0, largura - 1):
            if quase_branco[y, x] and not fundo[y, x]:
                fundo[y, x] = True
                fila.append((y, x))
    while fila:
        y, x = fila.popleft()
        for vy, vx in ((y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)):
            if 0 <= vy < altura and 0 <= vx < largura and quase_branco[vy, vx] and not fundo[vy, vx]:
                fundo[vy, vx] = True
                fila.append((vy, vx))

    cores[..., 3] = np.where(fundo, 0, cores[..., 3])
    resultado = Image.fromarray(cores)
    caixa = resultado.getchannel("A").getbbox()
    if caixa:
        resultado = resultado.crop(caixa)
    resultado.save(saida)
    print(f"Salvo em {saida} ({resultado.size[0]} x {resultado.size[1]})")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("Uso: python recortar_fundo_branco.py entrada.png saida.png")
    recortar(sys.argv[1], sys.argv[2])
