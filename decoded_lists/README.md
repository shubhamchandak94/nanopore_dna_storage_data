This directory contains the output of the convolutional code decoder for each experiment. 
These decoded lists are used by the RS outer code decoder to recover the encoded file.
Each subdirectory corresponds to an experiment and contains three files:
- `read_ids.txt`: the read ids corresponding to the decoded lists.
- `info.txt`: the read ids and the original oligo sequence corresponding to the decoded lists.
- `lists.tar.gz`: the decoded lists.

To decompress the decoded lists for a particular experiment, run
```
tar -xzf lists.tar.gz
```
This produces one file per read, named as `list_0`, `list_1`, etc. Missing file denotes that the primer removal failed and the convolutional code decoding was not performed.
