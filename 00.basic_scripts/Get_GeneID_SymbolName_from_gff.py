#!/usr/bin/env python3.4
'''
#-------------------------------------------------------------------------------
#Author:Pan Xiangyu(bendanpanxiangyu@163.com)
#Time:  2016/12/5
#Version: 1.0
#-------------------------------------------------------------------------------
'''
#######################modle####
import sys
import re
import os
import getopt
def usage():
    print('''Useage: python script.py [option] [parameter]
    -f/--gtf        input merge gtf
    -o/--output          extraction file
    -h/--help            show possible options''')
####################### argv ######
opts, args = getopt.getopt(sys.argv[1:], "hf:o:",["help","gtf=","output="])
for op, value in opts:
    if op == "-f" or op == "--gtf":
        gtf = value
    elif op == "-o" or op == "--output":
        output = value
    elif op == "-h" or op == "--help":
        usage()
        sys.exit(1)
if len(sys.argv) < 2:
    usage()
    sys.exit(1)
f1=open(gtf)
f2=open(output,'w')
'''
##gff-version 3
#!gff-spec-version 1.21
#!processor NCBI annotwriter
#!genome-build Oar_v4.0
#!genome-build-accession NCBI_Assembly:GCF_000298735.2
##sequence-region NC_019458.2 1 275406953
##species http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=9940
1       RefSeq  region  1       275406953       .       +       .       ID=id0;Dbxref=taxon:9940;Name=1;breed=Texel;chromosome=1;gbkey=Src;genome=chromosome;mol_type=genomic DNA
1       Gnomon  gene    49237   54549   .       +       .       ID=gene0;Dbxref=GeneID:106990386;Name=LOC106990386;gbkey=Gene;gene=LOC106990386;gene_biotype=lncRNA
1       Gnomon  ncRNA   49237   54549   .       +       .       ID=rna0;Parent=gene0;Dbxref=GeneID:106990386,Genbank:XR_001433683.1;Name=XR_001433683.1;gbkey=ncRNA;gene=LOC106990386;ncrna_class=lncRNA;product=uncharacterized LOC106990386%2C transcript variant X1;transcript_id=XR_001433683.1
###
# stringtie --merge -G /stor9000/apps/users/NWSUAF/2016050001/goat_pan/my_clean_data/bwa_mem/GCF_001704415.1_ASM170441v1_genomic_CHR.gff -o ./Rumen_goat.merge.gff gtf_file.txt -g 100 -m 200 -c 0.8
# StringTie version 1.2.2
1       StringTie       transcript      72191   79644   1000    +       .       gene_id "MSTRG.1"; transcript_id "rna1"; gene_name "ATP5O"; ref_gene_id "gene1";
1       StringTie       exon    72191   72309   1000    +       .       gene_id "MSTRG.1"; transcript_id "rna1"; exon_number "1"; gene_name "ATP5O"; ref_gene_id "gene1";
1       StringTie       exon    73696   73746   1000    +       .       gene_id "MSTRG.1"; transcript_id "rna1"; exon_number "2"; gene_name "ATP5O"; ref_gene_id "gene1";
1       StringTie       exon    74679   74789   1000    +       .       gene_id "MSTRG.1"; transcript_id "rna1"; exon_number "3"; gene_name "ATP5O"; ref_gene_id "gene1";
1       StringTie       exon    76942   77071   1000    +       .       gene_id "MSTRG.1"; transcript_id "rna1"; exon_number "4"; gene_name "ATP5O"; ref_gene_id "gene1";
1       StringTie       exon    77760   77872   1000    +       .       gene_id "MSTRG.1"; transcript_id "rna1"; exon_number "5"; gene_name "ATP5O"; ref_gene_id "gene1";
1       StringTie       exon    79089   79175   1000    +       .       gene_id "MSTRG.1"; transcript_id "rna1"; exon_number "6"; gene_name "ATP5O"; ref_gene_id "gene1";
1       StringTie       exon    79463   79644   1000    +       .       gene_id "MSTRG.1"; transcript_id "rna1"; exon_number "7"; gene_name "ATP5O"; ref_gene_id "gene1";
'''

namedict={}
iddict={}
for reads in f1:
    if '#' in reads:
        pass
    else:
        reads=reads.split("\t")
        if reads[2] =='gene' :
            info=reads[8]
#            info_s=info.split("; ")
            x=re.search('GeneID:(.*);',info)
            #print(x)
       #     x.group(1)
         #   print(x.group(1))
            if x==None:
                pass
            else:
#                i=x[0].split("=")
                i = x.group(1)
                z=i.split(";")
#                print(z)
            y=re.search('Name=(.*);',info)
#            y.group(1)
            #print(y)
            if y==None:
#               namedict[z[0]]=z[0]
                pass
            else:
                p = y.group(1)
                
#                n=i[1][:-1]
                m = p.split(";")
#                print(m[0])
                namedict[m[0]]=z[0]
#            else:
#                namedict[info_s[0][8:]]=info_s[1][14:]
        else:
            pass
#print(namedict)
for key,value in namedict.items():
    f2.write(key+"\t"+value+"\n")
'''
for line in f2:
    if 'FPKM' in line:
        f3.write(line)
    else:
        line_s=line.strip().split()
        expression='\t'.join(line_s[1:])
#        print(line_s[0])
        if line_s[0] in namedict:
#            print(line_s[0])
            f3.write(namedict[line_s[0]]+'\n')
        else:
            f3.write(line_s[0]+'\n')
#            pass
'''
f1.close()
f2.close()
