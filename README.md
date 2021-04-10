# Nanopore DNA storage data
Convolutional coding and basecaller-decoder integration for nanopore sequencing based DNA storage - data

This branch contains data for the experiments corresponding to https://github.com/shubhamchandak94/nanopore_dna_storage/tree/bonito. Some of the files used in the analysis are not available here, but can be generated using the data available here and the scripts available at https://github.com/shubhamchandak94/nanopore_dna_storage/tree/bonito/.

Note that the data here is in compressed format and in some cases, hosted outside GitHub. The instructions for downloading/decompressing the data are available in the respective directories. We include data from two sequencing runs:
- `20200814_MIN_0880` - all 18 code parameter experiments
- `20210304_MIN_0964` - 5 code parameter experiments (`exp_0`, `exp_1`, `exp_2`, `exp_5`, `exp_8`), 6 replicates (organized in folders as `barcode01` to `barcode06`)

Directory description:
- `decoded_lists`: contains the output of the convolutional code decoder for each experiment. These decoded lists are used by the RS outer code decoder to recover the encoded file.
- `encoded_file`: contains the files that were encoded as part of the experiments.
- `fast5`: contains the original raw signal data in the fast5 format.
- `fastq`: contains the basecalled reads.
- `oligo_files`: contains the files containing the oligos that were sent for synthesis (one file for each experiment and a merged file). Also contains the input to the convolutional code encoder, which is helpful for error analysis.
- `raw_signal`: contains raw signal data split by experiment, which is used to run the convolutional code decoder. Also, contains the read ids that were decoded.
- `stats`: contains some statistics of the basecalled reads including error rates.

**Note**: `exp_9` for `20200814_MIN_0880` did not amplify properly and was not decoded since we got very few reads. Thus, it is missing in several directories.
