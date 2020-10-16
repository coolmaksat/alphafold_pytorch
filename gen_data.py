#!/usr/bin/env python

import click as ck
import numpy as np
import pandas as pd
import gzip
import os

import logging

logging.basicConfig(level=logging.INFO)

@ck.command()
@ck.option(
    '--data-file', '-df', default='data/swissprot_exp.pkl',
    help='Pandas dataframe with protein sequences')
def main(data_file):
    # Load interpro data
    df = pd.read_pickle(data_file)
    cnt = {}
    lf = open('swissprot/proteins.list', 'w')
    for row in df.itertuples():
        p = row.proteins
        lf.write(p + '\n')
        out_path = f'swissprot/{p[0]}/{p[1]}/{p}/'
        if not os.path.exists(out_path):
            os.makedirs(out_path)
        out_file = out_path + p + '.seq'
        with open(out_file, 'w') as f:
            f.write('>' + row.proteins + '\n')
            f.write(row.sequences + '\n')
    lf.close()


if __name__ == '__main__':
    main()
