# Custom scripts  
Custom scripts for manuscript "Tracing the origin of a new organ by inferring the genetic basis of rumen evolution"  

## 00.basic_scripts   
This part including two scripts:
The first script *Get_GeneID_from_gff.py* was used to transer gene official name to NCBI Entrez ID by command line:    
`python3.5 Get_GeneID_from_gff.py -f GCF_000298735.2_Oar_v4.0_genomic.gff -g demo.esophagus.gene.list -o demo.esophagus.gene.list.ID`   
The second script *Get_GeneID_SymbolName_from_gff.py* was used to transer NCBI Entrez ID to gene official name.

## 01.Trimmomatic   
The script *trimmomatic.sh* was used to filter low-quality reads of raw reads to obtain clean reads for transcriptome sequencing.

## 02.Mapping   
The first script *STAR.index.sh* was used to build genome index for mapping next. 
The second script *STAR.map.sh* was used to map clean reads to reference genome including three steps.   

## 03.First-Chamber_Stomach_Specifically_expressed_genes       
This part including two scripts:   
The first script *01_calE50.ipynb* was used to calculate the E50 index of the first-chamber stomach with the gene expression profile table of sheep, camels and cetaceans, respectively. We only retained protein-coding genes as the candidate first-chamber stomach specifically expressded genes based on the annotation file in gff format of sheep (*Ovis aries*), Bactrian camel (*Camelus bactrianus*) and Indo-Pacific Finless Porpoise (*Neophocaena asiaeorientalis*), respectively.    
The second script *02_E50cutoff.ipynb* was used to detect the threshold of E50 index with type I error less than 0.05.   

## 04.Gene_Ontology_Enrichment    
The script *GoEnrichment.pl* was used to conduct gene ontology (GO) enrichment analysis.   
All the GO enrichment analyses were conducted by command line as follow:    
`perl GoEnrichment.pl demo.esophagus.gene.list sheep.background.list`   
The file "gene_ontology.obo.zip" need to be unziped before used.    

## 05.Cut_adapt_and_fastqc     
The script *cutadapt.sh* was used to cut adapter and detect the quality of raw reads from ATAC-seq.   

## 06.Mapping_ATAC-seq  
The first shell script *bowtie2.index.sh* was used to build index files for mapping clean reads to reference geneome by bowtie2.  
The second shell script *bowtie_dedup_MT2.sh* was used to map reads, remove duplicated reads and reads mapped to mitochondria and retain the unique mapping reads.    

## 07.Peak_Calling    
The shell script *macs2.call.peak.sh* was used to call open accessible chromatin regions.  

## 08.Peak_Annotation   
The R script was used to annotate genes in the vicinty of peaks with the annotation file in gff format.   
