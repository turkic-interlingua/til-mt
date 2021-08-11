# Machine Translation Corpus for Turkic Languages


<p align="center">
<kbd>
  <img width="300" height="300" src="./logo.jpg">
  </kbd>
</p>


## Getting started

### Simplest option!

#### If you are using GPU-enabled (local) machine
Install the necessary libraries
```
pip install -r requirements.txt
```

Run the baseline script by passing in two language codes. This will automatically download the data, process it, install the necesssary libraries and framework and start the training process. The script assumes you are on a GPU-enabled device with CUDA support.

```
bash train_baseline.sh <source_language> <target_language>
```

#### If you are using free preemptible GPUs on Google Colab
You can download the file `joeynmt_colab_bilingual.ipynb` and upload it onto the Google Colab system. You can change the languages codes in the script and the data will be automatically downloaded. It is recommended that you connect your Google Drive account to the Colab to save your progress. Google Colab deletes everything from its workspace periodically (~12 hours). 


### Visualize your results

Make sure *tensorboard* is installed and launch the visualization server (for example for **uz** and **ru**):

```
pip install tensorboard

tensorboard --logdir=experiments/uz-ru-bilingual_baseline/models/uzru_transformer/tensorboard
```

After launching the visualization server, you can view your visualizations in a web browser at http://localhost:6006.

You should see something like this:
![alt text][tensorboard]

[tensorboard]: ./tb_train_metrics.png "Tensorboard example"

### Create a submission to the leaderboard

Once you have your *amazing* model ready, you can create a submission (.zip file) by simply running `create_submission.sh` script along with some parameters:

```
bash create_submission.sh <path_to_joeynmt_config.yaml> <source_language_code> <target_language_code>
# For example:
bash create_submission.sh joeynmt/configs/transformer_uzru.yaml uz ru
```

The script will automatically download the needed test files, load the model specified in the config file, run the test and output the predictions under `\submissions` folder. 

## Useful scripts

### Download the parallel data
To get started, download the data for a pair that you are interested
```
python download_data.py --source_language=<language code> --target_language=<language_code> --split=<train,dev,test,all>
```

### Download the monolingual data
You can also download monolingual data for any of the languages in the table below. Monolingual data are crawled from our parallel corpus, Wikipedia dumps, news websites and a few manual crawls whenever possible.

```
python download_monolingual.py --language=<language code>
```

### Install JoeyNMT

```
git clone https://github.com/joeynmt/joeynmt.git
cd joeynmt; pip3 install .
pip install torch==1.8.0+cu101 -f https://download.pytorch.org/whl/torch_stable.html
```

| Rank | Source | Target | Training size |
|------|--------|--------|----------|
| 1    | en     | tr     | 35879592 |
| 2    | tr     | en     | 35879592 |
| 3    | ru     | tr     | 15092464 |
| 4    | tr     | ru     | 15092464 |
| 5    | kk     | ru     | 4403385  |
| 6    | ru     | kk     | 4403385  |
| 7    | ru     | uz     | 1321013  |
| 8    | uz     | ru     | 1321013  |
| 9    | cv     | ru     | 794654   |
| 10   | ru     | cv     | 794654   |
| 11   | en     | kk     | 564760   |
| 12   | kk     | en     | 564760   |
| 13   | az     | en     | 548901   |
| 14   | en     | az     | 548901   |
| 15   | en     | uz     | 529574   |
| 16   | uz     | en     | 529574   |
| 17   | ba     | ru     | 523719   |
| 18   | ru     | ba     | 523719   |
| 19   | az     | tr     | 410140   |
| 20   | tr     | az     | 410140   |
| 21   | az     | ru     | 331144   |
| 22   | ru     | az     | 331144   |
| 23   | en     | tt     | 320323   |
| 24   | tt     | en     | 320323   |
| 25   | en     | ky     | 312644   |
| 26   | ky     | en     | 312644   |
| 27   | ky     | ru     | 293652   |
| 28   | ru     | ky     | 293652   |
| 29   | tr     | tt     | 289604   |
| 30   | tt     | tr     | 289604   |
| 31   | ky     | tr     | 275028   |
| 32   | tr     | ky     | 275028   |
| 33   | ru     | tt     | 270462   |
| 34   | tt     | ru     | 270462   |
| 35   | ky     | tt     | 220203   |
| 36   | tt     | ky     | 220203   |
| 37   | az     | uz     | 217159   |
| 38   | uz     | az     | 217159   |
| 39   | tr     | uz     | 217078   |
| 40   | uz     | tr     | 217078   |
| 41   | az     | ky     | 205758   |
| 42   | ky     | az     | 205758   |
| 43   | az     | tt     | 201280   |
| 44   | tt     | az     | 201280   |
| 45   | en     | tk     | 130480   |
| 46   | tk     | en     | 130480   |
| 47   | tk     | tr     | 126803   |
| 48   | tr     | tk     | 126803   |
| 49   | tt     | uz     | 126249   |
| 50   | uz     | tt     | 126249   |
| 51   | ky     | uz     | 119946   |
| 52   | uz     | ky     | 119946   |
| 53   | tk     | tt     | 118578   |
| 54   | tt     | tk     | 118578   |
| 55   | az     | tk     | 114895   |
| 56   | tk     | az     | 114895   |
| 57   | ru     | tk     | 111913   |
| 58   | tk     | ru     | 111913   |
| 59   | kk     | uz     | 111519   |
| 60   | uz     | kk     | 111519   |
| 61   | ky     | tk     | 110942   |
| 62   | tk     | ky     | 110942   |
| 63   | en     | ug     | 96898    |
| 64   | ug     | en     | 96898    |
| 65   | cv     | tt     | 85317    |
| 66   | tt     | cv     | 85317    |
| 67   | cv     | tr     | 81451    |
| 68   | tr     | cv     | 81451    |
| 69   | cv     | ky     | 79700    |
| 70   | ky     | cv     | 79700    |
| 71   | az     | cv     | 78310    |
| 72   | cv     | az     | 78310    |
| 73   | cv     | en     | 78288    |
| 74   | en     | cv     | 78288    |
| 75   | cv     | tk     | 71263    |
| 76   | tk     | cv     | 71263    |
| 77   | kaa    | uz     | 65527    |
| 78   | uz     | kaa    | 65527    |
| 79   | kjh    | ru     | 60295    |
| 80   | ru     | kjh    | 60295    |
| 81   | tr     | ug     | 58083    |
| 82   | ug     | tr     | 58083    |
| 83   | cv     | uz     | 57451    |
| 84   | uz     | cv     | 57451    |
| 85   | kk     | tr     | 55815    |
| 86   | tr     | kk     | 55815    |
| 87   | ru     | ug     | 41867    |
| 88   | ug     | ru     | 41867    |
| 89   | ba     | tt     | 40086    |
| 90   | tt     | ba     | 40086    |
| 91   | ba     | tr     | 35910    |
| 92   | tr     | ba     | 35910    |
| 93   | ba     | ky     | 35651    |
| 94   | ky     | ba     | 35651    |
| 95   | ba     | en     | 34308    |
| 96   | en     | ba     | 34308    |
| 97   | ba     | cv     | 33001    |
| 98   | cv     | ba     | 33001    |
| 99   | az     | ba     | 32184    |
| 100  | ba     | az     | 32184    |
| 101  | kaa    | ru     | 29882    |
| 102  | ru     | kaa    | 29882    |
| 103  | ba     | tk     | 28528    |
| 104  | tk     | ba     | 28528    |
| 105  | ba     | uz     | 27478    |
| 106  | uz     | ba     | 27478    |
| 107  | ug     | uz     | 17661    |
| 108  | uz     | ug     | 17661    |
| 109  | en     | kaa    | 17071    |
| 110  | kaa    | en     | 17071    |
| 111  | crh    | en     | 15377    |
| 112  | en     | crh    | 15377    |
| 113  | crh    | tr     | 14497    |
| 114  | tr     | crh    | 14497    |
| 115  | alt    | ba     | 12613    |
| 116  | ba     | alt    | 12613    |
| 117  | ba     | tyv    | 12531    |
| 118  | tyv    | ba     | 12531    |
| 119  | crh    | ru     | 12401    |
| 120  | ru     | crh    | 12401    |
| 121  | alt    | tt     | 12372    |
| 122  | tt     | alt    | 12372    |
| 123  | kk     | ky     | 12216    |
| 124  | ky     | kk     | 12216    |
| 125  | alt    | ky     | 12123    |
| 126  | ky     | alt    | 12123    |
| 127  | tr     | tyv    | 12065    |
| 128  | tyv    | tr     | 12065    |
| 129  | ky     | tyv    | 12053    |
| 130  | tyv    | ky     | 12053    |
| 131  | tt     | tyv    | 11929    |
| 132  | tyv    | tt     | 11929    |
| 133  | alt    | tr     | 11768    |
| 134  | tr     | alt    | 11768    |
| 135  | en     | tyv    | 11482    |
| 136  | tyv    | en     | 11482    |
| 137  | alt    | uz     | 11394    |
| 138  | uz     | alt    | 11394    |
| 139  | cv     | tyv    | 11338    |
| 140  | tyv    | cv     | 11338    |
| 141  | alt    | en     | 11174    |
| 142  | en     | alt    | 11174    |
| 143  | alt    | cv     | 11033    |
| 144  | cv     | alt    | 11033    |
| 145  | alt    | az     | 10738    |
| 146  | az     | alt    | 10738    |
| 147  | alt    | tk     | 10553    |
| 148  | tk     | alt    | 10553    |
| 149  | az     | tyv    | 10352    |
| 150  | tyv    | az     | 10352    |
| 151  | tk     | tyv    | 9881     |
| 152  | tyv    | tk     | 9881     |
| 153  | crh    | kaa    | 9377     |
| 154  | kaa    | crh    | 9377     |
| 155  | crh    | tt     | 9362     |
| 156  | tt     | crh    | 9362     |
| 157  | crh    | uz     | 9299     |
| 158  | uz     | crh    | 9299     |
| 159  | kjh    | krc    | 9254     |
| 160  | krc    | kjh    | 9254     |
| 161  | ru     | sah    | 9237     |
| 162  | sah    | ru     | 9237     |
| 163  | kaa    | kum    | 9173     |
| 164  | kum    | kaa    | 9173     |
| 165  | kjh    | sah    | 9162     |
| 166  | sah    | kjh    | 9162     |
| 167  | az     | crh    | 9153     |
| 168  | crh    | az     | 9153     |
| 169  | kum    | uz     | 9131     |
| 170  | uz     | kum    | 9131     |
| 171  | crh    | kjh    | 9107     |
| 172  | kjh    | crh    | 9107     |
| 173  | kk     | tt     | 9103     |
| 174  | tt     | kk     | 9103     |
| 175  | az     | kk     | 9093     |
| 176  | kk     | az     | 9093     |
| 177  | crh    | tk     | 9066     |
| 178  | tk     | crh    | 9066     |
| 179  | kaa    | ky     | 9064     |
| 180  | ky     | kaa    | 9064     |
| 181  | crh    | kum    | 9041     |
| 182  | kum    | crh    | 9041     |
| 183  | alt    | kaa    | 9012     |
| 184  | kaa    | alt    | 9012     |
| 185  | crh    | cv     | 9003     |
| 186  | cv     | crh    | 9003     |
| 187  | kum    | tr     | 9000     |
| 188  | tr     | kum    | 9000     |
| 189  | tk     | ug     | 8997     |
| 190  | ug     | tk     | 8997     |
| 191  | en     | kjh    | 8991     |
| 192  | kjh    | en     | 8991     |
| 193  | az     | krc    | 8988     |
| 194  | krc    | az     | 8988     |
| 195  | cv     | krc    | 8981     |
| 196  | krc    | cv     | 8981     |
| 197  | tk     | uz     | 8966     |
| 198  | uz     | tk     | 8966     |
| 199  | kaa    | tt     | 8962     |
| 200  | tt     | kaa    | 8962     |
| 201  | crh    | ug     | 8958     |
| 202  | ug     | crh    | 8958     |
| 203  | ba     | kaa    | 8947     |
| 204  | kaa    | ba     | 8947     |
| 205  | kaa    | tk     | 8939     |
| 206  | tk     | kaa    | 8939     |
| 207  | kjh    | kum    | 8938     |
| 208  | kum    | kjh    | 8938     |
| 209  | kaa    | ug     | 8927     |
| 210  | ug     | kaa    | 8927     |
| 211  | cv     | kjh    | 8921     |
| 212  | kjh    | cv     | 8921     |
| 213  | kk     | kum    | 8921     |
| 214  | kum    | kk     | 8921     |
| 215  | az     | kum    | 8908     |
| 216  | kum    | az     | 8908     |
| 217  | az     | kaa    | 8902     |
| 218  | kaa    | az     | 8902     |
| 219  | kaa    | tr     | 8894     |
| 220  | tr     | kaa    | 8894     |
| 221  | kjh    | ug     | 8884     |
| 222  | ug     | kjh    | 8884     |
| 223  | kaa    | kk     | 8874     |
| 224  | kk     | kaa    | 8874     |
| 225  | alt    | crh    | 8867     |
| 226  | crh    | alt    | 8867     |
| 227  | az     | gag    | 8848     |
| 228  | gag    | az     | 8848     |
| 229  | kjh    | tr     | 8845     |
| 230  | tr     | kjh    | 8845     |
| 231  | ba     | kjh    | 8814     |
| 232  | kjh    | ba     | 8814     |
| 233  | kum    | tt     | 8813     |
| 234  | tt     | kum    | 8813     |
| 235  | kum    | ru     | 8807     |
| 236  | ru     | kum    | 8807     |
| 237  | alt    | kum    | 8798     |
| 238  | crh    | gag    | 8798     |
| 239  | gag    | crh    | 8798     |
| 240  | kum    | alt    | 8798     |
| 241  | crh    | kk     | 8795     |
| 242  | kk     | crh    | 8795     |
| 243  | kum    | ky     | 8795     |
| 244  | ky     | kum    | 8795     |
| 245  | kjh    | tt     | 8793     |
| 246  | tt     | kjh    | 8793     |
| 247  | ba     | kum    | 8777     |
| 248  | kum    | ba     | 8777     |
| 249  | ba     | crh    | 8774     |
| 250  | crh    | ba     | 8774     |
| 251  | krc    | tk     | 8753     |
| 252  | tk     | krc    | 8753     |
| 253  | kjh    | tk     | 8736     |
| 254  | tk     | kjh    | 8736     |
| 255  | krc    | sah    | 8732     |
| 256  | sah    | krc    | 8732     |
| 257  | kjh    | uz     | 8727     |
| 258  | uz     | kjh    | 8727     |
| 259  | kaa    | kjh    | 8722     |
| 260  | kjh    | kaa    | 8722     |
| 261  | az     | ug     | 8717     |
| 262  | ug     | az     | 8717     |
| 263  | ky     | ug     | 8706     |
| 264  | ug     | ky     | 8706     |
| 265  | krc    | uz     | 8693     |
| 266  | uz     | krc    | 8693     |
| 267  | alt    | krc    | 8684     |
| 268  | krc    | alt    | 8684     |
| 269  | az     | kjh    | 8677     |
| 270  | kjh    | az     | 8677     |
| 271  | gag    | tr     | 8670     |
| 272  | tr     | gag    | 8670     |
| 273  | alt    | kjh    | 8663     |
| 274  | kjh    | alt    | 8663     |
| 275  | cv     | ug     | 8662     |
| 276  | ug     | cv     | 8662     |
| 277  | kk     | ug     | 8650     |
| 278  | ug     | kk     | 8650     |
| 279  | kaa    | krc    | 8644     |
| 280  | krc    | kaa    | 8644     |
| 281  | alt    | ru     | 8643     |
| 282  | ru     | alt    | 8643     |
| 283  | tyv    | uz     | 8637     |
| 284  | uz     | tyv    | 8637     |
| 285  | kum    | tk     | 8572     |
| 286  | tk     | kum    | 8572     |
| 287  | cv     | kaa    | 8568     |
| 288  | kaa    | cv     | 8568     |
| 289  | cv     | gag    | 8556     |
| 290  | gag    | cv     | 8556     |
| 291  | crh    | ky     | 8552     |
| 292  | en     | kum    | 8552     |
| 293  | kum    | en     | 8552     |
| 294  | ky     | crh    | 8552     |
| 295  | krc    | tr     | 8550     |
| 296  | tr     | krc    | 8550     |
| 297  | ba     | ug     | 8526     |
| 298  | kjh    | ky     | 8526     |
| 299  | ky     | kjh    | 8526     |
| 300  | ug     | ba     | 8526     |
| 301  | cv     | kum    | 8520     |
| 302  | kum    | cv     | 8520     |
| 303  | kum    | ug     | 8519     |
| 304  | ug     | kum    | 8519     |
| 305  | ba     | kk     | 8518     |
| 306  | gag    | tk     | 8518     |
| 307  | kk     | ba     | 8518     |
| 308  | tk     | gag    | 8518     |
| 309  | ba     | krc    | 8509     |
| 310  | krc    | ba     | 8509     |
| 311  | alt    | kk     | 8506     |
| 312  | kk     | alt    | 8506     |
| 313  | crh    | krc    | 8501     |
| 314  | krc    | crh    | 8501     |
| 315  | cv     | sah    | 8488     |
| 316  | cv     | kk     | 8488     |
| 317  | kk     | cv     | 8488     |
| 318  | sah    | cv     | 8488     |
| 319  | tt     | ug     | 8488     |
| 320  | ug     | tt     | 8488     |
| 321  | krc    | kum    | 8473     |
| 322  | kum    | krc    | 8473     |
| 323  | krc    | tt     | 8471     |
| 324  | tt     | krc    | 8471     |
| 325  | gag    | kjh    | 8468     |
| 326  | kjh    | gag    | 8468     |
| 327  | kjh    | kk     | 8452     |
| 328  | kk     | kjh    | 8452     |
| 329  | kk     | tk     | 8448     |
| 330  | tk     | kk     | 8448     |
| 331  | krc    | ru     | 8442     |
| 332  | ru     | krc    | 8442     |
| 333  | gag    | uz     | 8419     |
| 334  | uz     | gag    | 8419     |
| 335  | az     | sah    | 8403     |
| 336  | sah    | az     | 8403     |
| 337  | crh    | sah    | 8367     |
| 338  | sah    | crh    | 8367     |
| 339  | gag    | krc    | 8358     |
| 340  | krc    | gag    | 8358     |
| 341  | en     | gag    | 8350     |
| 342  | gag    | en     | 8350     |
| 343  | gag    | kaa    | 8342     |
| 344  | kaa    | gag    | 8342     |
| 345  | sah    | uz     | 8339     |
| 346  | uz     | sah    | 8339     |
| 347  | alt    | gag    | 8328     |
| 348  | gag    | alt    | 8328     |
| 349  | krc    | ug     | 8327     |
| 350  | ug     | krc    | 8327     |
| 351  | sah    | tt     | 8293     |
| 352  | tt     | sah    | 8293     |
| 353  | alt    | ug     | 8270     |
| 354  | ug     | alt    | 8270     |
| 355  | en     | krc    | 8220     |
| 356  | krc    | en     | 8220     |
| 357  | sah    | tr     | 8210     |
| 358  | tr     | sah    | 8210     |
| 359  | ba     | gag    | 8167     |
| 360  | gag    | ba     | 8167     |
| 361  | alt    | sah    | 8163     |
| 362  | sah    | alt    | 8163     |
| 363  | gag    | tt     | 8143     |
| 364  | tt     | gag    | 8143     |
| 365  | sah    | tk     | 8134     |
| 366  | tk     | sah    | 8134     |
| 367  | kk     | krc    | 8114     |
| 368  | krc    | kk     | 8114     |
| 369  | en     | sah    | 8106     |
| 370  | sah    | en     | 8106     |
| 371  | ba     | sah    | 8082     |
| 372  | sah    | ba     | 8082     |
| 373  | gag    | ru     | 8080     |
| 374  | ru     | gag    | 8080     |
| 375  | krc    | ky     | 8069     |
| 376  | ky     | krc    | 8069     |
| 377  | kaa    | sah    | 8021     |
| 378  | sah    | kaa    | 8021     |
| 379  | gag    | kum    | 7999     |
| 380  | kum    | gag    | 7999     |
| 381  | gag    | ug     | 7988     |
| 382  | ug     | gag    | 7988     |
| 383  | kk     | sah    | 7970     |
| 384  | sah    | kk     | 7970     |
| 385  | sah    | ug     | 7904     |
| 386  | ug     | sah    | 7904     |
| 387  | kum    | sah    | 7853     |
| 388  | sah    | kum    | 7853     |
| 389  | gag    | sah    | 7852     |
| 390  | sah    | gag    | 7852     |
| 391  | ky     | sah    | 7820     |
| 392  | sah    | ky     | 7820     |
| 393  | gag    | ky     | 7795     |
| 394  | ky     | gag    | 7795     |
| 395  | gag    | kk     | 7694     |
| 396  | kk     | gag    | 7694     |
| 397  | alt    | tyv    | 2922     |
| 398  | tyv    | alt    | 2922     |
| 399  | cjs    | ru     | 2294     |
| 400  | ru     | cjs    | 2294     |
| 401  | en     | slr    | 766      |
| 402  | slr    | en     | 766      |
| 403  | en     | uum    | 491      |
| 404  | uum    | en     | 491      |


