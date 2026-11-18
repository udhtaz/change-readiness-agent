"""Schema for a synthetic infrastructure change request."""

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


class ChangeRequest(BaseModel):
    """Input data for a future readiness assessment."""

    model_config = ConfigDict(extra="forbid")

    is_synthetic: Literal[True] = True
    change_id: str = Field(min_length=1)
    title: str = Field(min_length=1)
    summary: str = Field(min_length=1)
    environment: str = Field(min_length=1)
    change_type: str = Field(min_length=1)
    approval_evidence: list[str] = Field(default_factory=list)
    deployment_steps: list[str] = Field(default_factory=list)
    rollback_steps: list[str] = Field(default_factory=list)
    testing_evidence: list[str] = Field(default_factory=list)
    monitoring_checks: list[str] = Field(default_factory=list)
