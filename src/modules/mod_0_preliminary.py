# Imports
import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import seaborn as sns
from cycler import cycler
import itertools
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn import metrics
from sklearn.metrics import make_scorer
from sklearn.model_selection import StratifiedKFold
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import  MinMaxScaler, PolynomialFeatures
from sklearn.compose import ColumnTransformer
from sklearn import set_config
from sklearn.model_selection import train_test_split
import joblib
import graphviz

# Modules
# from mod_1_preprocessing import *
# from mod_3_feature_engineering import *


def package_and_module_imports():
    '''imports all into the kernel'''
    
    # Imports
    import pandas as pd
    import numpy as np
    import statsmodels.formula.api as smf
    import matplotlib.pyplot as plt
    import seaborn as sns
    from cycler import cycler
    import itertools
    from sklearn.linear_model import LogisticRegression
    from sklearn.ensemble import BaggingClassifier
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.ensemble import GradientBoostingClassifier
    from sklearn import metrics
    from sklearn.metrics import make_scorer
    from sklearn.model_selection import StratifiedKFold
    from sklearn.pipeline import Pipeline, FeatureUnion
    from sklearn.base import BaseEstimator, TransformerMixin
    from sklearn.preprocessing import  MinMaxScaler, PolynomialFeatures
    from sklearn.compose import ColumnTransformer
    from sklearn import set_config
    from sklearn.model_selection import train_test_split
    import joblib

    

def data_ingest():
    global delivery_df, delivery_df_raw
    delivery_df = pd.read_csv(r'../data/delivery_2_excel_edits.csv')
    delivery_df_raw = pd.read_csv(r'../data/delivery_2_excel_edits.csv')
    
    return delivery_df