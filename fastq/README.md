Basecalled FASTQ file, compressed with [SPRING](https://github.com/shubhamchandak94/Spring). 
The file `merged.fastq.spring` can be downloaded from [this link](https://drive.google.com/file/d/1yFOChP7qlOvS29llTD7WdhTNHaR9BySy/view?usp=sharing) or using the command
```
./gdrive_download.sh 1yFOChP7qlOvS29llTD7WdhTNHaR9BySy merged.fastq.spring
```

To decompress and obtain `merged.fastq`, download and install [SPRING](https://github.com/shubhamchandak94/Spring) and run
```
./spring -d -i merged.fastq.spring -o merged.fastq
```
