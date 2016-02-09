
# coding: utf-8

# In[ ]:

# Conversion from rpm to g-force for centrifuge


from scipy import constants

def rpm_to_g(radius, rpm):
    
    rev_per_sec = rpm / 60.0
    R = radius * 0.01
    v= 2 * constants.pi * R * rev_per_sec
    cent_acc = (v ** 2) / R
    g_acc = cent_acc / constants.g
    
    print "The g-force at %.0f rpm is %.1f g" % (rpm,g_acc)
    print '\n'
    
radius = float(raw_input("What is the radius of centrifuge in cm? \n"))
rpm = float(raw_input("What rpm did you use? \n"))

rpm_to_g(radius,rpm)


# In[ ]:



