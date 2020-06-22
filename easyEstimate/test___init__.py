from unittest import TestCase


class TestEstimate(TestCase):
    def test_estimer(self):
        import easyEstimate
        self.assertEqual(easyEstimate.estimer(20, "rue", "alphonse pluchet", 92220, 55, 4, 2, 0), 334181.0)


class TestAlphabetPosition(TestCase):
    def test_alphabet_position2a(self):
        import easyEstimate
        self.assertEqual(easyEstimate.alphabet_position("2A"), 21.0)

    def test_alphabet_position92(self):
        import easyEstimate
        self.assertEqual(easyEstimate.alphabet_position(92), 92)