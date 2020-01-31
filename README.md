# Custom scripts  
Custom scripts for manuscript "Tracing the origin of a new organ by inferring the genetic basis of rumen evolution"  

## 01.First-Chamber_Stomach_Specifically_expressed_genes       
This part including two scripts:   
The first script *01_calE50.ipynb* was used to calculate the E50 index of the first-chamber stomach with the gene expression profile table of sheep, camels and cetaceans, respectively. We only retained protein-coding genes as the candidate first-chamber stomach specifically expressded genes based on the annotation file in gff format of sheep (*Ovis aries*), Bactrian camel (*Camelus bactrianus*) and Indo-Pacific Finless Porpoise (*Neophocaena asiaeorientalis*), respectively.    
The second script *02_E50cutoff.ipynb* was used to detect the threshold of E50 index with type I error less than 0.05.    
