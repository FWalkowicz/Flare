import os
import init.kaggle_init
from kaggle.api.kaggle_api_extended import KaggleApi
import pandas as pd


class KaggleScrapping:
    """
    A class used to interact with Kaggle's API for searching and downloading datasets, and processing them.

    Methods
    -------
    search(dataset_name: str) -> pd.DataFrame:
        Searches Kaggle for datasets matching the provided name and filters them to include only those with .csv files.

    download(dataset_name: str, file_name: str) -> pd.DataFrame:
        Downloads a specified CSV file from a Kaggle dataset and processes it by removing rows with missing values.

    cut(data: pd.DataFrame, indexes_to_drop: list) -> pd.DataFrame:
        Drops specified columns from a DataFrame by their index positions.
    """

    def __init__(self):
        """
        Initializes the KaggleScrapping class by setting up a connection to the Kaggle API.

        This constructor attempts to authenticate with the Kaggle API using the credentials
        set up in the environment. If authentication fails, a NameError is caught, and a message is printed.
        """
        try:
            self.api = KaggleApi()
            self.api.authenticate()
        except NameError:
            print("Can't connect to Kaggle")

    def search(self, dataset_name: str) -> pd.DataFrame:
        """
        Searches for datasets on Kaggle that match the provided dataset name or keyword.

        This method retrieves a list of datasets matching the search criteria and filters
        them to include only those datasets that contain .csv files. The results are returned
        in a pandas DataFrame.

        :param dataset_name: str
            The name or keyword to search for on Kaggle.
        :return: pd.DataFrame
            A DataFrame containing the dataset reference, subtitle, and a list of .csv files available in each dataset.
        """
        dataset_list = self.api.dataset_list(search=dataset_name)
        datasets_with_csv_files = []

        for dataset in dataset_list:
            ds_files = self.api.dataset_list_files(dataset.ref)
            csv_files = [file.name for file in ds_files.files if file.name.endswith('.csv')]

            if csv_files:
                datasets_with_csv_files.append({
                    'dataset_ref': dataset.ref,
                    'dataset_subtitle': dataset.subtitle,
                    'files': csv_files
                })

        df_with_csv_files = pd.DataFrame(datasets_with_csv_files)

        return df_with_csv_files

    def download(self, dataset_name: str, file_name: str) -> pd.DataFrame:
        """
        Downloads a specific CSV file from a Kaggle dataset, saves it locally, and processes it by removing any rows with missing values.

        The file is downloaded to a 'utils' directory, renamed to 'dataset.csv', and then loaded into a pandas DataFrame.
        The DataFrame is cleaned by removing any rows that contain missing values.

        :param dataset_name: str
            The reference name of the dataset on Kaggle.
        :param file_name: str
            The name of the CSV file within the dataset to download.
        :return: pd.DataFrame
            A cleaned pandas DataFrame containing the data from the downloaded CSV file.
        """
        self.api.dataset_download_file(dataset_name, file_name, path='./utils')
        os.rename('./utils/' + file_name, './utils/dataset.csv')
        dataset = pd.read_csv('./utils/dataset.csv').dropna()
        return dataset

    @staticmethod
    def cut(data: pd.DataFrame, indexes_to_drop: list) -> pd.DataFrame:
        """
        Removes specified columns from the given DataFrame based on column index positions.

        :param data: pd.DataFrame
            The DataFrame from which columns will be removed.
        :param indexes_to_drop: list
            A list of column index positions to drop from the DataFrame.
        :return: pd.DataFrame
            A DataFrame with the specified columns removed.
        """
        dataset = data.drop(data.columns[indexes_to_drop], axis=1)
        return dataset
