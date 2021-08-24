#!/bin/bash

mkdir checkpoints
gsutil -m cp gs://til-corpus/large_mnmt/checkpoints/checkpoint_best.pt checkpoints/