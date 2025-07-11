# Cody Rorick
# algorithm for the fast decoupled newton raphson method

import cmath
import numpy as np
import math

#need to invert impedances, this is the impedance not the admittance
print("ybus:")
ybus = np.array([[20-50j, -10+30j, -10+20j],
                [-10+30j, 26-62j, -16+32j],
                [-10+20j, -16+32j, 26-52j]])
print(ybus)
for i in range(0, ybus.shape[0]):
    print('\n')
    print("Row Number",i+1, "in polar coordinates")
    print(ybus[i,0])
    print("magnitude =", cmath.polar(ybus[i,0])[0]) 
    print("angle =", math.degrees(cmath.polar(ybus[i,0])[1]))
    print(ybus[i,1])
    print("magnitude =", cmath.polar(ybus[i,1])[0]) 
    print("angle =", math.degrees(cmath.polar(ybus[i,1])[1]))
    print(ybus[i,2])
    print("magnitude =", cmath.polar(ybus[i,2])[0]) 
    print("angle =", math.degrees(cmath.polar(ybus[i,2])[1]))


#define B matrix
Bmatrix = ybus.imag
print("B matrix:")
print(Bmatrix)

#define Jacobian 1
Jacobian1 = np.array([[-ybus[1,1].imag, -ybus[1,2].imag], [-ybus[2,1].imag, -ybus[2,2].imag]])
print("\nJacobian 1:")
print(Jacobian1)

#define Jacobian 4
Jacobian4 = -ybus[2,2].imag
print("\nJacobian 4:")
print(Jacobian4)

#scheduled power
scheduledP2 = 2
scheduledP3 = -4
scheduledQ3 = -2.5
V1 = 1
V2 = 1.04
V3 = 1
delta2 = 0
delta3 = 0
delta_array = np.array([[delta2],[delta3]])
inverse_jacobian1 = np.linalg.inv(Jacobian1)
inverse_jacobian4 = math.pow(Jacobian4, -1)
count = 1

while(abs(P2difference)>=0.000001 or abs(P3difference)>=0.000001 or abs(Q3difference)>=0.000001 or count<=1):
    #print new values
    print("V3:", V3)
    print("delta2:", delta_array[0])
    print("delta3:", delta_array[1])
    
    #calculate difference between scheduled real and reactive power and new real and reactive power
    P2difference = scheduledP2 - (31.62*(V1*V2)*math.cos(math.radians(delta_array[0]-108.44)) + 
                                  67.23*(V2*V2)*math.cos(math.radians(67.23)) + 
                                  35.78*V3*V2*math.cos(math.radians(delta_array[0]-116.6-delta_array[1])))
    print("P2 residual", abs(P2difference))
    P3difference = scheduledP3 - (22.36*(V1*V3)*math.cos(math.radians(delta_array[1]-116.6)) + 
                                  35.78*(V2*V3)*math.cos(math.radians(delta_array[1]-116.6-delta_array[0])) + 
                                  58.14*(V3*V3)*math.cos(math.radians(63.4)))
    print("P3 residual", abs(P3difference))
    Q3difference = scheduledQ3 - (22.36*(V1*V3)*math.sin(math.radians(delta_array[1]-116.6)) + 
                                  35.78*(V2*V3)*math.sin(math.radians(delta_array[1]-116.6-delta_array[0])) + 
                                  58.14*(V3*V3)*math.sin(math.radians(63.4)))
    print("Q3 residual", abs(Q3difference))
    
    #assign power difference to matrix
    P_matrix = np.array([[P2difference], [P3difference]])
    
    #matrix multiplication between inverse jacobian and power difference matrix
    P_differential_matrix = np.dot(inverse_jacobian1, P_matrix)
    
    #new delta array will be old delta array plus the power differntial matrix
    delta_array = delta_array.__add__(P_differential_matrix)
    
    
    #new voltage will be old voltage plus reactive power differential matrix
    V3 = V3 + inverse_jacobian4 * Q3difference
    print("iteration number:", count)
    count+=1


print("delta2 (degrees): ", delta_array[0])
print("delta3 (degrees): ", delta_array[1])
print("V3 (pu): ", V3)

Voltage_Matrix = np.array([[cmath.rect(V1, 0)], [cmath.rect(V2, math.radians(delta_array[0]))], [cmath.rect(V3, math.radians(delta_array[1]))]])
Current_Matrix = ybus.dot(Voltage_Matrix)
Apparent_Power = np.conj(Current_Matrix)*Voltage_Matrix


# Outputs
print("Voltage Matrix")
print(Voltage_Matrix)
print('\n')
print("Current Matrix")
print(Current_Matrix)
print('\n')
print("Power Matrix")
print(Apparent_Power)

Line_Loss = Apparent_Power[0] + Apparent_Power[1] + Apparent_Power[2]
print("loss in lines:", Line_Loss)
S_in = Apparent_Power[0] + Apparent_Power[1]
S_out = Apparent_Power[2]
Power_Balanced = S_in + S_out - Line_Loss
print("Power in the network sums to: ", Power_Balanced)

