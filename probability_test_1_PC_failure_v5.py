# This program simulates work of computer machine
# and faulure event in one of subsystems
# for estimation failure event detection probability
# in every subsystem.
# Igor Lobanov 2019

import random

# Simulations amount
cycles = 100000

class Device():    
    def __init__(self,
                 isFailureHappened = False,
                 isFailureFound = False,
                 isFailureNotHappened = True,
                 isFailureNotFound = True):
        
        self.isFailureHappened = isFailureHappened
        self.isFailureFound = isFailureFound
        self.isFailureNotHappened = isFailureHappened
        self.isFailureNotFound = isFailureFound
        

    def isFailureHappenedStatus(self):
        return self.isFailureHappened
    

    def isFailureFoundStatus(self):
        return self.isFailureFound
    

    def isFailureNotHappenedStatus(self):
        return self.isFailureNotHappened
    

    def isFailureNotFoundStatus(self):
        return self.isFailureNotFound
    

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
        self.isFailureNotHappened = False
        self.isFailureNotFound = False

        # Event not happened utility variables
        self.notHappendInDevice = [0]
        self.devicesAmount = 1
        
        # useRamDeviceHardware       
        __failureHappened = random.uniform(0.0, 100.0)
        
        if(__failureHappened < self.__failureHappenedProbability):
            self.isFailureHappened = True        

            
            __failureFound = random.uniform(0.0, 100.0)
            if(__failureFound < self.__failureFoundProbability):
                self.isFailureFound = True 
            else:
                self.isFailureNotFound = True
        else:
            self.notHappendInDevice[0] += 1
                

        if(self.notHappendInDevice[0] == self.devicesAmount):
            self.isFailureNotHappened = True


            
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
        
        self.isFailureNotHappened = False
        self.isFailureNotFound = False

        # Event not happened utility variables
        self.notHappendInDevice = [0]
        self.devicesAmount = 3
        
        # Use sub devices (sequence here mean parallel work because
        # methods (which simulate sub devices independent work processes)
        # do not interfere each other work
        # and only simulate independent failure appearance event)

        # If failure happened - then simulate for this certain failure appearance
        # event dependent of it failure detection event.
        # If single failure occured and then was detected -
        # this fact will rise flag isFailureFound
        # which means that certain single simulation had a failure detected
        self.__useRamDeviceHardware()       
        self.__useRamDeviceLogic()        
        self.__useRamDeviceHardwareFactoryDefect()

        if(self.notHappendInDevice[0] == self.devicesAmount):
            self.isFailureNotHappened = True
              

    # Use methods
    def __useRamDeviceHardware(self):
        # Simulate failure 
        __failureHappened = random.uniform(0.0, 100.0)        
        if(__failureHappened < self.__failureHappenedProbabilityHardware):
            # Failure happened
            self.isFailureHappened = True
            
            # Simulate happened failure detection
            __failureFound = random.uniform(0.0, 100.0)
            if(__failureFound < self.__failureFoundProbabilityHardware):
                # Happened failure detected
                self.isFailureFound = True
            else:
                self.isFailureNotFound = True 
        else:
            self.notHappendInDevice[0] += 1

            
    def __useRamDeviceLogic(self):        
        __failureHappened = random.uniform(0.0, 100.0)        
        if(__failureHappened < self.__failureHappenedProbabilityLogic):            
            self.isFailureHappened = True

            __failureFound = random.uniform(0.0, 100.0)
            if(__failureFound < self.__failureFoundProbabilityLogic):
                self.isFailureFound = True
            else:
                self.isFailureNotFound = True 
        else:
            self.notHappendInDevice[0] += 1

            
    def __useRamDeviceHardwareFactoryDefect(self):        
        __failureHappened = random.uniform(0.0, 100.0)        
        if(__failureHappened < self.__failureHappenedProbabilityFactoryDefect):
            self.isFailureHappened = True

            __failureFound = random.uniform(0.0, 100.0)
            if(__failureFound < self.__failureFoundProbabilityFactoryDefect):
                self.isFailureFound = True
            else:
                self.isFailureNotFound = True      
        else:
            self.notHappendInDevice[0] += 1


            
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
        self.isFailureNotHappened = False
        self.isFailureNotFound = False

        # Event not happened utility variables
        self.notHappendInDevice = [0]
        self.devicesAmount = 4
        
        self.__usePowerSource()
        self.__useDataBus()
        self.__useSDD()
        self.__useCPU()

        if(self.notHappendInDevice[0] == self.devicesAmount):
            self.isFailureNotHappened = True


    # Use methods
    def __usePowerSource(self):
        __failureHappened = random.uniform(0.0, 100.0)
        
        if(__failureHappened < self.__failureHappenedProbabilityPower):
            self.isFailureHappened = True               

            __failureHappened = random.uniform(0.0, 100.0)
            
            if(__failureHappened < self.__failureFoundProbabilityPower):
                self.isFailureFound = True
            else:
                self.isFailureNotFound = True 
        else:
            self.notHappendInDevice[0] += 1
        
            
    def __useDataBus(self):
        __failureHappened = random.uniform(0.0, 100.0)
        
        if(__failureHappened < self.__failureHappenedProbabilityDataBus):
            self.isFailureHappened = True

            __failureHappened = random.uniform(0.0, 100.0)
        
            if(__failureHappened < self.__failureFoundProbabilityPowerDataBus):
                self.isFailureFound = True
            else:
                self.isFailureNotFound = True 
        else:
            self.notHappendInDevice[0] += 1

            
    def __useSDD(self):
        __failureHappened = random.uniform(0.0, 100.0)
        
        if(__failureHappened < self.__failureHappenedProbabilityPowerSDD):
            self.isFailureHappened = True

            __failureHappened = random.uniform(0.0, 100.0)
        
            if(__failureHappened < self.__failureFoundProbabilityPowerSDD):
                self.isFailureFound = True
            else:
                self.isFailureNotFound = True 
        else:
            self.notHappendInDevice[0] += 1

            
    def __useCPU(self):
        __failureHappened = random.uniform(0.0, 100.0)
        
        if(__failureHappened < self.__failureHappenedProbabilityPowerCPU):
            self.isFailureHappened = True

            __failureHappened = random.uniform(0.0, 100.0)
        
            if(__failureHappened < self.__failureFoundProbabilityPowerCPU):
                self.isFailureFound = True
            else:
                self.isFailureNotFound = True 
        else:
            self.notHappendInDevice[0] += 1

            
            
# Single functions
def useDevice(cycles,
              device,
              counter1,
              counter2,
              counter3,
              counter4):

        device.useDevice()
        if(device.isFailureHappenedStatus() == True):
            counter1[0] = counter1[0] + 1
            
        if(device.isFailureNotHappenedStatus() == True):
            counter3[0] = counter3[0] + 1
            
        if(device.isFailureFoundStatus() == True):
            counter2[0] = counter2[0] + 1

        if(device.isFailureNotFoundStatus() == True):
            counter4[0] = counter4[0] + 1



def outputResults(rounds,
                  counter1,
                  counter2,
                  counter3,
                  counter4,
                  counter5,
                  counter6,
                  counter7,
                  counter8,
                  counter9,
                  counter10,
                  counter11,
                  counter12):
    print('Simulated cycles with potential failures           : ', rounds)
    print()
    print('Failures happened in Arithmetic Device,           %:',
          counter1[0] * 100.0 / rounds)
    print('Failures happened in Ram Device,                  %:',
          counter2[0] * 100.0 / rounds)
    print('Failures happened in Another Device,              %:',
          counter3[0] * 100.0 / rounds)
    happened    = (counter1[0] + counter2[0] + counter3[0]) * 100.0 / rounds
    notHappened = (counter7[0] + counter8[0] + counter9[0]) * 100.0 / rounds
    print('    Failures happened AT LEAST IN 1 DEVICE total, %:', happened)
    print()
    print('Failures not happened in Arithmetic Device,       %:',
          counter7[0] * 100.0 / rounds)
    print('Failures not happened in Ram Device,              %:',
          counter8[0] * 100.0 / rounds)
    print('Failures not happened in Another Device,          %:',
          counter9[0] * 100.0 / rounds)    
    print('    Failures not happened IN ALL DEVICES total,   %:', notHappened)
    print()
    print('Failures detected in Arithmetic Device,           %:',
          counter4[0] * 100.0 / rounds)
    print('Failures detected in Ram Device,                  %:',
          counter5[0] * 100.0 / rounds)
    print('Failures detected in Another Device,              %:',
          counter6[0] * 100.0 / rounds)
    detected    = (counter4[0] + counter5[0] + counter6[0]) * 100.0 / rounds
    notDetected = (counter10[0] + counter11[0] + counter12[0]) * 100.0 / rounds
    print('    Failures detected AT LEAST IN 1 DEVICE total, %:', detected)
    print()
    print('Failures not detected in Arithmetic Device,       %:',
          counter10[0] * 100.0 / rounds)
    print('Failures not detected in Ram Device,              %:',
          counter11[0] * 100.0 / rounds)
    print('Failures not detected in Another Device,          %:',
          counter12[0] * 100.0 / rounds)
    print('    Failures not detected IN ALL DEVICES total,   %:', notDetected)



def main():

    # Seed random device (we use it when access any device to simulate
    # random failures and its random detection
    random.seed(version=3)

    # Create failures counters
    #   1.Happened
    failuresHappenedInArithmeticDevice    = [0]
    failuresHappenedInRamDevice           = [0]
    failuresHappenedInAnotherDevice       = [0]
    #   2.Detected
    failuresFoundInArithmeticDevice       = [0]
    failuresFoundInRamDevice              = [0]
    failuresFoundInAnotherDevice          = [0]
    #   3.~Happened
    failuresNotHappenedInArithmeticDevice = [0]
    failuresNotHappenedInRamDevice        = [0]
    failuresNotHappenedInAnotherDevice    = [0]
    #   4.~Detected
    failuresNotFoundInArithmeticDevice    = [0]
    failuresNotFoundInRamDevice           = [0]
    failuresNotFoundInAnotherDevice       = [0]

    # Create devices
    arithmeticDevice = ArithmeticDevice()
    ramDevice        = RamDevice()
    anotherDevice    = AnotherDevice()
    
    # Use all devices (simulate machine work cycles times)
    for index in range(cycles):
        useDevice(cycles,
                  arithmeticDevice,
                  failuresHappenedInArithmeticDevice,
                  failuresFoundInArithmeticDevice,
                  failuresNotHappenedInArithmeticDevice,
                  failuresNotFoundInArithmeticDevice)
        useDevice(cycles,
                  ramDevice,
                  failuresHappenedInRamDevice,
                  failuresFoundInRamDevice,
                  failuresNotHappenedInRamDevice,
                  failuresNotFoundInRamDevice)
        useDevice(cycles,
                  anotherDevice,
                  failuresHappenedInAnotherDevice,
                  failuresFoundInAnotherDevice,
                  failuresNotHappenedInAnotherDevice,
                  failuresNotFoundInAnotherDevice)

    # Logical correctness check
    assert(failuresHappenedInArithmeticDevice >= failuresFoundInArithmeticDevice)
    assert(failuresHappenedInRamDevice >= failuresFoundInRamDevice)
    assert(failuresHappenedInAnotherDevice >= failuresFoundInAnotherDevice)
    
    # Output results
    outputResults(cycles,
                  failuresHappenedInArithmeticDevice ,
                  failuresHappenedInRamDevice,
                  failuresHappenedInAnotherDevice,
                  
                  failuresFoundInArithmeticDevice,
                  failuresFoundInRamDevice,
                  failuresFoundInAnotherDevice,
                  
                  failuresNotHappenedInArithmeticDevice,
                  failuresNotHappenedInRamDevice,
                  failuresNotHappenedInAnotherDevice,
                  
                  failuresNotFoundInArithmeticDevice,
                  failuresNotFoundInRamDevice,
                  failuresNotFoundInAnotherDevice)


            
# Start from here
main()

