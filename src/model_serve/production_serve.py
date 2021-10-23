import os
from time import sleep

def up_to_production(model_name, port):
    sleep(30)
    get_container_id = f'docker ps -a -q --filter ancestor={model_name}'
    container_id = os.popen(get_container_id).read()[:-1]
    sleep(5)

    build_new_model = f'mlflow models build-docker -m "models:/{model_name}/Production" -n "{model_name}"'# noqa
    os.system(build_new_model)
    sleep(5)

    remove_last_model = f'docker rm $(docker stop {container_id})'
    os.system(remove_last_model)
    sleep(5)

    up_new_model = f'docker run -p {port}:8080 -h 0.0.0.0 --restart unless-stopped -d "{model_name}"'
    os.system(up_new_model)
    sleep(5)

    remove_none_image = 'docker rmi $(docker images --filter "dangling=true" -q --no-trunc)'# noqa
    os.system(remove_none_image)
