#Richter Scale
#Daniel Jaffe
#The program converts the Richter scale value of the earthquake to joules of a comparsion
#Last motified 2/18/24

# This is the subroutine for the conversion for earthquakes to joules equilvalents of comparsions
def converter_for_earthquakes(earthquake_magnitude_richter,richter_in_Joules,tntexplosion,kraktoa_eruptions,hiroshima_bombing):
    if earthquake_magnitude_richter<=0:
        return("Richter scale cannot be a negative number.")
    elif earthquake_richter> 10:
        return("Richter scale does not extend beyond a practical maximum value of 10.0")
    else:
        richter_in_Joules = 10**(1.5*earthquake_richter+4.8)
        tntexplosion = richter_in_Joules/(4.184*(10**9))
        kraktoa_eruptions = richter_in_Joules/(8*(10**17))
        hiroshimabombing = richter_in_Joules/(6.3*(10**13))
        return ("A " + "{:,.4f}".format(earthquake_magnitude_richter) + " magnitude earthquake releases " + "{:,.4f}".format(richter_in_Joules) + " joules of energy."
                +'\n' + "This is equivalent to " + "{:,.4f}".format(tntexplosion) + " metric tons of exploded TNT. "
                +'\n' +"This is equivalent to " + "{:,.4f}".format(kraktoa_eruptions) + " krakatoa eruptions and " + "{:,.4f}".format(hiroshimabombing) + " Hiroshima bombs.")


#Main program for richter scale program
earthquake_richter = 0
richter_in_Joules = 0
tntexplosion=0
kraktoa_eruptions = 0
hiroshima_bombing=0
while  0 <= earthquake_richter <= 10:
    earthquake_richter = float(input("Input a number on the Richter scale: "))
    earthquake_richter_conversion = converter_for_earthquakes(earthquake_richter,richter_in_Joules,tntexplosion,kraktoa_eruptions,hiroshima_bombing)
    print(earthquake_richter_conversion)
