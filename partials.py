print "TVG'S WONDROUS PARTIALS QUOTING MACHINE"

print " "
print " "

print "Let's determine the rate that XPO will pay for your load"

print " "

print "I will need the shipper ZIP, receiver ZIP, linear footage, and the weight of the load"

print "Make sure that you enter them in that order, separated by commas"

print "**For standard skids, footage will equal skid count multiplied by 2**"

print " "

info = raw_input("Please enter: ")

pieces = info.split(",")

if len(pieces) != 4:
  print "WRONG NUMBER OF INPUTS! RATE MAY NOT BE VALID"
  print " SHIPPER ZIP, COMMA, CONSIGNEE ZIP, COMMA, LINEAR FOOTAGE, COMMA, WEIGHT. ENTER NOTHING BESIDES FOR THAT"


ship = int(pieces[0])

cons = int(pieces[1])

footage = int(pieces[2])

if footage / 2 != 0:
  footage = footage + 1

weight = int(pieces[3])

if weight > (footage * 700):
  footage = (weight / 700)

def city(ship):
  if ship >= 60000 and ship <=60899:
    return "Chicago"
  elif ship >= 75000 and ship <= 75999:
    return "Dallas"
  elif ship >= 76000 and ship <= 76299:
    return "Dallas"
  elif ship >= 90000 and ship <= 90999:
    return "Los Angeles"
  elif ship >= 91100 and ship <= 91299:
    return "Los Angeles"
  elif ship >= 91400 and ship <= 91899:
    return "Los Angeles"
  elif ship >= 92400 and ship <= 92999:
    return "Los Angeles"
  elif ship >= 94000 and ship <= 94999:
    return "Northern California"
  elif ship >= 95000 and ship <= 95399:
    return "Northern California"
  elif ship >= 95600 and ship <= 95999:
    return "Northern California"
  elif ship >= 95400 and ship <= 95599:
    return "Remote northern California"
  elif ship >= 96000 and ship <= 96199:
    return "Remote northern California"
  elif ship >= 91000 and ship <= 91099:
    return "Central California"
  elif ship >= 91300 and ship <= 91399:
    return "Central California"
  elif ship >= 91900 and ship <= 92399:
    return "Central California"
  elif ship >= 93000 and ship <= 93999:
    return "Central California"
  elif ship >= 97000 and ship <= 97299:
    return "Portland"
  elif ship >= 98600 and ship <= 98699:
    return "Portland"
  elif ship >= 98000 and ship <= 98499:
    return "Seattle"
  elif ship >= 97300 and ship <= 97999:
    return "Remote PNW"
  elif ship >= 98700 and ship <= 98999:
    return "Remote PNW"
  elif ship >= 98500 and ship <= 98599:
    return "Remote PNW"
  elif ship >= 82000 and ship <= 83999:
    return "Remote PNW"
  elif ship >= 59000 and ship <= 59999:
    return "Remote PNW"
  elif ship >= 80000 and ship <= 81999:
    return "Rocky Mountains"
  elif ship >= 84000 and ship <= 84999:
    return "Rocky Mountains"
  elif ship >= 85100 and ship <= 89099:
    return "Rocky Mountains"
  elif ship >= 89200 and ship <= 89999:
    return "Rocky Mountains"
  elif ship >= 85000 and ship <= 85099:
    return "Phoenix/Las Vegas"
  elif ship >= 89100 and ship <= 89199:
    return "Phoenix/Las Vegas"
  elif ship >= 76000 and ship <= 76299:
    return "Dallas"
  elif ship >= 75400 and ship <= 75999:
    return "Eastern Texas"
  elif ship >= 76300 and ship <= 78799:
    return "Eastern Texas"
  elif ship >= 78900 and ship <= 78999:
    return "Eastern Texas"
  elif ship >= 79000 and ship <= 79999:
    return "Western Texas"
  elif ship >= 73000 and ship <= 74999:
    return "Oklahoma"
  elif ship >= 70000 and ship <= 72999:
    return "Arkansas/Louisiana"
  elif ship >= 30000 and ship <= 30399:
    return "Atlanta"
  elif ship >= 30400 and ship <= 31999:
    return "the Gulf of Mexico"
  elif ship >= 32300 and ship <= 32599:
    return "the Gulf of Mexico"
  elif ship >= 39500 and ship <= 39599:
    return "the Gulf of Mexico"
  elif ship >= 35000 and ship <= 39499:
    return "the Southeast"
  elif ship >= 39600 and ship <= 39999:
    return "the Southeast"
  elif ship >= 20000 and ship <= 26999:
    return "the Mid-Atlantic region"
  elif ship >= 27000 and ship <= 27799:
    return "the Carolinas"
  elif ship >= 28000 and ship <= 28299:
    return "the Carolinas"
  elif ship >= 28600 and ship <= 29999:
    return "the Carolinas"
  elif ship >= 27800 and ship <= 27999:
    return "coastal North Carolina"
  elif ship >= 28300 and ship <= 28599:
    return "coastal North Carolina"
  elif ship >= 32000 and ship <= 32299:
    return "Northeastern Florida"
  elif ship >= 32600 and ship <= 32699:
    return "Northeastern Florida"
  elif ship >= 32700 and ship <= 34999:
    return "South Florida"
  elif ship >= 7000 and ship <= 8999:
    return "New Jersey"
  elif ship >= 18900 and ship <= 19199:
    return "New Jersey"
  elif ship >= 18000 and ship <= 18199:
    return "New Jersey"
  elif ship >= 15000 and ship <= 17999:
    return "Pennsylvania"
  elif ship >= 18200 and ship <= 18899:
    return "Pennsylvania"
  elif ship >= 19200 and ship <= 19699:
    return "Pennsylvania"
  elif ship >= 12000 and ship <= 14999:
    return "New York state"
  elif ship >= 10000 and ship <= 11999:
    return "the island"
  elif ship >= 0 and ship <= 2999:
    return "New England"
  elif ship >= 6000 and ship <= 6999:
    return "New England"
  elif ship >= 3900 and ship <= 4999:
    return "Maine"
  elif ship >= 3000 and ship <= 3899:
    return "New Hampshire/Vermont"
  elif ship >= 5000 and ship <= 5999:
    return "New Hampshire/Vermont"
  elif ship >= 44000 and ship <= 44599:
    return "Cleveland area"
  elif ship >= 44700 and ship <= 44799:
    return "Cleveland area"
  elif ship >= 43000 and ship <= 43999:
    return "Ohio"
  elif ship >= 44600 and ship <= 44699:
    return "Ohio"
  elif ship >= 44800 and ship <= 45999:
    return "Ohio"
  elif ship >= 40000 and ship <= 42999:
    return "Kentucky"
  elif ship >= 49600 and ship <= 49999:
    return "remote northern Michigan"
  elif ship >= 48000 and ship <= 49599:
    return "lower Michigan"
  elif ship >= 46000 and ship <= 47999:
    return "Indiana"
  elif ship >= 60900 and ship <= 61999:
    return "rural Illinois"
  elif ship >= 62300 and ship <= 62999:
    return "rural Illinois"
  elif ship >= 62000 and ship <= 62299:
    return "St. Louis"
  elif ship >= 63000 and ship <= 63399:
    return "St. Louis"
  elif ship >= 53100 and ship <= 53499:
    return "Milwaukee"
  elif ship >= 53000 and ship <= 53499:
    return "rural Wisconsin"
  elif ship >= 53500 and ship <= 53999:
    return "rural Wisconsin"
  elif ship >= 54100 and ship <= 54999:
    return "rural Wisconsin"
  elif ship >= 54000 and ship <= 54199:
    return "the Twin Cities"
  elif ship >= 55000 and ship <= 55599:
    return "the Twin Cities"
  elif ship >= 55600 and ship <= 58999:
    return "rural MN/Dakotas"
  elif ship >= 50000 and ship <= 52999:
    return "Iowa"
  elif ship >= 64000 and ship <= 64399:
    return "Kansas City"
  elif ship >= 66100 and ship <= 66299:
    return "Kansas City"
  elif ship >= 63400 and ship <= 63999:
    return "rural Missouri/ Kansas/Nebraska"
  elif ship >= 64400 and ship <= 66099:
    return "rural Missouri/ Kansas/Nebraska"
  elif ship >= 66300 and ship <= 69999:
    return "rural Missouri/ Kansas/Nebraska"
  else:
    return "off the map"




def skidrate(ship, cons):
  if (city(ship) == "Chicago") and (city(cons) == "Dallas"):
    return 100
  elif (city(ship) == "Chicago") and (city(cons) == "Northern California"):
    return 150
  elif (city(ship) == "Chicago") and (city(cons) == "Remote northern California"):
    return 175
  elif (city(ship) == "Chicago") and (city(cons) == "Central California"):
    return 150
  elif (city(ship) == "Chicago") and (city(cons) == "Portland"):
    return 200
  elif (city(ship) == "Chicago") and (city(cons) == "Seattle"):
    return 200
  elif (city(ship) == "Chicago") and (city(cons) == "Remote PNW"):
    return 200
  elif (city(ship) == "Chicago") and (city(cons) == "Rocky Mountains"):
    return 150
  elif (city(ship) == "Chicago") and (city(cons) == "Phoenix/Las Vegas"):
    return 150
  elif (city(ship) == "Chicago") and (city(cons) == "Eastern Texas"):
    return 125
  elif (city(ship) == "Chicago") and (city(cons) == "Western Texas"):
    return 150
  elif (city(ship) == "Chicago") and (city(cons) == "Los Angeles"):
    return 125
  elif (city(ship) == "Chicago") and (city(cons) == "Oklahoma"):
    return 110
  elif (city(ship) == "Chicago") and (city(cons) == "Arkansas/Louisiana"):
    return 100
  elif (city(ship) == "Chicago") and (city(cons) == "Atlanta"):
    return 100
  elif (city(ship) == "Chicago") and (city(cons) == "the Gulf of Mexico"):
    return 110
  elif (city(ship) == "Chicago") and (city(cons) == "the Southeast"):
    return 100
  elif (city(ship) == "Chicago") and (city(cons) == "the Mid-Atlantic region"):
    return 110
  elif (city(ship) == "Chicago") and (city(cons) == "the Carolinas"):
    return 100
  elif (city(ship) == "Chicago") and (city(cons) == "coastal North Carolina"):
    return 135
  elif (city(ship) == "Chicago") and (city(cons) == "Northeastern Florida"):
    return 125
  elif (city(ship) == "Chicago") and (city(cons) == "South Florida"):
    return 150
  elif (city(ship) == "Chicago") and (city(cons) == "New Jersey"):
    return 100
  elif (city(ship) == "Chicago") and (city(cons) == "Pennsylvania"):
    return 100
  elif (city(ship) == "Chicago") and (city(cons) == "New York state"):
    return 100
  elif (city(ship) == "Chicago") and (city(cons) == "the island"):
    return 125
  elif (city(ship) == "Chicago") and (city(cons) == "New England"):
    return 125
  elif (city(ship) == "Chicago") and (city(cons) == "Maine"):
    return 150
  elif (city(ship) == "Chicago") and (city(cons) == "New Hampshire/Vermont"):
    return 135
  elif (city(ship) == "Chicago") and (city(cons) == "Cleveland area"):
    return 95
  elif (city(ship) == "Chicago") and (city(cons) == "Ohio"):
    return 85
  elif (city(ship) == "Chicago") and (city(cons) == "Kentucky"):
    return 85
  elif (city(ship) == "Chicago") and (city(cons) == "remote northern Michigan"):
    return 100
  elif (city(ship) == "Chicago") and (city(cons) == "lower Michigan"):
    return 65
  elif (city(ship) == "Chicago") and (city(cons) == "Indiana"):
    return 65
  elif (city(ship) == "Chicago") and (city(cons) == "St. Louis"):
    return 50
  elif (city(ship) == "Chicago") and (city(cons) == "the Twin Cities"):
    return 75
  elif (city(ship) == "Chicago") and (city(cons) == "rural MN/Dakotas"):
    return 150
  elif (city(ship) == "Chicago") and (city(cons) == "Iowa"):
    return 100
  elif (city(ship) == "Chicago") and (city(cons) == "Kansas City"):
    return 100
  elif (city(ship) == "Chicago") and (city(cons) == "rural Missouri/ Kansas/Nebraska"):
    return 115
  elif (city(ship) == "Los Angeles") and (city(cons) == "Chicago"):
    return 125
  elif (city(ship) == "Los Angeles") and (city(cons) == "Dallas"):
    return 135
  elif (city(ship) == "Los Angeles") and (city(cons) == "Northern California"):
    return 75
  elif (city(ship) == "Los Angeles") and (city(cons) == "Central California"):
    return 75
  elif (city(ship) == "Los Angeles") and (city(cons) == "Portland"):
    return 150
  elif (city(ship) == "Los Angeles") and (city(cons) == "Seattle"):
    return 150
  elif (city(ship) == "Los Angeles") and (city(cons) == "Remote PNW"):
    return 165
  elif (city(ship) == "Los Angeles") and (city(cons) == "Rocky Mountains"):
    return 150
  elif (city(ship) == "Los Angeles") and (city(cons) == "Phoenix/Las Vegas"):
    return 75
  elif (city(ship) == "Los Angeles") and (city(cons) == "Eastern Texas"):
    return 150
  elif (city(ship) == "Los Angeles") and (city(cons) == "Western Texas"):
    return 125
  elif (city(ship) == "Los Angeles") and (city(cons) == "Oklahoma"):
    return 140
  elif (city(ship) == "Los Angeles") and (city(cons) == "Arkansas/Louisiana"):
    return 170
  elif (city(ship) == "Los Angeles") and (city(cons) == "Atlanta"):
    return 175
  elif (city(ship) == "Los Angeles") and (city(cons) == "the Gulf of Mexico"):
    return 200
  elif (city(ship) == "Los Angeles") and (city(cons) == "the Southeast"):
    return 175
  elif (city(ship) == "Los Angeles") and (city(cons) == "the Mid-Atlantic region"):
    return 215
  elif (city(ship) == "Los Angeles") and (city(cons) == "the Carolinas"):
    return 185
  elif (city(ship) == "Los Angeles") and (city(cons) == "coastal North Carolina"):
    return 200
  elif (city(ship) == "Los Angeles") and (city(cons) == "Northeastern Florida"):
    return 200
  elif (city(ship) == "Los Angeles") and (city(cons) == "South Florida"):
    return 215
  elif (city(ship) == "Los Angeles") and (city(cons) == "New Jersey"):
    return 200
  elif (city(ship) == "Los Angeles") and (city(cons) == "Pennsylvania"):
    return 200
  elif (city(ship) == "Los Angeles") and (city(cons) == "New York state"):
    return 215
  elif (city(ship) == "Los Angeles") and (city(cons) == "the island"):
    return 235
  elif (city(ship) == "Los Angeles") and (city(cons) == "New England"):
    return 235
  elif (city(ship) == "Los Angeles") and (city(cons) == "Maine"):
    return 275
  elif (city(ship) == "Los Angeles") and (city(cons) == "New Hampshire/Vermont"):
    return 260
  elif (city(ship) == "Los Angeles") and (city(cons) == "Cleveland area"):
    return 180
  elif (city(ship) == "Los Angeles") and (city(cons) == "Ohio"):
    return 180
  elif (city(ship) == "Los Angeles") and (city(cons) == "Kentucky"):
    return 180
  elif (city(ship) == "Los Angeles") and (city(cons) == "remote northern Michigan"):
    return 225
  elif (city(ship) == "Los Angeles") and (city(cons) == "lower Michigan"):
    return 170
  elif (city(ship) == "Los Angeles") and (city(cons) == "Indiana"):
    return 160
  elif (city(ship) == "Los Angeles") and (city(cons) == "St. Louis"):
    return 150
  elif (city(ship) == "Los Angeles") and (city(cons) == "the Twin Cities"):
    return 180
  elif (city(ship) == "Los Angeles") and (city(cons) == "rural MN/Dakotas"):
    return 200
  elif (city(ship) == "Los Angeles") and (city(cons) == "Iowa"):
    return 150
  elif (city(ship) == "Los Angeles") and (city(cons) == "Kansas City"):
    return 135
  elif (city(ship) == "Los Angeles") and (city(cons) == "rural Missouri/ Kansas/Nebraska"):
    return 150
  elif (city(ship) == "Dallas") and (city(cons) == "Los Angeles"):
    return 100
  elif (city(ship) == "Dallas") and (city(cons) == "Northern California"):
    return 175
  elif (city(ship) == "Dallas") and (city(cons) == "Northern California"):
    return 175
  elif (city(ship) == "Dallas") and (city(cons) == "Central California"):
    return 175
  elif (city(ship) == "Dallas") and (city(cons) == "Portland"):
    return 250
  elif (city(ship) == "Dallas") and (city(cons) == "Seattle"):
    return 250
  elif (city(ship) == "Dallas") and (city(cons) == "Remote PNW"):
    return 265
  elif (city(ship) == "Dallas") and (city(cons) == "Rocky Mountains"):
    return 250
  elif (city(ship) == "Dallas") and (city(cons) == "Atlanta"):
    return 75
  elif (city(ship) == "Dallas") and (city(cons) == "the Carolinas"):
    return 100
  elif (city(ship) == "Chicago") and (city(cons) == "coastal North Carolina"):
    return 150
  elif (city(ship) == "Dallas") and (city(cons) == "the Mid-Atlantic region"):
    return 125
  elif (city(ship) == "Dallas") and (city(cons) == "New Jersey"):
    return 125
  elif (city(ship) == "Dallas") and (city(cons) == "Pennsylvania"):
    return 125
  elif (city(ship) == "Dallas") and (city(cons) == "the island"):
    return 175
  elif (city(ship) == "Dallas") and (city(cons) == "New England"):
    return 150
  elif (city(ship) == "Dallas") and (city(cons) == "Cleveland area"):
    return 125
  elif (city(ship) == "Northern California") and (city(cons) == "Chicago"):
    return 150
  elif (city(ship) == "Northern California") and (city(cons) == "Dallas"):
    return 175
  elif (city(ship) == "Northern California") and (city(cons) == "Eastern Texas"):
    return 200
  elif (city(ship) == "Northern California") and (city(cons) == "Atlanta"):
    return 250
  elif (city(ship) == "Northern California") and (city(cons) == "the Gulf of Mexico"):
    return 275
  elif (city(ship) == "Northern California") and (city(cons) == "the Southeast"):
    return 250
  elif (city(ship) == "Northern California") and (city(cons) == "the Mid-Atlantic region"):
    return 275
  elif (city(ship) == "Northern California") and (city(cons) == "the Carolinas"):
    return 250
  elif (city(ship) == "Northern California") and (city(cons) == "coastal North Carolina"):
    return 285
  elif (city(ship) == "Northern California") and (city(cons) == "Northeastern Florida"):
    return 275
  elif (city(ship) == "Northern California") and (city(cons) == "South Florida"):
    return 285
  elif (city(ship) == "Northern California") and (city(cons) == "New Jersey"):
    return 250
  elif (city(ship) == "Northern California") and (city(cons) == "Pennsylvania"):
    return 250
  elif (city(ship) == "Northern California") and (city(cons) == "New York state"):
    return 250
  elif (city(ship) == "Northern California") and (city(cons) == "the island"):
    return 275
  elif (city(ship) == "Northern California") and (city(cons) == "New England"):
    return 275
  elif (city(ship) == "Northern California") and (city(cons) == "Maine"):
    return 325
  elif (city(ship) == "Northern California") and (city(cons) == "New Hampshire/Vermont"):
    return 275
  elif (city(ship) == "Northern California") and (city(cons) == "Cleveland area"):
    return 225
  elif (city(ship) == "Northern California") and (city(cons) == "Ohio"):
    return 225
  elif (city(ship) == "Northern California") and (city(cons) == "remote northern Michigan"):
    return 325
  elif (city(ship) == "Northern California") and (city(cons) == "lower Michigan"):
    return 225
  elif (city(ship) == "Northern California") and (city(cons) == "Indiana"):
    return 195
  elif (city(ship) == "Northern California") and (city(cons) == "rural Illinois"):
    return 195
  elif (city(ship) == "Northern California") and (city(cons) == "St. Louis"):
    return 200
  elif (city(ship) == "Northern California") and (city(cons) == "Milwaukee"):
    return 175
  elif (city(ship) == "Northern California") and (city(cons) == "rural Wisconsin"):
    return 200
  elif (city(ship) == "Northern California") and (city(cons) == "the Twin Cities"):
    return 225
  elif (city(ship) == "Northern California") and (city(cons) == "Northeastern Florida"):
    return 275
  elif (city(ship) == "Northern California") and (city(cons) == "rural MN/Dakotas"):
    return 275
  elif (city(ship) == "Northern California") and (city(cons) == "Iowa"):
    return 200
  elif (city(ship) == "Northern California") and (city(cons) == "Kansas City"):
    return 250
  elif (city(ship) == "Northern California") and (city(cons) == "ruralmoskne"):
    return 275
  elif (city(ship) == "Portland") and (city(cons) == "Los Angeles"):
    return 75
  elif (city(ship) == "Portland") and (city(cons) == "Dallas"):
    return 175
  elif (city(ship) == "Portland") and (city(cons) == "Eastern Texas"):
    return 200
  elif (city(ship) == "Portland") and (city(cons) == "Northeastern Florida"):
    return 225
  elif (city(ship) == "Portland") and (city(cons) == "South Florida"):
    return 250
  elif (city(ship) == "Portland") and (city(cons) == "the Carolinas"):
    return 215
  elif (city(ship) == "Portland") and (city(cons) == "coastal North Carolina"):
    return 265
  elif (city(ship) == "Portland") and (city(cons) == "Atlanta"):
    return 200
  elif (city(ship) == "Portland") and (city(cons) == "New Jersey"):
    return 225
  elif (city(ship) == "Portland") and (city(cons) == "New England"):
    return 250
  elif (city(ship) == "Seattle") and (city(cons) == "Los Angeles"):
    return 85
  elif (city(ship) == "Seattle") and (city(cons) == "Dallas"):
    return 185
  elif (city(ship) == "Seattle") and (city(cons) == "Eastern Texas"):
    return 210
  elif (city(ship) == "Seattle") and (city(cons) == "Northeastern Florida"):
    return 235
  elif (city(ship) == "Seattle") and (city(cons) == "South Florida"):
    return 260
  elif (city(ship) == "Seattle") and (city(cons) == "the Carolinas"):
    return 225
  elif (city(ship) == "Seattle") and (city(cons) == "coastal North Carolina"):
    return 285
  elif (city(ship) == "Seattle") and (city(cons) == "Atlanta"):
    return 210
  elif (city(ship) == "Seattle") and (city(cons) == "New Jersey"):
    return 235
  elif (city(ship) == "Seattle") and (city(cons) == "New England"):
    return 260
  elif (city(ship) == "Atlanta") and (city(cons) == "Dallas"):
    return 100
  elif (city(ship) == "Atlanta") and (city(cons) == "Los Angeles"):
    return 150
  elif (city(ship) == "Atlanta") and (city(cons) == "Northern California"):
    return 185
  elif (city(ship) == "Atlanta") and (city(cons) == "Central California"):
    return 185
  elif (city(ship) == "Atlanta") and (city(cons) == "Remote northern California"):
    return 200
  elif (city(ship) == "Atlanta") and (city(cons) == "Portland"):
    return 200
  elif (city(ship) == "Atlanta") and (city(cons) == "Seattle"):
    return 215
  elif (city(ship) == "Atlanta") and (city(cons) == "Remote PNW"):
    return 250
  elif (city(ship) == "Atlanta") and (city(cons) == "Rocky Mountains"):
    return 175
  elif (city(ship) == "Atlanta") and (city(cons) == "Phoenix/Las Vegas"):
    return 175
  elif (city(ship) == "Atlanta") and (city(cons) == "Eastern Texas"):
    return 125
  elif (city(ship) == "Atlanta") and (city(cons) == "Oklahoma"):
    return 125
  elif (city(ship) == "Atlanta") and (city(cons) == "South Florida"):
    return 100
  elif (city(ship) == "the Carolinas") and (city(cons) == "Dallas"):
    return 100
  elif (city(ship) == "the Carolinas") and (city(cons) == "Los Angeles"):
    return 175
  elif (city(ship) == "the Carolinas") and (city(cons) == "Northern California"):
    return 185
  elif (city(ship) == "the Carolinas") and (city(cons) == "Central California"):
    return 185
  elif (city(ship) == "the Carolinas") and (city(cons) == "Remote northern California"):
    return 210
  elif (city(ship) == "the Carolinas") and (city(cons) == "Portland"):
    return 225
  elif (city(ship) == "the Carolinas") and (city(cons) == "Seattle"):
    return 235
  elif (city(ship) == "the Carolinas") and (city(cons) == "Remote PNW"):
    return 250
  elif (city(ship) == "the Carolinas") and (city(cons) == "Phoenix/Las Vegas"):
    return 225
  elif (city(ship) == "the Carolinas") and (city(cons) == "Rocky Mountains"):
    return 200
  elif (city(ship) == "the Carolinas") and (city(cons) == "Eastern Texas"):
    return 125
  elif (city(ship) == "the Carolinas") and (city(cons) == "Oklahoma"):
    return 125
  elif (city(ship) == "New Jersey") and (city(cons) == "Dallas"):
    return 125
  elif (city(ship) == "New Jersey") and (city(cons) == "Los Angeles"):
    return 175
  elif (city(ship) == "New Jersey") and (city(cons) == "Northern California"):
    return 200
  elif (city(ship) == "New Jersey") and (city(cons) == "Remote northern California"):
    return 200
  elif (city(ship) == "New Jersey") and (city(cons) == "Central California"):
    return 190
  elif (city(ship) == "New Jersey") and (city(cons) == "Portland"):
    return 250
  elif (city(ship) == "New Jersey") and (city(cons) == "Seattle"):
    return 250
  elif (city(ship) == "New Jersey") and (city(cons) == "rural pnw"):
    return 250
  elif (city(ship) == "New Jersey") and (city(cons) == "Rocky Mountains"):
    return 175
  elif (city(ship) == "New Jersey") and (city(cons) == "Phoenix/Las Vegas"):
    return 175
  elif (city(ship) == "New Jersey") and (city(cons) == "Eastern Texas"):
    return 160
  elif (city(ship) == "New Jersey") and (city(cons) == "Western Texas"):
    return 200
  elif (city(ship) == "New Jersey") and (city(cons) == "Oklahoma"):
    return 150
  elif (city(ship) == "New Jersey") and (city(cons) == "Northeastern Florida"):
    return 125
  elif (city(ship) == "New Jersey") and (city(cons) == "South Florida"):
    return 135
  elif (city(ship) == "the island") and (city(cons) == "Dallas"):
    return 175
  elif (city(ship) == "the island") and (city(cons) == "Los Angeles"):
    return 215
  elif (city(ship) == "the island") and (city(cons) == "Northern California"):
    return 235
  elif (city(ship) == "the island") and (city(cons) == "Remote northern California"):
    return 250
  elif (city(ship) == "the island") and (city(cons) == "Central California"):
    return 235
  elif (city(ship) == "the island") and (city(cons) == "Rocky Mountains"):
    return 215
  elif (city(ship) == "the island") and (city(cons) == "Phoenix/Las Vegas"):
    return 215
  elif (city(ship) == "the island") and (city(cons) == "Eastern Texas"):
    return 200
  elif (city(ship) == "the island") and (city(cons) == "Western Texas"):
    return 205
  elif (city(ship) == "the island") and (city(cons) == "Oklahoma"):
    return 200
  elif (city(ship) == "the island") and (city(cons) == "Northeastern Florida"):
    return 165
  elif (city(ship) == "the island") and (city(cons) == "South Florida"):
    return 185
  elif (city(ship) == "New England") and (city(cons) == "Dallas"):
    return 150
  elif (city(ship) == "New England") and (city(cons) == "Los Angeles"):
    return 185
  elif (city(ship) == "New England") and (city(cons) == "Northern California"):
    return 200
  elif (city(ship) == "New England") and (city(cons) == "Remote northern California"):
    return 220
  elif (city(ship) == "New England") and (city(cons) == "Central California"):
    return 200
  elif (city(ship) == "New England") and (city(cons) == "Rocky Mountains"):
    return 200
  elif (city(ship) == "New England") and (city(cons) == "Phoenix/Las Vegas"):
    return 200
  elif (city(ship) == "New England") and (city(cons) == "Eastern Texas"):
    return 185
  elif (city(ship) == "New England") and (city(cons) == "Western Texas"):
    return 225
  elif (city(ship) == "New England") and (city(cons) == "Oklahoma"):
    return 225
  elif (city(ship) == "New England") and (city(cons) == "Northeastern Florida"):
    return 145
  elif (city(ship) == "New England") and (city(cons) == "South Florida"):
    return 150
  elif (city(ship) == "New Hampshire/Vermont") and (city(cons) == "Chicago"):
    return 115
  elif (city(ship) == "New Hampshire/Vermont") and (city(cons) == "Dallas"):
    return 200
  elif (city(ship) == "New Hampshire/Vermont") and (city(cons) == "Los Angeles"):
    return 200
  elif (city(ship) == "New Hampshire/Vermont") and (city(cons) == "Northern California"):
    return 200
  elif (city(ship) == "New Hampshire/Vermont") and (city(cons) == "Remote northern California"):
    return 225
  elif (city(ship) == "New Hampshire/Vermont") and (city(cons) == "Central California"):
    return 215
  elif (city(ship) == "New Hampshire/Vermont") and (city(cons) == "Portland"):
    return 300
  elif (city(ship) == "New Hampshire/Vermont") and (city(cons) == "Seattle"):
    return 300
  elif (city(ship) == "New Hampshire/Vermont") and (city(cons) == "Remote PNW"):
    return 315
  elif (city(ship) == "New Hampshire/Vermont") and (city(cons) == "Rocky Mountains"):
    return 200
  elif (city(ship) == "New Hampshire/Vermont") and (city(cons) == "Phoenix/Las Vegas"):
    return 215
  elif (city(ship) == "New Hampshire/Vermont") and (city(cons) == "Eastern Texas"):
    return 135
  elif (city(ship) == "New Hampshire/Vermont") and (city(cons) == "Western Texas"):
    return 200
  elif (city(ship) == "New Hampshire/Vermont") and (city(cons) == "Oklahoma"):
    return 200
  elif (city(ship) == "New Hampshire/Vermont") and (city(cons) == "Arkansas/Louisiana"):
    return 200
  elif (city(ship) == "New Hampshire/Vermont") and (city(cons) == "Atlanta"):
    return 200
  elif (city(ship) == "New Hampshire/Vermont") and (city(cons) == "the Gulf of Mexico"):
    return 215
  elif (city(ship) == "New Hampshire/Vermont") and (city(cons) == "the Southeast"):
    return 200
  elif (city(ship) == "New Hampshire/Vermont") and (city(cons) == "Northeastern Florida"):
    return 235
  elif (city(ship) == "New Hampshire/Vermont") and (city(cons) == "South Florida"):
    return 275
  elif (city(ship) == "New Hampshire/Vermont") and (city(cons) == "Ohio"):
    return 150
  elif (city(ship) == "New Hampshire/Vermont") and (city(cons) == "lower Michigan"):
    return 200
  elif (city(ship) == "New Hampshire/Vermont") and (city(cons) == "rural Illinois"):
    return 175
  elif (city(ship) == "New Hampshire/Vermont") and (city(cons) == "St. Louis"):
    return 185
  elif (city(ship) == "New Hampshire/Vermont") and (city(cons) == "Milwaukee"):
    return 165
  elif (city(ship) == "New Hampshire/Vermont") and (city(cons) == "rural Wisconsin"):
    return 200
  elif (city(ship) == "New Hampshire/Vermont") and (city(cons) == "ia"):
    return 200
  elif (city(ship) == "New Hampshire/Vermont") and (city(cons) == "Kansas City"):
    return 185
  elif (city(ship) == "Cleveland area") and (city(cons) == "Dallas"):
    return 150
  elif (city(ship) == "Cleveland area") and (city(cons) == "Los Angeles"):
    return 185
  elif (city(ship) == "Cleveland area") and (city(cons) == "Northern California"):
    return 200
  elif (city(ship) == "Cleveland area") and (city(cons) == "Remote northern California"):
    return 225
  elif (city(ship) == "Cleveland area") and (city(cons) == "Central California"):
    return 200
  elif (city(ship) == "Cleveland area") and (city(cons) == "Portland"):
    return 300
  elif (city(ship) == "Cleveland area") and (city(cons) == "Seattle"):
    return 300
  elif (city(ship) == "Cleveland area") and (city(cons) == "rural pnw"):
    return 300
  elif (city(ship) == "Cleveland area") and (city(cons) == "Rocky Mountains"):
    return 225
  elif (city(ship) == "Cleveland area") and (city(cons) == "Phoenix/Las Vegas"):
    return 225
  elif (city(ship) == "Cleveland area") and (city(cons) == "Eastern Texas"):
    return 160
  elif (city(ship) == "Cleveland area") and (city(cons) == "South Florida"):
    return 200
  elif (city(ship) == "Cleveland area") and (city(cons) == "New Jersey"):
    return 125
  elif (city(ship) == "Ohio") and (city(cons) == "Dallas"):
    return 115
  elif (city(ship) == "Ohio") and (city(cons) == "Los Angeles"):
    return 185
  elif (city(ship) == "Ohio") and (city(cons) == "Northern California"):
    return 200
  elif (city(ship) == "Ohio") and (city(cons) == "Remote northern California"):
    return 225
  elif (city(ship) == "Ohio") and (city(cons) == "Central California"):
    return 200
  elif (city(ship) == "Ohio") and (city(cons) == "Portland"):
    return 300
  elif (city(ship) == "Ohio") and (city(cons) == "Seattle"):
    return 300
  elif (city(ship) == "Ohio") and (city(cons) == "rural pnw"):
    return 300
  elif (city(ship) == "Ohio") and (city(cons) == "Rocky Mountains"):
    return 200
  elif (city(ship) == "Ohio") and (city(cons) == "Phoenix/Las Vegas"):
    return 225
  elif (city(ship) == "Ohio") and (city(cons) == "Eastern Texas"):
    return 150
  elif (city(ship) == "Ohio") and (city(cons) == "Northeastern Florida"):
    return 125
  elif (city(ship) == "Ohio") and (city(cons) == "South Florida"):
    return 165
  elif (city(ship) == "lower Michigan") and (city(cons) == "Dallas"):
    return 125
  elif (city(ship) == "lower Michigan") and (city(cons) == "Los Angeles"):
    return 175
  elif (city(ship) == "lower Michigan") and (city(cons) == "Northern California"):
    return 185
  elif (city(ship) == "lower Michigan") and (city(cons) == "Remote northern California"):
    return 205
  elif (city(ship) == "lower Michigan") and (city(cons) == "Central California"):
    return 185
  elif (city(ship) == "lower Michigan") and (city(cons) == "Portland"):
    return 275
  elif (city(ship) == "lower Michigan") and (city(cons) == "Seattle"):
    return 275
  elif (city(ship) == "lower Michigan") and (city(cons) == "rural pnw"):
    return 275
  elif (city(ship) == "lower Michigan") and (city(cons) == "Rocky Mountains"):
    return 175
  elif (city(ship) == "lower Michigan") and (city(cons) == "Phoenix/Las Vegas"):
    return 175
  elif (city(ship) == "lower Michigan") and (city(cons) == "Eastern Texas"):
    return 175
  elif (city(ship) == "lower Michigan") and (city(cons) == "Northeastern Florida"):
    return 165
  elif (city(ship) == "lower Michigan") and (city(cons) == "South Florida"):
    return 175
  elif (city(ship) == "Indiana") and (city(cons) == "Dallas"):
    return 125
  elif (city(ship) == "Indiana") and (city(cons) == "Los Angeles"):
    return 165
  elif (city(ship) == "Indiana") and (city(cons) == "Northern California"):
    return 175
  elif (city(ship) == "Indiana") and (city(cons) == "Remote northern California"):
    return 185
  elif (city(ship) == "Indiana") and (city(cons) == "Central California"):
    return 175
  elif (city(ship) == "Indiana") and (city(cons) == "Rocky Mountains"):
    return 175
  elif (city(ship) == "Indiana") and (city(cons) == "Phoenix/Las Vegas"):
    return 175
  elif (city(ship) == "Indiana") and (city(cons) == "Eastern Texas"):
    return 165
  elif (city(ship) == "rural Illinois") and (city(cons) == "Los Angeles"):
    return 145
  elif (city(ship) == "St. Louis") and (city(cons) == "Los Angeles"):
    return 150
  elif (city(ship) == "St. Louis") and (city(cons) == "Northern California"):
    return 175
  elif (city(ship) == "St. Louis") and (city(cons) == "Remote northern California"):
    return 185
  elif (city(ship) == "St. Louis") and (city(cons) == "Central California"):
    return 165
  elif (city(ship) == "St. Louis") and (city(cons) == "Rocky Mountains"):
    return 175
  elif (city(ship) == "St. Louis") and (city(cons) == "Phoenix/Las Vegas"):
    return 160
  elif (city(ship) == "St. Louis") and (city(cons) == "the Carolinas"):
    return 135
  elif (city(ship) == "Chicago") and (city(cons) == "coastal North Carolina"):
    return 185
  elif (city(ship) == "St. Louis") and (city(cons) == "New Jersey"):
    return 150
  elif (city(ship) == "St. Louis") and (city(cons) == "Dallas"):
    return 125
  elif (city(ship) == "St. Louis") and (city(cons) == "South Florida"):
    return 165
  elif (city(ship) == "St. Louis") and (city(cons) == "Northeastern Florida"):
    return 150
  elif (city(ship) == "Milwaukee") and (city(cons) == "Dallas"):
    return 125
  elif (city(ship) == "Milwaukee") and (city(cons) == "Northern California"):
    return 175
  elif (city(ship) == "Milwaukee") and (city(cons) == "Remote northern California"):
    return 185
  elif (city(ship) == "Milwaukee") and (city(cons) == "Central California"):
    return 175
  elif (city(ship) == "Milwaukee") and (city(cons) == "Portland"):
    return 215
  elif (city(ship) == "Milwaukee") and (city(cons) == "Seattle"):
    return 220
  elif (city(ship) == "Milwaukee") and (city(cons) == "Remote PNW"):
    return 225
  elif (city(ship) == "Milwaukee") and (city(cons) == "Rocky Mountains"):
    return 175
  elif (city(ship) == "Milwaukee") and (city(cons) == "Phoenix/Las Vegas"):
    return 175
  elif (city(ship) == "Milwaukee") and (city(cons) == "Eastern Texas"):
    return 145
  elif (city(ship) == "Milwaukee") and (city(cons) == "Western Texas"):
    return 185
  elif (city(ship) == "Milwaukee") and (city(cons) == "Los Angeles"):
    return 160
  elif (city(ship) == "Milwaukee") and (city(cons) == "Oklahoma"):
    return 135
  elif (city(ship) == "Milwaukee") and (city(cons) == "Arkansas/Louisiana"):
    return 125
  elif (city(ship) == "Milwaukee") and (city(cons) == "Atlanta"):
    return 125
  elif (city(ship) == "Milwaukee") and (city(cons) == "the Gulf of Mexico"):
    return 135
  elif (city(ship) == "Milwaukee") and (city(cons) == "the Southeast"):
    return 125
  elif (city(ship) == "Milwaukee") and (city(cons) == "the Mid-Atlantic region"):
    return 135
  elif (city(ship) == "Milwaukee") and (city(cons) == "the Carolinas"):
    return 125
  elif (city(ship) == "Milwaukee") and (city(cons) == "Northeastern Florida"):
    return 135
  elif (city(ship) == "Milwaukee") and (city(cons) == "South Florida"):
    return 165
  elif (city(ship) == "Milwaukee") and (city(cons) == "New Jersey"):
    return 125
  elif (city(ship) == "Milwaukee") and (city(cons) == "Pennsylvania"):
    return 125
  elif (city(ship) == "Milwaukee") and (city(cons) == "New York state"):
    return 125
  elif (city(ship) == "Milwaukee") and (city(cons) == "the island"):
    return 150
  elif (city(ship) == "Milwaukee") and (city(cons) == "New England"):
    return 150
  elif (city(ship) == "Milwaukee") and (city(cons) == "Maine"):
    return 175
  elif (city(ship) == "Milwaukee") and (city(cons) == "New Hampshire/Vermont"):
    return 165
  elif (city(ship) == "Milwaukee") and (city(cons) == "Kansas City"):
    return 150
  elif (city(ship) == "the Twin Cities") and (city(cons) == "Dallas"):
    return 150
  elif (city(ship) == "the Twin Cities") and (city(cons) == "Los Angeles"):
    return 175
  elif (city(ship) == "the Twin Cities") and (city(cons) == "Northern California"):
    return 200
  elif (city(ship) == "the Twin Cities") and (city(cons) == "Remote northern California"):
    return 225
  elif (city(ship) == "the Twin Cities") and (city(cons) == "Central California"):
    return 200
  elif (city(ship) == "the Twin Cities") and (city(cons) == "Rocky Mountains"):
    return 185
  elif (city(ship) == "the Twin Cities") and (city(cons) == "Eastern Texas"):
    return 175
  elif (city(ship) == "Kansas City") and (city(cons) == "Los Angeles"):
    return 135
  elif (city(ship) == "Kansas City") and (city(cons) == "New Jersey"):
    return 185
  elif (city(ship) == "Kansas City") and (city(cons) == "New England"):
    return 200
  elif (city(ship) == "South Florida") and (city(cons) == "Chicago"):
    return 100
  elif (city(ship) == "South Florida") and (city(cons) == "Dallas"):
    return 150
  elif (city(ship) == "South Florida") and (city(cons) == "Los Angeles"):
    return 200
  elif (city(ship) == "South Florida") and (city(cons) == "Northern California"):
    return 250
  elif (city(ship) == "South Florida") and (city(cons) == "Remote northern California"):
    return 275
  elif (city(ship) == "South Florida") and (city(cons) == "Central California"):
    return 250
  elif (city(ship) == "South Florida") and (city(cons) == "Portland"):
    return 300
  elif (city(ship) == "South Florida") and (city(cons) == "Seattle"):
    return 300
  elif (city(ship) == "South Florida") and (city(cons) == "Rocky Mountains"):
    return 275
  elif (city(ship) == "South Florida") and (city(cons) == "Phoenix/Las Vegas"):
    return 225
  elif (city(ship) == "South Florida") and (city(cons) == "Eastern Texas"):
    return 165
  elif (city(ship) == "South Florida") and (city(cons) == "New Jersey"):
    return 135
  elif (city(ship) == "South Florida") and (city(cons) == "Pennsylvania"):
    return 150
  elif (city(ship) == "South Florida") and (city(cons) == "the island"):
    return 165
  elif (city(ship) == "South Florida") and (city(cons) == "New England"):
    return 160
  elif (city(ship) == "South Florida") and (city(cons) == "rural Illinois"):
    return 115
  elif (city(ship) == "Northeastern Florida") and (city(cons) == "Dallas"):
    return 150
  elif (city(ship) == "Northeastern Florida") and (city(cons) == "Los Angeles"):
    return 200
  elif (city(ship) == "Northeastern Florida") and (city(cons) == "Northern California"):
    return 225
  elif (city(ship) == "Northeastern Florida") and (city(cons) == "New Jersey"):
    return 150
  elif (city(ship) == "South Florida") and (city(cons) == "New England"):
    return 175
  elif (city(ship) == "South Florida") and (city(cons) == "Eastern Texas"):
    return 175
  else:
    return 0





def spacerate(skidrate, footage):
  return skidrate(ship, cons) * (footage / 2)


xporate = spacerate(skidrate, footage)


if (footage < 14) and (xporate > 0):
  xporate = xporate + 200
  
print " "
print " "
print "XPO will pay : ", xporate
print " "
print " "
print city(ship), "to", city(cons)
print " "

if skidrate(ship, cons) == 0:
  print "This is not a good partials lane"

if (weight > (footage * 700)) and (skidrate(ship,cons) != 0):
  print "This freight is abnormally heavy for the amount of space it takes. Pricing based on weight."

if (skidrate(ship,cons) == 0) and (skidrate (cons, ship) > 0):
  print "Although actually I may be able to hook up a backhaul on this... hit me up and we we'll discuss!"

if (footage > 32) or (weight > 30000):
 print "This is a very large partial. I may have difficulty covering it as a partial, "
 print "so make sure you have truckload money in case we have to cover it with an FTL"

if (city(ship) == "off the map") or (city(cons) == "off the map"):
  print "I can only quote loads that ship within the mainland united states"
  
if city(ship) == city(cons):
  print "For local moves, it's best to quote truckload. Partials don't make much sense for these."


print " "
print " "

print "For coverage, or assistance of any kind related to partial truckload shipments, "
print "please contact (preferably via Lync): "
print " "
print "Tom von Geldern"
print "thomas.geldern@xpologistics.com"
print "extension 42119 or 42120"
print "312-361-0984"

print " "
print " "
print " "
print " *********DISCLAIMERS************"
print " "
print " - This is for customer use only when quoting loads to customers. Only about 20% of these rates are "
print "    ironclad, the rest are conservative estimates. QUOTING THESE RATES TO CARRIERS IS NOT ADVISED. "
print " "
print " - This program does not have a map built in to it, it only recognizes cities by ranges of ZIP codes. This can "
print "     occasionally cause problems (rare). For example, ZIP code 33401 corresponds to location Key West, FL "
print "     but my program will rate a load from there as if it were from Miami . While I have pretty good coverage in "
print "     Miami, I can promise you that I will not be able to cover any loads originating in Key West. The lesson here:"
print " ->  MAKE SURE YOU LOOK AT THE LANE ON A MAP BEFORE ACCEPTING A LOAD. If anything seems off, please don't"
print "     hesitate to contact me. I will be happy to help."


