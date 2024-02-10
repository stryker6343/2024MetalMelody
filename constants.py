from enum import Enum

class MotorIDs:
    PIVOTMOTOR = 0
    INTAKEMOTOR = 1
    ELEVATORMOTOR = 9

class IntakeConstants:
    PIVOTSPEED = .5
    INTAKESPEED = .2

class ElevatorConstants:
    
    CURRENTSUPPLYLIMIT = 2
    TOPPOSITION = 0
    BOTTOMPOSITION = -130
    MIDDLEPOSITION = (TOPPOSITION + BOTTOMPOSITION)/2
    USESUPPLYLIMIT = True
    kP = 1
    MOTIONMAGICACCELERATION = 20
    MOTIONMAGICVELOCITY = 40
    MOTIONMAGICJERK = 0

class ExternalConstants:
    DRIVERCONTROLLER = 0
    FUNCTIONSCONTROLLER = 1
