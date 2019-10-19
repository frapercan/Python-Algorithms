def label(dataframe,transforms,parameters):
    labels = ['_'+transform+str(parameter) if parameter else '_'+transform for transform,parameter in zip(transforms,parameters)]
    new_columns = [column+label for column,label in zip(dataframe.columns,labels)]
    return new_columns
