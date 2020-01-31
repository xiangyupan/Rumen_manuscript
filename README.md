# Custom scripts  
Custom scripts for manuscript "Tracing the origin of a new organ by inferring the genetic basis of rumen evolution"  

## 00.basic_scripts   
This part including two scripts:
The first script *Get_GeneID_from_gff.py* was used to transer gene official name to NCBI Entrez ID by command line: 
`python3.5 Get_GeneID_from_gff.py -f GCF_000298735.2_Oar_v4.0_genomic.gff -g demo.esophagus.gene.list -o demo.esophagus.gene.list.ID`   
The second script *Get_GeneID_SymbolName_from_gff.py* was used to transer NCBI Entrez ID to gene official name.

## 01.First-Chamber_Stomach_Specifically_expressed_genes       
This part including two scripts:   
The first script *01_calE50.ipynb* was used to calculate the E50 index of the first-chamber stomach with the gene expression profile table of sheep, camels and cetaceans, respectively. We only retained protein-coding genes as the candidate first-chamber stomach specifically expressded genes based on the annotation file in gff format of sheep (*Ovis aries*), Bactrian camel (*Camelus bactrianus*) and Indo-Pacific Finless Porpoise (*Neophocaena asiaeorientalis*), respectively.    
The second script *02_E50cutoff.ipynb* was used to detect the threshold of E50 index with type I error less than 0.05.   

## 02.Gene_Ontology_Enrichment    
The script *GoEnrichment.pl* was used to conduct gene ontology (GO) enrichment analysis.   
All the GO enrichment analyses were conducted by command line as follow:    
`perl GoEnrichment.pl demo.esophagus.gene.list sheep.background.list`   
The file "gene_ontology.obo.zip" need to be unziped before used.    

## 03.
