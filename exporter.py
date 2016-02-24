from dataFormatter import serialize
import json
def exporter(aList, item):

	exportedList = []
	for items in aList:
		if item == "total_calories":
			exportedList.append(items.calories)
		elif item == "meal":
			exportedList.append(items.meal)
		elif item == "date":
			exportedList.append(items.date)
	return exportedList