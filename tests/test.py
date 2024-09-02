from sdv.single_table import GaussianCopulaSynthesizer
import pandas as pd
from sdv.datasets.demo import download_demo
from sdv.metadata import SingleTableMetadata


# real_data, metadata = download_demo(
#     modality='single_table',
#     dataset_name='fake_hotel_guests'
# )

df = pd.read_csv("../data/used_cars.csv")
metadata = SingleTableMetadata()
metadata.detect_from_dataframe(df)
print(metadata)
# df = pd.read_csv("../data/engine_data.csv")
# metadata = SingleTableMetadata()

# metadata.detect_from_dataframe(df)
# print(metadata)

# synthesizer = GaussianCopulaSynthesizer(metadata)
# synthesizer.fit(df)


# synthetic_data = synthesizer.sample(num_rows=500)
# print(synthetic_data.head())

# from sdv.evaluation.single_table import evaluate_quality

# quality_report = evaluate_quality(
#     df,
#     synthetic_data,
#     metadata
# )

# print(quality_report)



# Define the metadata using a dictionary
# metadata_dict = {
#     "columns": {
#         "Engine rpm": {
#             "sdtype": "numerical",
#             "computer_representation": "Int64"
#         },
#         "Lub oil pressure": {
#             "sdtype": "numerical",
#             "computer_representation": "Float64"
#         },
#         "Fuel pressure": {
#             "sdtype": "numerical",
#             "computer_representation": "Float64"
#         },
#         "Coolant pressure": {
#             "sdtype": "numerical",
#             "computer_representation": "Float64"
#         },
#         "lub oil temp": {
#             "sdtype": "numerical",
#             "computer_representation": "Float64"
#         },
#         "Coolant temp": {
#             "sdtype": "numerical",
#             "computer_representation": "Float64"
#         },
#         "Engine Condition": {
#             "sdtype": "categorical"
#         }
#     },
# }


# def generate_metadata_from_dataframe(df: pd.DataFrame) -> dict:
    
#     metadata = {"columns": {}}

#     for column in df.columns:
#         dtype = df[column].dtype
#         column_metadata = {}

#         if pd.api.types.is_numeric_dtype(dtype):
#             column_metadata["sdtype"] = "numerical"
#             if pd.api.types.is_integer_dtype(dtype):
#                 column_metadata["computer_representation"] = "Int64"
#             elif pd.api.types.is_float_dtype(dtype):
#                 column_metadata["computer_representation"] = "Float64"
#         elif pd.api.types.is_categorical_dtype(df[column]) or df[column].dtype == object:
#             column_metadata["sdtype"] = "categorical"
#         elif pd.api.types.is_bool_dtype(dtype):
#             column_metadata["sdtype"] = "boolean"
#         elif pd.api.types.is_datetime64_any_dtype(dtype):
#             column_metadata["sdtype"] = "datetime"
#             column_metadata["datetime_format"] = "%Y-%m-%d %H:%M:%S"  
#         else:
#             column_metadata["sdtype"] = "unknown"

#         metadata["columns"][column] = column_metadata

#     return metadata


# test = generate_metadata_from_dataframe(df)
# print(test)
# Create a SingleTableMetadata object
# metadata = SingleTableMetadata()
# test_data = metadata.detect_from_dataframe(df)
# print("test_Data ", test_data)

#test_data_1 = metadata.detect_from_csv("../data/engine_data.csv")
#print(test_data_1)
# Update the metadata with the dictionary
# metadata_dict = metadata.load_from_dict(test)
# print(type(metadata_dict))
# Convert the dictionary to a SingleTableMetadata object







# from sdv.single_table import CTGANSynthesizer

# synthesizer = CTGANSynthesizer(metadata_dict)
# synthesizer.fit(df)

# synthetic_data = synthesizer.sample(num_rows=500)
# # print(synthetic_data.head())

# quality_report = evaluate_quality(
#     df,
#     synthetic_data,
#     metadata_dict
# )

# print(quality_report)


# from sdv.lite import SingleTablePreset

# synthesizer = SingleTablePreset(
#     metadata_dict,
#     name='FAST_ML'
# )


# synthesizer.fit(
#     data=df
# )

# synthetic_data = synthesizer.sample(
#     num_rows=500
# )

# print(synthetic_data.head())

# quality_report = evaluate_quality(
#     df,
#     synthetic_data,
#     metadata_dict
# )

# print(quality_report)