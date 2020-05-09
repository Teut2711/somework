from functools import wraps
from decouple import config
from mainapp import models


from abc import ABCMeta
import io
import pickle
import pandas as pd
import sqlite3
import os
import pathlib
from more_itertools.more import split_before
PATH = pathlib.Path(__file__).parent


def get_cols(cols_file):
    with open(cols_file, "rb") as p:
        cols = pickle.load(p)
    return cols


class GetDataFrame:

    @staticmethod
    def read_file_obj(file_obj, cols):
        # from nodeirc by _habnabit
        for chunk in split_before(
            (l.decode().strip() for l in file_obj),
                lambda l: l.startswith('01')):
            if len(chunk) <= 1:
                continue
            yield GetDataFrame.chunk_to_df(chunk, cols)
        # from nodeirc by _habnabit

    @staticmethod
    def chunk_to_df(chunk, cols):
        isin, date = chunk[0].split("##")[1:3]
        chunk = chunk[1:]
        data = [i.split("##")[2:] for i in chunk]

        df = pd.DataFrame(data=data, columns=cols)
        df["ISEN"] = isin
        df["DATE"] = date
        return df


class CleanFuncs:
    @staticmethod
    def dematad_clean(df):
        return df.drop_duplicates(
            subset=["DPID", "CLID"],
            keep='first')

    @staticmethod
    def demathol_clean(df):
        return df.drop_duplicates(
            subset=["DPID", "CLID"],
            keep='first')

class ProcessDf:
        
    def processdematad(self, df, cols_dematad, first_time=True):
        if first_time:
            models.Dematad.bulk_create(df[cols_dematad].to_dict(orient="records"))
        else:
            models.Dematad.bulk_update(df[cols_dematad].to_dict(orient="records"))

    def processdemathol(self, df, cols_demathol, first_time=True):
        if first_time:
            models.Demathol.bulk_create(df[cols_demathol].to_dict(orient="records"))
        else:    
            models.Demathol.bulk_update(df[cols_demathol].to_dict(orient="records"))

def main(file_obj):

    cols_df = get_cols(os.path.join(PATH, 'cols', 'cols.pk'))
    cols_dematad = get_cols(os.path.join(PATH, 'cols', 'dematad.pk'))
    cols_demathol = get_cols(os.path.join(PATH, 'cols', 'demathol.pk'))
    
    
    if models.Dematad.objects.all():
        for df in GetDataFrame.read_file_obj(file_obj, cols_df):
            ProcessDf.processdematad(df, cols_dematad, True)
            ProcessDf.processdemathol(df, cols_demathol, True)

    else:
        for df in GetDataFrame.read_file_obj(file_obj, cols_df):
            ProcessDf.processdematad(df, cols_dematad, False)
            ProcessDf.processdemathol(df, cols_demathol, False)