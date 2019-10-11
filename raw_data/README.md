This directory contains the raw signal data corresponding to each experiment, which is used to run the decoder. 
The raw data is stored as an HDF5 file with each group corresponding to a read with the read name/id being the group name/key. 
The group contains an attribute `ref` denoting the sequence to which the present read aligned
(this is only for analysis purposes and is not used for decoding) and 
contains a dataset `raw_signal` storing the raw signal.

The hdf5 files compressed with 7-zip can be downloaded from Google drive, either using the link or the script as shown in the table below.

| File  | Google drive link | Script to download |
| ------------- | ------------- | ------------- |
| `raw_signal_0.hdf5.7z` | [Link](https://drive.google.com/file/d/1bwOyvSUZlk-5bW9mVRj-MvE1PH0u5SZi/view?usp=sharing)  | `./gdrive_download.sh 1bwOyvSUZlk-5bW9mVRj-MvE1PH0u5SZi raw_signal_0.hdf5.7z` |
| `raw_signal_1.hdf5.7z` | [Link](https://drive.google.com/file/d/1EPcFCY8Ec1JvbauSOBgEIPZb97f7v5Hf/view?usp=sharing)  | `./gdrive_download.sh 1EPcFCY8Ec1JvbauSOBgEIPZb97f7v5Hf raw_signal_1.hdf5.7z` |
| `raw_signal_2.hdf5.7z` | [Link](https://drive.google.com/file/d/1cH_zalp45qC-S1k0TFte83ffP9F7kM6y/view?usp=sharing)  | `./gdrive_download.sh 1cH_zalp45qC-S1k0TFte83ffP9F7kM6y raw_signal_2.hdf5.7z` |
| `raw_signal_3.hdf5.7z` | [Link](https://drive.google.com/file/d/1QNJKElB7daOEz6vLn5twWSxokj8eVNwc/view?usp=sharing)  | `./gdrive_download.sh 1QNJKElB7daOEz6vLn5twWSxokj8eVNwc raw_signal_3.hdf5.7z` |
| `raw_signal_4.hdf5.7z` | [Link](https://drive.google.com/file/d/1r3qfg4iYu60qw0F6UcYDFxepCFFw1adE/view?usp=sharing)  | `./gdrive_download.sh 1r3qfg4iYu60qw0F6UcYDFxepCFFw1adE raw_signal_4.hdf5.7z` |
| `raw_signal_5.hdf5.7z` | [Link](https://drive.google.com/file/d/17O8KPvBAX4jfJHxvrR388HfHYFQbIcOR/view?usp=sharing)  | `./gdrive_download.sh 17O8KPvBAX4jfJHxvrR388HfHYFQbIcOR raw_signal_5.hdf5.7z` |
| `raw_signal_6.hdf5.7z` | [Link](https://drive.google.com/file/d/1Dmp9U9dhj6_QKnt729yyd0PFc1TKasWa/view?usp=sharing)  | `./gdrive_download.sh 1Dmp9U9dhj6_QKnt729yyd0PFc1TKasWa raw_signal_6.hdf5.7z` |
| `raw_signal_7.hdf5.7z` | [Link](https://drive.google.com/file/d/1oUoLvZctr_DVwoSw-GuSOuaXPMt_s_sA/view?usp=sharing)  | `./gdrive_download.sh 1oUoLvZctr_DVwoSw-GuSOuaXPMt_s_sA raw_signal_7.hdf5.7z` |
| `raw_signal_8.hdf5.7z` | [Link](https://drive.google.com/file/d/1DmQisQGmrD2xeGfiWHnHi5tNo1whYaAf/view?usp=sharing)  | `./gdrive_download.sh 1DmQisQGmrD2xeGfiWHnHi5tNo1whYaAf raw_signal_8.hdf5.7z` |
| `raw_signal_9.hdf5.7z` | [Link](https://drive.google.com/file/d/1zZligK-N5ZuVwXo9dVNc9WOAjNKVbNPO/view?usp=sharing)  | `./gdrive_download.sh 1zZligK-N5ZuVwXo9dVNc9WOAjNKVbNPO raw_signal_9.hdf5.7z` |
| `raw_signal_10.hdf5.7z` | [Link](https://drive.google.com/file/d/19W_vOb5Gu5jZikcMBZCQNqqdj3KAz_Ju/view?usp=sharing)  | `./gdrive_download.sh 19W_vOb5Gu5jZikcMBZCQNqqdj3KAz_Ju raw_signal_10.hdf5.7z` |

To extract the hdf5 file (for experiment 0) from the 7z archive, run
```
7z e raw_signal_0.hdf5.7z
```
If 7-zip is not installed, run (on Ubuntu)
```
sudo apt-get install p7zip-full
```
