from datetime import timedelta


class Master():
    def __init__(self, name, time):
        self.name = name
        self.time = time
        print(f'{self.time}')

    def show_time(self):
        print(f'{self.name} time is {self.time}')

    def TimeSync(self,client):
        MasterTime = timedelta(hours=3, minutes=0, seconds=0)
        avgtime=timedelta(hours=0, minutes=0, seconds=0)
        timeDiff = []
        timeDiff.append(self.time - MasterTime)
        count = 1
        print(f'{self.name} has a differce of {timeDiff[0]}')

        for x in client:
            timeDiff.append(x.time - MasterTime)
            print(f'{x.name} has a differce of {timeDiff[count]}')
            count +=1

        for x in timeDiff:
            avgtime = avgtime + x

        for x in client:
            x.time += (avgtime/3)
            print(f'Updated time of {x.name} is {self.time +avgtime/3}  ')

        print(f'Updated time of {self.name} is {self.time +avgtime/3}')



class Client():
    def __init__(self, name, time):
        self.name = name
        self.time = time

    def show_time(self):
        print(f'{self.name} time is {self.time}')


master1 = Master('Masterserver', timedelta(hours=3, minutes=0, seconds=0))
client_list = [Client('Client1', timedelta(hours=2, minutes=50, seconds=0)),
               Client('Client2', timedelta(hours=3, minutes=25, seconds=0))]
master1.show_time()
for i in client_list:
    i.show_time()

master1.TimeSync(client_list)



