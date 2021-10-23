from sklearn.ensemble import RandomForestRegressor
import mlflow
from mlflow.models.signature import infer_signature
from src.utils.constants import TRACKING_URI, HOUSE_PRICES_PORT_PRODUCTION
from src.tracking.stage import set_to_production


def run(X, y, model_name, to_production=False):
    mlflow.set_tracking_uri(TRACKING_URI)
    mlflow.set_experiment(model_name)

    with mlflow.start_run():
        model = RandomForestRegressor()
        model.fit(X, y)
        signature = infer_signature(X, model.predict(X))
        mlflow.sklearn.log_model(model, model_name, signature=signature)

        current_run = mlflow.active_run().info

    if to_production:
        set_to_production(
            current_run, model_name, HOUSE_PRICES_PORT_PRODUCTION
        )
