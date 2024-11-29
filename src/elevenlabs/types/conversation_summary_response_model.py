# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from .conversation_summary_response_model_status import ConversationSummaryResponseModelStatus
from .evaluation_success_result import EvaluationSuccessResult
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class ConversationSummaryResponseModel(UncheckedBaseModel):
    agent_id: str
    agent_name: typing.Optional[str] = None
    conversation_id: str
    start_time_unix_secs: int
    call_duration_secs: int
    message_count: int
    status: ConversationSummaryResponseModelStatus
    call_successful: EvaluationSuccessResult

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
