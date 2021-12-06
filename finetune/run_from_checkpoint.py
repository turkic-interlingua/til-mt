from fairseq.models.transformer import TransformerModel

model = TransformerModel.from_pretrained(
  './checkpoints/',
  checkpoint_file='checkpoint_best.pt',
  data_name_or_path='data-bin/',
  bpe='sentencepiece',
  sentencepiece_model='spm/64k_bpe.model'
)

model.translate('<2en> Assalomu aleykum! Bu chatga xush kelibsiz!')