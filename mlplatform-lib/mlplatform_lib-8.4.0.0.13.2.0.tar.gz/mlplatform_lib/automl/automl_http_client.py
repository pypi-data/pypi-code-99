from typing import List

from mlplatform_lib.mlplatform.mlplatform_http_client import (
    MlPlatformHttpClient,
    MlPlatformUserAuth,
    MlPlatformRequestType,
)
from mlplatform_lib.dataclass.model import ModelAutomlDto, ModelAutomlBestDto
from mlplatform_lib.utils.dataclass_utils import from_dict, to_dict

from mlplatform_lib.dataclass.experiment import ExperimentAutomlDto

from mlplatform_lib.dataclass.inference.inference_automl_dto import InferenceAutomlDto


class AutomlHttpClient(MlPlatformHttpClient):
    def __init__(self, mlplatform_addr):
        super().__init__(mlplatform_addr=mlplatform_addr)

    def get_models(self, experiment_id: int, train_id: int, auth: MlPlatformUserAuth) -> List[ModelAutomlDto]:
        res = self.send_request(
            "models",
            {"experiments": experiment_id, "trains": train_id},
            {},
            {},
            auth,
            MlPlatformRequestType.READ,
        )
        model_infos = []
        for model_info in res.data:
            model_infos.append(from_dict(ModelAutomlDto, model_info))
        return model_infos

    def get_experiment(self, experiment_id: int, auth: MlPlatformUserAuth) -> ExperimentAutomlDto:
        result = self.send_request(
            "", {"experiments": experiment_id}, {}, {}, auth, MlPlatformRequestType.READ
        )
        return from_dict(ExperimentAutomlDto, result.data)

    def get_inference(
        self, experiment_id: int, inference_id: int, auth: MlPlatformUserAuth
    ) -> InferenceAutomlDto:
        result = self.send_request(
            "",
            {"experiments": experiment_id, "inferences": inference_id},
            {},
            {},
            auth,
            MlPlatformRequestType.READ,
        )
        return from_dict(InferenceAutomlDto, result.data)

    def update_inference(
        self, experiment_id: int, inference_automl_dto: InferenceAutomlDto, auth: MlPlatformUserAuth,
    ) -> InferenceAutomlDto:
        result = self.send_request(
            "inferences",
            {"experiments": experiment_id},
            {},
            to_dict(inference_automl_dto),
            auth,
            MlPlatformRequestType.UPDATE,
        )
        return from_dict(InferenceAutomlDto, result.data)

    def insert_model(
        self, experiment_id: int, train_id: int, model: ModelAutomlDto, auth: MlPlatformUserAuth
    ) -> ModelAutomlDto:
        res = self.send_request(
            "models",
            {"experiments": experiment_id, "trains": train_id},
            {},
            to_dict(model),
            auth,
            MlPlatformRequestType.CREATE,
        )
        return from_dict(ModelAutomlDto, res.data)

    def insert_model_automl_best(
        self,
        experiment_id: int,
        train_id: int,
        model_automl_best: ModelAutomlBestDto,
        auth: MlPlatformUserAuth,
    ) -> ModelAutomlBestDto:
        result = self.send_request(
            "model-automl-bests",
            {"experiments": experiment_id, "trains": train_id},
            {},
            to_dict(model_automl_best),
            auth,
            MlPlatformRequestType.CREATE,
        )
        return from_dict(ModelAutomlBestDto, result.data)
