"""Example test to demonstrate pytest.

Copy this pattern for your own tests!
"""

import pytest
import pandas as pd


@pytest.fixture
def sample_df():
    """Sample DataFrame for testing."""
    return pd.DataFrame({
        'id': [1, 2, 3],
        'name': ['Alice', 'Bob', 'Charlie']
    })


def test_example_len(sample_df):
    """Example test - shows pytest working."""
    assert len(sample_df) == 3
    assert 'id' in sample_df.columns
    assert sample_df['id'].is_unique

def test_example_id(sample_df):
    """Example test - shows pytest working."""
    assert len(sample_df) == 3
    assert 'id' in sample_df.columns
    assert sample_df['id'].is_unique

def test_example_unique(sample_df):
    """Example test - shows pytest working."""
    assert len(sample_df) == 3
    assert 'id' in sample_df.columns
    assert sample_df['id'].is_unique

@pytest.mark.skip(reason="not implemented yet")
def test_example_skip(sample_df):
    """Example test - shows pytest working."""
    assert len(sample_df) == 3
    assert 'id' in sample_df.columns
    assert sample_df['id'].is_unique

@pytest.mark.skip(reason="Will Always Fail")
def test_example_fail(sample_df):
    """Example test - shows pytest working."""
    assert len(sample_df) == 33
    assert 'id' in sample_df.columns
    assert sample_df['id'].is_unique