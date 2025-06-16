import numpy as np

P_feed = 2      # bar
T_feed = 300    # K
u_feed = 1      # m/s
y1_feed = 0.15  # mol/mol (CO2)
R_gas = 8.3145  # J/mol/K
C1_feed = y1_feed*P_feed/R_gas/T_feed*1E5
C2_feed = (1-y1_feed)*P_feed/R_gas/T_feed*1E5

P_perm = 1      # bar
y1_prem = 0.5   # mol/mol

print(C1_feed)
