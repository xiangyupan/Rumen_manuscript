#!/bin/sh
file="Rumen_T1
"
for i in $file
do
echo $i
#/stor9000/apps/appsoftware/BioSoftware/bin/bowtie2 -x ~/Chip_RNA/ATAC-seq/02.bowtie.index/sheep.v4.bowtie2.index -X 2000 -1 /stor9000/apps/users/NWSUAF/2016050001/Chip_RNA/ATAC-seq/New_development/2.cutadapt/$i\_1_val_1.fq.gz -2 /stor9000/apps/users/NWSUAF/2016050001/Chip_RNA/ATAC-seq/New_development/2.cutadapt/$i\_2_val_2.fq.gz -S $i.sam
#samtools view -bS $i.sam > $i.bam
#samtools view -q 20 -u $i.bam > $i.uniq20.bam
#samtools sort -o $i.uniq20.sort.bam -@ 8 -O bam  $i.uniq20.bam
#samtools index $i.uniq20.sort.bam
/stor9000/apps/appsoftware/BioSoftware/bin/java -Xmx50g -Djava.io.tmpdir=/stor9000/apps/users/NWSUAF/2016050001/tmp -jar ~/../2015060152/bin/picard-tools-2.1.1/picard.jar MarkDuplicates INPUT=$i.uniq20.sort.bam OUTPUT=$i.uniq20.sort.dedup.bam METRICS_FILE=$i\_dedup REMOVE_DUPLICATES=true CREATE_INDEX=true ASSUME_SORTED=true VALIDATION_STRINGENCY=LENIENT MAX_FILE_HANDLES=2000
samtools view -h $i.uniq20.sort.dedup.bam |awk '{if($3 != ''NC_001941.1''){print $0}}' |samtools view -Sb - > $i.uniq20.sort.dedup.noMT.bam
echo finish time: `date`
