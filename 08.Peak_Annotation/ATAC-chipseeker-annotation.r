library("GenomicFeatures")
library("ChIPseeker")
library(AnnotationHub)
library(ggplot2)
Oaries <- makeTxDbFromGFF("GCF_000298735.2_Oar_v4.0_genomic.gff.chr",format="gff3")
txdb = Oaries
rumen1 <- readPeakFile("Rumen_T1_peaks.narrowPeak",header=FALSE)
covplot(rumen1,chrs=c("1", "2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","NC_001941.1","X")) ##SHEEP
promoter <- getPromoters(TxDb=txdb, upstream=3000, downstream=3000)
tagMatrix <- getTagMatrix(rumen1, windows=promoter)
tagHeatmap(tagMatrix, xlim=c(-3000, 3000), color="red")
x = annotatePeak(rumen1, tssRegion=c(-1000, 1000), TxDb=txdb)
y = annotatePeak(rumen2, tssRegion=c(-1000, 1000), TxDb=txdb)
as.GRanges(y);head(3)
yy <- as.data.frame(y)
write.table(yy,file="RumenI.annotation",sep="\t",quote=FALSE)
dev.off()
