#!/bin/bash

test ! -f test.png

python plot_gtex.py GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt ACTA2 SMTS test.png

test -f test.png

rm test.png