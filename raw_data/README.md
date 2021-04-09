This directory contains the raw signal data corresponding to each experiment, which is used to run the decoder. 
The raw data is stored as an HDF5 file with each group corresponding to a read with the read name/id being the group name/key. 
The group contains an attribute `ref` denoting the sequence to which the present read aligned
(this is only for analysis purposes and is not used for decoding) and 
contains a dataset `raw_signal` storing the raw signal.

The hdf5 files are compressed with bzip2 and should be decompressed before use.
