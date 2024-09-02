from sdv.single_table import GaussianCopulaSynthesizer
import pandas as pd
from sdv.datasets.demo import download_demo
from sdv.metadata import SingleTableMetadata
from sdv.evaluation.single_table import evaluate_quality
from sdv.single_table import CTGANSynthesizer
from sdv.lite import SingleTablePreset



class SDVHandler:
    def __init__(self):
        self.df = pd.read_csv("../data/uploaded_data.csv")
        self.metadata = SingleTableMetadata()
        self.metadata_dict = self.generate_metadata_from_dataframe()
        self.metadata_dict = self.metadata.load_from_dict(self.metadata_dict)
        
    def generate_metadata_from_dataframe(self) -> dict:
        metadata = {"columns": {}}

        for column in self.df.columns:
            dtype = self.df[column].dtype
            column_metadata = {}

            if pd.api.types.is_numeric_dtype(dtype):
                column_metadata["sdtype"] = "numerical"
                if pd.api.types.is_integer_dtype(dtype):
                    column_metadata["computer_representation"] = "Int64"
                elif pd.api.types.is_float_dtype(dtype):
                    column_metadata["computer_representation"] = "Float64"
            elif pd.api.types.is_categorical_dtype(self.df[column]) or self.df[column].dtype == object:
                column_metadata["sdtype"] = "categorical"
            elif pd.api.types.is_bool_dtype(dtype):
                column_metadata["sdtype"] = "boolean"
            elif pd.api.types.is_datetime64_any_dtype(dtype):
                column_metadata["sdtype"] = "datetime"
                column_metadata["datetime_format"] = "%Y-%m-%d %H:%M:%S"  
            else:
                column_metadata["sdtype"] = "unknown"

            metadata["columns"][column] = column_metadata

        return metadata

    def generate_guassian(self, num_rows=500):
        
        synthesizer = GaussianCopulaSynthesizer(self.metadata_dict)
        synthesizer.fit(self.df)        
        synthetic_data = synthesizer.sample(num_rows)
        return synthetic_data

    def generate_ctgan(self, num_rows=500):
        synthesizer = CTGANSynthesizer(self.metadata_dict)
        synthesizer.fit(self.df)
        synthetic_data = synthesizer.sample(num_rows)
        return synthetic_data
    


    def generate_quality_report(self, synthetic_data):
        quality_report = evaluate_quality(
        self.df,
        synthetic_data,
        self.metadata_dict)
        score = quality_report.get_score()
        return score

    def generate_single_table_preset(self, num_rows=500):
        synthesizer = SingleTablePreset(
        self.metadata_dict,
        name='FAST_ML')
        synthesizer.fit(
            data=self.df)
        synthetic_data = synthesizer.sample(
            num_rows=num_rows)

        return synthetic_data
    
    def generate_data(self, num_rows=500, model_type="Gaussian"):
        if model_type == "Gaussian":
            return self.generate_guassian(num_rows)
        elif model_type == "CTGAN":
            return self.generate_ctgan(num_rows)
        elif model_type == "FAST_ML":
            return self.generate_single_table_preset(num_rows)