"""Initial package and fixture smoke tests."""

from pathlib import Path

import change_readiness_agent
from change_readiness_agent.agent import ChangeReadinessOrchestrator
from change_readiness_agent.llm import LLMProvider
from change_readiness_agent.schemas.change_request import ChangeRequest
from change_readiness_agent.tools import AgentTool
from change_readiness_agent.validation import ValidationRule


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def test_package_import() -> None:
    """The installed package and its architectural boundaries are importable."""
    assert change_readiness_agent.__name__ == "change_readiness_agent"
    assert ChangeReadinessOrchestrator.__name__ == "ChangeReadinessOrchestrator"
    assert LLMProvider.__name__ == "LLMProvider"
    assert AgentTool.__name__ == "AgentTool"
    assert ValidationRule.__name__ == "ValidationRule"


def test_example_change_request_matches_schema() -> None:
    """The bundled synthetic example is a valid change request."""
    fixture = PROJECT_ROOT / "data" / "synthetic" / "example_change_request.json"

    change_request = ChangeRequest.model_validate_json(
        fixture.read_text(encoding="utf-8")
    )

    assert change_request.is_synthetic is True
    assert change_request.change_id == "SYN-CR-001"
