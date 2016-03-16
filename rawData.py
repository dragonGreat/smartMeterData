#_*_ coding:utf-8 _*_
'''
@author:'dragon'
created on Wed. Mar 16 13:00:00 2016
'''
import numpy as np
import xlrd
import pickle
import scipy.io as sio
import matplotlib.pyplot as plt 
from pylab import *
# configuration 
# step:states of appliances ，dataGetNum:test number, plotFig:not used 
totalDev1 = [
    'fan', {'step': 3, 'dataGetNum': 2,'plotFig': 1},    
    'miphone',{'step':2,'dataGetNum':1,'plotFig':2},
    'monitor', {'step': 2, 'dataGetNum': 1,'plotFig': 3},
    'bus', {'step': 2, 'dataGetNum': 1, 'plotFig': 4}
]
totalDev2 = [
    'fan', {'step': 3, 'dataGetNum': 1,'plotFig': 1},  
    'lamp',{'step':1,'dataGetNum':1,'plotFig':2},
    'miphone',{'step':2,'dataGetNum':1,'plotFig':3},
    'monitor', {'step': 1, 'dataGetNum': 1,'plotFig': 4},
    'solderingIron', {'step': 3, 'dataGetNum': 1,'plotFig': 5},
    'mipad', {'step': 1, 'dataGetNum': 1,'plotFig': 6},
    'bus', {'step': 5, 'dataGetNum': 1,'plotFig': 7}
]
totalDev3 = [
    'fan', {'step': 4, 'dataGetNum': 1,'plotFig': 1},  
    'hairdryer', {'step': 2, 'dataGetNum': 1,'plotFig': 2},
    'kettle', {'step': 1, 'dataGetNum': 1,'plotFig': 3},
    'mipad', {'step': 1, 'dataGetNum': 1,'plotFig': 4},
    'pc', {'step': 1, 'dataGetNum': 1,'plotFig': 5},
    'bus', {'step': 15, 'dataGetNum': 1,'plotFig': 6}
]
totalDev4 = [
    'fan', {'step': 1, 'dataGetNum': 1,'plotFig': 1},  
    'blower', {'step': 1, 'dataGetNum': 1,'plotFig': 2},
    'kettle', {'step': 1, 'dataGetNum': 1,'plotFig': 3},
    'mipad', {'step': 1, 'dataGetNum': 1,'plotFig': 4},
    'pc', {'step': 1, 'dataGetNum': 1,'plotFig': 5},
    'honor', {'step': 1, 'dataGetNum': 1,'plotFig': 6}
]

flag_del0 = 0 #Whether to remove 0,defalut flag_del0 = 0,flag_del0=1 not used in this file.

def readExcel(totalDev, flag_del_0=flag_del0, flagSv2mat=0):
	##totalDev：config,flag_del_0=0,flqgSv2mat:not used
        allData = []
        j = 0  # index 
        for totalDevNum in range(len(totalDev) / 2):  # appliances
            for typeStep in range(totalDev[2 * totalDevNum + 1]['step']):  # steps
                for typeGetNum in range(totalDev[2 * totalDevNum + 1]['dataGetNum']): 
                    pathP = pre_path  + totalDev[2 * totalDevNum] + str(
                        typeStep + 1) + 'P' + str(
                        typeGetNum + 1) + '.xlsx'
                    pathPF = pre_path  + totalDev[2 * totalDevNum] + str(
                        typeStep + 1) + 'PF' + str(
                        typeGetNum + 1) + '.xlsx'
                    pathU = pre_path  + totalDev[2 * totalDevNum] + str(
                        typeStep + 1) + 'U' + str(
                        typeGetNum + 1) + '.xlsx'
                    pathI = pre_path  + totalDev[2 * totalDevNum] + str(
                        typeStep + 1) + 'I' + str(
                        typeGetNum + 1) + '.xlsx'
                    ###############################P######################################################################
                    dataP = xlrd.open_workbook(pathP)
                    tableP = dataP.sheets()[0]
                    P = tableP.col_values(3)[2:]
                    time = tableP.col_values(4)[2:]
                    ###############################PF######################################################################
                    dataPF = xlrd.open_workbook(pathPF)
                    tablePF = dataPF.sheets()[0]
                    PF = tablePF.col_values(3)[2:]
                    ###############################I######################################################################
                    dataI = xlrd.open_workbook(pathI)
                    tableI = dataI.sheets()[0]
                    I = tableI.col_values(3)[2:]
                    ###############################U######################################################################
                    dataU = xlrd.open_workbook(pathU)
                    tableU = dataU.sheets()[0]
                    U = tableU.col_values(3)[2:]
                    if flag_del_0:#not used in this file
                        for i in reversed(range(len(P))):# 
                            if P[i] == '000000':
                                del P[i]
                                del PF[i]
                                del I[i]
                                del U[i]
                                del time[i]
                        
                    allData.insert(2 * j, totalDev[2 * totalDevNum] + str(1 + typeStep))  # appliances name
                    allData.insert(2 * j + 1, {'P': P, 'PF': PF, 'I': I, 'U': U, 'time': time})  # the values
                    j = j + 1
        if 1 == flagSv2mat:
            # flagSv2mat=0,not used in this file
            print ('save allData to mat\n')
            sio.savemat('in readExcel, allData.mat', {'allData': allData})
        return allData


def all_metadata_save(data,flag_del_0=flag_del0):
        if(flag_del_0 ==1 ):
            output = open('allData.pkl', 'wb')
        else:
            output = open('allData_del0.pkl', 'wb')
        pickle.dump(data, output)
        output.close()


def load_metadata(flag_del_0=flag_del0):
        if flag_del_0:#去掉0       
            filename = 'allData.pkl'
        else:
            filename = 'allData_del0.pkl'
    	pkl_file = open(filename, 'rb')
    	alldata = pickle.load(pkl_file)
    	pkl_file.close()
    	return alldata



if __name__ == '__main__':
	totalDev = [totalDev1,totalDev2,totalDev3,totalDev4]
	data = {}
	for i in xrange(1,5):
		pre_path = './rawData'+str(i)+'/'  ##path of raw data
		data['data'+str(i)] = readExcel(totalDev[i-1])
	# print data['data4']
	all_metadata_save(data)
	allData = load_metadata()
	plt.figure(1,figsize=(9,6))
	plt.plot(allData['data1'][23]["P"])
	plt.show()
	



		


