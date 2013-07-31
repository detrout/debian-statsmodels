# -*- coding: utf-8 -*-
"""

Created on Sun Jun 30 23:14:36 2013

Author: Josef Perktold
"""

import numpy as np

class Holder():
    pass

res_t_dfest = Holder()
#> tfit3 <- tlm(m.marietta ~ CRSP, data = mm, start = list(dof = 3),estDof = TRUE)
#> cat_items(tfit3, "res_t_dfest.")
res_t_dfest.random = np.array([
     0.6242843, 1.349205, 1.224172, 1.272655, 1.323455, 1.091313, 1.227218,
     0.0316284, 0.7202973, 1.038392, 1.091907, 0.7966355, 0.784222,
     0.5042926, 0.1964543, 1.172123, 1.017338, 0.8799186, 0.7849335,
     0.790158, 0.8121724, 1.286998, 0.7286052, 1.330104, 1.054037,
     1.299656, 1.285306, 1.271166, 1.106877, 1.303909, 0.4250416, 1.277096,
     1.160106, 0.1871806, 1.074168, 1.197795, 1.046638, 1.104423, 1.301670,
     1.333217, 0.8156778, 1.309934, 1.142454, 1.347481, 0.6605017,
     1.035725, 1.172666, 1.281746, 0.8796436, 0.9597098, 0.6221453,
     1.149490, 1.291864, 1.207619, 1.239625, 1.351065, 1.248711, 0.3532520,
     0.6067273, 0.8180234
    ])
res_t_dfest.dof = 2.837183
res_t_dfest.dofse = 1.175296
res_t_dfest.iter = 7
res_t_dfest.logLik = 71.81292
res_t_dfest.endTime =  0.01

loc_fit = Holder()
#> cat_items(tfit3$loc.fit, "loc_fit.")
loc_fit.coefficients = np.array([-0.007248461, 1.263751])
loc_fit.residuals = np.array([
     -0.09133902, 0.004151492, -0.02737765, 0.02117769, 0.01251936,
     -0.0413709, -0.02701702, 0.5465314, -0.07922967, -0.04651135,
     -0.04131256, 0.07064283, -0.07199043, -0.1096804, 0.2051536,
     0.0331728, 0.04853971, 0.06197657, 0.07191273, -0.07134392,
     0.06897908, -0.01907315, -0.0782573, -0.01096341, 0.04500034,
     -0.01704652, -0.01933079, 0.02138696, 0.03983612, -0.01631880,
     0.1249257, -0.02054422, -0.03443716, 0.2110156, -0.04304691,
     0.03038995, 0.04571555, 0.04007908, -0.01670529, 0.01015959,
     0.06860706, -0.01523742, 0.03625959, 0.005138716, -0.08656302,
     -0.04676856, -0.03311507, -0.01986418, -0.06200429, 0.05410242,
     0.09163019, 0.03553772, 0.01831594, -0.02928904, 0.02551524,
     0.002713425, 0.02437713, -0.1422379, 0.09376145, -0.06835877
    ])
loc_fit.fitted_values = np.array([
     -0.04516098, -0.0810515, -0.03012235, 0.03142231, -0.05741936,
     -0.0445291, -0.04718298, 0.1413686, 0.002229668, 0.1315113,
     0.04431256, 0.004757169, 0.03079043, 0.02068043, 0.02674643,
     0.0755272, -0.01103971, 0.03382343, -0.05451273, -0.001056083,
     0.00602092, -0.03972685, 0.0162573, -0.02683659, -0.02810034,
     -0.06285348, 0.004630794, -0.01078696, -0.08193612, 0.01271880,
     -0.03732572, 0.1230442, -0.01546284, -0.01571559, -0.02835309,
     0.01651005, 0.08538445, 0.00602092, -0.01609471, -0.01975959,
     0.05859294, 0.00753742, -0.01975959, -0.02013872, -0.06133698,
     0.04026856, 0.07211507, 0.04216418, -0.006995711, 0.07969758,
     0.05416981, -0.02923772, 0.05088406, 0.005389044, -0.08231524,
     0.07868658, -0.1132771, 0.05353794, 0.009938546, -0.04794123
    ])
loc_fit.effects = np.array([
     -0.4809681, 6.645774, -0.6803134, 0.8423367, 0.5333795, -0.9748358,
     -0.6818408, 0.6716256, -1.239349, -0.9454051, -0.919986, 1.546571,
     -1.206974, -1.185012, 1.167586, 1.162168, 1.367571, 1.521386,
     1.514811, -1.224234, 1.541103, -0.4658513, -1.229607, -0.2132594,
     1.309335, -0.4211133, -0.4462804, 0.8224875, 1.194665, -0.3537337,
     1.443046, -0.4086050, -0.8295162, 1.122057, -0.9918254, 1.065403,
     1.388378, 1.252209, -0.3826760, 0.4819511, 1.571469, -0.3244968,
     1.166818, 0.3190928, -1.280510, -1.004244, -0.7489287, -0.4386115,
     -1.182836, 1.485040, 1.594513, 1.146952, 0.773323, -0.7043392,
     0.888233, 0.2990213, 0.8402323, -1.040679, 1.564756, -1.241512
    ])
loc_fit.weights = np.array([
     260.7666, 260.7666, 260.7666, 260.7666, 260.7666, 260.7666, 260.7666,
     260.7666, 260.7666, 260.7666, 260.7666, 260.7666, 260.7666, 260.7666,
     260.7666, 260.7666, 260.7666, 260.7666, 260.7666, 260.7666, 260.7666,
     260.7666, 260.7666, 260.7666, 260.7666, 260.7666, 260.7666, 260.7666,
     260.7666, 260.7666, 260.7666, 260.7666, 260.7666, 260.7666, 260.7666,
     260.7666, 260.7666, 260.7666, 260.7666, 260.7666, 260.7666, 260.7666,
     260.7666, 260.7666, 260.7666, 260.7666, 260.7666, 260.7666, 260.7666,
     260.7666, 260.7666, 260.7666, 260.7666, 260.7666, 260.7666, 260.7666,
     260.7666, 260.7666, 260.7666, 260.7666
    ])
loc_fit.qr = '''structure(list(qr = structure(c(-125.083961390618, 0.129099444873581,  0.129099444873581, 0.129099444873581, 0.129099444873581, 0.129099444873581,  0.129099444873581, 0.129099444873581, 0.129099444873581, 0.129099444873581,  0.129099444873581, 0.129099444873581, 0.129099444873581, 0.129099444873581,  0.129099444873581, 0.129099444873581, 0.129099444873581, 0.129099444873581,  0.129099444873581, 0.129099444873581, 0.129099444873581, 0.129099444873581,  0.129099444873581, 0.129099444873581, 0.129099444873581, 0.129099444873581,  0.129099444873581, 0.129099444873581, 0.129099444873581, 0.129099444873581,  0.129099444873581, 0.129099444873581, 0.129099444873581, 0.129099444873581,  0.129099444873581, 0.129099444873581, 0.129099444873581, 0.129099444873581,  0.129099444873581, 0.129099444873581, 0.129099444873581, 0.129099444873581,  0.129099444873581, 0.129099444873581, 0.129099444873581, 0.129099444873581,  0.129099444873581, 0.129099444873581, 0.129099444873581, 0.129099444873581,  0.129099444873581, 0.129099444873581, 0.129099444873581, 0.129099444873581,  0.129099444873581, 0.129099444873581, 0.129099444873581, 0.129099444873581,  0.129099444873581, 0.129099444873581, -1.09802870774065, 5.25877087979451,  0.068920957251135, -0.0806236351850806, 0.135248743629416, 0.103927288950783,  0.110375823737560, -0.34777721920871, -0.00968975253053064, -0.323825518572109,  -0.111945089863713, -0.0158312142322233, -0.0790882697596574,  -0.0545224229528869, -0.0692619310369492, -0.187792141879617,  0.0225529214033557, -0.0864580238016886, 0.128186062672469, -0.00170585231833022,  -0.0189019450830696, 0.092258511717567, -0.0437748649749248,  0.0609370570389346, 0.064007787889781, 0.148452886288055, -0.0155241411471386,  0.0219387752331864, 0.194820922135834, -0.0351768185925551, 0.0864241231009591,  -0.303251621871439, 0.0333004793813178, 0.0339146255514870, 0.0646219340599502,  -0.044389011145094, -0.211743842516218, -0.0189019450830696,  0.0348358448067410, 0.0437409642741953, -0.146644348478276, -0.0225868221040852,  0.0437409642741953, 0.0446621835294492, 0.144768009267039, -0.102118751141005,  -0.179501168582332, -0.106724847417274, 0.0127265826806475, -0.19792555368741,  -0.135896790500314, 0.0667714456555426, -0.127912890288114, -0.0173665796576464,  0.195742141391088, -0.195468969006733, 0.270975047236823, -0.134361425074891,  -0.0284212107206932, 0.112218262248068), assign = 0:1, .Dim = c(60L,  2L), .Dimnames = list(c("1", "2", "3", "4", "5", "6", "7", "8",  "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19",  "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30",  "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41",  "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52",  "53", "54", "55", "56", "57", "58", "59", "60"), c("(Intercept)",  "CRSP"))), qraux = c(1.12909944487358, 1.19267141054024), pivot = 1:2,      tol = 1e-07, rank = 2L), .Names = c("qr", "qraux", "pivot",  "tol", "rank"), class = "qr")'''
loc_fit.method = 'maximum likelihood'
loc_fit.formula = '''m.marietta ~ CRSP'''
loc_fit.terms = '''m.marietta ~ CRSP'''
loc_fit.iter = 7
loc_fit.call = '''tlm(lform = m.marietta ~ CRSP, data = mm, start = list(dof = 3),      estDof = TRUE)'''

#> s = summary(tfit3)
#> cat_items(s$loc.summary, prefix="loc_fit.")
# renamed coefficient -> table
loc_fit.table = np.array([
     -0.007248461, 1.263751, 0.008167043, 0.1901585, -0.8875258, 6.645774,
     0.3784616, 1.150536e-08
    ]).reshape(2,4, order='F')
loc_fit.table_rownames = ['(Intercept)', 'CRSP', ]
loc_fit.table_colnames = ['Estimate', 'Std. Error', 't value', 'Pr(>|t|)', ]
loc_fit.dispersion = 1
loc_fit.cov_unscaled = np.array([
     6.670059e-05, -0.0003174268, -0.0003174268, 0.03616026
    ]).reshape(2,2, order='F')
loc_fit.cov_unscaled_rownames = ['(Intercept)', 'CRSP', ]
loc_fit.cov_unscaled_colnames = ['(Intercept)', 'CRSP', ]
loc_fit.cov_scaled = np.array([
     6.670059e-05, -0.0003174268, -0.0003174268, 0.03616026
    ]).reshape(2,2, order='F')
loc_fit.cov_scaled_rownames = ['(Intercept)', 'CRSP', ]
loc_fit.cov_scaled_colnames = ['(Intercept)', 'CRSP', ]


scale_fit = Holder()
#> cat_items(tfit3$scale.fit, "scale_fit.")
scale_fit.coefficients = -5.983115
scale_fit.residuals = np.array([
     2.193327, -2.038408, -1.308573, -1.591579, -1.888103, -0.5330418,
     -1.326357, 5.653531, 1.632833, -0.2240806, -0.5364947, 1.187192,
     1.259662, 2.893897, 4.691185, -1.004751, -0.1011940, 0.7009929,
     1.255535, 1.224993, 1.096490, -1.675302, 1.584339, -1.926915,
     -0.3154245, -1.749184, -1.665424, -1.582882, -0.6238652, -1.774011,
     3.356624, -1.617496, -0.9346065, 4.74536, -0.4329547, -1.154602,
     -0.2722567, -0.6095562, -1.76094, -1.945082, 1.076003, -1.809181,
     -0.8315554, -2.028347, 1.98188, -0.2085298, -1.007913, -1.644641,
     0.702596, 0.2351866, 2.205829, -0.8726262, -1.703705, -1.211949,
     -1.398769, -2.049267, -1.451807, 3.775749, 2.295868, 1.062300
    ])
scale_fit.fitted_values = np.array([
     0.002520962, 0.002520962, 0.002520962, 0.002520962, 0.002520962,
     0.002520962, 0.002520962, 0.002520962, 0.002520962, 0.002520962,
     0.002520962, 0.002520962, 0.002520962, 0.002520962, 0.002520962,
     0.002520962, 0.002520962, 0.002520962, 0.002520962, 0.002520962,
     0.002520962, 0.002520962, 0.002520962, 0.002520962, 0.002520962,
     0.002520962, 0.002520962, 0.002520962, 0.002520962, 0.002520962,
     0.002520962, 0.002520962, 0.002520962, 0.002520962, 0.002520962,
     0.002520962, 0.002520962, 0.002520962, 0.002520962, 0.002520962,
     0.002520962, 0.002520962, 0.002520962, 0.002520962, 0.002520962,
     0.002520962, 0.002520962, 0.002520962, 0.002520962, 0.002520962,
     0.002520962, 0.002520962, 0.002520962, 0.002520962, 0.002520962,
     0.002520962, 0.002520962, 0.002520962, 0.002520962, 0.002520962
    ])
scale_fit.effects = np.array([
     32.31074, -1.595974, -1.087148, -1.284454, -1.491184, -0.5464648,
     -1.099547, 3.766681, 0.9635367, -0.3310637, -0.5488721, 0.6528456,
     0.70337, 1.842724, 3.095754, -0.8753306, -0.2453897, 0.3138777,
     0.7004929, 0.6791996, 0.5896097, -1.342824, 0.9297278, -1.518243,
     -0.3947467, -1.394333, -1.335937, -1.278391, -0.6097849, -1.411642,
     2.165327, -1.302523, -0.826427, 3.133524, -0.4766862, -0.979803,
     -0.364651, -0.599809, -1.402529, -1.530909, 0.5753267, -1.436162,
     -0.754582, -1.588959, 1.206885, -0.3202220, -0.8775351, -1.321448,
     0.3149953, -0.01087243, 1.363017, -0.7832157, -1.362626, -1.019784,
     -1.150031, -1.603544, -1.187008, 2.457531, 1.425790, 0.5657731
    ])
scale_fit.weights = np.array([
     0.4860579, 0.4860579, 0.4860579, 0.4860579, 0.4860579, 0.4860579,
     0.4860579, 0.4860579, 0.4860579, 0.4860579, 0.4860579, 0.4860579,
     0.4860579, 0.4860579, 0.4860579, 0.4860579, 0.4860579, 0.4860579,
     0.4860579, 0.4860579, 0.4860579, 0.4860579, 0.4860579, 0.4860579,
     0.4860579, 0.4860579, 0.4860579, 0.4860579, 0.4860579, 0.4860579,
     0.4860579, 0.4860579, 0.4860579, 0.4860579, 0.4860579, 0.4860579,
     0.4860579, 0.4860579, 0.4860579, 0.4860579, 0.4860579, 0.4860579,
     0.4860579, 0.4860579, 0.4860579, 0.4860579, 0.4860579, 0.4860579,
     0.4860579, 0.4860579, 0.4860579, 0.4860579, 0.4860579, 0.4860579,
     0.4860579, 0.4860579, 0.4860579, 0.4860579, 0.4860579, 0.4860579
    ])
scale_fit.formula = '''m.marietta ~ 1'''
scale_fit.terms = '''m.marietta ~ 1'''
scale_fit.iter = 7
scale_fit.call = '''tlm(lform = m.marietta ~ CRSP, data = mm, start = list(dof = 3),      estDof = TRUE)'''

res_t_dfest.loc_fit = loc_fit
res_t_dfest.scale_fit = scale_fit
