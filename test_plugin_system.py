import pytest
from plugin_system import PluginSystem

def test_plugin_loading():
    ps = PluginSystem()
    ps.load_plugins()
    assert "example_plugin" in ps.plugins

def test_plugin_execution():
    ps = PluginSystem()
    ps.load_plugins()
    result = ps.execute_plugin("example_plugin", 2, 3)
    assert result == 5

def test_nonexistent_plugin():
    ps = PluginSystem()
    ps.load_plugins()
    with pytest.raises(ValueError):
        ps.execute_plugin("nonexistent_plugin")

