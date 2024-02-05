"""Module defining the base guardrail abstract class."""

from abc import ABC, abstractmethod

class Guardrail(ABC):
    """Base abstract class for guardrail implementations."""

    @abstractmethod
    def check(self, data):
        """Abstract method to check data against guardrail logic.

        Args:
            data: Data to be checked against the guardrail logic.

        Returns:
            None

        """
        pass
