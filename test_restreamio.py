# test_restreamio.py
"""
Tests for Restreamio module.
"""

import unittest
from restreamio import Restreamio

class TestRestreamio(unittest.TestCase):
    """Test cases for Restreamio class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = Restreamio()
        self.assertIsInstance(instance, Restreamio)
        
    def test_run_method(self):
        """Test the run method."""
        instance = Restreamio()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
