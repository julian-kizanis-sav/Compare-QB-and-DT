print("Commpany:\tSAV Digital Environments\nDeveloper:\tJulian Kizanis\n\
Powered By:\tAnaconda\n\n")


#from pandas import DataFrame
import pandas as pd
#import os
import time
import csv
import re

#first match manufacturer
#Second match Accounting Item Name

QB = pd.read_csv("QB Exported.csv")

print("Are you analising Products (P) or Labor (L)?")
choice = input()
if choice == "P" or choice == "p":
	DT = pd.read_csv("Dtools Products.csv")
elif choice == "L" or choice == "l":
	DT = pd.read_csv("Dtools Labor.csv")
else:
	print("You must enter 'P' for Products or 'L' for labor")
#print(QB.loc[:, "Item"].head())
#print(DT.loc[:, "Accounting Item Name"].head())


#set(a).intersection(b)
MatchQB = []
MatchDT = []

matchIndexQBDT = 0
matchIndexDTQB = 0

QBindex = 0
DTindex = 0

QBindexLast = 0
DTindexLast = 0
QBItem = ""
DTItem = ""

BothApproved = []
BAindex = 0

ApprovedInQB = []
AiQBindex = 0

ApprovedInDT = []
ADTindex = 0

NeitherApproved = []
NAindex = 0

sizeOfQB = len(QB.loc[QBindex, "Item"])

for QBitem in QB.loc[:, "Item"]:
	DTindex = 0
	for DTItem in DT.loc[:, "Accounting Item Name"]:
		if DTItem == QBitem:
			MatchQB.insert(matchIndexQBDT, QBindex)
			MatchDT.insert(matchIndexQBDT, DTindex)
			DTindexLast = DTindex
			#print(f"Match[{matchIndexQBDT}][{QBindex}][{DTindex}]:\t{QBitem}")
			matchIndexQBDT += 1
		DTindex += 1
	QBindex += 1
			
if choice == "P" or choice == "p":	
	for matchIndex, (QBm, DTm) in enumerate(zip(MatchQB, MatchDT)):
		#print(QB.loc[QBm, "Active Status"], DT.loc[DTm, "Approved"])
		#time.sleep(.3)
		if QB.loc[QBm, "Active Status"] == "Active":
			#print(DT.loc[DTm, "Approved"])
			if DT.loc[DTm, "Approved"] == True and DT.loc[DTm, "Discontinued"] == False:
				BothApproved.insert(BAindex, matchIndex)
				BAindex += 1
			else:
				ApprovedInQB.insert(AiQBindex, matchIndex)
				AiQBindex += 1
		elif DT.loc[DTm, "Approved"] == True and DT.loc[DTm, "Discontinued"] == False:
			ApprovedInDT.insert(ADTindex, matchIndex)
			ADTindex += 1
		else:
			NeitherApproved.insert(NAindex, matchIndex)
			NAindex += 1
		
elif choice == "L" or choice == "l":	
	for matchIndex, (QBm, DTm) in enumerate(zip(MatchQB, MatchDT)):
		#print(QB.loc[QBm, "Active Status"], DT.loc[DTm, "Approved"])
		#time.sleep(.3)
		if QB.loc[QBm, "Active Status"] == "Active":
			#print(DT.loc[DTm, "Approved"])
			if DT.loc[DTm, "Discontinued"] == False:
				BothApproved.insert(BAindex, matchIndex)
				BAindex += 1
			else:
				ApprovedInQB.insert(AiQBindex, matchIndex)
				AiQBindex += 1
		elif DT.loc[DTm, "Discontinued"] == False:
			ApprovedInDT.insert(ADTindex, matchIndex)
			ADTindex += 1
		else:
			NeitherApproved.insert(NAindex, matchIndex)
			NAindex += 1
	
	
print(f"matchIndexQBDT:\t{matchIndexQBDT}")
print(f"BothApproved:\t{BAindex}")
print(f"ApprovedInQB:\t{AiQBindex}")
print(f"ApprovedInDT:\t{ADTindex}")
print(f"NeitherApproved:\t{NAindex}")
			
if choice == "P" or choice == "p":
	df1 = pd.DataFrame(columns = list(DT.columns))
	for index in ApprovedInDT:
		df1 = df1.append(DT.loc[[MatchDT[index]],:])
			
	export_csv = df1.to_csv ('Approved in DT Only (DT format).csv', header=True) #Don't forget to add '.csv' at the end of the path

	df2 = pd.DataFrame(columns = list(DT.columns))
	for index in ApprovedInQB:
		df2 = df2.append(DT.loc[[MatchDT[index]],:])
			
	export_csv = df2.to_csv ('Approved in QB Only (DT format).csv', header=True) #Don't forget to add '.csv' at the end of the path	


	df3 = pd.DataFrame(columns = list(QB.columns))
	for index in ApprovedInDT:
		df3 = df3.append(QB.loc[[MatchQB[index]],:])
			
	export_csv = df3.to_csv ('Approved in DT Only (QB format).csv', header=True) #Don't forget to add '.csv' at the end of the path

	df4 = pd.DataFrame(columns = list(QB.columns))
	for index in ApprovedInQB:
		df4 = df4.append(QB.loc[[MatchQB[index]],:])
			
	export_csv = df4.to_csv ('Approved in QB Only (QB format).csv', header=True) #Don't forget to add '.csv' at the end of the path	






















