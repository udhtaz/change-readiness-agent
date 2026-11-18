"""Contract for future deterministic validation rules."""

from typing import Protocol, Sequence

from change_readiness_agent.schemas import ChangeRequest


class ValidationRule(Protocol):
    """Validate a change request without assigning a readiness score."""

    name: str

    def validate(self, change_request: ChangeRequest) -> Sequence[str]:
        """Return human-readable findings for the supplied request."""
        ...
