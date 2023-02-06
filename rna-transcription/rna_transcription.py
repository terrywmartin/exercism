def to_rna(dna_strand):
    rna_strand = ''
    dna_rna = { 'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}

    for seq in dna_strand:
        rna_strand += dna_rna[seq]

    return rna_strand
