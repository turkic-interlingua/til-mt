
import tokenizers

tokenizer = tokenizers.SentencePieceUnigramTokenizer.from_spm("spm/64k_bpe.model")
 
print(tokenizer.tokenize("Salom do'stlar"))
