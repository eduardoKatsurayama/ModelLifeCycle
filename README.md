<div style="text-align:center"><img width="100px" src="doc/logo.png" /></div>

# ModelLifeCycle
Structure of a models life cycle manager application based on MLFlow and Docker in Cloud (GCP)


## Requirements:
- Unix System
- Python 3.9.6

## How to start
Clone the repository
```sh
git clone git@github.com:eduardoKatsurayama/ModelLifeCycle.git
```

Update the remote
```sh
git remote set-url origin git@github.com:eduardoKatsurayama/ModelLifeCycle.git
```

Create a branch homolog
```sh
git checkout -b "homolog"
```

Into a virtualenv install the dependencies:
```sh
pip install -r requirements/dev.txt
```

Create the .env based on .env.sample:
```sh
cp contrib/.env.sample .env
```

Set URI:
```sh
export MLFLOW_TRACKING_URI=http://<<SERVER_IP>>:<<SERVER_PORT>>
```

Start the server:
```sh
python -m src.main.py
```

Train a model and send to production:
```sh
mlflow run --experiment-name <<model_name>> ./src/models/<<model_name>>/
```