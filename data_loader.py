import kagglehub 

def download_dataset():
    path = kagglehub.dataset_download(
        "muhammadehsan02/healthcare-prediction-dataset"
    )
    return path