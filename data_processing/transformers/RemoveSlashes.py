from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd
import ast


class RemoveSlashes(BaseEstimator, TransformerMixin):
    def fit(self, dataset: pd.DataFrame, y=None):
        return self
    def transform(self, dataset: pd.DataFrame, y=None):
        print('Removing slashes...')

        # Find out which columns of dataframe contain lists
        columns_containing_lists = []
        column_names = dataset.columns
        first_instance = dataset.iloc[0]
        for column_name in column_names:
            first_instance_data_element = first_instance[column_name]
            is_list = type(first_instance_data_element) == list
            if is_list:
                columns_containing_lists.append(column_name)

        # Remove backslashes
        for column_with_lists in columns_containing_lists:
            # convert column with lists to strings
            dataset[column_with_lists] = dataset[column_with_lists].astype(str)
            # in the strings, remove blackslashes by doing literal evaluation, this way convert them back to lists too
            dataset[column_with_lists] = dataset[column_with_lists].apply(ast.literal_eval)


        return dataset

