from Robot import Robot

class WMS:

    def __init__(self,warehouse):
        self.__warehouse = warehouse

    def calculate_optimal_path(self,list_robots):
        print("Optimal path calculated for all robots")

    def send_path_to_robots(self,list_robots):
        print("Sending calculate optimal path to all robots")
    



#warehouse variable stores the whole warehouse in a form of matrix

warehouse = [['C',0,0,0,0,0,0,0,0,0,'CP2',0,0,0,0,0,0,0,0,0,'C'],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,'S11',0,'S21',0,'S31',0,'S41',0,'S51',0,'S61',0,'S71',0,'S81',0,'S91',0,'S101',0],
                    [0,'S12',0,'S22',0,'S32',0,'S42',0,'S52',0,'S62',0,'S72',0,'S82',0,'S92',0,'S102',0],
                    [0,'S13',0,'S23',0,'S33',0,'S43',0,'S53',0,'S63',0,'S73',0,'S83',0,'S93',0,'S103',0],
                    [0,'S14',0,'S24',0,'S34',0,'S44',0,'S54',0,'S64',0,'S74',0,'S84',0,'S94',0,'S104',0],
                    [0,'S15',0,'S25',0,'S35',0,'S45',0,'S55',0,'S65',0,'S75',0,'S85',0,'S95',0,'S105',0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,'S111',0,'S121',0,'S131',0,'S141',0,'S151',0,'S161',0,'S171',0,'S181',0,'S191',0,'S201',0],
                    [0,'S112',0,'S122',0,'S132',0,'S142',0,'S152',0,'S162',0,'S172',0,'S182',0,'S192',0,'S202',0],
                    [0,'S113',0,'S123',0,'S133',0,'S143',0,'S153',0,'S163',0,'S173',0,'S183',0,'S193',0,'S203',0],
                    [0,'S114',0,'S124',0,'S134',0,'S144',0,'S154',0,'S164',0,'S174',0,'S184',0,'S194',0,'S204',0],
                    [0,'S115',0,'S125',0,'S135',0,'S145',0,'S155',0,'S165',0,'S175',0,'S185',0,'S195',0,'S205',0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    ['C',0,0,0,0,0,0,0,0,0,'CP2',0,0,0,0,0,0,0,0,0,'C']
            ]

list_robots = []
for i in range(0,10):
    r = Robot(i+1)
    list_robots.append(r) 

wms_system = WMS(warehouse)
list_robots[0].route_to_follow([warehouse[0][7],warehouse[1][7],warehouse[1][8],warehouse[2][8],warehouse[3][8],warehouse[4][8]])
Error = False

while(Error != True):
    wms_system.calculate_optimal_path(list_robots)
    wms_system.send_path_to_robots(list_robots)
    list_robots[0].moving_to_destination("fetch")
    list_robots[1].moving_to_destination("deliver")
    
    if(list_robots[0].get_error_msg() == "Package Dropped"):
        print("Stopping all robots")
        print("Raising Alarm")
        Error = True
    





