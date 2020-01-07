class Robot:

    def __init__(self, id):
        self.__id = id  #denotes robot's id
        self.__wt_sensor = False #denotes status of weight sensor 0(False) or 1(True)
        self.__battery_level = 100 #Default battery level while initialization
        self.__arm_status = "Retracted" #status of the arm Retracted/Extended
        self.__rfid_reader = None #Value read using RFID
        self.__grip_status = True #denotes the hand status, True when hand is closed and False when hand is open
        self.__route = [] #Path each robot needs to follow, sequence of X,Y coordinates
        self.__error_status = False
        self.__radar_status = False
        self.__error_msg = ""
    
    def get_robot_id(self):
        return self.__id

    def get_battery_level(self):
        return self.__battery_level

    def get_wt_sensor(self):
        return self.__wt_sensor
    
    def get_arm_status(self):
        return self.__arm_status
    
    def get_rfid_reader(self):
        return self.__rfid_reader
    
    def get_grip_status(self):
        return self.__grip_status
    
    def get_error_status(self):
        return self.__error_status
    
    def get_radar_status(self):
        return self.__radar_status

    def get_error_msg(self):
        return self.__error_msg
    
    def set_error_msg(self,msg):
        self.__error_msg = msg
    
    def set_error_status(self,error_val):
        self.__error_status = error_val
    
    def set_grip_status(self,grip):
        self.__grip_status = grip
    
    def set_wt_sensor(self,wt):
        self.__wt_sensor = wt
    
    def set_rfid_reader(self,rfid_value):
        self.__rfid_reader = rfid_value
    
    def route_to_follow(self,route_received):
        self.__route = route_received
    
    def extend_arm(self):
        self.__arm_status = "Extended"
        return self.__arm_status
    
    def battery_level_to_distance(self):
        possible_distance = self.__battery_level
        return possible_distance
    
    def reroute_safe_position(self):
        print("Moving robot " + self.__id +"to safe position")
    
    def moving_to_destination(self,mode):
        '''Function handles all routing in robots'''
        
        print("Path Received")
        if(mode == "deliver"):
            if(self.__wt_sensor ==  True and self.battery_level_to_distance() > len(self.__route)):
                if(self.__radar_status):
                    print("Obstacle detected...Rerouting")
                    self.reroute_safe_position()
                elif(self.battery_level_to_distance() < len(self.__route)):
                    print("Reroute not possible, not enough battery")
                    print("Notifying to WMS")
                    print("Moving to charging station")
                else:
                    print("Notifying reroute error to WMS")
                    print("Waiting for new route")
                    print("New route recieved")
            elif(self.__wt_sensor ==  False):
                print("Package dropped or no package")
                print("Notifying WMS")
                self.__error_msg = "Package Dropped"
            elif(self.battery_level_to_distance() < len(self.__route)):
                print("Not enough battery")
                print("Moving to charging station")
            else:
                print("Delivery Successful")
                self.__battery_level = self.__battery_level - self.__route
        if(mode == "fetch"):
            if(self.__wt_sensor ==  False and self.battery_level_to_distance() > len(self.__route)):
                if(self.__radar_status):
                    print("Obstacle detected...Rerouting")
                    self.reroute_safe_position()
                elif(self.battery_level_to_distance() < len(self.__route)):
                    print("Reroute not possible, not enough battery")
                    print("Notifying to WMS")
                    print("Moving to charging station")
                else:
                    print("Notifying reroute error to WMS")
                    print("Waiting for new route")
                    print("New route recieved")
            elif(self.__wt_sensor ==  True):
                print("All ready carrying a package")
                print("Notifying WMS")
                self.set_error_msg("Carrying a package")
            elif(self.battery_level_to_distance() < len(self.__route)):
                print("Not enough battery")
                print("Moving to charging station")
            else:
                print("Fetch Successful")
                
                    

    




