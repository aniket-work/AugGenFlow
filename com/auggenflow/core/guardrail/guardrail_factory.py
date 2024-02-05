"""Module for creating guardrail instances."""

from guardrail_impl import NemoGuardrail, GuardrailAIGuardrail

class GuardrailFactory:
    """Factory class for creating guardrail instances."""
    
    @staticmethod
    def create_guardrail(guardrail_type: str):
        """Create a guardrail instance based on the specified type.

        Args:
            guardrail_type (str): The type of guardrail to create.

        Returns:
            Guardrail: An instance of the specified guardrail type.

        Raises:
            ValueError: If the specified guardrail type is not supported.
        """
        if guardrail_type == 'Nemo':
            return NemoGuardrail()
        elif guardrail_type == 'GuardrailAI':
            return GuardrailAIGuardrail()
        else:
            raise ValueError("Unsupported guardrail type")
