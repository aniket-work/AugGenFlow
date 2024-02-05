"""Module defining the AugGenFlow class."""

from guardrail.guardrail_factory import GuardrailFactory

class AugGenFlow:
    """Class representing the AugGenFlow framework."""

    def __init__(self, config):
        """Initialize AugGenFlow with the specified configuration.

        Args:
            config: Configuration object specifying parameters for AugGenFlow.

        """
        self.guardrail = GuardrailFactory.create_guardrail(config.guardrail_type)

    def run(self, data):
        """Run AugGenFlow tasks and perform guardrail checks on the provided data.

        Args:
            data: Data to be processed by AugGenFlow and checked by the guardrail.

        Returns:
            None

        """
        # Perform other AugGenFlow tasks
        self.guardrail.check(data)
