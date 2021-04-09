We generated the fastq files from the fast5 files using Guppy 4.0.14 basecaller. The results should be similar with more recent versions of the basecaller.

Downloading basecaller:
```
wget https://mirror.oxfordnanoportal.com/software/analysis/ont-guppy_4.0.14_linux64.tar.gz
tar -xzvf ont-guppy_4.0.14_linux64.tar.gz
```

To basecall, run:
```
./ont-guppy/bin/guppy_basecaller -i FAST5_PATH -s FASTQ_PATH/ -c dna_r9.4.1_450bps_hac.cfg -x cuda:all
```

For multiplexed experiments (pool `20210304_MIN_0964`), run the barcoder:
```
./ont-guppy/bin/guppy_barcoder --input_path FASTQ_PATH/ --save_path BARCODED_FASTQ_PATH/ --config configuration.cfg --barcode_kits "EXP-NBD104 EXP-NBD114" -x cuda:0
```

Finally, we get a single merged fastq file for each barcode:
```
cat BARCODED_FASTQ_PATH/barcode01/*.fastq > barcode01_merged.fastq
```
