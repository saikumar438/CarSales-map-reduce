import sys

thisKey = ""
thisValue = 0.0

for line in sys.stdin:
  datalist = line.strip().split('\t')
  if (len(datalist) == 2) : 
    Manufacturer, Sales_in_thousands = datalist

    if Manufacturer != thisKey:   # we've moved to another key
      if thisKey:
        # output the previous key-summaryvalue result
        print(thisKey,'\t',thisValue)

      # start over for each new key
      thisKey = Manufacturer 
      thisValue = 0.0
  
    # apply the aggregation function
    thisValue += float(Sales_in_thousands)

# output the final key-summaryvalue result outside the loop
print(thisKey,'\t',thisValue)