"""Base contract for future agent tools."""

from typing import Protocol


class AgentTool(Protocol):
    """A named asynchronous tool callable by a future agent loop."""

    name: str
    description: str

    async def run(self, **kwargs: object) -> object:
        """Run the tool with provider-specific arguments."""
        ...
