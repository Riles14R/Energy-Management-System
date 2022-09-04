from concurrent.futures.process import _system_limits_checked
import time
import random

EM=('E1B2','B212','ASRL2')
DP=('thirtyonesixtynine')

def welcomesys():
    print('Welcome'' '+user)
def sys(): #This is for the menu
    print("""
    **Welcome to Riles Energy Systems**
          1.Wind Turbine Status
          2.Wind Turbine Energy Battery
          3.Solar Panel Status
          4.Solar Panel Energy Battery
          5.Main Battery Status
          6.Wind Rotatation
          7.Log out
    """)
    
# password: thirtyonesixtynine
# EM Id:E1B2 or B212 or ASRL2

while True:
    user=input("Please enter your EM Id... ")
    
    if user in EM:
     userpassword=input("Please enter default password... ")
    elif not user in EM:
     print('Please Try Again')
     break
        
    if userpassword != DP: 
     print("Invalid password.")
     break
    if userpassword in DP:
        welcomesys()
        time.sleep(2)
        sys()
        sysc=input("What do you want to check? ")
    if sysc=='1':
        wtsr=["Wind Turbine is operational","Wind Turbine is Not Operational Right Now","CRITICAL:Wind Turbine is Damaged"]
        wts=random.choice(wtsr)
        print(wts)
        time.sleep(0.2)
        print('Logging out for Security Protocol')
        break
    if sysc =='2':
        wteb = random.sample(range(1, 5000), 1)
        print('Checking....')
        time.sleep(1)
        print(wteb,'kwH energy is stored')
        time.sleep(0.2)
        print('Logging out for Security Protocol')
        break
    if sysc=='3':
        solar_panel_status_randomize=[
        'Solar Panel is clean and operational','Solar Panel needs cleaning and operational',
        'Solar Panel is clean and not operational',
        'Solar Panel needs cleaning and not operational',
        'CRITICAL:Solar Panel is broken'
        ]
        sps=random.choice(solar_panel_status_randomize)
        print(sps)
        time.sleep(0.2)
        print('Logging out for Security Protocol')
        break
    if sysc =='4':
        spb = random.sample(range(1, 5000), 1)
        print('Checking Solar Panel....')
        time.sleep(1)
        print(spb,'kwH energy is stored')
        time.sleep(0.2)
        print('Logging out for Security Protocol')
        break
    if sysc=='5':
        spb = random.sample(range(1, 10000), 1)
        wteb = random.sample(range(1, 5000), 1)
        print('Main battery is calculating...')
        time.sleep(1)
        def mainb():
            return (spb+wteb)
        print(mainb())
        print('Logging out for Security Protocol')
        break
    if sysc=='6':
        wrr=['West','East','North','South']
        wr=random.choice(wrr)
        print("Wind Rotation is "+wr)
        print('Logging out for Security Protocol')
        break
    if sysc=='7':
        print('Thank you for using Riles Systems')
        time.sleep(0.7)
        print('Logging out now')
        break
    if sysc=='credits':
        open('https://github.com/Riles14R')
