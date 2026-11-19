print()

tabela = {
    "ALA": "A",
    "ARG": "R",
    "ASN": "N",
    "ASP": "D",
    "CYS": "C",
    "GLN": "Q",
    "GLU": "E",
    "GLY": "G",
    "HIS": "H",
    "ILE": "I",
    "LEU": "L",
    "LYS": "K",
    "MET": "M",
    "PHE": "F",
    "PRO": "P",
    "SER": "S",
    "THR": "T",
    "TRP": "W",
    "TYR": "Y",
    "VAL": "V",
}

def pegar_sequencia(arquivo, cadeia):
    sequencia = ""
    ultimo_lido = None
    
    with open(arquivo, "r") as arq:
        for linha in arq:
            if linha.startswith("ATOM"):
                cadel = linha[21]
                lido = linha[17:20].strip()
                numero = linha[22:26].strip()

                if cadel == cadeia and numero != ultimo_lido:
                    letra = tabela.get(lido, "?")
                    sequencia += letra
                    ultimo_lido = numero
    
    return sequencia

def comparar(sequencia_1, sequencia_2, nome_1, nome_2):
    iguais = 0
    total = min(len(sequencia_1), len(sequencia_2))

    for i in range(total):
        if sequencia_1[i] == sequencia_2[i]:
            iguais += 1
        else:
            print(f"  Posição {i + 1}: {nome_1} tem '{sequencia_1[i]}' | {nome_2} tem '{sequencia_2[i]}'")

    print()
    print("-" * 70)
    print()
    porcentagem = (iguais / total) * 100
    print(f"Identidade entre {nome_1} e {nome_2}: {porcentagem:.1f}%")
    print()
    print("-" * 70)
    print()

cavalo_a = pegar_sequencia("Horse.pdb", "A")
humano_a = pegar_sequencia("Humam.pdb", "A")

cavalo_b = pegar_sequencia("Horse.pdb", "B")
humano_b = pegar_sequencia("Humam.pdb", "B")

comparar(cavalo_a, humano_a, "Cavalo (Horse) - Cadeia A", "Humano (Humam) - Cadeia A")
comparar(cavalo_b, humano_b, "Cavalo (Horse) - Cadeia B", "Humano (Humam) - Cadeia B")

#print(cavalo_a + "\n" + humano_a)