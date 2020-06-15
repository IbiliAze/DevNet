import os
import sys

class Observer():
    def update(self, subject):
        print("Observer: my subject just updated and told me")
        print(f"Observer: it's state is now {str(subject._state)}")

class Subject():

    _state = ''
    _observers = []

    #### Subscribing Observers####
    def attach(self, observer):
        self._observers.append(observer)
    #### Unsubscribing Observers####
    def detach(self, observer):
        self._observers.remove(observer)



    def notify(self):

        print("notifying the observer")

        for observer in self._observers:
            observer.update(self)



    def updateState(self, n):

        print("received an update")

        self._state = n

        self.notify()

s = Subject()

observer1 = Observer()
observer2 = Observer()
observer3 = Observer()

s.attach(observer1)
s.attach(observer2)
s.attach(observer3)

s.updateState(7)



print(s)