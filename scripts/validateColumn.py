def validate_columns(data, required_columns):

    missing_columns = [col for col in required_columns if col not in data.columns]
    if missing_columns:
        raise ValueError(f"The dataset is missing the following required columns: {missing_columns}")
