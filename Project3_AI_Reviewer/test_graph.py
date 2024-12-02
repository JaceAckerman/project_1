import pytest
from graph import Graph
import numpy as np

# Test initialization
def test_initialization():
    graph = Graph()
    assert graph.products == ['Series 5', 'Series 6', 'Series 7', 'Series 8', 'Series 9']
    assert graph.positives == []
    assert graph.negatives == []
    assert graph.neutrals == []
    assert graph.barWidth == 0.25
    assert graph.x == []

# Test setting x values
def test_set_x_values():
    graph = Graph()
    graph.setXValues()
    expected_x = np.arange(len(graph.products))
    assert np.array_equal(graph.x, expected_x)

# Test setting bar width
def test_set_bar_width():
    graph = Graph()
    graph.setBarWidth(0.5)
    assert graph.barWidth == 0.5

# Test setting data and creating bar positions
def test_plot_data_preparation():
    graph = Graph()
    graph.positives = [10, 20, 15, 25, 30]
    graph.negatives = [5, 10, 5, 10, 5]
    graph.neutrals = [3, 5, 2, 4, 6]
    graph.setXValues()
    assert len(graph.positives) == len(graph.products)
    assert len(graph.negatives) == len(graph.products)
    assert len(graph.neutrals) == len(graph.products)

# Test plot creation (mocked)
def test_make_plot(monkeypatch):
    graph = Graph()
    graph.positives = [10, 20, 15, 25, 30]
    graph.negatives = [5, 10, 5, 10, 5]
    graph.neutrals = [3, 5, 2, 4, 6]
    
    # Mock plt.show() to prevent the actual display of the plot
    def mock_show():
        pass

    monkeypatch.setattr("matplotlib.pyplot.show", mock_show)

    graph.makePlot('Apple Watch Versions', 'Number of Reviews', 'Sentiment Analysis of Apple Watches')
    graph.displayPlot()  # Should not raise any errors

# Run tests using pytest
if __name__ == "__main__":
    pytest.main()