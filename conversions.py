# Main Project File
import sys
#Show title and available units
print ("Unit converter."
	"\nAvailable units:" +
	"\n[cm] - centimeters" +
	"\n[m] - meters" +
	"\n[km] - kilometers") 

#input units requested & enter value
unit1 = input("Which unit would you like to convert from?: ")
unit2 = input("Which unit would you like to convert to?: ")
val = input("Enter your value: ")

#[=== cm to m ===]
if (unit1 == "cm" and unit2 == "m"):
	ans = float(val)/100

#[=== m to cm ===]
elif unit1 == "m" and unit2 == "cm":
	ans = float(val)*100

#[=== km to m ===]
elif unit1 == "km" and unit2 == "m":
	ans = float(val)*1000

#[=== m to km ===]	
elif unit1 == "m" and unit2 == "km":
	ans = float(val)/1000

#[=== cm to km ===]	
elif unit1 == "cm" and unit2 == "km":
	ans = float(val)/100000	    

#[=== km to cm ===]	
elif unit1 == "km" and unit2 == "cm":
	ans = float(val)*100000

#[=== km to cm ===]	
elif unit1 == unit2:
	ans = float(val)

print(val,unit1,"converts to",ans,unit2)