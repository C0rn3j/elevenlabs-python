# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
from .evaluation_success_result import EvaluationSuccessResult
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import typing
import pydantic


class ConversationHistoryEvaluationCriteriaResultCommonModel(UncheckedBaseModel):
    criteria_id: str
    result: EvaluationSuccessResult
    rationale: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
