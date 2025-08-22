"""Gera um resumo de despesas a partir de um arquivo CSV."""

import argparse
import csv
import sys
from collections import defaultdict


def gerar_relatorio(caminho_csv, coluna_categoria="Categoria", coluna_valor="Valor"):
    """Lê um CSV e imprime o total de despesas por categoria."""
    try:
        with open(caminho_csv, newline='', encoding='utf-8') as csvfile:
            leitor = csv.DictReader(csvfile)
            if coluna_categoria not in leitor.fieldnames or coluna_valor not in leitor.fieldnames:
                print(f"O CSV deve conter as colunas '{coluna_categoria}' e '{coluna_valor}'.")
                return False
            totais = defaultdict(float)
            total = 0.0
            for linha in leitor:
                try:
                    valor = float(str(linha[coluna_valor]).replace(',', '.'))
                except (ValueError, TypeError):
                    continue
                categoria = linha[coluna_categoria]
                totais[categoria] += valor
                total += valor
    except FileNotFoundError:
        print(f"Erro: Arquivo '{caminho_csv}' não encontrado.")
        return False
    except Exception as e:
        print(f"Erro ao ler o CSV: {e}")
        return False

    print("--- Resumo de Despesas ---")
    for categoria, valor in sorted(totais.items(), key=lambda item: item[1], reverse=True):
        print(f"{categoria}: {valor:.2f}")
    print(f"Total: {total:.2f}")
    return True


def parse_args():
    """Processa argumentos da linha de comando."""
    parser = argparse.ArgumentParser(description="Gera um resumo de despesas a partir de um arquivo CSV.")
    parser.add_argument("arquivo", help="Caminho para o arquivo CSV.")
    parser.add_argument("--categoria", default="Categoria", help="Nome da coluna de categoria. Padrão: 'Categoria'.")
    parser.add_argument("--valor", default="Valor", help="Nome da coluna de valor. Padrão: 'Valor'.")
    return parser.parse_args()


def main():
    args = parse_args()
    sucesso = gerar_relatorio(args.arquivo, args.categoria, args.valor)
    if not sucesso:
        sys.exit(1)


if __name__ == "__main__":
    main()
