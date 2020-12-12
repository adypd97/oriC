# oriC

Predicting oriC in plasmids and chromosomes.
---

**See `../oriC/APInotes` for usage directions**

### Fetching Sequences

- See ```oriC/fetch_genome.py``` for fetching entire genomic sequence of   
an organism

- See ```oriC/fetch_oric.py``` for fetching only
oric sequence of an organism

In either case the sequence data is stored in ```data/``` directory.  
### The OriC Computational Problem
```INPUT :  A DNA string (genome)```  
```OUTPUT: Location of oriC in it```  


### Why is it important to know oriC ?
- To understand cell replication.
- To create biomedical therapies like **viral vectors**
- ...

![E. coli replication](https://upload.wikimedia.org/wikipedia/commons/8/8a/Subhash_nucleoid_01.png)

### Bacterial Genome
 Model organism _**Vibrio cholerae**_ with known oriC sequence.  
   
 **How does replication initiate?**  
 Initiation of replication begins with _DnaA_, a protein that binds to   
 a short segemento of the _oriC_ known as the **Dna Box**   
   
 The _DnaA Box_ tells the _DnaA_ to essentially bind there.  
   
 The key question then is to ask:  
 > **How to find this DnaA Box without knowing what it looks like?**

### LINK TO NCBI FTP SERVER
`https://ftp.ncbi.nlm.nih.gov/genomes/genbank/bacteria/`
### References
- Bioinformatics Algorithms Vol 1 (Book)
- [Ori-Finder](http://origin.tubic.org/Ori-Finder/)  
- [Cumulative-Skew](https://academic.oup.com/nar/article/26/10/2286/1030593)  
- [UNC-BioAlgorithms](http://csbio.unc.edu/mcmillan/Comp555S16/Lecture02.html#Where-Does-Replication-Begin?)
