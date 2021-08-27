# Machine Translation Corpus for Turkic Languages


<p align="center">
<kbd>
  <img width="300" height="300" src="./logo.jpg">
  </kbd>
</p>

## Directory

1. [Large-scale Study of Machine Translation in Turkic Languages (EMNLP 2021)](https://github.com/turkic-interlingua/til-mt/tree/master/corpus_paper)
2. [Evaluating Multiway Multilingual NMT in Turkic Languages (WMT 2021)](https://github.com/turkic-interlingua/til-mt/tree/master/multilingual_paper)
3. [TIL Corpus and how to access it](#Download-the-parallel-data)
4. [Finetuning the MNMT model on a downstream task](https://github.com/turkic-interlingua/til-mt/tree/master/finetune)
5. [Guide to getting started with the corpus and training your bilingual baselines](#Getting-started)
6. [Language pairs and data sizes in TIL Corpus](#Language-pairs)



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


## X-WMT Test Sets

To establish a comprehensive and challenging evaluation benchmark for Machine Translation in Turkic languages, we translate a test set originally introduced in WMT 2020 News Translation Task for English-Russian. The [original dataset](https://www.statmt.org/wmt20/translation-task.html#download) is profesionally translated and consists of sentences from news articles that are both English and Russian-centric. We adopt this evaluation set (X-WMT) and begin efforts to translate it into several Turkic languages. The current version of X-WMT includes covers 8 Turkic languages and 88 language directions with a minimum of 300 sentences per language direction. Currently covered languages are Azerbaijani (az), Bashkir (ba), Karakalpak (kaa), Kazakh (kk), Kirghiz (ky), Turkish (tr), Sakha (sah) and Uzbek (uz). You can download the evaluation sets here.

|     | *en*   | *ru*   | *ba*  | *tr*  | *uz*  | *ky*  | *kk*  | *az*  | *sah* | *kaa* |
|-----|------|------|-----|-----|-----|-----|-----|-----|-----|-----|
| *en*  | -    |      |     |     |     |     |     |     |     |     |
| *ru*  | *1000* | -    |     |     |     |     |     |     |     |     |
| *ba*  | 1000 | *1000* | -   |     |     |     |     |     |     |     |
| *tr*  | *800*  | 800  | 800 | -   |     |     |     |     |     |     |
| *uz*  | *900*  | 900  | 900 | 600 | -   |     |     |     |     |     |
| *ky*  | 500  | *500*  | 500 | 400 | 500 | -   |     |     |     |     |
| *kk*  | 700  | 700  | 700 | 500 | *700* | 500 | -   |     |     |     |
| *az*  | *600*  | 600  | 600 | 500 | 600 | 500 | 500 | -   |     |     |
| *sah* | 300  | *300*  | 300 | 300 | 300 | 300 | 300 | 300 | -   |     |
| *kaa* | 300  | 300  | 300 | *300* | 300 | 300 | 300 | 300 | 300 | -   |


Table above shows the amount of data available for each language pair. Bolded entries indicate the original translation direction. 

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


### Install JoeyNMT

```
git clone https://github.com/joeynmt/joeynmt.git
cd joeynmt; pip3 install .
pip install torch==1.8.0+cu101 -f https://download.pytorch.org/whl/torch_stable.html
```

## How to cite

If you are using the TIL Corpus or X-WMT test sets, please cite:

(here)


If you are using the MNMT model in your research, please cite:

(here)

If you want to talk about the Turkic Interlingua (TIL) community overall, please cite:
```
@phdthesis{mirzakhalov2021turkic,
  title={Turkic Interlingua: A Case Study of Machine Translation in Low-resource Languages},
  author={Mirzakhalov, Jamshidbek},
  year={2021},
  school={University of South Florida}
}
```

## Language pairs

| Rank | Source          | Target          | Source LC | Target LC | Training size |
|------|-----------------|-----------------|-----------|-----------|---------------|
| 1    | English         | Turkish         | en        | tr        | 35879592      |
| 2    | Turkish         | English         | tr        | en        | 35879592      |
| 3    | Russian         | Turkish         | ru        | tr        | 15092464      |
| 4    | Turkish         | Russian         | tr        | ru        | 15092464      |
| 5    | Kazakh          | Russian         | kk        | ru        | 4403385       |
| 6    | Russian         | Kazakh          | ru        | kk        | 4403385       |
| 7    | Russian         | Uzbek           | ru        | uz        | 1321013       |
| 8    | Uzbek           | Russian         | uz        | ru        | 1321013       |
| 9    | Chuvash         | Russian         | cv        | ru        | 794654        |
| 10   | Russian         | Chuvash         | ru        | cv        | 794654        |
| 11   | English         | Kazakh          | en        | kk        | 564760        |
| 12   | Kazakh          | English         | kk        | en        | 564760        |
| 13   | Azerbaijani     | English         | az        | en        | 548901        |
| 14   | English         | Azerbaijani     | en        | az        | 548901        |
| 15   | English         | Uzbek           | en        | uz        | 529574        |
| 16   | Uzbek           | English         | uz        | en        | 529574        |
| 17   | Bashkir         | Russian         | ba        | ru        | 523719        |
| 18   | Russian         | Bashkir         | ru        | ba        | 523719        |
| 19   | Azerbaijani     | Turkish         | az        | tr        | 410140        |
| 20   | Turkish         | Azerbaijani     | tr        | az        | 410140        |
| 21   | Azerbaijani     | Russian         | az        | ru        | 331144        |
| 22   | Russian         | Azerbaijani     | ru        | az        | 331144        |
| 23   | English         | Tatar           | en        | tt        | 320323        |
| 24   | Tatar           | English         | tt        | en        | 320323        |
| 25   | English         | Kirghiz         | en        | ky        | 312644        |
| 26   | Kirghiz         | English         | ky        | en        | 312644        |
| 27   | Kirghiz         | Russian         | ky        | ru        | 293652        |
| 28   | Russian         | Kirghiz         | ru        | ky        | 293652        |
| 29   | Turkish         | Tatar           | tr        | tt        | 289604        |
| 30   | Tatar           | Turkish         | tt        | tr        | 289604        |
| 31   | Kirghiz         | Turkish         | ky        | tr        | 275028        |
| 32   | Turkish         | Kirghiz         | tr        | ky        | 275028        |
| 33   | Russian         | Tatar           | ru        | tt        | 270462        |
| 34   | Tatar           | Russian         | tt        | ru        | 270462        |
| 35   | Kirghiz         | Tatar           | ky        | tt        | 220203        |
| 36   | Tatar           | Kirghiz         | tt        | ky        | 220203        |
| 37   | Azerbaijani     | Uzbek           | az        | uz        | 217159        |
| 38   | Uzbek           | Azerbaijani     | uz        | az        | 217159        |
| 39   | Turkish         | Uzbek           | tr        | uz        | 217078        |
| 40   | Uzbek           | Turkish         | uz        | tr        | 217078        |
| 41   | Azerbaijani     | Kirghiz         | az        | ky        | 205758        |
| 42   | Kirghiz         | Azerbaijani     | ky        | az        | 205758        |
| 43   | Azerbaijani     | Tatar           | az        | tt        | 201280        |
| 44   | Tatar           | Azerbaijani     | tt        | az        | 201280        |
| 45   | English         | Turkmen         | en        | tk        | 130480        |
| 46   | Turkmen         | English         | tk        | en        | 130480        |
| 47   | Turkmen         | Turkish         | tk        | tr        | 126803        |
| 48   | Turkish         | Turkmen         | tr        | tk        | 126803        |
| 49   | Tatar           | Uzbek           | tt        | uz        | 126249        |
| 50   | Uzbek           | Tatar           | uz        | tt        | 126249        |
| 51   | Kirghiz         | Uzbek           | ky        | uz        | 119946        |
| 52   | Uzbek           | Kirghiz         | uz        | ky        | 119946        |
| 53   | Turkmen         | Tatar           | tk        | tt        | 118578        |
| 54   | Tatar           | Turkmen         | tt        | tk        | 118578        |
| 55   | Azerbaijani     | Turkmen         | az        | tk        | 114895        |
| 56   | Turkmen         | Azerbaijani     | tk        | az        | 114895        |
| 57   | Russian         | Turkmen         | ru        | tk        | 111913        |
| 58   | Turkmen         | Russian         | tk        | ru        | 111913        |
| 59   | Kazakh          | Uzbek           | kk        | uz        | 111519        |
| 60   | Uzbek           | Kazakh          | uz        | kk        | 111519        |
| 61   | Kirghiz         | Turkmen         | ky        | tk        | 110942        |
| 62   | Turkmen         | Kirghiz         | tk        | ky        | 110942        |
| 63   | English         | Uyghur          | en        | ug        | 96898         |
| 64   | Uyghur          | English         | ug        | en        | 96898         |
| 65   | Chuvash         | Tatar           | cv        | tt        | 85317         |
| 66   | Tatar           | Chuvash         | tt        | cv        | 85317         |
| 67   | Chuvash         | Turkish         | cv        | tr        | 81451         |
| 68   | Turkish         | Chuvash         | tr        | cv        | 81451         |
| 69   | Chuvash         | Kirghiz         | cv        | ky        | 79700         |
| 70   | Kirghiz         | Chuvash         | ky        | cv        | 79700         |
| 71   | Azerbaijani     | Chuvash         | az        | cv        | 78310         |
| 72   | Chuvash         | Azerbaijani     | cv        | az        | 78310         |
| 73   | Chuvash         | English         | cv        | en        | 78288         |
| 74   | English         | Chuvash         | en        | cv        | 78288         |
| 75   | Chuvash         | Turkmen         | cv        | tk        | 71263         |
| 76   | Turkmen         | Chuvash         | tk        | cv        | 71263         |
| 77   | Karakalpak      | Uzbek           | kaa       | uz        | 65527         |
| 78   | Uzbek           | Karakalpak      | uz        | kaa       | 65527         |
| 79   | Khakas          | Russian         | kjh       | ru        | 60295         |
| 80   | Russian         | Khakas          | ru        | kjh       | 60295         |
| 81   | Turkish         | Uyghur          | tr        | ug        | 58083         |
| 82   | Uyghur          | Turkish         | ug        | tr        | 58083         |
| 83   | Chuvash         | Uzbek           | cv        | uz        | 57451         |
| 84   | Uzbek           | Chuvash         | uz        | cv        | 57451         |
| 85   | Kazakh          | Turkish         | kk        | tr        | 55815         |
| 86   | Turkish         | Kazakh          | tr        | kk        | 55815         |
| 87   | Russian         | Uyghur          | ru        | ug        | 41867         |
| 88   | Uyghur          | Russian         | ug        | ru        | 41867         |
| 89   | Bashkir         | Tatar           | ba        | tt        | 40086         |
| 90   | Tatar           | Bashkir         | tt        | ba        | 40086         |
| 91   | Bashkir         | Turkish         | ba        | tr        | 35910         |
| 92   | Turkish         | Bashkir         | tr        | ba        | 35910         |
| 93   | Bashkir         | Kirghiz         | ba        | ky        | 35651         |
| 94   | Kirghiz         | Bashkir         | ky        | ba        | 35651         |
| 95   | Bashkir         | English         | ba        | en        | 34308         |
| 96   | English         | Bashkir         | en        | ba        | 34308         |
| 97   | Bashkir         | Chuvash         | ba        | cv        | 33001         |
| 98   | Chuvash         | Bashkir         | cv        | ba        | 33001         |
| 99   | Azerbaijani     | Bashkir         | az        | ba        | 32184         |
| 100  | Bashkir         | Azerbaijani     | ba        | az        | 32184         |
| 101  | Karakalpak      | Russian         | kaa       | ru        | 29882         |
| 102  | Russian         | Karakalpak      | ru        | kaa       | 29882         |
| 103  | Bashkir         | Turkmen         | ba        | tk        | 28528         |
| 104  | Turkmen         | Bashkir         | tk        | ba        | 28528         |
| 105  | Bashkir         | Uzbek           | ba        | uz        | 27478         |
| 106  | Uzbek           | Bashkir         | uz        | ba        | 27478         |
| 107  | Uyghur          | Uzbek           | ug        | uz        | 17661         |
| 108  | Uzbek           | Uyghur          | uz        | ug        | 17661         |
| 109  | English         | Karakalpak      | en        | kaa       | 17071         |
| 110  | Karakalpak      | English         | kaa       | en        | 17071         |
| 111  | Crimean Tatar   | English         | crh       | en        | 15377         |
| 112  | English         | Crimean Tatar   | en        | crh       | 15377         |
| 113  | Crimean Tatar   | Turkish         | crh       | tr        | 14497         |
| 114  | Turkish         | Crimean Tatar   | tr        | crh       | 14497         |
| 115  | Altai           | Bashkir         | alt       | ba        | 12613         |
| 116  | Bashkir         | Altai           | ba        | alt       | 12613         |
| 117  | Bashkir         | Tuvinian        | ba        | tyv       | 12531         |
| 118  | Tuvinian        | Bashkir         | tyv       | ba        | 12531         |
| 119  | Crimean Tatar   | Russian         | crh       | ru        | 12401         |
| 120  | Russian         | Crimean Tatar   | ru        | crh       | 12401         |
| 121  | Altai           | Tatar           | alt       | tt        | 12372         |
| 122  | Tatar           | Altai           | tt        | alt       | 12372         |
| 123  | Kazakh          | Kirghiz         | kk        | ky        | 12216         |
| 124  | Kirghiz         | Kazakh          | ky        | kk        | 12216         |
| 125  | Altai           | Kirghiz         | alt       | ky        | 12123         |
| 126  | Kirghiz         | Altai           | ky        | alt       | 12123         |
| 127  | Turkish         | Tuvinian        | tr        | tyv       | 12065         |
| 128  | Tuvinian        | Turkish         | tyv       | tr        | 12065         |
| 129  | Kirghiz         | Tuvinian        | ky        | tyv       | 12053         |
| 130  | Tuvinian        | Kirghiz         | tyv       | ky        | 12053         |
| 131  | Tatar           | Tuvinian        | tt        | tyv       | 11929         |
| 132  | Tuvinian        | Tatar           | tyv       | tt        | 11929         |
| 133  | Altai           | Turkish         | alt       | tr        | 11768         |
| 134  | Turkish         | Altai           | tr        | alt       | 11768         |
| 135  | English         | Tuvinian        | en        | tyv       | 11482         |
| 136  | Tuvinian        | English         | tyv       | en        | 11482         |
| 137  | Altai           | Uzbek           | alt       | uz        | 11394         |
| 138  | Uzbek           | Altai           | uz        | alt       | 11394         |
| 139  | Chuvash         | Tuvinian        | cv        | tyv       | 11338         |
| 140  | Tuvinian        | Chuvash         | tyv       | cv        | 11338         |
| 141  | Altai           | English         | alt       | en        | 11174         |
| 142  | English         | Altai           | en        | alt       | 11174         |
| 143  | Altai           | Chuvash         | alt       | cv        | 11033         |
| 144  | Chuvash         | Altai           | cv        | alt       | 11033         |
| 145  | Altai           | Azerbaijani     | alt       | az        | 10738         |
| 146  | Azerbaijani     | Altai           | az        | alt       | 10738         |
| 147  | Altai           | Turkmen         | alt       | tk        | 10553         |
| 148  | Turkmen         | Altai           | tk        | alt       | 10553         |
| 149  | Azerbaijani     | Tuvinian        | az        | tyv       | 10352         |
| 150  | Tuvinian        | Azerbaijani     | tyv       | az        | 10352         |
| 151  | Turkmen         | Tuvinian        | tk        | tyv       | 9881          |
| 152  | Tuvinian        | Turkmen         | tyv       | tk        | 9881          |
| 153  | Crimean Tatar   | Karakalpak      | crh       | kaa       | 9377          |
| 154  | Karakalpak      | Crimean Tatar   | kaa       | crh       | 9377          |
| 155  | Crimean Tatar   | Tatar           | crh       | tt        | 9362          |
| 156  | Tatar           | Crimean Tatar   | tt        | crh       | 9362          |
| 157  | Crimean Tatar   | Uzbek           | crh       | uz        | 9299          |
| 158  | Uzbek           | Crimean Tatar   | uz        | crh       | 9299          |
| 159  | Khakas          | Karachay-Balkar | kjh       | krc       | 9254          |
| 160  | Karachay-Balkar | Khakas          | krc       | kjh       | 9254          |
| 161  | Russian         | Sakha           | ru        | sah       | 9237          |
| 162  | Sakha           | Russian         | sah       | ru        | 9237          |
| 163  | Karakalpak      | Kumyk           | kaa       | kum       | 9173          |
| 164  | Kumyk           | Karakalpak      | kum       | kaa       | 9173          |
| 165  | Khakas          | Sakha           | kjh       | sah       | 9162          |
| 166  | Sakha           | Khakas          | sah       | kjh       | 9162          |
| 167  | Azerbaijani     | Crimean Tatar   | az        | crh       | 9153          |
| 168  | Crimean Tatar   | Azerbaijani     | crh       | az        | 9153          |
| 169  | Kumyk           | Uzbek           | kum       | uz        | 9131          |
| 170  | Uzbek           | Kumyk           | uz        | kum       | 9131          |
| 171  | Crimean Tatar   | Khakas          | crh       | kjh       | 9107          |
| 172  | Khakas          | Crimean Tatar   | kjh       | crh       | 9107          |
| 173  | Kazakh          | Tatar           | kk        | tt        | 9103          |
| 174  | Tatar           | Kazakh          | tt        | kk        | 9103          |
| 175  | Azerbaijani     | Kazakh          | az        | kk        | 9093          |
| 176  | Kazakh          | Azerbaijani     | kk        | az        | 9093          |
| 177  | Crimean Tatar   | Turkmen         | crh       | tk        | 9066          |
| 178  | Turkmen         | Crimean Tatar   | tk        | crh       | 9066          |
| 179  | Karakalpak      | Kirghiz         | kaa       | ky        | 9064          |
| 180  | Kirghiz         | Karakalpak      | ky        | kaa       | 9064          |
| 181  | Crimean Tatar   | Kumyk           | crh       | kum       | 9041          |
| 182  | Kumyk           | Crimean Tatar   | kum       | crh       | 9041          |
| 183  | Altai           | Karakalpak      | alt       | kaa       | 9012          |
| 184  | Karakalpak      | Altai           | kaa       | alt       | 9012          |
| 185  | Crimean Tatar   | Chuvash         | crh       | cv        | 9003          |
| 186  | Chuvash         | Crimean Tatar   | cv        | crh       | 9003          |
| 187  | Kumyk           | Turkish         | kum       | tr        | 9000          |
| 188  | Turkish         | Kumyk           | tr        | kum       | 9000          |
| 189  | Turkmen         | Uyghur          | tk        | ug        | 8997          |
| 190  | Uyghur          | Turkmen         | ug        | tk        | 8997          |
| 191  | English         | Khakas          | en        | kjh       | 8991          |
| 192  | Khakas          | English         | kjh       | en        | 8991          |
| 193  | Azerbaijani     | Karachay-Balkar | az        | krc       | 8988          |
| 194  | Karachay-Balkar | Azerbaijani     | krc       | az        | 8988          |
| 195  | Chuvash         | Karachay-Balkar | cv        | krc       | 8981          |
| 196  | Karachay-Balkar | Chuvash         | krc       | cv        | 8981          |
| 197  | Turkmen         | Uzbek           | tk        | uz        | 8966          |
| 198  | Uzbek           | Turkmen         | uz        | tk        | 8966          |
| 199  | Karakalpak      | Tatar           | kaa       | tt        | 8962          |
| 200  | Tatar           | Karakalpak      | tt        | kaa       | 8962          |
| 201  | Crimean Tatar   | Uyghur          | crh       | ug        | 8958          |
| 202  | Uyghur          | Crimean Tatar   | ug        | crh       | 8958          |
| 203  | Bashkir         | Karakalpak      | ba        | kaa       | 8947          |
| 204  | Karakalpak      | Bashkir         | kaa       | ba        | 8947          |
| 205  | Karakalpak      | Turkmen         | kaa       | tk        | 8939          |
| 206  | Turkmen         | Karakalpak      | tk        | kaa       | 8939          |
| 207  | Khakas          | Kumyk           | kjh       | kum       | 8938          |
| 208  | Kumyk           | Khakas          | kum       | kjh       | 8938          |
| 209  | Karakalpak      | Uyghur          | kaa       | ug        | 8927          |
| 210  | Uyghur          | Karakalpak      | ug        | kaa       | 8927          |
| 211  | Chuvash         | Khakas          | cv        | kjh       | 8921          |
| 212  | Khakas          | Chuvash         | kjh       | cv        | 8921          |
| 213  | Kazakh          | Kumyk           | kk        | kum       | 8921          |
| 214  | Kumyk           | Kazakh          | kum       | kk        | 8921          |
| 215  | Azerbaijani     | Kumyk           | az        | kum       | 8908          |
| 216  | Kumyk           | Azerbaijani     | kum       | az        | 8908          |
| 217  | Azerbaijani     | Karakalpak      | az        | kaa       | 8902          |
| 218  | Karakalpak      | Azerbaijani     | kaa       | az        | 8902          |
| 219  | Karakalpak      | Turkish         | kaa       | tr        | 8894          |
| 220  | Turkish         | Karakalpak      | tr        | kaa       | 8894          |
| 221  | Khakas          | Uyghur          | kjh       | ug        | 8884          |
| 222  | Uyghur          | Khakas          | ug        | kjh       | 8884          |
| 223  | Karakalpak      | Kazakh          | kaa       | kk        | 8874          |
| 224  | Kazakh          | Karakalpak      | kk        | kaa       | 8874          |
| 225  | Altai           | Crimean Tatar   | alt       | crh       | 8867          |
| 226  | Crimean Tatar   | Altai           | crh       | alt       | 8867          |
| 227  | Azerbaijani     | Gagauz          | az        | gag       | 8848          |
| 228  | Gagauz          | Azerbaijani     | gag       | az        | 8848          |
| 229  | Khakas          | Turkish         | kjh       | tr        | 8845          |
| 230  | Turkish         | Khakas          | tr        | kjh       | 8845          |
| 231  | Bashkir         | Khakas          | ba        | kjh       | 8814          |
| 232  | Khakas          | Bashkir         | kjh       | ba        | 8814          |
| 233  | Kumyk           | Tatar           | kum       | tt        | 8813          |
| 234  | Tatar           | Kumyk           | tt        | kum       | 8813          |
| 235  | Kumyk           | Russian         | kum       | ru        | 8807          |
| 236  | Russian         | Kumyk           | ru        | kum       | 8807          |
| 237  | Altai           | Kumyk           | alt       | kum       | 8798          |
| 238  | Crimean Tatar   | Gagauz          | crh       | gag       | 8798          |
| 239  | Gagauz          | Crimean Tatar   | gag       | crh       | 8798          |
| 240  | Kumyk           | Altai           | kum       | alt       | 8798          |
| 241  | Crimean Tatar   | Kazakh          | crh       | kk        | 8795          |
| 242  | Kazakh          | Crimean Tatar   | kk        | crh       | 8795          |
| 243  | Kumyk           | Kirghiz         | kum       | ky        | 8795          |
| 244  | Kirghiz         | Kumyk           | ky        | kum       | 8795          |
| 245  | Khakas          | Tatar           | kjh       | tt        | 8793          |
| 246  | Tatar           | Khakas          | tt        | kjh       | 8793          |
| 247  | Bashkir         | Kumyk           | ba        | kum       | 8777          |
| 248  | Kumyk           | Bashkir         | kum       | ba        | 8777          |
| 249  | Bashkir         | Crimean Tatar   | ba        | crh       | 8774          |
| 250  | Crimean Tatar   | Bashkir         | crh       | ba        | 8774          |
| 251  | Karachay-Balkar | Turkmen         | krc       | tk        | 8753          |
| 252  | Turkmen         | Karachay-Balkar | tk        | krc       | 8753          |
| 253  | Khakas          | Turkmen         | kjh       | tk        | 8736          |
| 254  | Turkmen         | Khakas          | tk        | kjh       | 8736          |
| 255  | Karachay-Balkar | Sakha           | krc       | sah       | 8732          |
| 256  | Sakha           | Karachay-Balkar | sah       | krc       | 8732          |
| 257  | Khakas          | Uzbek           | kjh       | uz        | 8727          |
| 258  | Uzbek           | Khakas          | uz        | kjh       | 8727          |
| 259  | Karakalpak      | Khakas          | kaa       | kjh       | 8722          |
| 260  | Khakas          | Karakalpak      | kjh       | kaa       | 8722          |
| 261  | Azerbaijani     | Uyghur          | az        | ug        | 8717          |
| 262  | Uyghur          | Azerbaijani     | ug        | az        | 8717          |
| 263  | Kirghiz         | Uyghur          | ky        | ug        | 8706          |
| 264  | Uyghur          | Kirghiz         | ug        | ky        | 8706          |
| 265  | Karachay-Balkar | Uzbek           | krc       | uz        | 8693          |
| 266  | Uzbek           | Karachay-Balkar | uz        | krc       | 8693          |
| 267  | Altai           | Karachay-Balkar | alt       | krc       | 8684          |
| 268  | Karachay-Balkar | Altai           | krc       | alt       | 8684          |
| 269  | Azerbaijani     | Khakas          | az        | kjh       | 8677          |
| 270  | Khakas          | Azerbaijani     | kjh       | az        | 8677          |
| 271  | Gagauz          | Turkish         | gag       | tr        | 8670          |
| 272  | Turkish         | Gagauz          | tr        | gag       | 8670          |
| 273  | Altai           | Khakas          | alt       | kjh       | 8663          |
| 274  | Khakas          | Altai           | kjh       | alt       | 8663          |
| 275  | Chuvash         | Uyghur          | cv        | ug        | 8662          |
| 276  | Uyghur          | Chuvash         | ug        | cv        | 8662          |
| 277  | Kazakh          | Uyghur          | kk        | ug        | 8650          |
| 278  | Uyghur          | Kazakh          | ug        | kk        | 8650          |
| 279  | Karakalpak      | Karachay-Balkar | kaa       | krc       | 8644          |
| 280  | Karachay-Balkar | Karakalpak      | krc       | kaa       | 8644          |
| 281  | Altai           | Russian         | alt       | ru        | 8643          |
| 282  | Russian         | Altai           | ru        | alt       | 8643          |
| 283  | Tuvinian        | Uzbek           | tyv       | uz        | 8637          |
| 284  | Uzbek           | Tuvinian        | uz        | tyv       | 8637          |
| 285  | Kumyk           | Turkmen         | kum       | tk        | 8572          |
| 286  | Turkmen         | Kumyk           | tk        | kum       | 8572          |
| 287  | Chuvash         | Karakalpak      | cv        | kaa       | 8568          |
| 288  | Karakalpak      | Chuvash         | kaa       | cv        | 8568          |
| 289  | Chuvash         | Gagauz          | cv        | gag       | 8556          |
| 290  | Gagauz          | Chuvash         | gag       | cv        | 8556          |
| 291  | Crimean Tatar   | Kirghiz         | crh       | ky        | 8552          |
| 292  | English         | Kumyk           | en        | kum       | 8552          |
| 293  | Kumyk           | English         | kum       | en        | 8552          |
| 294  | Kirghiz         | Crimean Tatar   | ky        | crh       | 8552          |
| 295  | Karachay-Balkar | Turkish         | krc       | tr        | 8550          |
| 296  | Turkish         | Karachay-Balkar | tr        | krc       | 8550          |
| 297  | Bashkir         | Uyghur          | ba        | ug        | 8526          |
| 298  | Khakas          | Kirghiz         | kjh       | ky        | 8526          |
| 299  | Kirghiz         | Khakas          | ky        | kjh       | 8526          |
| 300  | Uyghur          | Bashkir         | ug        | ba        | 8526          |
| 301  | Chuvash         | Kumyk           | cv        | kum       | 8520          |
| 302  | Kumyk           | Chuvash         | kum       | cv        | 8520          |
| 303  | Kumyk           | Uyghur          | kum       | ug        | 8519          |
| 304  | Uyghur          | Kumyk           | ug        | kum       | 8519          |
| 305  | Bashkir         | Kazakh          | ba        | kk        | 8518          |
| 306  | Gagauz          | Turkmen         | gag       | tk        | 8518          |
| 307  | Kazakh          | Bashkir         | kk        | ba        | 8518          |
| 308  | Turkmen         | Gagauz          | tk        | gag       | 8518          |
| 309  | Bashkir         | Karachay-Balkar | ba        | krc       | 8509          |
| 310  | Karachay-Balkar | Bashkir         | krc       | ba        | 8509          |
| 311  | Altai           | Kazakh          | alt       | kk        | 8506          |
| 312  | Kazakh          | Altai           | kk        | alt       | 8506          |
| 313  | Crimean Tatar   | Karachay-Balkar | crh       | krc       | 8501          |
| 314  | Karachay-Balkar | Crimean Tatar   | krc       | crh       | 8501          |
| 315  | Chuvash         | Sakha           | cv        | sah       | 8488          |
| 316  | Chuvash         | Kazakh          | cv        | kk        | 8488          |
| 317  | Kazakh          | Chuvash         | kk        | cv        | 8488          |
| 318  | Sakha           | Chuvash         | sah       | cv        | 8488          |
| 319  | Tatar           | Uyghur          | tt        | ug        | 8488          |
| 320  | Uyghur          | Tatar           | ug        | tt        | 8488          |
| 321  | Karachay-Balkar | Kumyk           | krc       | kum       | 8473          |
| 322  | Kumyk           | Karachay-Balkar | kum       | krc       | 8473          |
| 323  | Karachay-Balkar | Tatar           | krc       | tt        | 8471          |
| 324  | Tatar           | Karachay-Balkar | tt        | krc       | 8471          |
| 325  | Gagauz          | Khakas          | gag       | kjh       | 8468          |
| 326  | Khakas          | Gagauz          | kjh       | gag       | 8468          |
| 327  | Khakas          | Kazakh          | kjh       | kk        | 8452          |
| 328  | Kazakh          | Khakas          | kk        | kjh       | 8452          |
| 329  | Kazakh          | Turkmen         | kk        | tk        | 8448          |
| 330  | Turkmen         | Kazakh          | tk        | kk        | 8448          |
| 331  | Karachay-Balkar | Russian         | krc       | ru        | 8442          |
| 332  | Russian         | Karachay-Balkar | ru        | krc       | 8442          |
| 333  | Gagauz          | Uzbek           | gag       | uz        | 8419          |
| 334  | Uzbek           | Gagauz          | uz        | gag       | 8419          |
| 335  | Azerbaijani     | Sakha           | az        | sah       | 8403          |
| 336  | Sakha           | Azerbaijani     | sah       | az        | 8403          |
| 337  | Crimean Tatar   | Sakha           | crh       | sah       | 8367          |
| 338  | Sakha           | Crimean Tatar   | sah       | crh       | 8367          |
| 339  | Gagauz          | Karachay-Balkar | gag       | krc       | 8358          |
| 340  | Karachay-Balkar | Gagauz          | krc       | gag       | 8358          |
| 341  | English         | Gagauz          | en        | gag       | 8350          |
| 342  | Gagauz          | English         | gag       | en        | 8350          |
| 343  | Gagauz          | Karakalpak      | gag       | kaa       | 8342          |
| 344  | Karakalpak      | Gagauz          | kaa       | gag       | 8342          |
| 345  | Sakha           | Uzbek           | sah       | uz        | 8339          |
| 346  | Uzbek           | Sakha           | uz        | sah       | 8339          |
| 347  | Altai           | Gagauz          | alt       | gag       | 8328          |
| 348  | Gagauz          | Altai           | gag       | alt       | 8328          |
| 349  | Karachay-Balkar | Uyghur          | krc       | ug        | 8327          |
| 350  | Uyghur          | Karachay-Balkar | ug        | krc       | 8327          |
| 351  | Sakha           | Tatar           | sah       | tt        | 8293          |
| 352  | Tatar           | Sakha           | tt        | sah       | 8293          |
| 353  | Altai           | Uyghur          | alt       | ug        | 8270          |
| 354  | Uyghur          | Altai           | ug        | alt       | 8270          |
| 355  | English         | Karachay-Balkar | en        | krc       | 8220          |
| 356  | Karachay-Balkar | English         | krc       | en        | 8220          |
| 357  | Sakha           | Turkish         | sah       | tr        | 8210          |
| 358  | Turkish         | Sakha           | tr        | sah       | 8210          |
| 359  | Bashkir         | Gagauz          | ba        | gag       | 8167          |
| 360  | Gagauz          | Bashkir         | gag       | ba        | 8167          |
| 361  | Altai           | Sakha           | alt       | sah       | 8163          |
| 362  | Sakha           | Altai           | sah       | alt       | 8163          |
| 363  | Gagauz          | Tatar           | gag       | tt        | 8143          |
| 364  | Tatar           | Gagauz          | tt        | gag       | 8143          |
| 365  | Sakha           | Turkmen         | sah       | tk        | 8134          |
| 366  | Turkmen         | Sakha           | tk        | sah       | 8134          |
| 367  | Kazakh          | Karachay-Balkar | kk        | krc       | 8114          |
| 368  | Karachay-Balkar | Kazakh          | krc       | kk        | 8114          |
| 369  | English         | Sakha           | en        | sah       | 8106          |
| 370  | Sakha           | English         | sah       | en        | 8106          |
| 371  | Bashkir         | Sakha           | ba        | sah       | 8082          |
| 372  | Sakha           | Bashkir         | sah       | ba        | 8082          |
| 373  | Gagauz          | Russian         | gag       | ru        | 8080          |
| 374  | Russian         | Gagauz          | ru        | gag       | 8080          |
| 375  | Karachay-Balkar | Kirghiz         | krc       | ky        | 8069          |
| 376  | Kirghiz         | Karachay-Balkar | ky        | krc       | 8069          |
| 377  | Karakalpak      | Sakha           | kaa       | sah       | 8021          |
| 378  | Sakha           | Karakalpak      | sah       | kaa       | 8021          |
| 379  | Gagauz          | Kumyk           | gag       | kum       | 7999          |
| 380  | Kumyk           | Gagauz          | kum       | gag       | 7999          |
| 381  | Gagauz          | Uyghur          | gag       | ug        | 7988          |
| 382  | Uyghur          | Gagauz          | ug        | gag       | 7988          |
| 383  | Kazakh          | Sakha           | kk        | sah       | 7970          |
| 384  | Sakha           | Kazakh          | sah       | kk        | 7970          |
| 385  | Sakha           | Uyghur          | sah       | ug        | 7904          |
| 386  | Uyghur          | Sakha           | ug        | sah       | 7904          |
| 387  | Kumyk           | Sakha           | kum       | sah       | 7853          |
| 388  | Sakha           | Kumyk           | sah       | kum       | 7853          |
| 389  | Gagauz          | Sakha           | gag       | sah       | 7852          |
| 390  | Sakha           | Gagauz          | sah       | gag       | 7852          |
| 391  | Kirghiz         | Sakha           | ky        | sah       | 7820          |
| 392  | Sakha           | Kirghiz         | sah       | ky        | 7820          |
| 393  | Gagauz          | Kirghiz         | gag       | ky        | 7795          |
| 394  | Kirghiz         | Gagauz          | ky        | gag       | 7795          |
| 395  | Gagauz          | Kazakh          | gag       | kk        | 7694          |
| 396  | Kazakh          | Gagauz          | kk        | gag       | 7694          |
| 397  | Altai           | Tuvinian        | alt       | tyv       | 2922          |
| 398  | Tuvinian        | Altai           | tyv       | alt       | 2922          |
| 399  | Shor            | Russian         | cjs       | ru        | 2294          |
| 400  | Russian         | Shor            | ru        | cjs       | 2294          |
| 401  | English         | Salar           | en        | slr       | 766           |
| 402  | Salar           | English         | slr       | en        | 766           |
| 403  | English         | Urum            | en        | uum       | 491           |
| 404  | Urum            | English         | uum       | en        | 491           |

