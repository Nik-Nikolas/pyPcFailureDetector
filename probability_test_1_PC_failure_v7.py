# This program simulates work of a computer machine
# observing a faulure event which randomly occurs in one of subsystems
# for estimation the failure event detection probability
# in all subsystems.
# Igor Lobanov 2020

import random

# Simulations amount
cycles = 100

# Probabilities constants:
# 1. Arithmetic Device
failureHappenedArithmeticDeviceProbability = 10.0
failureFoundArithmeticDeviceProbability    = 80.0
# 2. Ram Device
failureHappenedProbabilityHardware         = 39.0
failureFoundProbabilityHardware            = 10.0
        
failureHappenedProbabilityLogic            = 20.0
failureFoundProbabilityLogic               = 5.0

failureHappenedProbabilityFactoryDefect    = 1.0
failureFoundProbabilityFactoryDefect       = 70.0
# 3. Other Devices
failureHappenedProbabilityPower            = 15.0
failureFoundProbabilityPower               = 40.0
        
failureHappenedProbabilityDataBus          = 3.0
failureFoundProbabilityPowerDataBus        = 30.0
        
failureHappenedProbabilitySSD              = 7.0
failureFoundProbabilitySSD                 = 25.0
        
failureHappenedProbabilityCPU              = 5.0
failureFoundProbabilityCPU                 = 10.0

# A base class. Abstract device.
class Device():    
    def __init__(self,
                 subDevicesAmount,
                 isFailureHappened = False,
                 isFailureFound = False,
                 isFailureNotHappened = True,
                 isFailureNotFound = True):

        # Failure flags.
        self.isFailureHappened = isFailureHappened
        self.isFailureFound = isFailureFound
        self.isFailureNotHappened = isFailureHappened
        self.isFailureNotFound = isFailureFound

        # sub devices amount
        self.subDevicesAmount = subDevicesAmount

        # Not happened in device events counter
        self.notHappenedInDevice = [0]

    # Flags getters
    def isFailureHappenedStatus(self):
        return self.isFailureHappened    

    def isFailureFoundStatus(self):
        return self.isFailureFound    

    def isFailureNotHappenedStatus(self):
        return self.isFailureNotHappened    

    def isFailureNotFoundStatus(self):
        return self.isFailureNotFound

    # Calc the fact of that the failure not happened.
    def calcFailureNotHappened(self):
        if(self.notHappenedInDevice[0] == self.subDevicesAmount):
            self.isFailureNotHappened = True
    
    # Prevent from using the base class directly.
    def useDevice(self):
        raise NotImplementedError("Subclass must implement abstract method")

    # Reset flags
    def resetFlags(self):
        self.isFailureHappened = False
        self.isFailureFound = False        
        self.isFailureNotHappened = False
        self.isFailureNotFound = False


    def useSpecificDevice(self, failureHappenedProbability, failureFoundProbability):

        # Simulate events: failure occured and, if yes, detected with certain probability
        __failureHappened = random.uniform(0.0, 100.0)

        # Happened?
        if(__failureHappened < failureHappenedProbability):
            self.isFailureHappened = True

            # Happened! Found?
            __failureFound = random.uniform(0.0, 100.0)
        
            if(__failureFound < failureFoundProbability):
                # Found!
                self.isFailureFound = True

            else:
                self.isFailureNotFound = True
                
        # Neither happened nor (obviously) found. 
        else:
            # self.isFailureNotHappened = True // should not set this flag here! it is to be set in calcFailureNotHappened()!
            
            # Increment the counter.
            self.notHappenedInDevice[0] += 1            
            

class ArithmeticDevice(Device):    
    def __init__(self):
        super().__init__(1)

        # Set constants (probability)
        self.__failureHappenedProbability = failureHappenedArithmeticDeviceProbability
        self.__failureFoundProbability    = failureFoundArithmeticDeviceProbability
        
    def useDevice(self):

        # Reset flags
        super().resetFlags()

        # Reset event not happened counter
        self.notHappenedInDevice = [0]       

        # Use sub devices:
        # Use Arithmetic Device Hardware     
        super().useSpecificDevice(self.__failureHappenedProbability, self.__failureFoundProbability)

        # Calc the fact of that the failure not happened.
        super().calcFailureNotHappened()



            
class RamDevice(Device):    
    def __init__(self):
        super().__init__(3)
        
        self.__failureHappenedProbabilityHardware      = failureHappenedProbabilityHardware
        self.__failureFoundProbabilityHardware         = failureFoundProbabilityHardware
        
        self.__failureHappenedProbabilityLogic         = failureHappenedProbabilityLogic
        self.__failureFoundProbabilityLogic            = failureFoundProbabilityLogic
        
        self.__failureHappenedProbabilityFactoryDefect = failureHappenedProbabilityFactoryDefect
        self.__failureFoundProbabilityFactoryDefect    = failureFoundProbabilityFactoryDefect
        
    def useDevice(self):
        # Reset flags
        super().resetFlags()

        # Reset event not happened counter
        self.notHappenedInDevice = [0]        
        
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
        
        # Calc the fact of that the failure not happened.
        super().calcFailureNotHappened()

              
    # Simulate failures
    # Use methods
    def __useRamDeviceHardware(self):
        super().useSpecificDevice(self.__failureHappenedProbabilityHardware, self.__failureFoundProbabilityHardware)
            
    def __useRamDeviceLogic(self):
        super().useSpecificDevice(self.__failureHappenedProbabilityLogic, self.__failureFoundProbabilityLogic)
            
    def __useRamDeviceHardwareFactoryDefect(self):
        super().useSpecificDevice(self.__failureHappenedProbabilityFactoryDefect, self.__failureFoundProbabilityFactoryDefect)

            
class AnotherDevice(Device):    
    def __init__(self):
        super().__init__(4)
        
        self.__failureHappenedProbabilityPower      = failureHappenedProbabilityPower
        self.__failureFoundProbabilityPower         = failureFoundProbabilityPower
        
        self.__failureHappenedProbabilityDataBus    = failureHappenedProbabilityDataBus
        self.__failureFoundProbabilityPowerDataBus  = failureFoundProbabilityPowerDataBus
        
        self.__failureHappenedProbabilitySSD        = failureHappenedProbabilitySSD
        self.__failureFoundProbabilitySSD           = failureFoundProbabilitySSD
        
        self.__failureHappenedProbabilityCPU        = failureHappenedProbabilityCPU
        self.__failureFoundProbabilityCPU           = failureFoundProbabilityCPU
        
        
    def useDevice(self):      
        # Reset flags
        super().resetFlags()

        # Reset event not happened counter
        self.notHappenedInDevice = [0]        

        # Use sub devices:
        self.__usePowerSource()
        self.__useDataBus()
        self.__useSSD()
        self.__useCPU()

        # Calc the fact of that the failure not happened.
        super().calcFailureNotHappened()



    # Use methods
    def __usePowerSource(self):
        super().useSpecificDevice(self.__failureHappenedProbabilityPower, self.__failureFoundProbabilityPower)
            
    def __useDataBus(self):
        super().useSpecificDevice(self.__failureHappenedProbabilityDataBus, self.__failureFoundProbabilityPowerDataBus)
            
    def __useSSD(self):
        super().useSpecificDevice(self.__failureHappenedProbabilitySSD, self.__failureFoundProbabilitySSD)
            
    def __useCPU(self):
        super().useSpecificDevice(self.__failureHappenedProbabilityCPU, self.__failureFoundProbabilityCPU)
            
            
# Use device attempt. During it any predetermined failure event may occur.
def useDevice(cycles,
              device,
              counter1,
              counter2,
              counter3,
              counter4):

        # Count the events.        
        device.useDevice()
        if(device.isFailureHappenedStatus() == True):
            counter1[0] = counter1[0] + 1
            
        if(device.isFailureNotHappenedStatus() == True):
            counter3[0] = counter3[0] + 1
            
        if(device.isFailureFoundStatus() == True):
            counter2[0] = counter2[0] + 1

        if(device.isFailureNotFoundStatus() == True):
            counter4[0] = counter4[0] + 1


# Output the results.
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

    __devicesGroups = 3;
    print('Simulated cycles with potential failures                    :', rounds)
    print()
    print('failure Happened in Arithmetic Device Probability          %:',failureHappenedArithmeticDeviceProbability)
    print('failure Detected in Arithmetic Device Probability          %:',failureFoundArithmeticDeviceProbability)
    print('failure Happened in RAM (hardware) Probability             %:',failureHappenedProbabilityHardware)
    print('failure Detected in RAM (hardware) Probability             %:',failureFoundProbabilityHardware)
    print('failure Happened in RAM (logic) Probability                %:',failureHappenedProbabilityLogic)
    print('failure Detected in RAM (logic) Probability                %:',failureFoundProbabilityLogic)
    print('failure Happened in RAM (defect) Probability               %:',failureHappenedProbabilityFactoryDefect)
    print('failure Detected in RAM (defect) Probability               %:',failureFoundProbabilityFactoryDefect)
    
    print('failure Happened in other Device (power) Probability       %:',failureHappenedProbabilityPower)
    print('failure Detected in other Device (power) Probability       %:',failureFoundProbabilityPower)
    print('failure Happened in other Device (data bus) Probability    %:',failureHappenedProbabilityDataBus)
    print('failure Detected in other Device (data bus) Probability    %:',failureFoundProbabilityPowerDataBus)
    print('failure Happened in other Device (SSD) Probability         %:',failureHappenedProbabilitySSD)
    print('failure Detected in other Device (SSD) Probability         %:',failureFoundProbabilitySSD)
    print('failure Happened in other Device (CPU) Probability         %:',failureHappenedProbabilityCPU)
    print('failure Detected in other Device (CPU) Probability         %:',failureFoundProbabilityCPU)
    print()
    print()
    print('Failures happened in Arithmetic Device,           %:',
          counter1[0] * 100.0 / rounds, ' (', counter1[0], 'events )')

    print('Failures happened in Ram Device,                  %:',
          counter2[0] * 100.0 / rounds, ' (', counter2[0], 'events )')
    print('Failures happened in Another Device,              %:',
          counter3[0] * 100.0 / rounds, ' (', counter3[0], 'events )')
    
    happenedP   = (counter1[0] + counter2[0] + counter3[0]) * 100.0 / rounds
    happened    = counter1[0] + counter2[0] + counter3[0]

    print('    Failures happened AT LEAST IN 1 DEVICE total, %:', happenedP, ' (', happened, 'events )')
    print()
    print('Failures not happened in Arithmetic Device,       %:',
          counter7[0] * 100.0 / rounds, ' (', counter7[0], 'events )')
    print('Failures not happened in Ram Device,              %:',
          counter8[0] * 100.0 / rounds, ' (', counter8[0], 'events )')
    print('Failures not happened in Another Device,          %:',
          counter9[0] * 100.0 / rounds, ' (', counter9[0], 'events )')
    
    #notHappenedP = (counter7[0] + counter8[0] + counter9[0]) * 100.0 / rounds
    #notHappened = counter7[0] + counter8[0] + counter9[0]

    #print('    Failures not happened IN ANY DEVICE total,    %:', notHappenedP, ' (', notHappened, ' events)')
    print()
    print('Failures detected in Arithmetic Device,           %:',
          counter4[0] * 100.0 / rounds, ' (', counter4[0], 'events )')
    print('Failures detected in Ram Device,                  %:',
          counter5[0] * 100.0 / rounds, ' (', counter5[0], 'events )')
    print('Failures detected in Another Device,              %:',
          counter6[0] * 100.0 / rounds, ' (', counter6[0], 'events )')
    
    detectedP    = (counter4[0] + counter5[0] + counter6[0]) * 100.0 / rounds
    detected    = counter4[0] + counter5[0] + counter6[0]

    print('    Failures detected AT LEAST IN 1 DEVICE total, %:', detectedP, ' (', detected, 'events )')
    print()
    print('Failures not detected in Arithmetic Device,       %:',
          counter10[0] * 100.0 / rounds, ' (', counter10[0], 'events )')
    print('Failures not detected in Ram Device,              %:',
          counter11[0] * 100.0 / rounds, ' (', counter11[0], 'events )')
    print('Failures not detected in Another Device,          %:',
          counter12[0] * 100.0 / rounds, ' (', counter12[0], 'events )')
    
    #notDetectedP = (counter10[0] + counter11[0] + counter12[0]) * 100.0 / rounds
    #notDetected = counter10[0] + counter11[0] + counter12[0]

    #print('    Failures not detected IN ANY DEVICE total,    %:', notDetectedP, ' (', notDetected, ' events)')



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

