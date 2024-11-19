class AppSettings:
    _instance = None  # Single instance

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AppSettings, cls).__new__(cls)
            cls._instance.sorting_preference = "alphabetical"  # Default setting
        return cls._instance

    def set_sorting_preference(self, preference):
        self._instance.sorting_preference = preference

    def get_sorting_preference(self):
        return self._instance.sorting_preference

# Usage
settings1 = AppSettings()
settings2 = AppSettings()
settings1.set_sorting_preference("by date")

print(settings2.get_sorting_preference())  # Output: by date
