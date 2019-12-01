def compare():
    PSO = {'Premium(Super)': 114.24,
           'HighSpeed Diesel':127.41,
           'LightSpeed Diesel':85.33,
           'Kerosene Oil':97.18}
    SHELL = {'Altron Premium':114.24,
             'Action+ Diesel':127.41,
             'LDO':85.33,
             'SKO':97.18}

    litres = 500
    litres_diesel = 300
    litres_kerosene = 200

    cost_pso_litres = 114.24 * litres
    cost_pso_diesel1 = 127.41 * litres_diesel
    cost_pso_diesel2 = 85.33 * litres_diesel
    cost_pso_kero = 97.18 * litres_kerosene

    cost_shell_litres = 114.24 * litres
    cost_shell_diesel1 = 127.41 * litres_diesel
    cost_shell_diesel2 = 85.33 * litres_diesel
    cost_shell_kero = 97.18 * litres_kerosene

    diff_litres = cost_pso_litres - cost_shell_litres
    diff_diesel1 = cost_pso_diesel1 - cost_shell_diesel1
    diff_diesel2 = cost_pso_diesel2 - cost_shell_diesel2
    diff_kero = cost_pso_kero - cost_shell_kero

    print('\t\t\tPSO\t\t\t\t\t\t\t\t\t\t  SHELL\t\t\t\t\t\t  Amount In Litres\t\t\t\tPSO COST\t\t\t\tSHELL COST\t\t\t\tDifference In Price\nPremium(Super)\t\t: {0}\t\t\t\tAltron Premium\t: {4}\t\t\t\t\t{8}\t\t\t\t\t\t{11}\t\t\t\t\t {15}\t\t\t\t\t\t{19}\nHighSpeed Diesel\t: {1}\t\t\t\tAction+ Diesel\t: {5}\t\t\t\t\t{9}\t\t\t\t\t\t{12}\t\t\t\t\t {16}\t\t\t\t\t\t{20}\nLightSpeed Diesel\t:  {2}\t\t\t\tLDO\t\t\t\t:  {6}\t\t\t\t\t{9}\t\t\t\t\t\t{13}\t\t\t\t\t {17}\t\t\t\t\t\t{21}\nKerosene Oil\t\t:  {3}\t\t\t\tSKO\t\t\t\t:  {7}\t\t\t\t\t{10}\t\t\t\t\t\t{14}\t\t\t\t\t {18}\t\t\t\t\t\t{22}'.format(PSO.get('Premium(Super)'),PSO.get('HighSpeed Diesel'), PSO.get('LightSpeed Diesel'),PSO.get('Kerosene Oil'),SHELL.get('Altron Premium'),SHELL.get('Action+ Diesel'),SHELL.get('LDO'),SHELL.get('SKO'),litres,litres_diesel,litres_kerosene,cost_pso_litres,cost_pso_diesel1,cost_pso_diesel2,cost_pso_kero,cost_shell_litres,cost_shell_diesel1,cost_shell_diesel2,cost_shell_kero,diff_litres,diff_diesel1,diff_diesel2,diff_kero))

compare()