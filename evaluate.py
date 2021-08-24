import argparse
import sys
import os
import json
import sacrebleu

def get_label_filepath(src, tgt, test_set):

    if not os.path.isdir(f"data/{src}-{tgt}/test/{test_set}"):
        os.system(f"python3 download_data.py --source_language={src} --target_language={tgt} --split=test")
    
    assert os.path.isdir(f"data/{src}-{tgt}/test/{test_set}")

    return f"data/{src}-{tgt}/test/{test_set}/{src}-{tgt}/{src}-{tgt}.{tgt}"


def get_sacrebleu(label_filepath, prediction_filepath):

    src = open(prediction_filepath, 'r').readlines()
    label_sentences = open(label_filepath, 'r').readlines()
    refs = []
    for label in label_sentences:
        refs.append(label.split('\t'))
    
    bleu = sacrebleu.corpus_bleu(src, refs)
    return bleu.score


def evaluate(prediction_folder, label_folder, verbose=False):
    language_pairs = next(os.walk(prediction_folder))[1]
    test_labels = next(os.walk(label_folder))[1]

    overall_scores = {}

    for pair in language_pairs:
        src_code = pair.split('-')[0]
        tgt_code = pair.split('-')[1]

        test_sets = next(os.walk(f"{prediction_folder}/{pair}"))[1]
        scores = {}
        for test_set in test_sets:
            filename = os.listdir(f"{prediction_folder}/{pair}/{test_set}")[0]
            prediction_filepath = f"{prediction_folder}/{pair}/{test_set}/{filename}"

            label_filepath = get_labels(src_code, tgt_code, test_set)

            bleu_score = get_sacrebleu(label_filepath, prediction_filepath)
            scores[test_set] = bleu_score
        
        overall_scores[pair] = scores
    
    return overall_scores

            

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--prediction_folder', default=None, type=str, required=True,
    help='the predictions of one model')
  parser.add_argument('--label_folder', default=None, type=str, required=True,
    help='the grouth truth file')
  parser.add_argument('--verbose', action='store_true', default=False,
    help='whether to print details')
  args = parser.parse_args()
  overall_scores = evaluate(args.prediction_folder, args.label_folder, args.verbose)

  print(overall_scores)
  