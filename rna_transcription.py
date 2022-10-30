def to_rna(dna_strand):
    dna = ['A', 'C', 'G', 'T']
    formula = ['U', 'G', 'C', 'A']

    rna = ''

    for i in range(len(dna_strand)):
        rna += formula[dna.index(dna_strand[i])]

    return
