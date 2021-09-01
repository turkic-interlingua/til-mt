


## Useful scripts

### Download the TIL Corpus
To get started, download the data for a pair that you are interested
```
python download_data.py --source_language=<language code> --target_language=<language_code> --split=<train,dev,test,all>
```

### Download the monolingual data
You can also download monolingual data for any of the languages in the table below. Monolingual data are crawled from our parallel corpus, Wikipedia dumps, news websites and a few manual crawls whenever possible.

```
python download_monolingual.py --language=<language code>
```