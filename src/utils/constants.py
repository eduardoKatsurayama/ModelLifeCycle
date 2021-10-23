TRACKING_URI = f'http://{SERVER_IP}:{SERVER_PORT}'
SERVER = 'mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root gs://bucket_name/artifacts --host 0.0.0.0'# noqa
GAC_MLFLOW = '/path/to/credentials.json'
