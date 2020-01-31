library(DiffBind)
dbObj <- dba(sampleSheet="sample.csv")
dbObj
dbObj <- dba.count(dbObj,bUseSummarizeOverlaps=TRUE)
dba.plotPCA(dbObj,attributes=DBA_FACTOR,label=DBA_ID)
plot(dbObj)
dbObj
names(dbObj$masks)
tamoxifen_consensus <- dba(dbObj, mask=dbObj$masks$Consensus,minOverlap=1)
consensus_peaks <- dba.peakset(tamoxifen_consensus, bRetrieve=TRUE)
consensus_peaks
write.table(consensus_peaks,file="Embryo.consensus.peaks.table",sep="\t",quote=FALSE)
