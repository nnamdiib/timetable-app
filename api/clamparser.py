from openpyxl import load_workbook

def get_headings(worksheet):
	"""
	Returns the table headings/headers for the Excel sheet.
	"""
	headings = []
	for row in worksheet.rows:
		if(row[0].row == 1):
			headings = [cell for cell in row]
			break
	return headings

def get_time(column_number, headings_list):
	"""
	Returns the time a particular class is holding
	based on its cell column column_number
	"""
	return str(headings_list[column_number - 1].value)

def get_double_period(time1, time2):
	"""
	This method concatenates two different time strings 
	and returns a single time interval string
	The order of the paramters does not matter.
	Example: get_double_period("08am-09am", "09am-10am") returns "08am-10am"
					 get_double_period("09am-10am", "08am-09am") returns "08am-09am"
	"""
	if int(time1[:2]) < int(time2[:2]):
		t1 = time1
		t2 = time2
	else:
		t1 = time2
		t2 = time1

	t1 = time1.split('-')
	t2 = time2.split('-')
	new_time = t1[0] + '-' + t2[1]

	return new_time


def magic(filename, day_object):
	wb = load_workbook(filename, read_only=True)
	ws = wb['Sheet1']

	headings = get_headings(ws)
	response = {}
	viable_rows = [row for row in ws.rows if (row[0].value)  and (row[0].row != 1)]

	for row in viable_rows:
		venue = " ".join([cell.value for cell in row[:2]])
		viable_cells = [cell for cell in row[2:] if cell.value]
		for cell in viable_cells:
			course_code = str(cell.value.lower())
			time = get_time(cell.column, headings)
			day = day_object

			if course_code in response.keys():
				# Just update the time to a double period.
				existing_time = response[course_code]['time']
				response[course_code]['time'] = get_double_period(existing_time, time)
			else:
				course_dict = {
												'time':time,
												'venue':venue,
												'day':day
											}
				response[course_code] = course_dict
	
	return response

if __name__ == '__main__':
	pass