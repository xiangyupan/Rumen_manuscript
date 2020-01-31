#!/bin/sh
export INDEX=/stor9000/apps/users/NWSUAF/2016050001/Camel/genome_data/
export IN=/stor9000/apps/users/NWSUAF/2016050001/Camel/Camel-1/data_release/my_clean
export OUT=/stor9000/apps/users/NWSUAF/2016050001/Camel/bam
export BAM=/stor9000/apps/users/NWSUAF/2016050001/Camel/bam
export TMP=/stor9000/apps/users/NWSUAF/2016050001/Camel/tmp
for i in \
1725_HFKKJALXX_L5 \
2421_HFKKJALXX_L5 \
244_HFKKJALXX_L5 \
2507_H7VJLALXX_L8 \
2551_HFKKJALXX_L5 \
2635_HFKKJALXX_L5 \
2644_HFKKJALXX_L5 \
2647_HFKKJALXX_L5 \
2659_HFKKJALXX_L5 \
2693 \
2759_H7VJLALXX_L8 \
2760_HFKKJALXX_L5 \
2786_HFKKJALXX_L5 \
2790_HFKKJALXX_L5 \
2794_HFKKJALXX_L6 \
2813_HFKKJALXX_L5 \
2927_HF72TALXX_L7 \
2938_HF72TALXX_L7 \
2960_HFKKJALXX_L5
do
STAR --genomeDir $INDEX --readFilesIn $IN/${i}_1.clean.fq.gz $IN/${i}_2.clean.fq.gz --readFilesCommand zcat --runThreadN 8 --outFilterMultimapNmax 1 --outFilterIntronMotifs RemoveNoncanonical Unannotated --outFilterMismatchNmax 10 --outSAMstrandField intronMotif --outSJfilterReads Unique --outSAMtype BAM Unsorted --outReadsUnmapped Fastx --outFileNamePrefix $OUT/${i}
hisat2 --dta-cufflinks --no-mixed --no-discordant -p 10 --rna-strandness RF --known-splicesite-infile /stor9000/apps/users/NWSUAF/2016050001/Camel/genome_data/Camel.splicing.site -x /stor9000/apps/users/NWSUAF/2016050001/Camel/genome_data/Camel.hisat.index -1 $OUT/${i}Unmapped.out.mate1 -2 $OUT/${i}Unmapped.out.mate2 -S $OUT/${i}.sam
/stor9000/apps/appsoftware/BioSoftware/bin/java -Djava.io.tmpdir=$TMP -jar /stor9000/apps/users/NWSUAF/2015060152/bin/picard-tools-2.1.1/picard.jar CleanSam I=$OUT/${i}Aligned.out.bam O=$OUT/${i}.STAR.bam
/stor9000/apps/appsoftware/BioSoftware/bin/java -Djava.io.tmpdir=$TMP -jar /stor9000/apps/users/NWSUAF/2015060152/bin/picard-tools-2.1.1/picard.jar CleanSam I=$OUT/${i}.sam O=$OUT/${i}.hisat.bam
/stor9000/apps/appsoftware/BioSoftware/bin/java -Djava.io.tmpdir=$TMP -jar /stor9000/apps/users/NWSUAF/2015060152/bin/picard-tools-2.1.1/picard.jar MergeSamFiles I=$OUT/${i}.STAR.bam I=$OUT/${i}.hisat.bam SORT_ORDER=coordinate O=$BAM/${i}.bam
done
