from animate_graphs import filter_dataframe_by_year
import pandas as pd
import logging

log = logging.getLogger()
log.setLevel(logging.INFO)

def test_filter_dataframe_by_year():
    df = pd.read_csv("test_data.csv")
    df_2010 = pd.read_csv("test_data_2010.csv").head().reset_index(drop=True)
    year = 2010
    test_filtered_data = filter_dataframe_by_year(df, year).head().reset_index(drop=True)

    assert test_filtered_data.to_dict() == df_2010.to_dict()
