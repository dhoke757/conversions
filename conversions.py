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
#<<<<<<<<<<<<<<<<<<               >>>>>>>>>>>>>>>>>>>>

#<<<<<<<<<<<<<<<<<< cross-convert >>>>>>>>>>>>>>>>>>>>
#============== cm ===================================
elif (unit1 == "cm" and unit2 == "in"):
	ans = round(float(val)*0.393,2)

elif (unit1 == "cm" and unit2 == "ft"):
	ans = round(float(val)*0.032,2)

elif (unit1 == "cm" and unit2 == "yd"):
	ans = round(float(val)*0.01,2)
#============== m ====================================
elif (unit1 == "m" and unit2 == "in"):
	ans = round(float(val)*39.37,2)

elif (unit1 == "m" and unit2 == "ft"):
	ans = round(float(val)*3.28,2)

elif (unit1 == "m" and unit2 == "yd"):
	ans = round(float(val)*1.09,2)
#============== km ===================================
elif (unit1 == "km" and unit2 == "in"):
	ans = round(float(val)*39370.1,2)

elif (unit1 == "km" and unit2 == "ft"):
	ans = round(float(val)*3280.84,2)

elif (unit1 == "km" and unit2 == "yd"):
	ans = round(float(val)*1093.61,2)
#============== in ====================================
elif (unit1 == "in" and unit2 == "cm"):
	ans = round(float(val)*2.54,2)

elif (unit1 == "in" and unit2 == "m"):
	ans = round(float(val)*0.0254,2)

elif (unit1 == "in" and unit2 == "km"):
	ans = round(float(val)*0.0000254,2)
#============== ft ====================================
elif (unit1 == "ft" and unit2 == "cm"):
	ans = round(float(val)*30.48,2)

elif (unit1 == "ft" and unit2 == "m"):
	ans = round(float(val)*0.3048,2)

elif (unit1 == "ft" and unit2 == "km"):
	ans = round(float(val)*0.0003048,2)
#============== yd ====================================
elif (unit1 == "yd" and unit2 == "cm"):
	ans = round(float(val)*91.44,2)

elif (unit1 == "yd" and unit2 == "m"):
	ans = round(float(val)*0.9144,2)

elif (unit1 == "yd" and unit2 == "km"):
	ans = round(float(val)*0.0009144,2)
#<<<<<<<<<<<<<<<<<<               >>>>>>>>>>>>>>>>>>>>
print(val,unit1,"converts to",ans,unit2)