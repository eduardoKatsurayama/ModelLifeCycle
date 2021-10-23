from mlflow.tracking import MlflowClient
from src.model_serve.production_serve import up_to_production


def set_to_production(current_run, model_name, port):
    client = MlflowClient()
    try:
        register_model(client, current_run, model_name)
    except:
        create_model(client, model_name)
        register_model(client, current_run, model_name)

    new_model_infos = client.search_model_versions(
        f"run_id='{current_run.run_id}'"
    )[0]

    old_model_infos = search_current_production_model(
        client, new_model_infos.name
    )

    if old_model_infos:
        transite_model_stage(client, old_model_infos, stage='Archived')
    
    transite_model_stage(client, new_model_infos, stage='Production')

    up_to_production(model_name, port)


def search_current_production_model(client, model_name):
    for model in client.search_model_versions(f"name='{model_name}'"):
        if model.current_stage == 'Production':
            return model


def transite_model_stage(client, model_infos, stage):
    client.transition_model_version_stage(
        name=model_infos.name,
        version=model_infos.version,
        stage=stage
    )


def create_model(client, model_name):
    client.create_registered_model(model_name)


def register_model(client, current_run, model_name):
    client.create_model_version(
        name=model_name,
        source=f'{current_run.artifact_uri}/{model_name}',
        run_id=current_run.run_id
    )
