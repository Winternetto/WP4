# WP4
#Let's gooo

#DETERMINE W/D = called X
Ktab = [6.]
Xtab = [0.]
X = 1.001


while (1.0 < X < 5.0):   
    Kt = ((1 - .68)/(4))*X + 0.36
    Ktab.append((Kt*(X - 1)))
    Xtab.append(X)
    X = X + 0.01
    if (Kt*(X - 1)) <= min(Ktab):
        WD = X

print(WD)





# MS = 1/((Ra**1.6 + Rtr**1.6)**0.625)-1 
# #so Ra**1.6 + Rtr**1.6 should equal 1 

# Ra = Pu_ax / min(Pu,Pbru)
# Rtr = Pu_t /Ptu

# Kty_1 linear from .0 to .6 to (Aav/Abr = .7),  
# Kty_2 linear from  .6 to .1.4, (Aav/Abr = 1.28)



# A_1 = ((w-D)/2 + r*(1- 2**-0.5))*t
# A_2 = (w-D)*t
# A_3 = 0.5*(w-D)*t
# A_4 = A_1
# # use yielding as the failure condition
# Aav = 6/(3/A_1 + 1/A_2 + 1/A_3 + 1/A_4)
# Abr = D * t

# if (Aav/Abr) < .7:
#     Kty = (.6/.7)*(Aav/Abr) 
# else:
#     Kty = (.8/.58)*(Aav/Abr) - 0.3655

# Pty = Kty * Abr * Fty







