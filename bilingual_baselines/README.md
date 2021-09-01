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


### Install JoeyNMT

```
git clone https://github.com/joeynmt/joeynmt.git
cd joeynmt; pip3 install .
pip install torch==1.8.0+cu101 -f https://download.pytorch.org/whl/torch_stable.html
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

<!-- ### Create a submission to the leaderboard

Once you have your *amazing* model ready, you can create a submission (.zip file) by simply running `create_submission.sh` script along with some parameters:

```
bash create_submission.sh <path_to_joeynmt_config.yaml> <source_language_code> <target_language_code>
# For example:
bash create_submission.sh joeynmt/configs/transformer_uzru.yaml uz ru
```

The script will automatically download the needed test files, load the model specified in the config file, run the test and output the predictions under `\submissions` folder.  -->

