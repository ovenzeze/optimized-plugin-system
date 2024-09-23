import importlib
import os
import asyncio

class PluginSystem:
    def __init__(self, plugin_dir='plugins'):
        self.plugin_dir = plugin_dir
        self.plugins = {}

    def load_plugins(self):
        for filename in os.listdir(self.plugin_dir):
            if filename.endswith('.py') and not filename.startswith('__'):
                module_name = filename[:-3]
                module_path = f"{self.plugin_dir}.{module_name}"
                module = importlib.import_module(module_path)
                
                if hasattr(module, 'register'):
                    plugin_name = module.register()
                    self.plugins[plugin_name] = module

    async def execute_plugin(self, plugin_name, *args, **kwargs):
        if plugin_name in self.plugins:
            plugin = self.plugins[plugin_name]
            if asyncio.iscoroutinefunction(plugin.run):
                return await plugin.run(*args, **kwargs)
            else:
                return plugin.run(*args, **kwargs)
        else:
            raise ValueError(f"Plugin {plugin_name} not found")

