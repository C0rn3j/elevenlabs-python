# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from .conversation_history_evaluation_criteria_result_common_model import (
    ConversationHistoryEvaluationCriteriaResultCommonModel,
)
from .data_collection_result_common_model import DataCollectionResultCommonModel
from .evaluation_success_result import EvaluationSuccessResult
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class ConversationHistoryAnalysisCommonModel(UncheckedBaseModel):
    evaluation_criteria_results: typing.Optional[
        typing.Dict[str, ConversationHistoryEvaluationCriteriaResultCommonModel]
    ] = None
    data_collection_results: typing.Optional[typing.Dict[str, DataCollectionResultCommonModel]] = None
    call_successful: EvaluationSuccessResult
    transcript_summary: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
