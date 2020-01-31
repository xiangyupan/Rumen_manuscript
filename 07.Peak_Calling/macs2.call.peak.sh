#!/bin/sh
file="Rumen_T1
"
for i in $file
do
echo $i
python2.7 macs2 callpeak -t ${i}.uniq20.sort.dedup.noMT.bam --shift -37 --extsize 73 -f BAM -g 2500000000 -n ${i}\_narrow_bedgraph -q 0.05 -B --outdir $i\_narrow
python2.7 macs2 bdgcmp -t $i\_narrow/$i\_narrow_bedgraph_treat_pileup.bdg -c $i\_narrow/$i\_narrow_bedgraph_control_lambda.bdg -o $i\_narrow/$i\_narrow_FE.bdg -m FE
echo finish time: `date`
done
