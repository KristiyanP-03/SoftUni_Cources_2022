from abc import ABC, abstractmethod


class BaseWorker(ABC):
    @abstractmethod
    def work(self):
        pass

class Worker(BaseWorker):
    def work(self):
        print("I'm working!!")

class SuperWorker(BaseWorker):
    def work(self):
        print("I work very hard!!!")

class BadWorker(BaseWorker):
    def work(self):
        print("I don't use the company car to do burnouts in the parking lot, noooo ...")




class Manager(BaseWorker):

    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        assert isinstance(worker, BaseWorker), '`worker` must be of type {}'.format(Worker)

        self.worker = worker

    def manage(self):
        if self.worker is not None:
            self.worker.work()

    def work(self):
        print("Going throughout papers...")








worker = Worker()
manager = Manager()
manager.set_worker(worker)
manager.manage()

super_worker = SuperWorker()
manager.set_worker(super_worker)
manager.manage()

bad_worker = BadWorker()
manager.set_worker(bad_worker)
manager.manage()