import json
from pathlib import Path


class Config:
    def __init__(self, config_file=None):
        self.config_file = config_file or Path.home() / ".veilnode" / "config.json"
        self.config_file.parent.mkdir(parents=True, exist_ok=True)
        self.settings = self.load()

    def load(self):
        """Load configuration from file"""
        if self.config_file.exists():
            with open(self.config_file, 'r') as f:
                return json.load(f)
        return self.get_defaults()

    def save(self):
        """Save configuration to file"""
        with open(self.config_file, 'w') as f:
            json.dump(self.settings, f, indent=2)

    def get_defaults(self):
        """Return default configuration"""
        return {
            "port": 8080,
            "tor_port": 9051,
            "log_level": "INFO"
        }

    def get(self, key, default=None):
        """Get configuration value"""
        return self.settings.get(key, default)

    def set(self, key, value):
        """Set configuration value"""
        self.settings[key] = value
        self.save()