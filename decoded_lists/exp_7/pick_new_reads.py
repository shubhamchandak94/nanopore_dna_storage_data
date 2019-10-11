import h5py
import random
HDF5_FILE = '/raid/nanopore/shubham/20190629_nanopore_data/raw_signal/raw_signal_7.hdf5'
NUMREADS=1607
NUMTHR = 15

# function from https://stackoverflow.com/a/2136090
def chunkify(lst,n):
    return [lst[i::n] for i in range(n)]

f = open('info.txt')
l = [r.strip('\n').split('\t')[0] for r in f.readlines()]

f_raw = h5py.File(HDF5_FILE)
readid_list = list(f_raw.keys())
remaining_set = set(readid_list).difference(set(l))
remaining_list = list(remaining_set)
remaining_list_small = random.sample(remaining_list,NUMREADS)
read_id_lists = chunkify(remaining_list_small,NUMTHR)
print(read_id_lists)
for i in range(NUMTHR):
    fout = open('../read_ids_'+str(i+10)+'.txt','w')
    for s in read_id_lists[i]:
        fout.write(s+'\n')
    fout.close()
