import pytest
from nanochain.app import App

def test_app_add_and_query():
    app = App()

    # Test add method
    sample_url = "https://arxiv.org/abs/2010.14701"
    app.add(sample_url)

    # Test query method
    query_str = "sample query"
    result = app.query(query_str)
    assert result, "Query result should not be empty"