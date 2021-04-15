# Machine Translation Corpus for Turkic Languages

## Getting started

### Simplest option!
Install the necessary libraries
```
pip install -r requirements.txt
```

Run the baseline script by passing in two language codes. This will automatically download the data, process it, install the necesssary libraries and framework and start the training process. The script assumes you are on a GPU-enabled device with CUDA support.

```
bash train_baseline.sh <source_language> <target_language>
```

## Useful scripts

### Download the data
To get started, download the data for a pair that you are interested
```
python download_data.py <source_language_code> <target_language_code>
```

### Install JoeyNMT

```
git clone https://github.com/joeynmt/joeynmt.git
cd joeynmt; pip3 install .
pip install torch==1.8.0+cu101 -f https://download.pytorch.org/whl/torch_stable.html
```

Languages with most critical need for MT technologies: **Karakalpak, Chuvash, Bashkir, Crimean Tatar, Sakha, Kumyk** etcss

|     | source          | target          | pair    |    train |   dev |   bible |   ted |   x-wmt |
|----:|:----------------|:----------------|:--------|---------:|------:|--------:|------:|--------:|
|   0 | English         | Turkish         | en-tr   | 37105506 |  5000 |    1263 |  5381 |     700 |
|   1 | Turkish         | English         | tr-en   | 37105506 |  5000 |    1263 |  5381 |     700 |
|   2 | Turkish         | Russian         | tr-ru   | 14973420 |  5000 |    1086 |  5297 |     700 |
|   3 | Russian         | Turkish         | ru-tr   | 14973420 |  5000 |    1086 |  5297 |     700 |
|   4 | Russian         | Kazakh          | ru-kk   |  4413843 |  5000 |    1042 |  3415 |     700 |
|   5 | Kazakh          | Russian         | kk-ru   |  4413843 |  5000 |    1042 |  3415 |     700 |
|   6 | Uzbek           | Russian         | uz-ru   |  1108756 |  5000 |    1117 |  2926 |     800 |
|   7 | Russian         | Uzbek           | ru-uz   |  1108756 |  5000 |    1117 |  2926 |     800 |
|   8 | Azerbaijani     | English         | az-en   |   736356 |  2500 |    1102 |  3887 |     600 |
|   9 | English         | Azerbaijani     | en-az   |   736356 |  2500 |    1102 |  3887 |     600 |
|  10 | Turkish         | Azerbaijani     | tr-az   |   595638 |  2500 |    1199 |  4237 |     500 |
|  11 | Azerbaijani     | Turkish         | az-tr   |   595638 |  2500 |    1199 |  4237 |     500 |
|  12 | English         | Kirghiz         | en-ky   |   566132 |  2500 |    1040 |   330 |     500 |
|  13 | Kirghiz         | English         | ky-en   |   566132 |  2500 |    1040 |   330 |     500 |
|  14 | Kazakh          | English         | kk-en   |   558612 |  2500 |    1013 |  3734 |     700 |
|  15 | English         | Kazakh          | en-kk   |   558612 |  2500 |    1013 |  3734 |     700 |
|  16 | Kirghiz         | Turkish         | ky-tr   |   510921 |  2500 |    1120 |     0 |     400 |
|  17 | Turkish         | Kirghiz         | tr-ky   |   510921 |  2500 |    1120 |     0 |     400 |
|  18 | English         | Tatar           | en-tt   |   508931 |  2500 |    1028 |     0 |       0 |
|  19 | Tatar           | English         | tt-en   |   508931 |  2500 |    1028 |     0 |       0 |
|  20 | English         | Uzbek           | en-uz   |   492871 |  2500 |    1078 |  3474 |     800 |
|  21 | Uzbek           | English         | uz-en   |   492871 |  2500 |    1078 |  3474 |     800 |
|  22 | Turkish         | Tatar           | tr-tt   |   483125 |  2500 |    1089 |     0 |       0 |
|  23 | Tatar           | Turkish         | tt-tr   |   483125 |  2500 |    1089 |     0 |       0 |
|  24 | Russian         | Azerbaijani     | ru-az   |   335969 |  2500 |    1123 |     0 |     600 |
|  25 | Azerbaijani     | Russian         | az-ru   |   335969 |  2500 |    1123 |     0 |     600 |
|  26 | Russian         | Kirghiz         | ru-ky   |   293703 |  2500 |    1092 |     0 |     500 |
|  27 | Kirghiz         | Russian         | ky-ru   |   293703 |  2500 |    1092 |     0 |     500 |
|  28 | Tatar           | Russian         | tt-ru   |   271356 |  2500 |    1133 |     0 |       0 |
|  29 | Russian         | Tatar           | ru-tt   |   271356 |  2500 |    1133 |     0 |       0 |
|  30 | Turkmen         | English         | tk-en   |   231930 |  2500 |    1118 |     0 |       0 |
|  31 | English         | Turkmen         | en-tk   |   231930 |  2500 |    1118 |     0 |       0 |
|  32 | Turkmen         | Turkish         | tk-tr   |   229238 |  2500 |    1281 |     0 |       0 |
|  33 | Turkish         | Turkmen         | tr-tk   |   229238 |  2500 |    1281 |     0 |       0 |
|  34 | Tatar           | Kirghiz         | tt-ky   |   220945 |  2500 |    1128 |     0 |       0 |
|  35 | Kirghiz         | Tatar           | ky-tt   |   220945 |  2500 |    1128 |     0 |       0 |
|  36 | Uzbek           | Azerbaijani     | uz-az   |   217829 |  2500 |    1153 |     0 |     600 |
|  37 | Azerbaijani     | Uzbek           | az-uz   |   217829 |  2500 |    1153 |     0 |     600 |
|  38 | Tatar           | Turkmen         | tt-tk   |   216406 |  2500 |    1135 |     0 |       0 |
|  39 | Turkmen         | Tatar           | tk-tt   |   216406 |  2500 |    1135 |     0 |       0 |
|  40 | Uzbek           | Turkish         | uz-tr   |   211021 |  2500 |    1187 |  3081 |     600 |
|  41 | Turkish         | Uzbek           | tr-uz   |   211021 |  2500 |    1187 |  3081 |     600 |
|  42 | Kirghiz         | Azerbaijani     | ky-az   |   206804 |  2500 |    1100 |     0 |     500 |
|  43 | Azerbaijani     | Kirghiz         | az-ky   |   206804 |  2500 |    1100 |     0 |     500 |
|  44 | Azerbaijani     | Tatar           | az-tt   |   202212 |  2500 |    1154 |     0 |       0 |
|  45 | Tatar           | Azerbaijani     | tt-az   |   202212 |  2500 |    1154 |     0 |       0 |
|  46 | Chuvash         | Tatar           | cv-tt   |   150810 |  2500 |    1122 |     0 |       0 |
|  47 | Tatar           | Chuvash         | tt-cv   |   150810 |  2500 |    1122 |     0 |       0 |
|  48 | Turkish         | Chuvash         | tr-cv   |   143324 |  2500 |    1195 |     0 |       0 |
|  49 | Chuvash         | Turkish         | cv-tr   |   143324 |  2500 |    1195 |     0 |       0 |
|  50 | Chuvash         | English         | cv-en   |   137644 |  2500 |    1128 |     0 |       0 |
|  51 | English         | Chuvash         | en-cv   |   137644 |  2500 |    1128 |     0 |       0 |
|  52 | Tatar           | Uzbek           | tt-uz   |   126827 |  2500 |    1134 |     0 |       0 |
|  53 | Uzbek           | Tatar           | uz-tt   |   126827 |  2500 |    1134 |     0 |       0 |
|  54 | Kirghiz         | Uzbek           | ky-uz   |   120385 |  2500 |    1151 |     0 |     500 |
|  55 | Uzbek           | Kirghiz         | uz-ky   |   120385 |  2500 |    1151 |     0 |     500 |
|  56 | Azerbaijani     | Turkmen         | az-tk   |   115304 |  2500 |    1211 |     0 |       0 |
|  57 | Turkmen         | Azerbaijani     | tk-az   |   115304 |  2500 |    1211 |     0 |       0 |
|  58 | Russian         | Turkmen         | ru-tk   |   112124 |  2500 |    1112 |     0 |       0 |
|  59 | Turkmen         | Russian         | tk-ru   |   112124 |  2500 |    1112 |     0 |       0 |
|  60 | Uzbek           | Kazakh          | uz-kk   |   111594 |  2500 |    1125 |     0 |     700 |
|  61 | Kazakh          | Uzbek           | kk-uz   |   111594 |  2500 |    1125 |     0 |     700 |
|  62 | Turkmen         | Kirghiz         | tk-ky   |   111510 |  2500 |    1138 |     0 |       0 |
|  63 | Kirghiz         | Turkmen         | ky-tk   |   111510 |  2500 |    1138 |     0 |       0 |
|  64 | English         | Uighur          | en-ug   |    96793 |   500 |     968 |     0 |       0 |
|  65 | Uighur          | English         | ug-en   |    96793 |   500 |     968 |     0 |       0 |
|  66 | Russian         | Chuvash         | ru-cv   |    80983 |   500 |    1111 |     0 |       0 |
|  67 | Chuvash         | Russian         | cv-ru   |    80983 |   500 |    1111 |     0 |       0 |
|  68 | Chuvash         | Kirghiz         | cv-ky   |    79252 |   500 |    1089 |     0 |       0 |
|  69 | Kirghiz         | Chuvash         | ky-cv   |    79252 |   500 |    1089 |     0 |       0 |
|  70 | Chuvash         | Azerbaijani     | cv-az   |    77854 |   500 |    1174 |     0 |       0 |
|  71 | Azerbaijani     | Chuvash         | az-cv   |    77854 |   500 |    1174 |     0 |       0 |
|  72 | Chuvash         | Turkmen         | cv-tk   |    70669 |   500 |    1210 |     0 |       0 |
|  73 | Turkmen         | Chuvash         | tk-cv   |    70669 |   500 |    1210 |     0 |       0 |
|  74 | Tatar           | Bashkir         | tt-ba   |    66458 |   500 |    1273 |     0 |       0 |
|  75 | Bashkir         | Tatar           | ba-tt   |    66458 |   500 |    1273 |     0 |       0 |
|  76 | Khakas          | Russian         | kjh-ru  |    61224 |   500 |    1075 |     0 |       0 |
|  77 | Russian         | Khakas          | ru-kjh  |    61224 |   500 |    1075 |     0 |       0 |
|  78 | Turkish         | Bashkir         | tr-ba   |    60767 |   500 |    1078 |     0 |       0 |
|  79 | Bashkir         | Turkish         | ba-tr   |    60767 |   500 |    1078 |     0 |       0 |
|  80 | English         | Bashkir         | en-ba   |    58092 |   500 |    1047 |     0 |       0 |
|  81 | Bashkir         | English         | ba-en   |    58092 |   500 |    1047 |     0 |       0 |
|  82 | Turkish         | Uighur          | tr-ug   |    56974 |   500 |    1166 |     0 |       0 |
|  83 | Uighur          | Turkish         | ug-tr   |    56974 |   500 |    1166 |     0 |       0 |
|  84 | Chuvash         | Uzbek           | cv-uz   |    56831 |   500 |    1139 |     0 |       0 |
|  85 | Uzbek           | Chuvash         | uz-cv   |    56831 |   500 |    1139 |     0 |       0 |
|  86 | Kazakh          | Turkish         | kk-tr   |    54206 |   500 |    1099 |     0 |     500 |
|  87 | Turkish         | Kazakh          | tr-kk   |    54206 |   500 |    1099 |     0 |     500 |
|  88 | Uighur          | Russian         | ug-ru   |    42200 |   500 |    1015 |     0 |       0 |
|  89 | Russian         | Uighur          | ru-ug   |    42200 |   500 |    1015 |     0 |       0 |
|  90 | Bashkir         | Russian         | ba-ru   |    35615 |   500 |    1131 |     0 |       0 |
|  91 | Russian         | Bashkir         | ru-ba   |    35615 |   500 |    1131 |     0 |       0 |
|  92 | Kirghiz         | Bashkir         | ky-ba   |    34948 |   500 |    1124 |     0 |       0 |
|  93 | Bashkir         | Kirghiz         | ba-ky   |    34948 |   500 |    1124 |     0 |       0 |
|  94 | Bashkir         | Chuvash         | ba-cv   |    32268 |   500 |    1124 |     0 |       0 |
|  95 | Chuvash         | Bashkir         | cv-ba   |    32268 |   500 |    1124 |     0 |       0 |
|  96 | Bashkir         | Azerbaijani     | ba-az   |    31498 |   500 |    1141 |     0 |       0 |
|  97 | Azerbaijani     | Bashkir         | az-ba   |    31498 |   500 |    1141 |     0 |       0 |
|  98 | Bashkir         | Turkmen         | ba-tk   |    27817 |   500 |    1137 |     0 |       0 |
|  99 | Turkmen         | Bashkir         | tk-ba   |    27817 |   500 |    1137 |     0 |       0 |
| 100 | Bashkir         | Uzbek           | ba-uz   |    26743 |   500 |    1120 |     0 |       0 |
| 101 | Uzbek           | Bashkir         | uz-ba   |    26743 |   500 |    1120 |     0 |       0 |
| 102 | Tuvinian        | Turkish         | tyv-tr  |    25583 |   500 |       0 |     0 |       0 |
| 103 | Turkish         | Tuvinian        | tr-tyv  |    25583 |   500 |       0 |     0 |       0 |
| 104 | English         | Tuvinian        | en-tyv  |    24658 |   500 |       0 |     0 |       0 |
| 105 | Tuvinian        | English         | tyv-en  |    24658 |   500 |       0 |     0 |       0 |
| 106 | Uzbek           | Uighur          | uz-ug   |    16528 |   500 |    1129 |     0 |       0 |
| 107 | Uighur          | Uzbek           | ug-uz   |    16528 |   500 |    1129 |     0 |       0 |
| 108 | Crimean Tatar   | English         | crh-en  |    14368 |   500 |    1123 |     0 |       0 |
| 109 | English         | Crimean Tatar   | en-crh  |    14368 |   500 |    1123 |     0 |       0 |
| 110 | Bashkir         | Tuvinian        | ba-tyv  |    14066 |   500 |       0 |     0 |       0 |
| 111 | Tuvinian        | Bashkir         | tyv-ba  |    14066 |   500 |       0 |     0 |       0 |
| 112 | Tuvinian        | Kirghiz         | tyv-ky  |    13593 |   500 |       0 |     0 |       0 |
| 113 | Kirghiz         | Tuvinian        | ky-tyv  |    13593 |   500 |       0 |     0 |       0 |
| 114 | Tatar           | Tuvinian        | tt-tyv  |    13482 |   500 |       0 |     0 |       0 |
| 115 | Tuvinian        | Tatar           | tyv-tt  |    13482 |   500 |       0 |     0 |       0 |
| 116 | Crimean Tatar   | Turkish         | crh-tr  |    13348 |   500 |    1223 |     0 |       0 |
| 117 | Turkish         | Crimean Tatar   | tr-crh  |    13348 |   500 |    1223 |     0 |       0 |
| 118 | Tuvinian        | Chuvash         | tyv-cv  |    12863 |   500 |       0 |     0 |       0 |
| 119 | Chuvash         | Tuvinian        | cv-tyv  |    12863 |   500 |       0 |     0 |       0 |
| 120 | Tuvinian        | Azerbaijani     | tyv-az  |    11906 |   500 |       0 |     0 |       0 |
| 121 | Azerbaijani     | Tuvinian        | az-tyv  |    11906 |   500 |       0 |     0 |       0 |
| 122 | Bashkir         | Altai           | ba-alt  |    11757 |   500 |    1166 |     0 |       0 |
| 123 | Altai           | Bashkir         | alt-ba  |    11757 |   500 |    1166 |     0 |       0 |
| 124 | Russian         | Crimean Tatar   | ru-crh  |    11548 |   500 |    1116 |     0 |       0 |
| 125 | Crimean Tatar   | Russian         | crh-ru  |    11548 |   500 |    1116 |     0 |       0 |
| 126 | Tatar           | Altai           | tt-alt  |    11515 |   500 |    1174 |     0 |       0 |
| 127 | Altai           | Tatar           | alt-tt  |    11515 |   500 |    1174 |     0 |       0 |
| 128 | Turkmen         | Tuvinian        | tk-tyv  |    11433 |   500 |       0 |     0 |       0 |
| 129 | Tuvinian        | Turkmen         | tyv-tk  |    11433 |   500 |       0 |     0 |       0 |
| 130 | Kirghiz         | Altai           | ky-alt  |    11320 |   500 |    1131 |     0 |       0 |
| 131 | Altai           | Kirghiz         | alt-ky  |    11320 |   500 |    1131 |     0 |       0 |
| 132 | Altai           | Turkish         | alt-tr  |    11029 |   500 |    1110 |     0 |       0 |
| 133 | Turkish         | Altai           | tr-alt  |    11029 |   500 |    1110 |     0 |       0 |
| 134 | Altai           | Uzbek           | alt-uz  |    10563 |   500 |    1146 |     0 |       0 |
| 135 | Uzbek           | Altai           | uz-alt  |    10563 |   500 |    1146 |     0 |       0 |
| 136 | Altai           | English         | alt-en  |    10531 |   500 |    1066 |     0 |       0 |
| 137 | English         | Altai           | en-alt  |    10531 |   500 |    1066 |     0 |       0 |
| 138 | Karakalpak      | Uzbek           | kaa-uz  |    10529 |   500 |    1257 |     0 |     300 |
| 139 | Uzbek           | Karakalpak      | uz-kaa  |    10529 |   500 |    1257 |     0 |     300 |
| 140 | Altai           | Chuvash         | alt-cv  |    10138 |   500 |    1173 |     0 |       0 |
| 141 | Chuvash         | Altai           | cv-alt  |    10138 |   500 |    1173 |     0 |       0 |
| 142 | Altai           | Azerbaijani     | alt-az  |     9942 |   500 |    1136 |     0 |       0 |
| 143 | Azerbaijani     | Altai           | az-alt  |     9942 |   500 |    1136 |     0 |       0 |
| 144 | Turkmen         | Altai           | tk-alt  |     9711 |   500 |    1153 |     0 |       0 |
| 145 | Altai           | Turkmen         | alt-tk  |     9711 |   500 |    1153 |     0 |       0 |
| 146 | Tuvinian        | Uzbek           | tyv-uz  |     9662 |   500 |       0 |     0 |       0 |
| 147 | Uzbek           | Tuvinian        | uz-tyv  |     9662 |   500 |       0 |     0 |       0 |
| 148 | Crimean Tatar   | Tatar           | crh-tt  |     8387 |   500 |    1177 |     0 |       0 |
| 149 | Tatar           | Crimean Tatar   | tt-crh  |     8387 |   500 |    1177 |     0 |       0 |
| 150 | Uzbek           | Crimean Tatar   | uz-crh  |     8216 |   500 |    1275 |     0 |       0 |
| 151 | Crimean Tatar   | Uzbek           | crh-uz  |     8216 |   500 |    1275 |     0 |       0 |
| 152 | Russian         | Yakut (Sakha)   | ru-sah  |     8163 |   500 |    1014 |     0 |     300 |
| 153 | Yakut (Sakha)   | Russian         | sah-ru  |     8163 |   500 |    1014 |     0 |     300 |
| 154 | Kumyk           | Karakalpak      | kum-kaa |     8103 |   500 |    1266 |     0 |       0 |
| 155 | Karakalpak      | Kumyk           | kaa-kum |     8103 |   500 |    1266 |     0 |       0 |
| 156 | Khakas          | Yakut (Sakha)   | kjh-sah |     8029 |   500 |    1032 |     0 |       0 |
| 157 | Yakut (Sakha)   | Khakas          | sah-kjh |     8029 |   500 |    1032 |     0 |       0 |
| 158 | Karachay-Balkar | Khakas          | krc-kjh |     7972 |   500 |    1120 |     0 |       0 |
| 159 | Khakas          | Karachay-Balkar | kjh-krc |     7972 |   500 |    1120 |     0 |       0 |
| 160 | Azerbaijani     | Kazakh          | az-kk   |     7904 |   500 |    1075 |     0 |     500 |
| 161 | Kazakh          | Azerbaijani     | kk-az   |     7904 |   500 |    1075 |     0 |     500 |
| 162 | Karakalpak      | Crimean Tatar   | kaa-crh |     7825 |   500 |    1258 |     0 |       0 |
| 163 | Crimean Tatar   | Karakalpak      | crh-kaa |     7825 |   500 |    1258 |     0 |       0 |
| 164 | Tatar           | Kazakh          | tt-kk   |     7773 |   500 |    1085 |     0 |       0 |
| 165 | Kazakh          | Tatar           | kk-tt   |     7773 |   500 |    1085 |     0 |       0 |
| 166 | Crimean Tatar   | Azerbaijani     | crh-az  |     7750 |   500 |    1191 |     0 |       0 |
| 167 | Azerbaijani     | Crimean Tatar   | az-crh  |     7750 |   500 |    1191 |     0 |       0 |
| 168 | Crimean Tatar   | Khakas          | crh-kjh |     7738 |   500 |    1154 |     0 |       0 |
| 169 | Khakas          | Crimean Tatar   | kjh-crh |     7738 |   500 |    1154 |     0 |       0 |
| 170 | Uzbek           | Kumyk           | uz-kum  |     7693 |   500 |    1199 |     0 |       0 |
| 171 | Kumyk           | Uzbek           | kum-uz  |     7693 |   500 |    1199 |     0 |       0 |
| 172 | Uighur          | Crimean Tatar   | ug-crh  |     7613 |   500 |    1144 |     0 |       0 |
| 173 | Crimean Tatar   | Uighur          | crh-ug  |     7613 |   500 |    1144 |     0 |       0 |
| 174 | Crimean Tatar   | Turkmen         | crh-tk  |     7602 |   500 |    1223 |     0 |       0 |
| 175 | Turkmen         | Crimean Tatar   | tk-crh  |     7602 |   500 |    1223 |     0 |       0 |
| 176 | Kirghiz         | Karakalpak      | ky-kaa  |     7600 |   500 |    1208 |     0 |     300 |
| 177 | Karakalpak      | Kirghiz         | kaa-ky  |     7600 |   500 |    1208 |     0 |     300 |
| 178 | Karakalpak      | Altai           | kaa-alt |     7586 |   500 |    1195 |     0 |       0 |
| 179 | Altai           | Karakalpak      | alt-kaa |     7586 |   500 |    1195 |     0 |       0 |
| 180 | Karakalpak      | Bashkir         | kaa-ba  |     7557 |   500 |    1181 |     0 |       0 |
| 181 | Bashkir         | Karakalpak      | ba-kaa  |     7557 |   500 |    1181 |     0 |       0 |
| 182 | Karachay-Balkar | Yakut (Sakha)   | krc-sah |     7555 |   500 |    1056 |     0 |       0 |
| 183 | Yakut (Sakha)   | Karachay-Balkar | sah-krc |     7555 |   500 |    1056 |     0 |       0 |
| 184 | Crimean Tatar   | Kumyk           | crh-kum |     7554 |   500 |    1216 |     0 |       0 |
| 185 | Kumyk           | Crimean Tatar   | kum-crh |     7554 |   500 |    1216 |     0 |       0 |
| 186 | Chuvash         | Crimean Tatar   | cv-crh  |     7550 |   500 |    1217 |     0 |       0 |
| 187 | Crimean Tatar   | Chuvash         | crh-cv  |     7550 |   500 |    1217 |     0 |       0 |
| 188 | Tatar           | Karakalpak      | tt-kaa  |     7527 |   500 |    1196 |     0 |       0 |
| 189 | Karakalpak      | Tatar           | kaa-tt  |     7527 |   500 |    1196 |     0 |       0 |
| 190 | Turkmen         | Uzbek           | tk-uz   |     7526 |   500 |    1203 |     0 |       0 |
| 191 | Uzbek           | Turkmen         | uz-tk   |     7526 |   500 |    1203 |     0 |       0 |
| 192 | Karakalpak      | Azerbaijani     | kaa-az  |     7497 |   500 |    1188 |     0 |     300 |
| 193 | Azerbaijani     | Karakalpak      | az-kaa  |     7497 |   500 |    1188 |     0 |     300 |
| 194 | Uighur          | Karakalpak      | ug-kaa  |     7485 |   500 |    1200 |     0 |       0 |
| 195 | Karakalpak      | Uighur          | kaa-ug  |     7485 |   500 |    1200 |     0 |       0 |
| 196 | Russian         | Karakalpak      | ru-kaa  |     7483 |   500 |    1111 |     0 |     300 |
| 197 | Karakalpak      | Russian         | kaa-ru  |     7483 |   500 |    1111 |     0 |     300 |
| 198 | Karakalpak      | Kazakh          | kaa-kk  |     7472 |   500 |    1184 |     0 |     300 |
| 199 | Kazakh          | Karakalpak      | kk-kaa  |     7472 |   500 |    1184 |     0 |     300 |
| 200 | Khakas          | Chuvash         | kjh-cv  |     7467 |   500 |    1201 |     0 |       0 |
| 201 | Chuvash         | Khakas          | cv-kjh  |     7467 |   500 |    1201 |     0 |       0 |
| 202 | Crimean Tatar   | Altai           | crh-alt |     7449 |   500 |    1192 |     0 |       0 |
| 203 | Altai           | Crimean Tatar   | alt-crh |     7449 |   500 |    1192 |     0 |       0 |
| 204 | Turkmen         | Karakalpak      | tk-kaa  |     7442 |   500 |    1227 |     0 |       0 |
| 205 | Karakalpak      | Turkmen         | kaa-tk  |     7442 |   500 |    1227 |     0 |       0 |
| 206 | Uzbek           | Khakas          | uz-kjh  |     7421 |   500 |    1128 |     0 |       0 |
| 207 | Khakas          | Uzbek           | kjh-uz  |     7421 |   500 |    1128 |     0 |       0 |
| 208 | Kumyk           | Tatar           | kum-tt  |     7416 |   500 |    1174 |     0 |       0 |
| 209 | Tatar           | Kumyk           | tt-kum  |     7416 |   500 |    1174 |     0 |       0 |
| 210 | Turkish         | Khakas          | tr-kjh  |     7410 |   500 |    1206 |     0 |       0 |
| 211 | Khakas          | Turkish         | kjh-tr  |     7410 |   500 |    1206 |     0 |       0 |
| 212 | Crimean Tatar   | Bashkir         | crh-ba  |     7409 |   500 |    1159 |     0 |       0 |
| 213 | Bashkir         | Crimean Tatar   | ba-crh  |     7409 |   500 |    1159 |     0 |       0 |
| 214 | Bashkir         | Kumyk           | ba-kum  |     7403 |   500 |    1163 |     0 |       0 |
| 215 | Kumyk           | Bashkir         | kum-ba  |     7403 |   500 |    1163 |     0 |       0 |
| 216 | Kirghiz         | Kumyk           | ky-kum  |     7398 |   500 |    1176 |     0 |       0 |
| 217 | Kumyk           | Kirghiz         | kum-ky  |     7398 |   500 |    1176 |     0 |       0 |
| 218 | Azerbaijani     | Khakas          | az-kjh  |     7389 |   500 |    1133 |     0 |       0 |
| 219 | Khakas          | Azerbaijani     | kjh-az  |     7389 |   500 |    1133 |     0 |       0 |
| 220 | Turkish         | Karakalpak      | tr-kaa  |     7376 |   500 |    1235 |     0 |     300 |
| 221 | Karakalpak      | Turkish         | kaa-tr  |     7376 |   500 |    1235 |     0 |     300 |
| 222 | Kumyk           | Altai           | kum-alt |     7369 |   500 |    1185 |     0 |       0 |
| 223 | Altai           | Kumyk           | alt-kum |     7369 |   500 |    1185 |     0 |       0 |
| 224 | Khakas          | Turkmen         | kjh-tk  |     7364 |   500 |    1175 |     0 |       0 |
| 225 | Turkmen         | Khakas          | tk-kjh  |     7364 |   500 |    1175 |     0 |       0 |
| 226 | Altai           | Russian         | alt-ru  |     7349 |   500 |    1137 |     0 |       0 |
| 227 | Russian         | Altai           | ru-alt  |     7349 |   500 |    1137 |     0 |       0 |
| 228 | Khakas          | Karakalpak      | kjh-kaa |     7344 |   500 |    1158 |     0 |       0 |
| 229 | Karakalpak      | Khakas          | kaa-kjh |     7344 |   500 |    1158 |     0 |       0 |
| 230 | Khakas          | Altai           | kjh-alt |     7303 |   500 |    1148 |     0 |       0 |
| 231 | Altai           | Khakas          | alt-kjh |     7303 |   500 |    1148 |     0 |       0 |
| 232 | English         | Khakas          | en-kjh  |     7252 |   500 |    1099 |     0 |       0 |
| 233 | Khakas          | English         | kjh-en  |     7252 |   500 |    1099 |     0 |       0 |
| 234 | Crimean Tatar   | Karachay-Balkar | crh-krc |     7233 |   500 |    1118 |     0 |       0 |
| 235 | Karachay-Balkar | Crimean Tatar   | krc-crh |     7233 |   500 |    1118 |     0 |       0 |
| 236 | Karachay-Balkar | Azerbaijani     | krc-az  |     7233 |   500 |    1119 |     0 |       0 |
| 237 | Azerbaijani     | Karachay-Balkar | az-krc  |     7233 |   500 |    1119 |     0 |       0 |
| 238 | Kazakh          | Kirghiz         | kk-ky   |     7193 |   500 |    1131 |  3318 |     500 |
| 239 | Kirghiz         | Kazakh          | ky-kk   |     7193 |   500 |    1131 |  3318 |     500 |
| 240 | Karakalpak      | English         | kaa-en  |     7173 |   500 |    1088 |     0 |     300 |
| 241 | English         | Karakalpak      | en-kaa  |     7173 |   500 |    1088 |     0 |     300 |
| 242 | Karachay-Balkar | Chuvash         | krc-cv  |     7170 |   500 |    1136 |     0 |       0 |
| 243 | Chuvash         | Karachay-Balkar | cv-krc  |     7170 |   500 |    1136 |     0 |       0 |
| 244 | Kumyk           | Turkmen         | kum-tk  |     7154 |   500 |    1189 |     0 |       0 |
| 245 | Turkmen         | Kumyk           | tk-kum  |     7154 |   500 |    1189 |     0 |       0 |
| 246 | Uighur          | Kumyk           | ug-kum  |     7151 |   500 |    1167 |     0 |       0 |
| 247 | Kumyk           | Uighur          | kum-ug  |     7151 |   500 |    1167 |     0 |       0 |
| 248 | Turkmen         | Uighur          | tk-ug   |     7149 |   500 |    1160 |     0 |       0 |
| 249 | Uighur          | Turkmen         | ug-tk   |     7149 |   500 |    1160 |     0 |       0 |
| 250 | Chuvash         | Karakalpak      | cv-kaa  |     7144 |   500 |    1182 |     0 |       0 |
| 251 | Karakalpak      | Chuvash         | kaa-cv  |     7144 |   500 |    1182 |     0 |       0 |
| 252 | Kirghiz         | Crimean Tatar   | ky-crh  |     7139 |   500 |    1178 |     0 |       0 |
| 253 | Crimean Tatar   | Kirghiz         | crh-ky  |     7139 |   500 |    1178 |     0 |       0 |
| 254 | Uighur          | Khakas          | ug-kjh  |     7113 |   500 |    1103 |     0 |       0 |
| 255 | Khakas          | Uighur          | kjh-ug  |     7113 |   500 |    1103 |     0 |       0 |
| 256 | Kumyk           | Azerbaijani     | kum-az  |     7097 |   500 |    1137 |     0 |       0 |
| 257 | Azerbaijani     | Kumyk           | az-kum  |     7097 |   500 |    1137 |     0 |       0 |
| 258 | Kumyk           | Khakas          | kum-kjh |     7089 |   500 |    1142 |     0 |       0 |
| 259 | Khakas          | Kumyk           | kjh-kum |     7089 |   500 |    1142 |     0 |       0 |
| 260 | Kumyk           | Turkish         | kum-tr  |     7088 |   500 |    1181 |     0 |       0 |
| 261 | Turkish         | Kumyk           | tr-kum  |     7088 |   500 |    1181 |     0 |       0 |
| 262 | Kumyk           | Kazakh          | kum-kk  |     7085 |   500 |    1151 |     0 |       0 |
| 263 | Kazakh          | Kumyk           | kk-kum  |     7085 |   500 |    1151 |     0 |       0 |
| 264 | Kumyk           | Chuvash         | kum-cv  |     7081 |   500 |    1193 |     0 |       0 |
| 265 | Chuvash         | Kumyk           | cv-kum  |     7081 |   500 |    1193 |     0 |       0 |
| 266 | Russian         | Kumyk           | ru-kum  |     7073 |   500 |    1107 |     0 |       0 |
| 267 | Kumyk           | Russian         | kum-ru  |     7073 |   500 |    1107 |     0 |       0 |
| 268 | Azerbaijani     | Gagauz          | az-gag  |     7042 |   500 |    1139 |     0 |       0 |
| 269 | Gagauz          | Azerbaijani     | gag-az  |     7042 |   500 |    1139 |     0 |       0 |
| 270 | Bashkir         | Khakas          | ba-kjh  |     7028 |   500 |    1112 |     0 |       0 |
| 271 | Khakas          | Bashkir         | kjh-ba  |     7028 |   500 |    1112 |     0 |       0 |
| 272 | Uighur          | Azerbaijani     | ug-az   |     7009 |   500 |    1083 |     0 |       0 |
| 273 | Azerbaijani     | Uighur          | az-ug   |     7009 |   500 |    1083 |     0 |       0 |
| 274 | Karachay-Balkar | Turkmen         | krc-tk  |     7007 |   500 |    1109 |     0 |       0 |
| 275 | Turkmen         | Karachay-Balkar | tk-krc  |     7007 |   500 |    1109 |     0 |       0 |
| 276 | Crimean Tatar   | Gagauz          | crh-gag |     6997 |   500 |    1125 |     0 |       0 |
| 277 | Gagauz          | Crimean Tatar   | gag-crh |     6997 |   500 |    1125 |     0 |       0 |
| 278 | Crimean Tatar   | Kazakh          | crh-kk  |     6991 |   500 |    1131 |     0 |       0 |
| 279 | Kazakh          | Crimean Tatar   | kk-crh  |     6991 |   500 |    1131 |     0 |       0 |
| 280 | Tatar           | Khakas          | tt-kjh  |     6982 |   500 |    1132 |     0 |       0 |
| 281 | Khakas          | Tatar           | kjh-tt  |     6982 |   500 |    1132 |     0 |       0 |
| 282 | Karachay-Balkar | Uzbek           | krc-uz  |     6975 |   500 |    1080 |     0 |       0 |
| 283 | Uzbek           | Karachay-Balkar | uz-krc  |     6975 |   500 |    1080 |     0 |       0 |
| 284 | Karachay-Balkar | Altai           | krc-alt |     6916 |   500 |    1101 |     0 |       0 |
| 285 | Altai           | Karachay-Balkar | alt-krc |     6916 |   500 |    1101 |     0 |       0 |
| 286 | Karakalpak      | Karachay-Balkar | kaa-krc |     6901 |   500 |    1101 |     0 |       0 |
| 287 | Karachay-Balkar | Karakalpak      | krc-kaa |     6901 |   500 |    1101 |     0 |       0 |
| 288 | Chuvash         | Uighur          | cv-ug   |     6896 |   500 |    1115 |     0 |       0 |
| 289 | Uighur          | Chuvash         | ug-cv   |     6896 |   500 |    1115 |     0 |       0 |
| 290 | Turkish         | Karachay-Balkar | tr-krc  |     6877 |   500 |    1080 |     0 |       0 |
| 291 | Karachay-Balkar | Turkish         | krc-tr  |     6877 |   500 |    1080 |     0 |       0 |
| 292 | Kazakh          | Uighur          | kk-ug   |     6872 |   500 |    1116 |     0 |       0 |
| 293 | Uighur          | Kazakh          | ug-kk   |     6872 |   500 |    1116 |     0 |       0 |
| 294 | Kirghiz         | Uighur          | ky-ug   |     6861 |   500 |    1143 |     0 |       0 |
| 295 | Uighur          | Kirghiz         | ug-ky   |     6861 |   500 |    1143 |     0 |       0 |
| 296 | Gagauz          | Turkish         | gag-tr  |     6854 |   500 |    1139 |     0 |       0 |
| 297 | Turkish         | Gagauz          | tr-gag  |     6854 |   500 |    1139 |     0 |       0 |
| 298 | Yakut (Sakha)   | Chuvash         | sah-cv  |     6841 |   500 |    1052 |     0 |       0 |
| 299 | Chuvash         | Yakut (Sakha)   | cv-sah  |     6841 |   500 |    1052 |     0 |       0 |
| 300 | Bashkir         | Uighur          | ba-ug   |     6814 |   500 |    1085 |     0 |       0 |
| 301 | Uighur          | Bashkir         | ug-ba   |     6814 |   500 |    1085 |     0 |       0 |
| 302 | Kazakh          | Bashkir         | kk-ba   |     6804 |   500 |    1094 |     0 |       0 |
| 303 | Bashkir         | Kazakh          | ba-kk   |     6804 |   500 |    1094 |     0 |       0 |
| 304 | Bashkir         | Karachay-Balkar | ba-krc  |     6802 |   500 |    1084 |     0 |       0 |
| 305 | Karachay-Balkar | Bashkir         | krc-ba  |     6802 |   500 |    1084 |     0 |       0 |
| 306 | Azerbaijani     | Yakut (Sakha)   | az-sah  |     6799 |   500 |    1037 |     0 |     300 |
| 307 | Yakut (Sakha)   | Azerbaijani     | sah-az  |     6799 |   500 |    1037 |     0 |     300 |
| 308 | Russian         | Karachay-Balkar | ru-krc  |     6788 |   500 |    1062 |     0 |       0 |
| 309 | Karachay-Balkar | Russian         | krc-ru  |     6788 |   500 |    1062 |     0 |       0 |
| 310 | English         | Kumyk           | en-kum  |     6787 |   500 |    1116 |     0 |       0 |
| 311 | Kumyk           | English         | kum-en  |     6787 |   500 |    1116 |     0 |       0 |
| 312 | Khakas          | Kirghiz         | kjh-ky  |     6783 |   500 |    1089 |     0 |       0 |
| 313 | Kirghiz         | Khakas          | ky-kjh  |     6783 |   500 |    1089 |     0 |       0 |
| 314 | Tatar           | Karachay-Balkar | tt-krc  |     6775 |   500 |    1077 |     0 |       0 |
| 315 | Karachay-Balkar | Tatar           | krc-tt  |     6775 |   500 |    1077 |     0 |       0 |
| 316 | Chuvash         | Gagauz          | cv-gag  |     6774 |   500 |    1120 |     0 |       0 |
| 317 | Gagauz          | Chuvash         | gag-cv  |     6774 |   500 |    1120 |     0 |       0 |
| 318 | Khakas          | Gagauz          | kjh-gag |     6772 |   500 |    1065 |     0 |       0 |
| 319 | Gagauz          | Khakas          | gag-kjh |     6772 |   500 |    1065 |     0 |       0 |
| 320 | Tatar           | Uighur          | tt-ug   |     6762 |   500 |    1096 |     0 |       0 |
| 321 | Uighur          | Tatar           | ug-tt   |     6762 |   500 |    1096 |     0 |       0 |
| 322 | Yakut (Sakha)   | Uzbek           | sah-uz  |     6753 |   500 |    1012 |     0 |     300 |
| 323 | Uzbek           | Yakut (Sakha)   | uz-sah  |     6753 |   500 |    1012 |     0 |     300 |
| 324 | Karachay-Balkar | Kumyk           | krc-kum |     6751 |   500 |    1077 |     0 |       0 |
| 325 | Kumyk           | Karachay-Balkar | kum-krc |     6751 |   500 |    1077 |     0 |       0 |
| 326 | Chuvash         | Kazakh          | cv-kk   |     6746 |   500 |    1100 |     0 |       0 |
| 327 | Kazakh          | Chuvash         | kk-cv   |     6746 |   500 |    1100 |     0 |       0 |
| 328 | Kazakh          | Altai           | kk-alt  |     6737 |   500 |    1110 |     0 |       0 |
| 329 | Altai           | Kazakh          | alt-kk  |     6737 |   500 |    1110 |     0 |       0 |
| 330 | Kazakh          | Khakas          | kk-kjh  |     6716 |   500 |    1089 |     0 |       0 |
| 331 | Khakas          | Kazakh          | kjh-kk  |     6716 |   500 |    1089 |     0 |       0 |
| 332 | Yakut (Sakha)   | Crimean Tatar   | sah-crh |     6715 |   500 |    1051 |     0 |       0 |
| 333 | Crimean Tatar   | Yakut (Sakha)   | crh-sah |     6715 |   500 |    1051 |     0 |       0 |
| 334 | Uighur          | Karachay-Balkar | ug-krc  |     6708 |   500 |    1045 |     0 |       0 |
| 335 | Karachay-Balkar | Uighur          | krc-ug  |     6708 |   500 |    1045 |     0 |       0 |
| 336 | Turkmen         | Gagauz          | tk-gag  |     6707 |   500 |    1134 |     0 |       0 |
| 337 | Gagauz          | Turkmen         | gag-tk  |     6707 |   500 |    1134 |     0 |       0 |
| 338 | Yakut (Sakha)   | Tatar           | sah-tt  |     6684 |   500 |    1026 |     0 |       0 |
| 339 | Tatar           | Yakut (Sakha)   | tt-sah  |     6684 |   500 |    1026 |     0 |       0 |
| 340 | Kazakh          | Turkmen         | kk-tk   |     6666 |   500 |    1121 |     0 |       0 |
| 341 | Turkmen         | Kazakh          | tk-kk   |     6666 |   500 |    1121 |     0 |       0 |
| 342 | Karachay-Balkar | English         | krc-en  |     6655 |   500 |    1026 |     0 |       0 |
| 343 | English         | Karachay-Balkar | en-krc  |     6655 |   500 |    1026 |     0 |       0 |
| 344 | Gagauz          | Karachay-Balkar | gag-krc |     6645 |   500 |    1083 |     0 |       0 |
| 345 | Karachay-Balkar | Gagauz          | krc-gag |     6645 |   500 |    1083 |     0 |       0 |
| 346 | Gagauz          | English         | gag-en  |     6640 |   500 |    1080 |     0 |       0 |
| 347 | English         | Gagauz          | en-gag  |     6640 |   500 |    1080 |     0 |       0 |
| 348 | Uzbek           | Gagauz          | uz-gag  |     6633 |   500 |    1107 |     0 |       0 |
| 349 | Gagauz          | Uzbek           | gag-uz  |     6633 |   500 |    1107 |     0 |       0 |
| 350 | Turkish         | Yakut (Sakha)   | tr-sah  |     6631 |   500 |    1020 |     0 |     300 |
| 351 | Yakut (Sakha)   | Turkish         | sah-tr  |     6631 |   500 |    1020 |     0 |     300 |
| 352 | Altai           | Uighur          | alt-ug  |     6598 |   500 |    1052 |     0 |       0 |
| 353 | Uighur          | Altai           | ug-alt  |     6598 |   500 |    1052 |     0 |       0 |
| 354 | Altai           | Gagauz          | alt-gag |     6594 |   500 |    1083 |     0 |       0 |
| 355 | Gagauz          | Altai           | gag-alt |     6594 |   500 |    1083 |     0 |       0 |
| 356 | Yakut (Sakha)   | English         | sah-en  |     6582 |   500 |     991 |     0 |     300 |
| 357 | English         | Yakut (Sakha)   | en-sah  |     6582 |   500 |     991 |     0 |     300 |
| 358 | Karakalpak      | Gagauz          | kaa-gag |     6539 |   500 |    1115 |     0 |       0 |
| 359 | Gagauz          | Karakalpak      | gag-kaa |     6539 |   500 |    1115 |     0 |       0 |
| 360 | Karachay-Balkar | Kazakh          | krc-kk  |     6518 |   500 |    1024 |     0 |       0 |
| 361 | Kazakh          | Karachay-Balkar | kk-krc  |     6518 |   500 |    1024 |     0 |       0 |
| 362 | Yakut (Sakha)   | Altai           | sah-alt |     6489 |   500 |    1049 |     0 |       0 |
| 363 | Altai           | Yakut (Sakha)   | alt-sah |     6489 |   500 |    1049 |     0 |       0 |
| 364 | Yakut (Sakha)   | Turkmen         | sah-tk  |     6485 |   500 |    1051 |     0 |       0 |
| 365 | Turkmen         | Yakut (Sakha)   | tk-sah  |     6485 |   500 |    1051 |     0 |       0 |
| 366 | Gagauz          | Bashkir         | gag-ba  |     6464 |   500 |    1076 |     0 |       0 |
| 367 | Bashkir         | Gagauz          | ba-gag  |     6464 |   500 |    1076 |     0 |       0 |
| 368 | Yakut (Sakha)   | Kazakh          | sah-kk  |     6454 |   500 |     974 |     0 |     300 |
| 369 | Kazakh          | Yakut (Sakha)   | kk-sah  |     6454 |   500 |     974 |     0 |     300 |
| 370 | Yakut (Sakha)   | Bashkir         | sah-ba  |     6450 |   500 |    1035 |     0 |       0 |
| 371 | Bashkir         | Yakut (Sakha)   | ba-sah  |     6450 |   500 |    1035 |     0 |       0 |
| 372 | Tatar           | Gagauz          | tt-gag  |     6441 |   500 |    1067 |     0 |       0 |
| 373 | Gagauz          | Tatar           | gag-tt  |     6441 |   500 |    1067 |     0 |       0 |
| 374 | Gagauz          | Russian         | gag-ru  |     6431 |   500 |    1053 |     0 |       0 |
| 375 | Russian         | Gagauz          | ru-gag  |     6431 |   500 |    1053 |     0 |       0 |
| 376 | Karachay-Balkar | Kirghiz         | krc-ky  |     6418 |   500 |    1041 |     0 |       0 |
| 377 | Kirghiz         | Karachay-Balkar | ky-krc  |     6418 |   500 |    1041 |     0 |       0 |
| 378 | Karakalpak      | Yakut (Sakha)   | kaa-sah |     6398 |   500 |    1030 |     0 |     300 |
| 379 | Yakut (Sakha)   | Karakalpak      | sah-kaa |     6398 |   500 |    1030 |     0 |     300 |
| 380 | Gagauz          | Uighur          | gag-ug  |     6370 |   500 |    1012 |     0 |       0 |
| 381 | Uighur          | Gagauz          | ug-gag  |     6370 |   500 |    1012 |     0 |       0 |
| 382 | Yakut (Sakha)   | Uighur          | sah-ug  |     6315 |   500 |    1012 |     0 |       0 |
| 383 | Uighur          | Yakut (Sakha)   | ug-sah  |     6315 |   500 |    1012 |     0 |       0 |
| 384 | Kumyk           | Gagauz          | kum-gag |     6269 |   500 |    1072 |     0 |       0 |
| 385 | Gagauz          | Kumyk           | gag-kum |     6269 |   500 |    1072 |     0 |       0 |
| 386 | Yakut (Sakha)   | Kirghiz         | sah-ky  |     6261 |   500 |     993 |     0 |     300 |
| 387 | Kirghiz         | Yakut (Sakha)   | ky-sah  |     6261 |   500 |     993 |     0 |     300 |
| 388 | Kumyk           | Yakut (Sakha)   | kum-sah |     6249 |   500 |    1015 |     0 |       0 |
| 389 | Yakut (Sakha)   | Kumyk           | sah-kum |     6249 |   500 |    1015 |     0 |       0 |
| 390 | Gagauz          | Yakut (Sakha)   | gag-sah |     6226 |   500 |    1029 |     0 |       0 |
| 391 | Yakut (Sakha)   | Gagauz          | sah-gag |     6226 |   500 |    1029 |     0 |       0 |
| 392 | Kirghiz         | Gagauz          | ky-gag  |     6130 |   500 |    1039 |     0 |       0 |
| 393 | Gagauz          | Kirghiz         | gag-ky  |     6130 |   500 |    1039 |     0 |       0 |
| 394 | Gagauz          | Kazakh          | gag-kk  |     6063 |   500 |    1022 |     0 |       0 |
| 395 | Kazakh          | Gagauz          | kk-gag  |     6063 |   500 |    1022 |     0 |       0 |
| 396 | Tuvinian        | Altai           | tyv-alt |     3431 |   500 |       0 |     0 |       0 |
| 397 | Altai           | Tuvinian        | alt-tyv |     3431 |   500 |       0 |     0 |       0 |
| 398 | Russian         | Shor            | ru-cjs  |     2317 |     0 |       0 |     0 |       0 |
| 399 | Shor            | Russian         | cjs-ru  |     2317 |     0 |       0 |     0 |       0 |
| 400 | English         | Salar           | en-slr  |      781 |     0 |       0 |     0 |       0 |
| 401 | Salar           | English         | slr-en  |      781 |     0 |       0 |     0 |       0 |
| 402 | Urum            | English         | uum-en  |      493 |     0 |       0 |     0 |       0 |
| 403 | English         | Urum            | en-uum  |      493 |     0 |       0 |     0 |       0 |