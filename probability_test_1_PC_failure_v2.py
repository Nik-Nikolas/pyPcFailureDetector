import random

rounds = 100000

class Device():    
    def __init__(self, isFailureHappened = False, isFailureFound = False):
        self.isFailureHappened = isFailureHappened
        self.isFailureFound = isFailureFound
        
    def checkStatus(self):
        return self.isFailureFound


    def useDevice(self):
        raise NotImplementedError("Subclass must implement abstract method")   



class ArithmeticDevice(Device):    
    def __init__(self):
        super().__init__()
        
        self.__failureHappenedProbability = 10.0
        self.__failureFoundProbability    = 80.0

        
    def useDevice(self):
        # Reset flags
        self.isFailureHappened = False
        self.isFailureFound = False
        
        # useRamDeviceHardware       
        __failureHappened = random.uniform(0.0, 100.0)
        
        if(__failureHappened < self.__failureHappenedProbability):
            self.isFailureHappened = True
        

        if (self.isFailureHappened == True):
            __failureFound = random.uniform(0.0, 100.0)
            if(__failureFound < self.__failureFoundProbability):
                self.isFailureFound = True



class RamDevice(Device):    
    def __init__(self):
        super().__init__()
        
        self.__failureHappenedProbabilityHardware      = 39.0
        self.__failureFoundProbabilityHardware         = 10.0
        
        self.__failureHappenedProbabilityLogic         = 20.0
        self.__failureFoundProbabilityLogic            = 5.0
        
        self.__failureHappenedProbabilityFactoryDefect = 1.0
        self.__failureFoundProbabilityFactoryDefect    = 70.0
        
    def useDevice(self):
        # Reset flags
        self.isFailureHappened = False
        self.isFailureFound = False

        # Use sub devices (sequence here mean parallel work because
        # methods (which emulate sub devices work) do not interfere each other work
        # and only emulate failure appearance event)
        self.__useRamDeviceHardware()
        self.__useRamDeviceLogic()
        self.__useRamDeviceHardwareFactoryDefect()

        # If failure happened at least once - emulate failure detection event:
        # if at least one failure was detected - this fact will enable flag isFailureFound
        if (self.isFailureHappened == True):        
            self.__checkRamDeviceHardware()
            self.__checkRamDeviceLogic()
            self.__checkRamDeviceHardwareFactoryDefect()

    # Use methods
    def __useRamDeviceHardware(self):       
        __failureHappened = random.uniform(0.0, 100.0)
        
        if(__failureHappened < self.__failureHappenedProbabilityHardware):
            self.isFailureHappened = True

    
    def __useRamDeviceLogic(self):        
        __failureHappened = random.uniform(0.0, 100.0)        
        if(__failureHappened < self.__failureHappenedProbabilityLogic):            
            self.isFailureHappened = True


    def __useRamDeviceHardwareFactoryDefect(self):        
        __failureHappened = random.uniform(0.0, 100.0)        
        if(__failureHappened < self.__failureHappenedProbabilityFactoryDefect):
            self.isFailureHappened = True

       
    def __checkRamDeviceHardware(self):
        __failureFound = random.uniform(0.0, 100.0)
        if(__failureFound < self.__failureFoundProbabilityHardware):
            self.isFailureFound = True

    # Check methods    
    def __checkRamDeviceLogic(self):
        __failureFound = random.uniform(0.0, 100.0)
        if(__failureFound < self.__failureFoundProbabilityLogic):
            self.isFailureFound = True


    def __checkRamDeviceHardwareFactoryDefect(self):
        __failureFound = random.uniform(0.0, 100.0)
        if(__failureFound < self.__failureFoundProbabilityFactoryDefect):
            self.isFailureFound = True
            
      

class AnotherDevice(Device):    
    def __init__(self):
        super().__init__()
        
        self.__failureHappenedProbabilityPower      = 15.0
        self.__failureFoundProbabilityPower         = 40.0
        
        self.__failureHappenedProbabilityDataBus    = 3.0
        self.__failureFoundProbabilityPowerDataBus  = 30.0
        
        self.__failureHappenedProbabilityPowerSDD   = 7.0
        self.__failureFoundProbabilityPowerSDD      = 25.0
        
        self.__failureHappenedProbabilityPowerCPU   = 5.0
        self.__failureFoundProbabilityPowerCPU      = 10.0
        
        
    def useDevice(self):      
        # Reset flags
        self.isFailureHappened = False
        self.isFailureFound = False
        
        self.__usePowerSource()
        self.__useDataBus()
        self.__useSDD()
        self.__useCPU()

        if (self.isFailureHappened == True):
            self.__checkPowerSource()
            self.__checkDataBus()
            self.__checkSDD()
            self.__checkCPU()

    # Use methods
    def __usePowerSource(self):
        __failureHappened = random.uniform(0.0, 100.0)
        
        if(__failureHappened < self.__failureHappenedProbabilityPower):
            self.isFailureHappened = True
            
        
    def __useDataBus(self):
        __failureHappened = random.uniform(0.0, 100.0)
        
        if(__failureHappened < self.__failureHappenedProbabilityDataBus):
            self.isFailureHappened = True


    def __useSDD(self):
        __failureHappened = random.uniform(0.0, 100.0)
        
        if(__failureHappened < self.__failureHappenedProbabilityPowerSDD):
            self.isFailureHappened = True


    def __useCPU(self):
        __failureHappened = random.uniform(0.0, 100.0)
        
        if(__failureHappened < self.__failureHappenedProbabilityPowerCPU):
            self.isFailureHappened = True

    # Check methods 
    def __checkPowerSource(self):
        __failureHappened = random.uniform(0.0, 100.0)
        
        if(__failureHappened < self.__failureFoundProbabilityPower):
            self.isFailureFound = True

        
    def __checkDataBus(self):
        __failureHappened = random.uniform(0.0, 100.0)
        
        if(__failureHappened < self.__failureFoundProbabilityPowerDataBus):
            self.isFailureFound = True


    def __checkSDD(self):
        __failureHappened = random.uniform(0.0, 100.0)
        
        if(__failureHappened < self.__failureFoundProbabilityPowerSDD):
            self.isFailureFound = True


    def __checkCPU(self):
        __failureHappened = random.uniform(0.0, 100.0)
        
        if(__failureHappened < self.__failureFoundProbabilityPowerCPU):
            self.isFailureFound = True            


# Single functions
def useDeviceMultipleTimes(rounds, device, counter):
    for index in range(rounds):
        device.useDevice()
        if(device.checkStatus() == True):
            counter[0] = counter[0] + 1



def outputResults(rounds, counter1, counter2, counter3):
    print('Emulated cycles with failures: ', rounds)
    print()
    print('Failures detected in Arithmetic Device, %:', counter1[0]  * 100.0 / rounds)
    print('Failures detected in Ram Device, %:',        counter2[0]  * 100.0 / rounds)
    print('Failures detected in Another Device, %:',    counter3[0]  * 100.0 / rounds)
    print()
    print('Failures detected total, %: ', (counter1[0] +       
                                           counter2[0] +
                                           counter3[0]) * 100.0 / rounds)

    print('Failures not detected total, %: ', 100.0 - (counter1[0] +       
                                                       counter2[0] +
                                                       counter3[0]) * 100.0 / rounds)



def main():

    # Seed random device (we use it when access any device to emulate
    # random failures and its random detection
    random.seed(version=3)

    # Create failures counters
    failuresFoundInArithmeticDevice = [0]
    failuresFoundInRamDevice        = [0]
    failuresFoundInAnotherDevice    = [0]

    # Create devices
    arithmeticDevice = ArithmeticDevice()
    ramDevice        = RamDevice()
    anotherDevice    = AnotherDevice()
    
    # Use devices
    useDeviceMultipleTimes(rounds, arithmeticDevice, failuresFoundInArithmeticDevice)
    useDeviceMultipleTimes(rounds, ramDevice,        failuresFoundInRamDevice)
    useDeviceMultipleTimes(rounds, anotherDevice,    failuresFoundInAnotherDevice)

    # Output results
    outputResults(rounds,
                  failuresFoundInArithmeticDevice,
                  failuresFoundInRamDevice,
                  failuresFoundInAnotherDevice)


            
# Start from here
main()

