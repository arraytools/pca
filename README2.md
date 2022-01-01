Original source: https://github.com/MariaNattestad/pca-on-genotypes

On Ubuntu 20.04


```
$ curl -O https://1000genomes.s3.amazonaws.com/release/20110521/ALL.chr22.phase1_release_v3.20101123.snps_indels_svs.genotypes.vcf.gz

$ curl -O https://1000genomes.s3.amazonaws.com/release/20110521/ALL.chr22.phase1_release_v3.20101123.snps_indels_svs.genotypes.vcf.gz.tbi

$ curl -O https://1000genomes.s3.amazonaws.com/release/20110521/phase1_integrated_calls.20101123.ALL.panel

$ pip3 install pysam
$ pip3 install sklearn

$ python3 vcf_to_matrix.py  # generate matrix.csv

```


There are no graph ouput if we run the python code from the terminal.
```
$ nano pca_on_genotypes_used_in_video.py # delete "learning_rate='auto' "

$ pip3 install altair

$ python3 pca_on_genotypes_used_in_video.py
(1092, 4943)
[0.08253525 0.05412034]
[188.93732058 152.99536559]
```

We can get the graph output if we run the notebook in Jupyterlab

```
$ pip3 install jupyterlab
$ export PATH="$HOME/.local/bin:$PATH"
$ jupyter-lab
```

Double click "pca_on_genotypes_used_in_video.ipynb" file. Continuously cick the little triangle to run the code line-by-line.


