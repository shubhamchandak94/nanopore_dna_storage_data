# Nanopore DNA storage data
Convolutional coding and basecaller-decoder integration for nanopore sequencing based DNA storage - data

This repository contains data for the experiments corresponding to https://github.com/shubhamchandak94/nanopore_dna_storage/. Some of the files used in the analysis are not available here, but can be generated using the data available here and the scripts available at https://github.com/shubhamchandak94/nanopore_dna_storage/.

Note that the data here is in compressed format and in some cases, hosted outside GitHub. The instructions for downloading/decompressing the data are available in the respective directories.

Directory description:
- `decoded_lists`: contains the output of the convolutional code decoder for each experiment. These decoded lists are used by the RS outer code decoder to recover the encoded file.
- `encoded_file`: contains the files that were encoded as part of the experiments.
- `fast5_pass`: contains the original raw signal data in the fast5 format.
- `fastq`: contains the basecalled reads.
- `oligo_files`: contains the files containing the oligos that were sent for synthesis (one file for each experiment and a merged file). Also contains the input to the convolutional code encoder, which is helpful for error analysis.
- `raw_data`: contains raw signal data split by experiment, which is used to run the convolutional code decoder.
- `stats`: contains some statistics of the basecalled reads including error rates and read length distribution.
