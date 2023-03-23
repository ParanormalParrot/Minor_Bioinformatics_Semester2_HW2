import pandas

df = pandas.read_csv('simple_somatic_mutation.open.tsv.gz', sep='\t', usecols=['gene_affected'])

HRAS = "ENSG00000174775"
TP53 = "ENSG00000141510"
KDM6A = "ENSG00000147050"
PIK3CA = "ENSG00000121879"
KMT2D = "ENSG00000167548"

print("Mutations in HRAS gene: \t%s" % len(df[df.gene_affected == HRAS]))
print("Mutations in TP53 gene:  \t%s" % len(df[df.gene_affected == TP53]))
print("Mutations in KDM6A gene: \t%s" % len(df[df.gene_affected == KDM6A]))
print("Mutations in PIK3CA gene: \t%s" % len(df[df.gene_affected == PIK3CA]))
print("Mutations in KMT2D gene: \t%s" % len(df[df.gene_affected == KMT2D]))