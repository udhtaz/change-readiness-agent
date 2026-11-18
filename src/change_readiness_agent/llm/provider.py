"""Provider-neutral language-model contract."""

from typing import Protocol


class LLMProvider(Protocol):
    """Contract implemented by future MLX, Ollama, vLLM, or hosted providers."""

    async def generate(
        self,
        prompt: str,
        *,
        temperature: float = 0.1,
        max_tokens: int = 2_048,
    ) -> str:
        """Generate text for a prompt."""
        ...
