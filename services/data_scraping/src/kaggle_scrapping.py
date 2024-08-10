import init.kaggle_init
from kaggle.api.kaggle_api_extended import KaggleApi
import pandas as pd


class KaggleScrapping:
    """
    A class used to interact with Kaggle's API.

    Methods
    -------
    search(dataset_name: str) -> pd.DataFrame:
        Searches Kaggle for datasets matching the provided name and filters them to include only those with .csv files.
    """
    def __init__(self):
        try:
            self.api = KaggleApi()
            self.api.authenticate()
        except NameError:
            print("Can't connect to Kaggle")

    def search(self, dataset_name: str) -> pd.DataFrame:
        """
        Search for dataset on Kaggle with provided dataset name

        :param dataset_name: (str) The name or key word to search on Kaggle
        :return: (pd.DataFrame) A dataframe containing dataset name and files
        """
        dataset_list = self.api.dataset_list(search=dataset_name)
        datasets_with_csv_files = []

        for dataset in dataset_list:
            ds_files = self.api.dataset_list_files(dataset.ref)
            csv_files = [file.name for file in ds_files.files if file.name.endswith('.csv')]

            if csv_files:
                datasets_with_csv_files.append({
                    'dataset_ref': dataset.ref,
                    'files': csv_files
                })

        df_with_csv_files = pd.DataFrame(datasets_with_csv_files)

        return df_with_csv_files

    def download(self, dataset_name: str):
        pass


if __name__ == '__main__':
    scraper = KaggleScrapping()
    print(scraper.search('pokemon'))
