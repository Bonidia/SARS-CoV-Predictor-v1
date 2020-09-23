#######################################
#######################################
# -*- coding: utf-8 -*-
#######################################
#######################################

import pandas as pd
import warnings
import numpy as np
import argparse
import sys
import os
from datetime import datetime, timedelta
warnings.filterwarnings("ignore")
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import MinMaxScaler


def save_results(foutput, name_seq, preds):
  file = open(foutput, 'a')
  file.write("Sequence,Label")
  file.write("\n")
  for i in range(len(preds)):
    file.write("%s," % (name_seq[i]))
    file.write("%s" % ("SARS-CoV-2" if preds[i] == 1 else "Other"))
    file.write("\n")
  return


def evaluate_model(ftrain, finput, foutput):
  df = pd.read_csv(ftrain)	
  train = df[df.columns[1:(len(df.columns) - 1)]]
  train_labels = df['label']
  #################################################
  df_test = pd.read_csv(finput)	
  name_seq = df_test['nameseq']
  test = df_test[df_test.columns[1:(len(df_test.columns) - 1)]]
  #################################################
  sc = MinMaxScaler()
  train = sc.fit_transform(train)
  test = sc.transform(test)
  #################################################
  clf = RandomForestClassifier(random_state=63, n_estimators=100)
  model = clf.fit(train, train_labels)
  preds = clf.predict(test)
  save_results(foutput, name_seq, preds)
  return


if __name__ == "__main__":
  print("\n")
  print("###################################################################################")
  print("##########               Author: Robson Parmezan Bonidia                ###########")
  print("###################################################################################")
  print("\n")
  parser = argparse.ArgumentParser()
  parser.add_argument('-t', '--train', help='csv format file, E.g., train.csv')
  parser.add_argument('-s', '--sequences', help='fasta format file, E.g., sequences.fasta')
  parser.add_argument('-o', '--output', help='CSV format file, E.g., results.csv')
  args = parser.parse_args()
  ftrain = str(args.train)
  finput = str(args.sequences)
  foutput = str(args.output)
  print("Extracting Features......")
  out = "features-" + (datetime.now() + timedelta(hours=9)).strftime('%H:%M:%S')
  os.system("python3.7 featureExtraction/TsallisEntropy.py -i " + finput + " -o " + out + " -l ? -k 12 -q 6.0")
  print("\n")
  print("###################################################################################")
  print("##########               Classifying sequences....                     ###########")
  print("###################################################################################")
  print("\n")
  evaluate_model(ftrain, out, foutput)
  print("Finished")