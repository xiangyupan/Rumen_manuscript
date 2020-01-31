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
    -g/--gene            input gene name list
    -o/--output          extraction NCBI Entrez ID file
    -h/--help            show possible options''')
####################### argv ######
opts, args = getopt.getopt(sys.argv[1:], "hf:g:o:",["help","gtf=","gene","output="])
for op, value in opts:
    if op == "-f" or op == "--gtf":
        gtf = value
    elif op == "-g" or op == "--gene":
        gene = value
    elif op == "-o" or op == "--output":
        output = value
    elif op == "-h" or op == "--help":
        usage()
        sys.exit(1)
if len(sys.argv) < 5:
    usage()
    sys.exit(1)
f1=open(gtf)
f2=open(gene)
f3=open(output,'w')
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
###gene
"FPKM.sheep_10banjianji_H37TGALXX_L1" "FPKM.sheep_10banmoji_H37TGALXX_L1" "FPKM.sheep_10beizuichangji_H37TGALXX_L1" "FPKM.sheep_10ganzang_H35KVALXX_L7" "FPKM.sheep_10liuwei_H32YGALXX_L8" "FPKM.sheep_10pixiazhifang_H33NKALXX_L5" "FPKM.sheep_10tipi_H33NKALXX_L5" "FPKM.sheep_10weizhi_H37TGALXX_L2" "FPKM.sheep_11banjianji_H37TGALXX_L1" "FPKM.sheep_11banmoji_H37TGALXX_L1" "FPKM.sheep_11beizuichangji_H37TGALXX_L1" "FPKM.sheep_11ganzang_H35KVALXX_L7" "FPKM.sheep_11liuwei_H32YGALXX_L8" "FPKM.sheep_11pixiazhifang_H33NKALXX_L5" "FPKM.sheep_11tipi_H33NKALXX_L5" "FPKM.sheep_11weizhi_H33NKALXX_L5" "FPKM.sheep_1banmo_HWNMLCCXX_L5" "FPKM.sheep_1fupi_HWNMLCCXX_L5" "FPKM.sheep_1liuwei_H32YYALXX_L2" "FPKM.sheep_1pizhi_HWLNNCCXX_L7" "FPKM.sheep_1tipi_HWNMLCCXX_L6" "FPKM.sheep_1tuoye_H32YYALXX_L2" "FPKM.sheep_1wangwei_H32YYALXX_L2" "FPKM.sheep_1weizhi_HWNMLCCXX_L5" "FPKM.sheep_2banjian_H37TGALXX_L1" "FPKM.sheep_2banmo_H37TGALXX_L1" "FPKM.sheep_2beichang_H37TGALXX_L1" "FPKM.sheep_2gan_H37LWALXX_L8" "FPKM.sheep_2liuwei_H35KVALXX_L7" "FPKM.sheep_2pizhi_H37TGALXX_L2" "FPKM.sheep_2tipi_H37TGALXX_L1" "FPKM.sheep_2weizhi_H33NKALXX_L5" "FPKM.sheep_3banmo_HWNMLCCXX_L6" "FPKM.sheep_3beichang_HWNMLCCXX_L6" "FPKM.sheep_3fupi_HWNMLCCXX_L6" "FPKM.sheep_3pizhi_HWNMLCCXX_L6" "FPKM.sheep_3tipi_HWNMLCCXX_L6" "FPKM.sheep_3weizhi_HWNYYCCXX_L4" "FPKM.sheep_4banjian_HWNMLCCXX_L6" "FPKM.sheep_4banmo_HWNMLCCXX_L6" "FPKM.sheep_4beichang_HWNMLCCXX_L6" "FPKM.sheep_4fupi_HWNMLCCXX_L6" "FPKM.sheep_4pizhi_HWNMLCCXX_L6" "FPKM.sheep_4tipi_HWNMLCCXX_L6" "FPKM.sheep_4weizhi_HWNMLCCXX_L6" "FPKM.sheep_5banjian_HWNNLCCXX_L3" "FPKM.sheep_5banmo_HWNNLCCXX_L3" "FPKM.sheep_5beichang_HWNNLCCXX_L3" "FPKM.sheep_5fupi_HWM57CCXX_L3" "FPKM.sheep_5tipi_HWM57CCXX_L3" "FPKM.sheep_5weizhi_HWNNLCCXX_L3" "FPKM.sheep_6banjian_H3533ALXX_L3" "FPKM.sheep_6banmo_H3533ALXX_L6" "FPKM.sheep_6beichang_H3533ALXX_L3" "FPKM.sheep_6gan_H3533ALXX_L5" "FPKM.sheep_6liuwei_H3533ALXX_L5" "FPKM.sheep_6pizhi_H3533ALXX_L3" "FPKM.sheep_6tipi_H3533ALXX_L4" "FPKM.sheep_6weizhi_H3533ALXX_L3" "FPKM.sheep_7banjianji_H37LWALXX_L8" "FPKM.sheep_7banmoji_H37LWALXX_L8" "FPKM.sheep_7banwei_H32YGALXX_L5" "FPKM.sheep_7beizuichangji_H37LWALXX_L8" "FPKM.sheep_7biantaoti_H35KVALXX_L7" "FPKM.sheep_7chuiti_H32YGALXX_L6" "FPKM.sheep_7ganzang_H35KVALXX_L7" "FPKM.sheep_7jiaozhi_H35KVALXX_L7" "FPKM.sheep_7liuwei_H32YGALXX_L4" "FPKM.sheep_7pixiazhifang_H37LWALXX_L8" "FPKM.sheep_7shidao_H35KVALXX_L7" "FPKM.sheep_7tipi_H37LWALXX_L8" "FPKM.sheep_7tuoyexian_H3533ALXX_L5" "FPKM.sheep_7wangwei_H32YGALXX_L4" "FPKM.sheep_7weizhi_H37LWALXX_L8" "FPKM.sheep_7xiaqiunao_H35KVALXX_L7" "FPKM.sheep_7zhouwei_H32YGALXX_L5" "FPKM.sheep_8banjianji_H37LWALXX_L8" "FPKM.sheep_8banmoji_H3727ALXX_L4" "FPKM.sheep_8banwei_H32YGALXX_L8" "FPKM.sheep_8beizuichangji_H37LWALXX_L8" "FPKM.sheep_8biantaoti_H35KVALXX_L7" "FPKM.sheep_8chuiti_H35KVALXX_L7" "FPKM.sheep_8ganzang_H32YGALXX_L7" "FPKM.sheep_8jiaozhi_H35KVALXX_L7" "FPKM.sheep_8liuwei_H35KVALXX_L7" "FPKM.sheep_8pixiazhifang_H3727ALXX_L4" "FPKM.sheep_8shidao_H35KVALXX_L7" "FPKM.sheep_8tipi_H3727ALXX_L4" "FPKM.sheep_8tuoyexian_H32YGALXX_L6" "FPKM.sheep_8wangwei_H32YGALXX_L7" "FPKM.sheep_8weizhi_H3727ALXX_L4" "FPKM.sheep_8xiaqiunao_H35KVALXX_L7" "FPKM.sheep_8zhouwei_H32YGALXX_L8" "FPKM.sheep_9banjianji_H3727ALXX_L4" "FPKM.sheep_9banmoji_H37TGALXX_L1" "FPKM.sheep_9beizuichangji_H3727ALXX_L4" "FPKM.sheep_9ganzang_H3533ALXX_L5" "FPKM.sheep_9liuwei_H32YGALXX_L8" "FPKM.sheep_9pixiazhifang_H37TGALXX_L1" "FPKM.sheep_9tipi_H37TGALXX_L1" "FPKM.sheep_9weizhi_H33NKALXX_L5" "FPKM.sheep_banwei1_H32NYALXX_L4" "FPKM.sheep_banwei3_H32NYALXX_L4" "FPKM.sheep_biantao1_HW3K2CCXX_L8" "FPKM.sheep_biantao3_HW3K2CCXX_L8" "FPKM.sheep_gan1_H32NYALXX_L4" "FPKM.sheep_gan3_H32YYALXX_L2" "FPKM.sheep_gan4_H32YYALXX_L2" "FPKM.sheep_gan5_H32NYALXX_L4" "FPKM.sheep_jiaozhi1_H32NYALXX_L4" "FPKM.sheep_liuwei3_H32NYALXX_L7" "FPKM.sheep_liuwei4_H32NYALXX_L4" "FPKM.sheep_liuwei5_H32NYALXX_L4" "FPKM.sheep_naochuiti3_HW3K2CCXX_L8" "FPKM.sheep_shidao1_HW3K2CCXX_L8" "FPKM.sheep_shidao3_HW3K2CCXX_L8" "FPKM.sheep_shidao4_H32NYALXX_L4" "FPKM.sheep_shidao5_H32NYALXX_L4" "FPKM.sheep_wangwei3_HW3K2CCXX_L8" "FPKM.sheep_xiaqiu1_HW3K2CCXX_L8" "FPKM.sheep_xiaqiu3_HW3K2CCXX_L8" "FPKM.sheep_zhouwei1_H32NYALXX_L4" "FPKM.sheep_zhouwei3_HW3K2CCXX_L8"
"gene1" 0 0 0 0 0 0.037641 0.017228 0.037075 0 0 0 0 0 0.100106 0 0.031717 0 0 0 0.10855 0 0 0 0 0 0 0 0 0.010759 0 0 0 0 0 0 0 0 0 0 0 0 0 0.047431 0 0 0 0 0 0.07421 0 0 0.008543 0.036775 0 0 0 0.018289 0.027791 0 0 0 0 0 0.031515 0.228462 0 0 0 0 0 0.019091 0 0 0 0.03318 0 0 0 0.001697 0 0.080252 0.399506 0 0 0 0 0 0.009058 0 0 0 0.078732 0 0 0 0 0 0 0 0 0.004401 0 0 0.097722 0.227099 0 0 0 0 0 0 0 0.00393 0.089076 0 0 0 0 0 0.050466 0 0 0
"gene10009" 0 0 0.000340303858254678 0.0178501356184799 0.0162526174863388 0.0446782401059778 0.025225622619639 0.0703067476403378 0 0 0.0011464884914721 0 0 0.0349832366285809 0.0188422891207153 0.104052458022851 0.0204412379533035 0.0304605504222553 0 0.0980765305514158 0.0208170101010101 0 0 0.131245132803444 0.0091115159794668 0 0.00959752740519954 0 0 0.0899961799966882 0.00158456979632389 0.0916590478556052 0.0190704364961086 0 0.0457483417784401 0.0916538943533698 0.0943092230501739 0.0826219423745653 0.01141695479384 0.0258209147209803 0 0 0.112921447590661 0.0448913512170889 0.168291281834741 0.0289900543136281 0.0136409124027157 0.0182383695976155 0.0168675681404206 0.0969894754098361 0.0958077888723299 0.016439072859745 0 0.0154718430203676 0 0.0434889158801126 0.0878549529723464 0.0255394131478722 0.106161383341613 0 0 0.0349496855439642 0 0.0920775966219573 0.011271247226362 0.00908275790693823 0.0327822854777281 0.010315520615996 0 0.0295450851134294 0.00953234244080146 0.00889007882099685 0.00683100082795165 0.0359188325881769 0.269735382679252 0.0550266545785726 0.00151175856929955 0 0.0105522954131479 0.0130360342771982 0.112764236794171 0.0810929715184633 0.00868685510846167 0.0280841750289783 0.0250262333167743 0.0340485992714026 0.00991099039576089 0.0225271568140421 0 0.0363527478059281 0.0364383950985262 0.116918819672131 0 0.019630260307998 0 0.00166703825136612 0.00960615482695811 0.0505290162278523 0.0592665530717006 0.0403504515648286 0.0188106552409339 0.0103471544957774 0.0279394260639179 0.0603229329359165 0.248711306838881 0.0107890702102997 0.0229604451068058 0.0968251352872992 0.0107037545951316 0.0201855979466799 0.0119068006292433 0.0169749316111939 0.0308056472925981 0.0924514515648286 0.0433879986752774 0.0159693576751118 0.0202255524093393 0.0130053589998344 0.0225130923994039 0.0985357011094552 0.0833648592482199 0.0269060526577248 0
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
f1.close()
f2.close()
f3.close()
