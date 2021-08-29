## X-WMT Test Sets

To establish a comprehensive and challenging evaluation benchmark for Machine Translation in Turkic languages, we translate a test set originally introduced in WMT 2020 News Translation Task for English-Russian. The [original dataset](https://www.statmt.org/wmt20/translation-task.html#download) is profesionally translated and consists of sentences from news articles that are both English and Russian-centric. We adopt this evaluation set (X-WMT) and begin efforts to translate it into several Turkic languages. The current version of X-WMT includes covers 8 Turkic languages and 88 language directions with a minimum of 300 sentences per language direction. Currently covered languages are Azerbaijani (az), Bashkir (ba), Karakalpak (kaa), Kazakh (kk), Kirghiz (ky), Turkish (tr), Sakha (sah) and Uzbek (uz). You can download the evaluation sets [here](https://drive.google.com/drive/folders/1SsG-dRDfMy1Ira3PP7TdXOPrKD8BK-Ln?usp=sharing).

|     | **en**   | **ru**   | **ba**  | **tr**  | **uz**  | **ky**  | **kk**  | **az**  | **sah** | **kaa** |
|-----|------|------|-----|-----|-----|-----|-----|-----|-----|-----|
| **en**  | -    |      |     |     |     |     |     |     |     |     |
| **ru**  | **1000** | -    |     |     |     |     |     |     |     |     |
| **ba**  | 1000 | **1000** | -   |     |     |     |     |     |     |     |
| **tr**  | **800**  | 800  | 800 | -   |     |     |     |     |     |     |
| **uz**  | **900**  | 900  | 900 | 600 | -   |     |     |     |     |     |
| **ky**  | 500  | **500**  | 500 | 400 | 500 | -   |     |     |     |     |
| **kk**  | 700  | 700  | 700 | 500 | **700** | 500 | -   |     |     |     |
| **az**  | **600**  | 600  | 600 | 500 | 600 | 500 | 500 | -   |     |     |
| **sah** | 300  | **300**  | 300 | 300 | 300 | 300 | 300 | 300 | -   |     |
| **kaa** | 300  | 300  | 300 | **300** | 300 | 300 | 300 | 300 | 300 | -   |


Table above shows the amount of data available for each language pair. Bolded entries indicate the original translation direction. 