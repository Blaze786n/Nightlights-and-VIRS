import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Load your data
data = pd.read_csv('processed2.csv')

# Define preprocessing for numerical and categorical data
numeric_features = ['slope_2012_2013', 'slope_2013_2014', 'slope_2014_2015', 'slope_2015_2016', 
                    'slope_2016_2017', 'slope_2017_2018', 'slope_2018_2019', 'slope_2019_2020', 'slope_2020_2021']
categorical_features = ['state_name', 'district_name', 'subdistrict_name', 'town_name', 'village_name', 'place_name', 'category']

# Create a column transformer
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numeric_features),
        ('cat', OneHotEncoder(), categorical_features)])

# Apply preprocessing
data_preprocessed = preprocessor.fit_transform(data)
