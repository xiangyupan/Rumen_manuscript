#!/bin/sh
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
2693_H7VFTALXX_L6 \
2693_H7VJLALXX_L8 \
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
java -Xmx30g -jar /stor9000/apps/appsoftware/BioSoftware/bin/trimmomatic-0.36.jar PE -threads 10 /stor9000/apps/users/NWSUAF/2016050001/Camel/Camel-1/data_release/raw_data/${i}_1.fq.gz  /stor9000/apps/users/NWSUAF/2016050001/Camel/Camel-1/data_release/raw_data/${i}_2.fq.gz  /stor9000/apps/users/NWSUAF/2016050001/Camel/Camel-1/data_release/my_clean/${i}_1.clean.fq.gz /stor9000/apps/users/NWSUAF/2016050001/Camel/Camel-1/data_release/my_clean/${i}_1.unpaired.fq.gz /stor9000/apps/users/NWSUAF/2016050001/Camel/Camel-1/data_release/my_clean/${i}_2.clean.fq.gz /stor9000/apps/users/NWSUAF/2016050001/Camel/Camel-1/data_release/my_clean/${i}_2.unpaired.fq.gz LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:40 TOPHRED33 > /stor9000/apps/users/NWSUAF/2016050001/Camel/Camel-1/data_release/my_clean/${i}.log
done
