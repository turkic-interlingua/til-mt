# Machine Translation for Turkic Languages

<p align="center">
<kbd>
  <img width="300" height="300" src="./logo.jpg">
  </kbd>
</p>

## Table of Contents

1. [Introduction](#Introduction)
2. [TIL Corpus](https://github.com/turkic-interlingua/til-mt/tree/master/til_corpus)
3. [Replicating Paper Results](https://github.com/turkic-interlingua/til-mt/tree/master/replicate_results)
4. [X-WMT Test Sets](https://github.com/turkic-interlingua/til-mt/tree/master/test-xwmt)
5. [MNMT model](https://github.com/turkic-interlingua/til-mt/tree/master/finetune)
6. [How to cite the work?](#How-to-cite)
7. [Contributors](#Contributors)

## Introduction

### What is Turkic Interlingua (TIL)?
Turkic Interlingua (TIL) is a community of researchers, Machine Learning (ML) engineers, language enthusiasts and community leaders whose mission is to develop language technologies (from spell checkers to translation models), collect diverse datasets, and explore linguistic phenomena through the lens of academic research for Turkic languages.

### What is TIL Corpus?
TIL Corpus is a large-scale parallel corpus combining most of the public datasets for 22 Turkic languages. The current version of the corpus yields data for almost 400 language directions with development and test sets available for >300 of them. You can learn more about the corpus and how to use it [here](https://github.com/turkic-interlingua/til-mt/tree/master/til_corpus).


### What is this repo?
This repo is a collection of resources for training and researching Machine Translation models. It includes links and scripts to download the TIL Corpus, X-WMT test sets, multilingual models and more. The repo also allows researchers to replicate our results from our publications in the past. 


## Model results on the X-WMT test set 

| **Pairs**  | **Train size** | **Bilingual** |       | **MNMT** |       | **Improvement** |        |
|:--------:|:------------:|:-----------:|:-------:|:------:|:-------:|:-------------:|:--------:|
|        |            | **Chrf**      | **BLEU**  | **Chrf** | **BLEU**  | **▲ Chrf**      | **▲ BLEU** |
| ru-ba  | 523.7K     | 0.59      | 24.31 | 0.56 | 23.13 | -0.03       | -1.18  |
| ba-ru  | 523.7K     | 0.58      | 24.39 | 0.57 | 24.57 | -0.02       | 0.18   |
| en-tr  | 35.8M      | 0.55      | 16.04 | 0.56 | 26.74 | 0.01        | 10.70  |
| tr-en  | 35.8M      | 0.51      | 20.39 | 0.55 | 24.66 | 0.04        | 4.27   |
| az-tr  | 410.1K     | 0.43      | 10.61 | 0.48 | 19.63 | 0.05        | 9.02   |
| kk-en  | 564.8K     | 0.42      | 12.00 | 0.44 | 15.71 | 0.02        | 3.71   |
| az-en  | 548.9K     | 0.41      | 12.01 | 0.49 | 20.41 | 0.08        | 8.40   |
| ru-uz  | 1.3M       | 0.41      | 6.58  | 0.42 | 6.70  | 0.01        | 0.12   |
| en-kk  | 564.8K     | 0.40      | 7.82  | 0.43 | 9.92  | 0.03        | 2.10   |
| en-uz  | 529.6K     | 0.40      | 6.34  | 0.42 | 9.89  | 0.02        | 3.55   |
| tr-az  | 410.1K     | 0.39      | 7.78  | 0.42 | 8.21  | 0.03        | 0.43   |
| en-az  | 548.9K     | 0.38      | 6.79  | 0.43 | 9.71  | 0.05        | 2.92   |
| uz-ru  | 1.3M       | 0.36      | 6.08  | 0.39 | 9.16  | 0.03        | 3.08   |
| ru-ky  | 293.7K     | 0.35      | 4.42  | 0.45 | 10.35 | 0.10        | 5.93   |
| ky-ru  | 293.7K     | 0.30      | 5.23  | 0.44 | 14.08 | 0.14        | 8.85   |
| ky-en  | 312.6K     | 0.29      | 4.65  | 0.39 | 10.87 | 0.10        | 6.22   |
| en-ky  | 312.6K     | 0.27      | 2.33  | 0.34 | 4.64  | 0.07        | 2.31   |
| uz-en  | 529.6K     | 0.24      | 4.81  | 0.45 | 14.45 | 0.21        | 9.64   |
| kaa-en | 17.1K      | 0.21      | 1.04  | 0.38 | 10.21 | 0.17        | 9.17   |
| sah-en | 8.1K       | 0.21      | 0.16  | 0.24 | 3.38  | 0.03        | 3.22   |
| ba-en  | 34.3K      | 0.19      | 0.32  | 0.40 | 10.55 | 0.21        | 10.23  |
| en-kaa | 17.1K      | 0.19      | 0.31  | 0.27 | 2.82  | 0.08        | 2.51   |
| sah-ru | 9.2K       | 0.18      | 0.42  | 0.25 | 4.41  | 0.07        | 3.99   |
| ru-sah | 9.2K       | 0.16      | 0.12  | 0.17 | 4.64  | 0.01        | 4.52   |
| en-ba  | 34.3K      | 0.14      | 0.16  | 0.34 | 8.35  | 0.20        | 8.19   |
| en-sah | 8.1K       | 0.14      | 0.04  | 0.12 | 3.46  | -0.02       | 3.42   |


## How to cite

If you are using the TIL Corpus or X-WMT test sets, please cite:

```
@misc{mirzakhalov2021largescale,
      title={A Large-Scale Study of Machine Translation in the Turkic Languages}, 
      author={Jamshidbek Mirzakhalov and Anoop Babu and Duygu Ataman and Sherzod Kariev and Francis Tyers and Otabek Abduraufov and Mammad Hajili and Sardana Ivanova and Abror Khaytbaev and Antonio Laverghetta Jr. au2 and Behzodbek Moydinboyev and Esra Onal and Shaxnoza Pulatova and Ahsan Wahab and Orhan Firat and Sriram Chellappan},
      year={2021},
      eprint={2109.04593},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

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

# Contributors

This project was carried out with the help and contributions from dozens of individuals and organizations. We acknowledge and greatly appreciate each and every one of them:

**Authors on the publications** (in alphabetical order)

Abror Khaytbaev  
Ahsan Wahab  
Aigiz Kunafin  
Anoop Babu  
Antonio Laverghetta Jr.  
Behzod Moydinboyev  
Behzodbek Moydinboyev  
Dr. Duygu Ataman  
Esra Onal  
Dr. Francis Tyers  
Jamshidbek Mirzakhalov  
Dr. John Licato  
Dr. Julia Kreutzer  
Mammad Hajili  
Mokhiyakhon Uzokova  
Dr. Orhan Firat  
Otabek Abduraufov  
Sardana Ivanova  
Shaxnoza Pulatova  
Sherzod Kariev  
Dr. Sriram Chellappan  

**Translators, annotators and dataset contributors** (in alphabetical order)

Abilxayr Zholdybai  
Aigiz Kunafin  
Akylbek Khamitov  
Alperen Cantez  
Aydos Muxammadiyarov  
Doniyorbek Rafikjonov  
Erkinbek Vokhabov  
Ipek Baris  
Iskander Shakirov  
Madina Zokirjonova  
Mohiyaxon Uzoqova  
Mukhammadbektosh Khaydarov  
Nurlan Maharramli  
Petr Popov  
Rasul Karimov  
Sariya Kagarmanova  
Ziyodabonu Qobiljon qizi  

**Industry supporters**

[Google Cloud](https://cloud.google.com/solutions/education)  
[Khan Academy Oʻzbek](https://uz.khanacademy.org/)  
[The Foundation for the Preservation and Development of the Bashkir Language](https://bsfond.ru/)  
