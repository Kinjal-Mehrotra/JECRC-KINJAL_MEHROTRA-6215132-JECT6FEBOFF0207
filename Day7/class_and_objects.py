class Car:
    #below variables are known as Properties/states/members
    wheelers=4
    engine='Petrol'
    base_speed='40kmph'
    max_speed='120kmph'
    gears=4

#below instances are objects
tata=Car()
mahindra=Car()
suzuki=Car()
toyota=Car()

print(tata) #returns the object location
print(tata.wheelers)

#adding object properties - each object property will only be for that object only 
tata.air_bags=True
tata.security='Level 5'

#for acccessing the properties
print("----Properties of Tata----")
print(f'No of wheelers: {tata.wheelers}')
print(f'Engine type: {tata.engine}')
print(f'Base speed: {tata.base_speed}')
print(f'Max speed: {tata.max_speed}')
print(f'Number of manual gears: {tata.gears}')
print(f'Air bags: {tata.air_bags}')
print(f'Security: {tata.security}')


print("----Properties of Mahindra----")
print(f'No of wheelers: {mahindra.wheelers}')
print(f'Engine type: {mahindra.engine}')
print(f'Base speed: {mahindra.base_speed}')
print(f'Max speed: {mahindra.max_speed}')
print(f'Number of manual gears: {mahindra.gears}')

print("----Properties of Suzuki----")
print(f'No of wheelers: {suzuki.wheelers}')
print(f'Engine type: {suzuki.engine}')
print(f'Base speed: {suzuki.base_speed}')
print(f'Max speed: {suzuki.max_speed}')
print(f'Number of manual gears: {suzuki.gears}')

print("----Properties of Toyota----")
print(f'No of wheelers: {toyota.wheelers}')
print(f'Engine type: {toyota.engine}')
print(f'Base speed: {toyota.base_speed}')
print(f'Max speed: {toyota.max_speed}')
print(f'Number of manual gears: {toyota.gears}')

#we can also access the properties of class using the class name
print("----class properties----")
print(Car.wheelers)

