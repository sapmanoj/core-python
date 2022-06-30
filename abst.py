from abc   import  ABC,abstractmethod
class Computer(ABC):
    @abstractmethod
    def  process(self):
        pass
class laptop(Computer):
    def process(self):
        print('this is process')
x=laptop()
x.process()