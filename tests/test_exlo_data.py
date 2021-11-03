"""Tests for the exlo module."""

# Standard library
from pathlib import Path

# Non standard
import pytest

import exlo_data

basefolder = Path(exlo_data.__file__).parent

def test_exlo():
    """Check that all required files are present."""
    assert (basefolder / 'config.json').exists()
    assert (basefolder / 'users.json').exists()
    assert (basefolder / 'projects.json').exists()
    assert (basefolder / 'equipment.json').exists()
