"""Composition boundary for future change-readiness orchestration."""

from dataclasses import dataclass, field

from change_readiness_agent.llm import LLMProvider
from change_readiness_agent.validation import ValidationRule


@dataclass(slots=True)
class ChangeReadinessOrchestrator:
    """Hold replaceable dependencies until orchestration is implemented."""

    llm_provider: LLMProvider
    validation_rules: tuple[ValidationRule, ...] = field(default_factory=tuple)
