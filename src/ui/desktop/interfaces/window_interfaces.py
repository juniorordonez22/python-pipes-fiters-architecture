from abc import ABC, abstractmethod

class BasicWindowActions(ABC):
    @abstractmethod
    def CreateWindowAndWidgets(self):
        pass
    @abstractmethod
    def DisplayWindowAndWidgets(self):
        pass
    @abstractmethod
    def DestroyWindow(self):
        pass