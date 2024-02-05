from auggenflow.core.guardrail.guardrail_impl import NemoGuardrail, GuardrailAIGuardrail

import unittest

class TestNemoGuardrail(unittest.TestCase):
    def test_check(self):
        nemo_guardrail = NemoGuardrail()
        # Assume data is provided for testing
        data = ...
        result = nemo_guardrail.check(data)
        # Assert the result based on expected behavior
        self.assertTrue(result, "NemoGuardrail check should return True for valid data")

class TestGuardrailAIGuardrail(unittest.TestCase):
    def test_check(self):
        guardrailai_guardrail = GuardrailAIGuardrail()
        # Assume data is provided for testing
        data = ...
        result = guardrailai_guardrail.check(data)
        # Assert the result based on expected behavior
        self.assertTrue(result, "GuardrailAIGuardrail check should return True for valid data")

if __name__ == '__main__':
    unittest.main()
