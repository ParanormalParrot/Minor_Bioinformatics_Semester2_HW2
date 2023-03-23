import pandas

df = pandas.read_csv('simple_somatic_mutation.open.tsv.gz', sep='\t', usecols=['icgc_donor_id', 'gene_affected'])

APC = "ENSG00000134982"
TP53 = "ENSG00000141510"
KRAS = "ENSG00000133703"
PIK3CA = "ENSG00000121879"
SMAD4 = "ENSG00000141646"

print("Mutations in APC gene:  \t%s" % len(df[df.gene_affected == APC]))
print("Mutations in TP53 gene: \t%s" % len(df[df.gene_affected == TP53]))
print("Mutations in KRAS gene: \t%s" % len(df[df.gene_affected == KRAS]))
print("Mutations in PIK3CA gene: \t%s" % len(df[df.gene_affected == PIK3CA]))
print("Mutations in SMAD4 gene: \t%s" % len(df[df.gene_affected == SMAD4]))