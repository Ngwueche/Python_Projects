# PASSWORD GENERATOR
import random
uppercase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase="abcdefghijklmnopqrstuvwxyz"
numbers= "0123456789"
symbols= "!@#$%^&*()?\/><[]~`':;"

parameters= uppercase + lowercase + numbers + symbols
length =  10

password= "".join(random.sample(parameters, length))

print("Your generator password is :" + password)