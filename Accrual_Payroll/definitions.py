

# Department : [GL Account(Accrued Payroll), GL Account(Accrued Payroll Tax)]

pay_mappings = {
    100100 : [52010, 52200], 
    100200 : [52010, 52200], 
    100300 : [52010, 52200], 
    100400 : [60010, 60200], 
    200100 : [60010, 60200], 
    200200 : [60010, 60200], 
    300100 : [60010, 60200], 
    300200 : [60010, 60200], 
    300250 : [60010, 60200], 
    300300 : [60010, 60200], 
    300400 : [60010, 60200], 
    300500 : [60010, 60200], 
    400100 : [60010, 60200], 
    700100 : [60010, 60200], 
    700110 : [60010, 60200], 
    700120 : [60010, 60200], 
    700200 : [60010, 60200], 
    700205 : [60010, 60200], 
    700210 : [60010, 60200], 
    700215 : [60010, 60200], 
    700230 : [60010, 60200], 
    700300 : [60010, 60200], 
    700305 : [60010, 60200], 
    700310 : [60010, 60200], 
    700315 : [60010, 60200], 
    700320 : [60010, 60200], 
    700325 : [60010, 60200], 
    700326 : [60010, 60200], 
    700327 : [60010, 60200], 
    700330 : [60010, 60200], 
    700335 : [60010, 60200], 
    700340 : [60010, 60200], 
    700345 : [60010, 60200], 
    700350 : [60010, 60200], 
    700355 : [60010, 60200], 
    700360 : [60010, 60200], 
    701000 : [60010, 60200], 
    701100 : [60010, 60200], 
    701200 : [60010, 60200], 
    701210 : [60010, 60200], 
    702010 : [60010, 60200], 
    702100 : [60010, 60200], 
    702300 : [60010, 60200], 
    702400 : [60010, 60200], 
    702410 : [60010, 60200], 
    702415 : [60010, 60200], 
    702420 : [60010, 60200], 
    703000 : [60010, 60200], 
    704000 : [60010, 60200], 
    704100 : [60010, 60200], 
    704500 : [60010, 60200], 
    704505 : [60010, 60200], 
    705000 : [60010, 60200], 
    705500 : [60010, 60200], 
    705600 : [60010, 60200], 

}


locations_dict = {
    'The Oncology Institute, Inc.' : 101, \
    'Parent' : 100, \
    'Acquisition' : 200, \
    'MGMT' : 300, \
    'Cerritos Corporate' : 9001, \
    'Florida Corporate' : 9002, \
    'TOI' : 400, \
    'Clinical Research' : 410, \
    'TOI FL' : 500, \
    'TOI TX' : 600, \
    'TOI North' : 'North', \
    'California North' : 'CA-North', \
    'Pod 1' : 1, \
    'TOI Downey' : 1001, \
    'TOI Lynwood' : 1002, \
    'TOI Whittier' : 1003, \
    'Pod 2' : 2, \
    'TOI Lakewood' : 1004, \
    'TOI Los Alamitos' : 1005, \
    'TOI Torrance' : 1006, \
    'TOI Culver City' : 1048, \
    'Pod 3' : 3, \
    'TOI Downtown LA' : 1007, \
    'TOI East LA' : 1008, \
    'TOI Montebello' : 1009, \
    'TOI City West' : 1047, \
    'Pod 4' : 4, \
    'TOI Mission Hills' : 1010, \
    'TOI Northridge' : 1011, \
    'TOI Valencia' : 1012, \
    'TOI Burbank' : 1016, \
    'TOI Glendale' : 1017, \
    'Pod 5' : 5, \
    'TOI Simi Valley' : 1013, \
    'TOI Thousand Oaks' : 1014, \
    'TOI West Hills' : 1015, \
    'Pod 6' : 6, \
    'TOI Pasadena' : 1018, \
    'TOI West Covina' : 1028, \
    'TOI San Gabriel' : 1042, \
    'TOI Alhambra' : 1049, \
    'TOI Hacienda Heights' : 1050, \
    'TOI Monterey Park' : 1054, \
    'TOI South' : 'South', \
    'California South' : 'CA-South', \
    'Pod 7' : 7, \
    'TOI Anaheim' : 1019, \
    'TOI Fountain Valley' : 1020, \
    'TOI Mission Viejo' : 1021, \
    'TOI Santa Ana' : 1022, \
    'Pod 8' : 8, \
    'TOI Corona' : 1023, \
    'TOI Riverside2' : 1025, \
    'TOI Riverside' : 1025, \
    'TOI San Bernardino' : 1026, \
    'TOI Upland' : 1027, \
    'TOI Victorville' : 1046, \
    'Pod 9' : 9, \
    'Pod 10' : 10, \
    'TOI Hemet' : 1029, \
    'TOI Murrieta' : 1030, \
    'TOI Temecula' : 1031, \
    'Pod 15' : 15, \
    'TOI Vista' : 1043, \
    'TOI Hillcrest' : 1044, \
    'TOI Chula Vista' : 1045, \
    'TOI Fresno' : 'Fresno', \
    'Pod 17' : 17, \
    'Fresno WCC' : 1051, \
    'RadOnc' : 'RadOnc', \
    'Pod R1' : 'R1', \
    'TOI R1- Lakewood' : 1801, \
    'Nevada' : 'NV', \
    'Pod 11' : 11, \
    'TOI Henderson' : 1032, \
    'TOI Las Vegas' : 1033, \
    'TOI Spring Valley' : 1034, \
    'TOI Henderson 2' : 1052, \
    'TOI Spring Valley 2' : 1053, \
    'Arizona' : 'AZ', \
    'Pod 12' : 12, \
    'TOI Green Valley' : 1035, \
    'TOI Oro Valley' : 1036, \
    'TOI East Tucson' : 1037, \
    'TOI West Tucson' : 1038, \
    'Florida' : 'Florida', \
    'Pod 13' : 13, \
    'TOI FL Mid-Pinellas' : 2001, \
    'TOI FL Downtown St. Pete' : 2002, \
    'Pod 14' : 14, \
    'TOI FL Tampa-Habana' : 2003, \
    'TOI FL Brandon' : 2004, \
    'TOI FL Plant City' : 2005, \
    'TOI FL Lakeland' : 2006, \
    'Pod 18' : 18, \
    'TOI Fort Lauderdale-17th Street' : 2007, \
    'TOI Fort Lauderdale-Imperial Point' : 2008, \
    'TOI Plantation' : 2009, \
    'Pod 19' : 19, \
    'TOI North Miami' : 2015, \
    'TOI South Miami' : 2010, \
    'TOI South Miami-West' : 2011, \
    'Texas' : 'Texas', \
    'Pod 16' : 16, \
    'TOI TX Central Austin' : 3001, \
    'TOI TX Southwest Austin' : 3002, \
    'TOI Hospitals' : 'Hospitals', \
    'TOI Closed Clinics' : 'Closed', \
    'Pod 99' : 99, \
    'TOI Alhambra CLOSED' : 1040, \
    'TOI San Pedro CLOSED' : 1041, \
    'TOI Riverside CLOSED' : 1024, \
    'TOI Marana CLOSED' : 1039, \
    'TOI Chino/Chino Hills' : 1055, \
    'TOI Hollywood' : 2014, \
    'TOI R1-Downey RadOnce' : 1802, \
    'TOI R-1 Pomona RadOnc' : 1803, \
    'TOI R1-Covina RadOnc' : 1804, \
    'TOI R1-Victorville RadOnc' : 1805, \
    'TOI R-1 Hemet RadOnc' : 1806, \
    'TOI Palm Desert' : 1057, \
    'TOI Hialeah' : 2013, \
    'TOI PH1-Westminster' : 4001, \
    'TOI Temecula 2' : 1058

}