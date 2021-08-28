# A Large­Scale Study of Machine Translation in the Turkic Languages

## Abstract
Recent advances in neural machine translation (NMT) have pushed the quality of machine translation systems to the point where they are becoming widely adopted to build competitive systems. However, there is still a large number of languages that are yet to reap the benefits of NMT. In this paper, we provide the first large-scale case study of the practical application of MT in the Turkic language family in order to realize the gains of NMT for Turkic languages under high-resource to extremely low-resource scenarios. In addition to presenting an extensive analysis that identifies the bottlenecks towards building competitive systems to ameliorate data scarcity, our study has several key contributions, including, i) a large parallel corpus covering 22 Turkic languages consisting of common public datasets in combination with new datasets of approximately 1.4 million parallel sentences, ii) bilingual baselines for 26 language pairs, iii) novel high-quality test sets in three different translation domains and iv) human evaluation scores. All models, scripts, and data will be released to the public.

## Reproducing the bilingual baselines from the paper

Our paper titled "Large-scale study of Machine Translation in Turkic Languages" was accepted to appear in the main proceedings of EMNLP 2021. You can find the full paper here. 

We present a number of bilingual baselines for Turkic languages using the TIL parallel corpus. This repo will help the community to reproduce the results obtained in the paper. 

*NOTE* The contents, size and quality of the corpus have improved dramatically since these experiments were run. The scripts in this repo will be using the snapshot of the corpus at the time of the paper submission. For more accurate baseline results, refer to the til-mt repo which uses the updated corpus.

All experiments except high-resource pairs are run on preemptible [Google Colab](https://colab.research.google.com/notebooks/intro.ipynb#recent=true) instances. Certain pairs may take around 36-48 hours which mean the model has to be resumed (due to Google Colab usage limits). All Experiments are performed using [JoeyNMT](https://github.com/joeynmt/joeynmt) framework.

## Access to the dataset

To access the snapshot of the corpus used to produce the results, use this [link](https://drive.google.com/drive/folders/1sbkwGuKVSxWCVbMOQhOiizdlJSumahRD?usp=sharing). You can make a copy of the corpus to your Google Drive account or choose to download it to your local storage (WARNING: Corpus size could be over 20GBs)


## Hyperparameters

We refer the reader to Section 4.1 for exact hyperparameters for the specific set of language pairs. The baselines script provided assumes a "medium-resource" language pair and uses the corresponding hyperparameters. 


##
| Source                           | Link                                              | Languages  | Size  | Licence/Usage                                      |
|----------------------------------|---------------------------------------------------|------------|-------|----------------------------------------------------|
| Tatoeba Challenge (OPUS+Tatoeba+Gourmet+JW300) | https://github.com/Helsinki-NLP/Tatoeba-Challenge | tr, uz, ka | ~40m  | https://creativecommons.org/licenses/by-nc-sa/4.0/ |
| UDHR                                 |    https://www.ohchr.org/EN/UDHR/Pages/SearchByLang.aspx                       | alt, ba, az, cv, cjs, crh, en, gag, kaa, kjh, kk, ky, sah, slr, tk, tt, ug, uz, tr           |      ~100 per direction |                                                    |
| Bible                                |      https://www.faithcomesbyhearing.com/audio-bible-resources/recordings-database                    | alt, ba, az, cjs,cv, crh, en, gag, kaa, kjh, kk, ky, sah, tk, tt, ug, uz, tr           |      ~9k per direction |                                   |
| Ted Talks                                |      https://www.ted.com/participate/translate/our-languages    | az, en, kk, ky, ru, tt, tr, tt, uz, ug   |      ~600k |  https://www.ted.com/about/our-organization/our-policies-terms/ted-com-terms-of-use    |
| Mozilla    |          | az, ba, cv, en, kk, ky, sah, tk, tt, ug, uz, tr, ru          |      ~300 per direction |  https://www.mozilla.org/en-US/about/legal/terms/mozilla/    |
| Azerbaijani News    |    https://github.com/derintelligence/en-az-parallel-corpus      | az, en |      ~68k | Author's permission |
| Uzbek/English News   |   https://data.gov.uz/,  https://president.uz/, https://uz.usembassy.gov/,  https://www.gov.uz/,      | uz, en |      ~60k | |
| Uzbekistan Legislative Dataset (Law)   |    https://lex.uz/  | uz, ru, en |      ~1.5m |  |
| KhanAcademy Project Translations (Math/Science)   |    https://uz.khanacademy.org/ | uz, en |      ~200k | Author's permission |
| Karakalpak News   |  https://kknews.uz/, https://www.gov.uz/, http://karakalpakstan.uz/, https://www.qrstat.uz/kk/   | kaa, uz, ru, en |      ~60k | |
| Bashkir-Russian Corpus   | https://github.com/AigizK/bashkort-parallel-corpora  | ba,ru |      ~600k | Author's permission |
| Salar Language Materials   | http://www.sino-platonic.org/complete/spp043_salar_language.pdf | slr,en |      ~700 |  |
| Urum Language Materials   | https://web.archive.org/web/20180919233848/http://projects.turkmas.uoa.gr/urum/  | urum, en |      ~500 |  |
| Russian-Shor Online Dictionary   | http://tili.tadarlar.ru/tadar/rus-shor.html  | ru,cjs |      ~300 | |







