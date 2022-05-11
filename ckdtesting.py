import csv
import numpy as np
from neuralnet import NeuralNet

#Read the csv file
file = open('ckddata.csv')
filereader = csv.reader(file)

#Headings
header = []
header = next(filereader)

#Create separate lists of records for each heading
#Assigning variables
#Age in Years
age = []
#Diastolic Blood Pressure in mm/Hg
bp = []
#Specific Gravity of Urine (one of 1.005,1.010,1.015,1.020,1.025)
sg = []
#Albumin in Urine (on a 5-point scale)
al = []
#Sugar in Urine (on a 5-point scale)
sug = []
#Red Blood Cells in Urine (normal or abnormal)
rbcu = []
#Pus Cell in Urine (normal or abnormal)
pus = []
#Pus Cell Clumps in Urine (present or not present)
pcc = []
#Bacteria in Urine (present or not present)
bac = []
#Blood Glucose Random (mgs/dl)
bgr = []
#Blood Urea (mgs/dl)
bu = []
#Serum Creatinine (mgs/dl)
sc = []
#Sodium (mEq/L)
na = []
#Potassium (mEq/L)
k = []
#Hemoglobin (gms)
hem = []
#Packed Cell Volume (%)
pcv = []
#White Blood Cell Count (cells/cumm)
wbc = []
#Red Blood Cell Count (millions/cmm)
rbc = []
#Hypertension (yes or no)
hyp = []
#Diabetes Mellitus (yes or no)
dia = []
#Coronary Artery Disease (yes or no)
cad = []
#Appetite (good or bad)
app = []
#Pedal Edema (yes or no)
ed = []
#Anemia (yes or no)
an = []
#Chronic Kidney Disease (1 for yes, 0 for no)
ckd = []
#Assigning data
rows = []
for row in filereader:
    rows.append(row)
i = 0
while i < len(rows):
    #Shuffle the data so that there are ckd patients in testing and training data 
    if i == len(rows)-2:
        i = 1
    row = rows[i]
    i+=2
    #Make everything a 1 or a 0
    age.append(float(row[0])/50)
    bp.append(float(row[1])/74)
    sg.append(float(row[2]))
    al.append(float(row[3]))
    sug.append(float(row[4]))
    if row[5] == "normal":
        rbcu.append(0)
    if row[5] == "abnormal":
        rbcu.append(1)
    if row[6] == "normal":
        pus.append(0)
    if row[6] == "abnormal":
        pus.append(1)
    if row[7] == "notpresent":
        pcc.append(0)
    if row[7] == "present":
        pcc.append(1)
    if row[8] == "notpresent":
        bac.append(0)
    if row[8] == "present":
        bac.append(1)
    bgr.append(float(row[9])/131)
    bu.append(float(row[10])/52)
    sc.append(float(row[11])/2)
    na.append(float(row[12])/138)
    k.append(float(row[13])/4)
    hem.append(float(row[14])/14)
    pcv.append(float(row[15])/42)
    wbc.append(float(row[16])/8475)
    rbc.append(float(row[17])/5)
    if row[18] == "no":
        hyp.append(0)
    if row[18] == "yes":
        hyp.append(1)
    if row[19] == "no":
        dia.append(0)
    if row[19] == "yes":
        dia.append(1)
    if row[20] == "no":
        cad.append(0)
    if row[20] == "yes":
        cad.append(1)
    if row[21] == "good":
        app.append(0)
    if row[21] == "poor":
        app.append(1)
    if row[22] == "no":
        ed.append(0)
    if row[22] == "yes":
        ed.append(1)
    if row[23] == "no":
        an.append(0)
    if row[23] == "yes":
        an.append(1)
    ckd.append(float(row[24]))

file.close()

traininputs = [age[0:int(len(age)/2)], 
               bp[0:int(len(age)/2)], 
               sg[0:int(len(age)/2)], 
               al[0:int(len(age)/2)], 
               sug[0:int(len(age)/2)], 
               rbcu[0:int(len(age)/2)], 
               pus[0:int(len(age)/2)], 
               pcc[0:int(len(age)/2)], 
               bac[0:int(len(age)/2)], 
               bgr[0:int(len(age)/2)], 
               bu[0:int(len(age)/2)], 
               sc[0:int(len(age)/2)], 
               na[0:int(len(age)/2)], 
               k[0:int(len(age)/2)], 
               hem[0:int(len(age)/2)], 
               pcv[0:int(len(age)/2)], 
               wbc[0:int(len(age)/2)], 
               rbc[0:int(len(age)/2)], 
               hyp[0:int(len(age)/2)], 
               dia[0:int(len(age)/2)], 
               cad[0:int(len(age)/2)], 
               app[0:int(len(age)/2)], 
               ed[0:int(len(age)/2)], 
               an[0:int(len(age)/2)]]
trainoutputs = [np.array(ckd[0:int(len(age)/2)])]
testinputs = [age[int(len(age)/2):int(len(age)-1)], 
               bp[int(len(age)/2):int(len(age)-1)], 
               sg[int(len(age)/2):int(len(age)-1)], 
               al[int(len(age)/2):int(len(age)-1)], 
               sug[int(len(age)/2):int(len(age)-1)], 
               rbcu[int(len(age)/2):int(len(age)-1)], 
               pus[int(len(age)/2):int(len(age)-1)], 
               pcc[int(len(age)/2):int(len(age)-1)], 
               bac[int(len(age)/2):int(len(age)-1)], 
               bgr[int(len(age)/2):int(len(age)-1)], 
               bu[int(len(age)/2):int(len(age)-1)], 
               sc[int(len(age)/2):int(len(age)-1)], 
               na[int(len(age)/2):int(len(age)-1)], 
               k[int(len(age)/2):int(len(age)-1)], 
               hem[int(len(age)/2):int(len(age)-1)], 
               pcv[int(len(age)/2):int(len(age)-1)], 
               wbc[int(len(age)/2):int(len(age)-1)], 
               rbc[int(len(age)/2):int(len(age)-1)], 
               hyp[int(len(age)/2):int(len(age)-1)], 
               dia[int(len(age)/2):int(len(age)-1)], 
               cad[int(len(age)/2):int(len(age)-1)], 
               app[int(len(age)/2):int(len(age)-1)], 
               ed[int(len(age)/2):int(len(age)-1)], 
               an[int(len(age)/2):int(len(age)-1)]]
testoutputs = [np.array(ckd[int(len(age)/2):int(len(age)-1)])]
inputs = np.array(traininputs).astype(float).T
outputs = np.array(trainoutputs).astype(float).T
testinputs = np.array(testinputs).astype(float).T
tesoutputs = np.array(testoutputs).astype(float).T
neural_network = NeuralNet(24)
neural_network.train(outputs, inputs, 100000)
results = neural_network.calc_output(testinputs)
normalize = []
for element in results:
    if element < .5:
        normalize.append(0)
    else:
        normalize.append(1)
print(normalize)
print(testoutputs)
error = np.array(normalize) - testoutputs
print(error)


