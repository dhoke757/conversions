# Main Project File
import sys
#Show title and available units
print ("Unit converter."
	"\nAvailable units:" +
	"\n[cm] - centimeters" +
	"\n[m] - meters" +
	"\n[km] - kilometers" +
	"\n[in] - inches" +
	"\n[ft] - feet" + 
	"\n[yd] - yard") 

#input units requested & enter value
unit1 = input("Which unit would you like to convert from?: ")
unit1 = unit1.lower()
unit2 = input("Which unit would you like to convert to?: ")
unit2 = unit2.lower()
val = input("Enter your value: ")

#<<<<<<<<<<<<<<<<<<< cm - m - km >>>>>>>>>>>>>>>>>>>>>
#[=== cm to m ===]
if (unit1 == "cm" and unit2 == "m"):
	ans = round(float(val)/100,2)

#[=== m to cm ===]
elif unit1 == "m" and unit2 == "cm":
	ans = round(float(val)*100,2)

#[=== km to m ===]
elif unit1 == "km" and unit2 == "m":
	ans = round(float(val)*1000,2)

#[=== m to km ===]	
elif unit1 == "m" and unit2 == "km":
	ans = round(float(val)/1000,2)

#[=== cm to km ===]	
elif unit1 == "cm" and unit2 == "km":
	ans = round(float(val)/100000,2)	    

#[=== km to cm ===]	
elif unit1 == "km" and unit2 == "cm":
	ans = round(float(val)*100000,2)

#<<<<<<<<<<<<<<<<<<<               >>>>>>>>>>>>>>>>>>>>

#<<<<<<<<<<<<<<<<<<< equal 2 self  >>>>>>>>>>>>>>>>>>>>
elif unit1 == unit2:
	ans = round(float(val),2)
#<<<<<<<<<<<<<<<<<<<               >>>>>>>>>>>>>>>>>>>>

#<<<<<<<<<<<<<<<<<<< in - ft - yd  >>>>>>>>>>>>>>>>>>>>
#[=== in to ft ===]
elif (unit1 == "in" and unit2 == "ft"):
	ans = round(float(val)/12,2)

#[=== in to yd ===]
elif (unit1 == "in" and unit2 == "yd"):
	ans = round(float(val)/36,2)

#[=== ft to in ===]
elif (unit1 == "ft" and unit2 == "in"):
	ans = round(float(val)*12,2)

#[=== ft to yd ===]
elif (unit1 == "ft" and unit2 == "yd"):
	ans = round(float(val)/3,2)

#[=== yd to ft ===]
elif (unit1 == "yd" and unit2 == "ft"):
	ans = round(float(val)*3,2)

#[=== yd to in ===]
elif (unit1 == "yd" and unit2 == "in"):
	ans = round(float(val)*36,2)
#<<<<<<<<<<<<<<<<<<<              >>>>>>>>>>>>>>>>>>>>

print(val,unit1,"converts to",ans,unit2)