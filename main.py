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

cavalo_a = pegar_sequencia("Horse.pdb", "A")
humano_a = pegar_sequencia("Humam.pdb", "A")

print(cavalo_a + "\n" + humano_a)