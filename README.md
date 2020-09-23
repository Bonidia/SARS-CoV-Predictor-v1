# Identifying SARS-CoV-2 Sequences with Machine Learning: SARS-CoV-Predictor

We proposed a novel alignment-free approach based on machine learning to identify SARS-CoV-2 sequences (here called SARS-CoV-Predictor). Our proposal uses mathematical modeling to generate features through Tsallis entropy. Specifically, 12 informative features are extracted based on the combination of different subsequences (k-mer).

## Authors

* Robson Parmezan Bonidia and Anderson Paulo Ávila Santos.

* **Correspondence:** robservidor@gmail.com or bonidia@usp.br


## Publication

If you use this code in a scientific publication, we would appreciate citations to the following paper:

Submitted


## List of files

 - **Examples:** Sequence of Example

 - **README:** Documentation;

 - **Requirements:** List of items to be installed using pip install;

 - **Train:** Training set;

 - **SARS-CoV-Predictor** Main File - Python.


## Dependencies

- Python (>=3.7)
- NumPy 
- Pandas
- Biopython
- Scikit-learn


## Installing our tool

It is important to note that we consider that the Python language is installed. Otherwise, access: https://www.python.org/downloads/release/python-375/.

```sh
$ git clone https://github.com/Bonidia/SARS-CoV-Predictor-v1.git SARS-CoV-Predictor

$ cd SARS-CoV-Predictor

$ pip3 install -r requirements.txt
```

## Usange and Examples


```sh
Access folder: $ cd SARS-CoV-Predictor
 
To run our tool (Example): $ python3.7 SARS-CoV-Predictor.py -t train/train.csv -s example/sequences.fasta -o results.csv

Where:

-h = help

-t = TRAIN - training set (csv format file, E.g., train/train.csv)

-s = SEQUENCES - new sequences (fasta format file, E.g., example/sequences.fasta)

-o = OUTPUT, - CSV format file, E.g., results.csv

This example will generate a csv file with the results.
```

**Note** Input sequences must be in fasta format.

## About

If you use this code in a scientific publication, we would appreciate citations to the following paper:

Submitted
