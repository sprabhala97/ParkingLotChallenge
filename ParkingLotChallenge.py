import random
import json

class ParkingLot:
    def __init__(self,Size_In_Square_Footage,Parking_Spot_Size):
        self.Spot_Size = int(Parking_Spot_Size)
        self.Num_Spots = Size_In_Square_Footage // self.Spot_Size
        self.Parking_lot= ["empty"] * self.Num_Spots

    
class Car:
    def __init__(self,License_Plate):
        self.LicensePlateNumber= License_Plate

    def string(self, Licenseplate):
        return str(self.LicensePlateNumber)
        
    def park(self,Parkinglot,Spot):
        # print(Parkinglot)
        if(Parkinglot[Spot] == "empty"):
            Parkinglot[Spot] = self
            return "Car sucessfully parked"
        else:
            return "Car not parked"

def main(Licenseplates):
    for lp in Licenseplates:
        car= Car(lp)
        if ("empty" not in Parkinglot.Parking_lot):
            print("Parking lot is full")
            break
        Spot = Parkinglot.Parking_lot.index("empty") if "empty" in Parkinglot.Parking_lot else -1
        status = car.park(Parkinglot.Parking_lot,Spot)
        print(f"Car with license plate {lp} parked successfully in spot {Spot+1}")
        Output[Spot+1] = lp


Output = {}
NumberOfCars = random.randint(1,100)
License_plates = [random.randint(1000000,9999999) for plate in range(NumberOfCars)]
ParkingLotSize = input("Enter the parking lot size: ")
ParkingSpotSize = input("Enter the parking spot size in (length*Widith) format: ")
Parkinglot = ParkingLot(int(ParkingLotSize),int(ParkingSpotSize.split('*')[0])*int(ParkingSpotSize.split('*')[1]))
main(License_plates)
with open("Response.json", 'w') as file:
    json.dump(Output, file)
