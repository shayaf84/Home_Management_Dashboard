# Shaya Farahmand
# Year 9 - TDJ20-1
# Home Maintenance Dashboard

# Imports the necessary packages that will be use

#For GUI Development
import tkinter as tk
#Use fonts
import tkinter.font as tkFont
#Use different types of buttons, so the background can change colour
from tkmacosx import Button
#Use this for the treeview
from tkinter import ttk
#Use this for database development and manipulation
import sqlite3
#Use this for developing pie charts
import matplotlib.pyplot as plt
#Use this to place the pie charts on the GUI
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


########################################################################################################

#Develop a GUI window called "Home Maintenance Dashboard", with a minimum size of 900x700
root = tk.Tk()
root.title("Home Maintenance Dashboard")
root.minsize(900,700)

########################################################################################################

# Global variables that will be initialized
# Not all the global variables will be declared at the top, the only global variables declared are \
# the label widgets that are deleted before placing another one in the same location

#Initializes the status_show variable, type label widget, will be manipulated
global status_show
status_show = tk.Label(root)
#Initializes the entry_show variable, type label widget, will be manipulated
global entry_show
entry_show = tk.Label(root)
#Initializes the show variable, type label widget, will be manipulated
global show
show = tk.Label(root)
#Initializes the good variable, type label widget, will be manipulated
global good
good = tk.Label(root)

#Initializes the not_int and not_float variables, type label widget, will be manipulated

########################################################################################################

#Fonts that will be initialized

#Font that will be used for titles
title_font = tkFont.Font(family="Open Sans", size=50)
#Font that will be used for headers
header_font = tkFont.Font(family="Open Sans", size = 36)
#Font that will be used for subtitles
subtitle_font = tkFont.Font(family="Open Sans", size = 20, weight ="bold")
#Font that will be used for warnings (eg: invalid entries)
warning_font = tkFont.Font(family = "Open Sans", size = 30, weight="bold")

########################################################################################################

#Establish a connection to a database called "home_management.db" (essentially creates the database)
#Database is made wtih SQLite
connect = sqlite3.connect("home_management.db")
#Develops a cursor for that database --- all actions, querys will be done using that database
cursor = connect.cursor()

########################################################################################################


def frame(row,column):
	'''
	Takes in formal parameters row and column
	
	Returns a tkinter frame, and is placed using the grid layout manager in the actual parameters given
	for row and column.
	'''
	#Width of the frame is 900 (being the minsize), but is expandable, as sticky is NESW
	your_frame = tk.Frame(root,width=900)
	your_frame.grid(row=row, column=column,sticky="NESW")
	return(your_frame)

def headings(text):
	'''
	Takes in one formal parameter text
	Displays the header text in the top row of the window
	Displays a button which takes the user back to the landing page in the second row
	
	'''

	#Displays a frame that encompasses the entire window
	page = tk.Frame(root)
	page.grid()

	#Header of the frame - displays the text that was passed into the function, placed at the top \
	#of the window
	title = tk.Label(page, text = text,font=header_font)
	title.grid(row = 0,column=0)

	#Uses the frame function defined earlier to construct the frame
	nav_frame = frame(1,0)
	root.columnconfigure(0,weight=1)
	#Constructs a button called go back home which takes the user back to the landing page (shown later)
	#Button expands with the frame (sticky = "NESW")
	home = Button(nav_frame, text='Go Back to Home', bg='blue',fg='white', borderless=1, height = 75, width = 300,command=back)
	home.grid(row=0,column=1,sticky="NESW")
	nav_frame.columnconfigure(1,weight=1)


def basic_info(text,frame,row,column,col):
	'''
	A function that will be used to construct a label, and an entry widget beside it.

	Takes in 5 formal parameters:
	Text is the label widget's content
	Frame is the master of both widgets
	Row and column will be used as parameters for the label's grid value
	Col will be used as parameters for the entry widget's column value in the grid. It \
	uses the same row as the label widget

	Only the entry widget is returned, as that is the value which will be manipulated in other \
	functions


	'''
	# Master -> frame, text option -> Formal parameter text
	prop_name = tk.Label(frame, text = text)
	# row -> Formal parameter row, column -> Formal parameter column
	prop_name.grid(row = row, column=column,padx=30)
	#Master -> frame
	prop_e = tk.Entry(frame)
	#row -> Formal parameter row, column -> Formal parameter col
	prop_e.grid(row=row, column=col,padx=30)

	return prop_e



def landing(root):
	'''
	The landing page of the GUI
	
	Takes in one formal parameter root (defined above)
	Returns the interface for the landing page

	'''
	
	#Calls the frame function, which develops a frame at the top row (using the frame allows pack \
	# layout manager)
	title_frame = frame(0,0)
	#The title label of this window (the text is Home Management Dashboard)
	title = tk.Label(title_frame,text = "Home Management Dashboard", foreground = "black", font = title_font)
	title.pack(side=tk.TOP)
	#Calls the frame function, which develops a frame at the second row for the nav buttons
	nav_frame = frame(1,0)
	#Blank row
	row_filler = tk.Label(nav_frame, text=" ")
	row_filler.grid(row=0,column=1)


	root.columnconfigure(0,weight=1)
	#Creates 4 buttons each on top of one another which, when clicked,takes the user to a different \
	#part of the GUI. The buttons stay in the middle as the frame expands
	#Each button is blue (thanks to tkmacosx)
	#One blank row is in between the two buttons

	#When clicked, the user is taken to the dashboard page
	dashboard = Button(nav_frame, text='Dashboard', bg='blue',fg='white', borderless=1, height = 75, width = 300,command = switch_to_dashboard)
	dashboard.grid(row=1,column=1,sticky="NESW")
	nav_frame.columnconfigure(0,weight=1)

	row_filler = tk.Label(nav_frame, text=" ")
	row_filler.grid(row=2,column=1)
	#When clicked, the user is taken to the dashboard page
	tracking = Button(nav_frame, text='Tracking', bg='blue',fg='white', borderless=1, height = 75, width = 300,command=switch_to_track)
	tracking.grid(row=3,column=1,sticky="NESW")
	nav_frame.columnconfigure(1,weight=1)

	row_filler = tk.Label(nav_frame, text=" ")
	row_filler.grid(row=4,column=1)
	#When clicked, the user is taken to the properties page
	properties = Button(nav_frame, text='Properties', bg='blue',fg='white', borderless=1, height = 75, width = 300,command=enter)
	properties.grid(row=5,column=1,sticky="NESW")
	nav_frame.columnconfigure(2,weight=1)

	row_filler = tk.Label(nav_frame, text=" ")
	row_filler.grid(row=6,column=1)
	#When clicked, the user is taken to the administration page
	admin = Button(nav_frame, text='Administration', bg='blue',fg='white', borderless=1, height = 75, width = 300,command=switch_admin)
	admin.grid(row=7,column=1,sticky="NESW")
	nav_frame.columnconfigure(2,weight=1)



def enterNewProperty(root):
	'''
	The page where the user can enter a new property
	
	This page just returns the interface, where the user can enter the information about the property

	Takes in one formal parameter root (defined above)

	'''
	# Calls the headings function, with actual parameter "Enter New Property". This makes a header \
	# with the actual parameter as the title, and one button underneath, prompting the user to return \
	# to the main page
	headings("Enter New Property")

	#Creates a frame that all widgets will be placed in
	global input_frame
	input_frame = frame(2,0)

	#Blank row
	row_filler = tk.Label(input_frame, text=" ")
	row_filler.grid(row=0,column=0)
	
	#First four categories. Four label widgets, with four corresponding entry widgets
	#Done by calling the "basic_info" function
	#Seeks information about the property name, property type, address, and city/town
	global name,prop_type,address,city
	name = basic_info("Property Name: ",input_frame,1,0,1)
	prop_type = basic_info("Property Type: ",input_frame,2,0,1)
	address = basic_info("Address: ", input_frame,3,0,1)
	city = basic_info("City/Town: ", input_frame,4,0,1)
	
	#Blank row
	another_filler = tk.Label(input_frame,text=" ")
	another_filler.grid(row=5, column = 0)


	#Declarations of global variables. Each row represents all the variable from one category
	#A category is a home maintenance task (landscaping, snowplowing, etc.)
	#The names of each variable, followed by the first letter of the question asked (first two in \
	# the event of a same letter)
	global l_c,l_p,l_sa,l_so,l_f
	global s_c,s_p,s_sa,s_so,s_f
	global w_c, w_p, w_sa, w_so, w_f
	global r_c, r_p, r_sa, r_so, r_f
	global h_c, h_p, h_sa, h_so, h_f

	#First category: Landscaping - displays it in bold above all questions asked
	landscape = tk.Label(input_frame,text="Landscaping",font=subtitle_font)
	landscape.grid(row=6, column=0, padx=10)
	#Calls the basic_info function showing a label and an entry widget beside it
	#First row: contractor, Second row: Frequency, Third row: Start Month \
	#Fourth row: Stop Month, Fifth row: Fee
	#The information about property is not really used in the future. Just shown
	l_c = basic_info("Contractor: ", input_frame, 7,0,1)
	l_p = basic_info("How often in a year (enter a number)?: ",input_frame,8,0,1)
	l_sa = basic_info("Start Month (Enter a valid month): ", input_frame,9,0,1)
	l_so = basic_info("Stop Month (Enter a valid month): ",input_frame,10,0,1)
	l_f = basic_info("What is the annual fee? (enter a number): ", input_frame, 11, 0, 1)
	#Second category: Snowplowing - displays it in bold above all questions asked
	snow = tk.Label(input_frame,text="Snowplowing",font=subtitle_font)
	snow.grid(row=12, column=0, padx=10)
	#Calls the basic_info function showing a label and an entry widget beside it
	#First row: contractor, Second row: Frequency, Third row: Start Month \
	#Fourth row: Stop Month, Fifth row: Fee
	#The information about property is not really used in the future. Just shown
	s_c = basic_info("Contractor: ", input_frame, 13,0,1)
	s_p = basic_info("How often in a year (enter a number)?: ",input_frame,14,0,1)
	s_sa = basic_info("Start Month (Enter a valid month): ", input_frame,15,0,1)
	s_so = basic_info("Stop Month (Enter a valid month): ",input_frame,16,0,1)
	s_f = basic_info("What is the annual fee? (enter a number): ", input_frame, 17, 0, 1)
	#Third category: Window Maintenance - displays it in bold above all questions asked
	window = tk.Label(input_frame,text="Windows",font=subtitle_font)
	window.grid(row=1, column=2, padx=10)
	#Calls the basic_info function showing a label and an entry widget beside it
	#First row: contractor, Second row: Frequency, Third row: Start Month \
	#Fourth row: Stop Month, Fifth row: Fee
	#The information about property is not really used in the future. Just shown
	w_c = basic_info("Contractor: ", input_frame, 2,2,3)
	w_p = basic_info("How often in a year (enter a number)?: ",input_frame,3,2,3)
	w_sa = basic_info("Start Month (Enter a valid month): ", input_frame,4,2,3)
	w_so = basic_info("Stop Month (Enter a valid month): ",input_frame,5,2,3)
	w_f = basic_info("What is the annual fee? (enter a number): ", input_frame, 6, 2,3)
	#Fourth category: Roof Maintenance - displays it in bold above all questions asked
	roof = tk.Label(input_frame,text="Roof Maintenance",font=subtitle_font)
	roof.grid(row=7, column=2, padx=10)
	#Calls the basic_info function showing a label and an entry widget beside it
	#First row: contractor, Second row: Frequency, Third row: Start Month \
	#Fourth row: Stop Month, Fifth row: Fee
	#The information about property is not really used in the future. Just shown
	r_c = basic_info("Contractor: ", input_frame, 8,2,3)
	r_p = basic_info("How often in a year (enter a number)?: ",input_frame,9,2,3)
	r_sa = basic_info("Start Month (Enter a valid month): ", input_frame,10,2,3)
	r_so = basic_info("Stop Month (Enter a valid month): ",input_frame,11,2,3)
	r_f = basic_info("What is the annual fee? (enter a number): ", input_frame, 12, 2,3)
	#Fifth category: HVAC Maintenance - displays it in bold above all questions asked
	hvac = tk.Label(input_frame,text="HVAC Maintenance",font=subtitle_font)
	hvac.grid(row=13, column=2, padx=10)
	#Calls the basic_info function showing a label and an entry widget beside it
	#First row: contractor, Second row: Frequency, Third row: Start Month \
	#Fourth row: Stop Month, Fifth row: Fee
	#The information about property is not really used in the future. Just shown
	h_c = basic_info("Contractor: ", input_frame, 14,2,3)
	h_p = basic_info("How often in a year (enter a number)?: ",input_frame,15,2,3)
	h_sa = basic_info("Start Month (Enter a valid month): ", input_frame,16,2,3)
	h_so = basic_info("Stop Month (Enter a valid month): ",input_frame,17,2,3)
	h_f = basic_info("What is the annual fee? (enter a number): ", input_frame, 18, 2,3)

	#Button to submit the info and save it in a database
	submit = tk.Button(input_frame, text = "Save", command = collect)
	submit.grid(row=19,column = 1)


def back():
	'''
	This function will be used to switch from any secondary pages, back to the landing page.

	It takes in no parameters - called by the command of a button

	Destroys all existing widgets. On any page other than the landing page, the page variable is 2,\
	 so always the landing function (line 323) can be called.

	By calling landing, the window will switch to the landing page
	'''
	global page
	for i in root.winfo_children():
		i.destroy()
	if page ==2:
		landing(root)
		page=1

def search():
	'''
	This is a function that will be used to query to object identifier from an entry in the database

	It takes in no parameters
	'''
	# Extracts every entry from the property table in the database
	# Also attaches an object identifier (oid) to every entry (a row). First row has an oid of 0, \
	# second has 1, etc. 
	cursor.execute("SELECT *, oid FROM property")
	#Records is a list, with each index being a tuple. The contents of that tuple is a row in the table
	records = cursor.fetchall()
	# Empty variable initialized, values added in the loop below
	r=""
	# Loops through the 8th index in records (the oid)
	for record in records[8]:
		r += str(record) + "\n"
	query_label = tk.Label(input_frame,text=r)
	query_label.grid(row=20, column=0)
	connect.commit()



def collect():

	#Establish a connection to a database called "home_management.db" (essentially creates the database)
	#Database is made wtih SQLite
	# Connections made at the beginning of the program, but is made again as it has to be done in any \
	#functions developed
	connect = sqlite3.connect("home_management.db")
	#Develops a cursor for that database --- all actions, querys will be done using that database
	cursor = connect.cursor()

	

	#Get the value from each of the entry widgets defined in the enterNewProperty function, and store \
	#them in another variable
	col_name = name.get()
	col_ptype = prop_type.get()
	col_addr = address.get()
	col_cit = city.get()
	

	lc = l_c.get()
	lp = l_p.get()
	lsa = l_sa.get()
	lso = l_so.get()
	lf = l_f.get()

	sc = s_c.get()
	sp = s_p.get()
	ssa = s_sa.get()
	sso = s_so.get()
	sf = s_f.get()

	wc = w_c.get()
	wp = w_p.get()
	wsa = w_sa.get()
	wso = w_so.get()
	wf = w_f.get()

	rc = r_c.get()
	rp = r_p.get()
	rsa = r_sa.get()
	rso = r_so.get()
	rf = r_f.get()

	hc = h_c.get()
	hp = h_p.get()
	hsa = h_sa.get()
	hso = h_so.get()
	hf = h_f.get()

	

	# After, the value of the entry widget is retrieved, the entry widget's variable (not the ones \
	#from the .get) is deleted, just so that when you click the button, the values you inputted will \
	#no longer remain in the entry widget.
	name.delete(0,tk.END)
	prop_type.delete(0,tk.END)
	address.delete(0,tk.END)
	city.delete(0,tk.END)

	l_c.delete(0,tk.END)
	l_p.delete(0,tk.END)
	l_sa.delete(0,tk.END)
	l_so.delete(0,tk.END)
	l_f.delete(0,tk.END)

	s_c.delete(0,tk.END)
	s_p.delete(0,tk.END)
	s_sa.delete(0,tk.END)
	s_so.delete(0,tk.END)
	s_f.delete(0,tk.END)

	w_c.delete(0,tk.END)
	w_p.delete(0,tk.END)
	w_sa.delete(0,tk.END)
	w_so.delete(0,tk.END)
	w_f.delete(0,tk.END)

	r_c.delete(0,tk.END)
	r_p.delete(0,tk.END)
	r_sa.delete(0,tk.END)
	r_so.delete(0,tk.END)
	r_f.delete(0,tk.END)

	h_c.delete(0,tk.END)
	h_p.delete(0,tk.END)
	h_sa.delete(0,tk.END)
	h_so.delete(0,tk.END)
	h_f.delete(0,tk.END)

	
	# A table in the home_management.db database will be created, only if one does not exist (if it \
	#does exist, the program will just continue - line 478)
	# In the table there are 29 rows, some of them only accepting integer values, some only accepting \
	# integer values (int data type), some only accepting decimals (real data type), and some \
	#accepting any value, but treated like a string (text data type)
	try:

		cursor.execute("""CREATE TABLE property (
			property_name text, 
			property_type text,
			address text,
			city text,
			landscape_contractor text,
			landscape_frequency int,
			landscape_start text,
			landscape_stop text,
			landscape_fee real,
			snowplowing_contractor text,
			snowplowing_frequency int,
			snowplowing_start text,
			snowplowing_stop text,
			snowplowing_fee real,
			window_contractor text,
			window_frequency int,
			window_start text,
			window_stop text,
			window_fee real,
			roof_contractor text,
			roof_frequency int,
			roof_start text,
			roof_stop text,
			roof_fee real,
			hvac_contractor text,
			hvac_frequency int,
			hvac_start text,
			hvac_stop text,
			hvac_fee real
		)""")
	
	except:
		pass
	
	

	#This section will place the values that were extracted from the entry widet, into a row in the \
	#property table (in the database)
	cursor.execute("INSERT INTO property VALUES (\
		:col_name,:col_ptype,:col_addr,:col_cit,:lc,:lp,:lsa,:lso,:lf,:sc,:sp,:ssa,:sso,:sf,:wc,:wp,:wsa\
		,:wso,:wf,:rc,:rp,:rsa,:rso,:rf,:hc,:hp,:hsa,:hso,:hf)", 

		{
		#No category
		'col_name':col_name,
		'col_ptype':col_ptype,
		'col_addr':col_addr,
		'col_cit':col_cit,
		#Landscaping Category
		'lc':lc,
		'lp':lp,
		'lsa':lsa,
		'lso':lso,
		'lf':lf,
		#Roofing Category
		'sc':sc,
		'sp':sp,
		'ssa':ssa,
		'sso':sso,
		'sf':sf,
		#Window Maintenance Category
		'wc':wc,
		'wp':wp,
		'wsa':wsa,
		'wso':wso,
		'wf':wf,
		#Roofing Maintenance Category
		'rc':rc,
		'rp':rp,
		'rsa':rsa,
		'rso':rso,
		'rf':rf,
		#HVAC Maintenance category
		'hc':hc,
		'hp':hp,
		'hsa':hsa,
		'hso':hso,
		'hf':hf,

		}

	)
	#Committ any and all changes to the database
	connect.commit()



	


def dashboard(root):
	#Establish a connection to a database called "home_management.db" (essentially creates the database)
	#Database is made wtih SQLite
	# Connections made at the beginning of the program, but is made again as it has to be done in any \
	#functions developed
	connect = sqlite3.connect("home_management.db")
	#Develops a cursor for that database --- all actions, querys will be done using that database
	cursor = connect.cursor()


	# Calls the headings function, with actual parameter "Dashboard". This makes a header \
	# with the actual parameter as the title, and one button underneath, prompting the user to return \
	# to the main page
	headings("Dashboard")
	#Nested function that will be called when the dropdown menu changes
	def change_dropdown(*args):
		#Gets the value of the dropdown menu
		global dropdown 
		global status_table
		dropdown = str(display.get())
		#Queries all the values from the status table (not the variable...the table in the database)
		#Places all the values in the status_table variable - data type list - each index is a tuple
		cursor.execute("SELECT *, oid FROM status")
		status_table = cursor.fetchall()	


		#Given that each entry of the dropdown menu is an oid for each row, once the user selects that \
		#value, the row will appear as a label
		#Any existing label will have to be destroyed before adding a new one because 
		global status_show 
		global entry_show
		status_show.destroy()
		entry_show.destroy()
		#See line 589 for explanation
		stat2 = status_table[int(dropdown)-1]
		entry_show = tk.Label(status_frame,text="The property for this entry is: "+ str(stat2[0]),font=subtitle_font,anchor="w")
		status_show = tk.Label(status_frame,text="Entry Number "+ str(stat2[21]),font=subtitle_font,anchor="w")
		status_show.grid(row=2, column = 0,padx=30)
		entry_show.grid(row=3, column=0,padx=30)
		#Creates a new frame to add a table 
		table_frame = frame(4,0)
		#Creates a treeview and places it in the table frame
		tree = ttk.Treeview(table_frame)
		#Identifies the column of the treeview -> The categories defined aboved 
		# all columns have width of 120
		tree['columns'] = ("Landscaping","Snowplowing","Roofing","Window Maintenance","HVAC Maintenance")
		# Extra column Created (not specified above - automatically created)
		# Used to label rows. 
		tree.column("#0",width=120)
		# Specifies the size for each column (width = 120) and anchor (west)
		tree.column("Landscaping",anchor="w",width=120)
		tree.column("Snowplowing",anchor="w",width=120)
		tree.column("HVAC Maintenance",anchor="w",width=120)
		tree.column("Roofing",anchor="w", width=120)
		tree.column("Window Maintenance",anchor="w",width=120)
		#Inserts a heading (title) for each of the labels - on the top row in the tree
		tree.heading("#0", text="Label",anchor="w")
		tree.heading("Landscaping",text="Landscaping",anchor="w")
		tree.heading("Snowplowing",text="Snowplowing",anchor="w")
		tree.heading("Roofing",text="Roofing")
		tree.heading("Window Maintenance",text="Window",anchor="w")
		tree.heading("HVAC Maintenance",text="HVAC",anchor="w")
		#stat2 is a tuple, representing one of the rows in the sqlite database
		#The row it represents is the value indicated in the dropdown menu minus 1
		# The value indicated in the dropdown menu is the oid of the row
		# Subtract one because indices start from 0

		#Stat is another value, with same contents of stat2, just a list data type
		stat = list(stat2)

		#Convert every instance of a yes to the unicode symbol for checkmark
		# Convert every instance of a no to the unicode symbol for a red x
		for i,val in enumerate(stat):
			if val == "Yes":
				stat[i] = u"\u2705"
			elif val == "No":
				stat[i] = u"\u274C"





		#Insert all the values for hired (from each of the categories) to the tree
		#Indices 1, 5, 9, 13, and 17 are the indices for hired
		tree.insert(parent ='',index='end',iid=0,text="Hired",values = (stat[1],stat[5],stat[9],stat[13],stat[17]))
		#Insert all the values for paid (from each of the categories) to the tree
		#Indices 2, 6, 10, 14, and 18 are the indices for hired
		tree.insert(parent ='',index='end',iid=1,text="Paid",values = (stat[2],stat[6],stat[10],stat[14],stat[18]))
		#Insert all the values for concern (from each of the categories) to the tree
		#Indices 3, 7, 11, 15, and 19 are the indices for hired
		tree.insert(parent ='',index='end',iid=2,text="Concern",values = (stat[3],stat[7],stat[11],stat[15],stat[19]))
		#Insert all the values for paid (from each of the categories) to the tree
		#Indices 2, 6, 10, 14, and 18 are the indices for hired
		tree.insert(parent ='',index='end',iid=3,text="Description",values = (stat[4],stat[8],stat[12],stat[16],stat[20]))
		tree.pack(pady=20,expand=1)
		
		#Counters for yes and no
		yes = 0
		no = 0
		#Lists that contain the indices for hired, paid, and concern
		hired = [stat[1],stat[5],stat[9],stat[13],stat[17]]
		paid = [stat[2],stat[6],stat[10],stat[14],stat[18]]
		concern = [stat[3],stat[7],stat[11],stat[15],stat[19]]

		#Creates a frame in the 4th row (add one to row)
		global canvas_frame
		canvas_frame = frame(5,0)
		#Creates a nested function inside a nested function
		def plot(yes,no,first,second,list_of_choice,row,col):
			#If there is a checkmark, add one to yes, if there is an x, add one to no
			#Only for hired and paid -- if it was concern, it would be the other way around
			for i in list_of_choice:
				if i == u"\u2705":
					yes += 1
				else:
					no += 1

				values = [yes,no]
				#Formal parameters first and second
				labels = first,second
			#5 values in hired and paid (separately), multiply by 20 to get 100%
			size = [yes*20,no*20]
			#Creates a pie chart where the values for yes and no will be plot
			fig1, ax1 = plt.subplots()
			ax1.pie(size, explode=None, labels=labels, autopct='%1.1f%%',shadow=True, startangle=90,colors=["green","red"])
			ax1.axis('equal')
			fig = plt.gcf()
			fig.set_size_inches(3.5,3.5) # or (4,4) or (5,5) or whatever
			global canvas_frame
			#Places the graph on a tkinter canvas
			canvas = FigureCanvasTkAgg(fig1,master=canvas_frame)
			canvas.draw()
			canvas.get_tk_widget().grid(row=row,column=col,sticky="nesw")


		#Calls the plot function to make a pie chart for both hired and paid
		plot(yes,no,"Hired","Not \nHired",hired,0,0)
		plot(yes,no,"Paid","Not \nPaid",paid,0,1)
		
		
	#If an error shows up with the "try" command, a warning message will be brought up prompting the \
	#user to input a property/status (whichever they didn't input)
	try:
		#Creates a frame called status_frame in the fourth row
		status_frame = frame(3,0)
		#Label prompting the user to select a property to display the status
		select=tk.Label(status_frame,text="Select a Property to display status")
		select.grid(column=0,row=0,padx=30)

		#SQLite query selecting all from the status table, fetching all, and placing in the stat_all \
		#variable
		cursor.execute("SELECT *, oid FROM status")
		stat_all = cursor.fetchall()
		#list called list_of_status, currently prompting the user to click to see, however, will be \
		#populated
		list_of_status = ["Click to see"]
		#Taking every object identifier from every row in the status table, and adding it to the \
		#list_of_status variable. 
		
		
		for row in stat_all:
			list_of_status.append(row[21])
			print(list_of_status)
			
		#Creates a dropdown menu, with the contents of it being the list_of_status variable
		#Once the value of the dropdown menu changes, the change_dropdown function will be called
		global display
		display = tk.StringVar(status_frame) 
		display.set(list_of_status[0])
	 
		inquiry = tk.OptionMenu(status_frame, display, *list_of_status)
		inquiry.grid(row=0, column=1)	

		display.trace('w', change_dropdown)
	except:
		#Warning the user to enter a property or status
		status_warning = tk.Label(status_frame,text="Make sure you enter a status under tracking",font=warning_font)
		status_warning.grid(row=3,column=0)


	


def status_info(frame, text, row, column):
	'''
	This function contains the standard yes/no dropdown menu and a corresponding label

	Takes in 4 parameters -> frame, text (label corresponding), row, and column
	'''
	#Contents of the dropdown menu -> in the options list
	global options
	options  = [


	"Yes",
	"No"

	]
	#Create a label, text=the parameter text
	prop_name = tk.Label(frame,text=text)
	prop_name.grid(row=row, column=column, padx = 30)
	#Set the initial value of the dropdown menu to "Yes"
	status_store = tk.StringVar(frame) 
	status_store.set(options[0])
	 
	#Creates the dropdown menu, with the contents being options
	prop_ddm = tk.OptionMenu(frame, status_store, *options)
	prop_ddm.grid(row=row, column=column+1)
	return status_store

def tracking(root):
	#Establish a connection to a database called "home_management.db" (essentially creates the database)
	#Database is made wtih SQLite
	connect = sqlite3.connect("home_management.db")
	#Develops a cursor for that database --- all actions, querys will be done using that database
	cursor = connect.cursor()

	def change_dropdown(*args):
		#Gets the value of the dropdown menu
		global dropdown 
		dropdown = str(variable.get())
		#Queries all the values from the status table (not the variable...the table in the database)
		#Places all the values in the status_table variable - data type list - each index is a tuple
		cursor.execute("SELECT *, oid FROM property")
		table = cursor.fetchall()	
		
		#Given that each entry of the dropdown menu is an oid for each row, once the user selects that \
		#value, the row will appear as a label
		#Any existing label will have to be destroyed before adding a new one because 
		global show 
		show.destroy()
		one_entry = table[int(dropdown)-1]
		shown = []
		for i in range(4):
			shown.append(one_entry[i])
		show = tk.Label(drop_frame,text=shown)
		show.grid(row=2, column = 0,padx=30)

	# Calls the headings function, with actual parameter "Dashboard". This makes a header \
	# with the actual parameter as the title, and one button underneath, prompting the user to return \
	# to the main page
	headings("Tracking")
	#If an error shows up with the "try" command, a warning message will be brought up prompting the \
	#user to input a property/status (whichever they didn't input)
	try:
		#Creates a frame called status_frame in the fourth row
		drop_frame = frame(3,0)
		#Label prompting the user to select a property to display the status
		select=tk.Label(drop_frame,text="Select a Property")
		select.grid(column=0,row=0)
		#Queries all the values from the property table (not the variable...the table in the database)
		#Places all the values in the all_of_the_table variable - data type list -\
		# each index is a tuple
		cursor.execute("SELECT *, oid FROM property")
		
		all_of_the_table = cursor.fetchall()
		#list called list_of_name, currently prompting the user to click to see, however, will be \
		#populated
		
		list_of_name = ["Click to see"]
		#Taking every object identifier from every row in the status table, and adding it to the \
		#list_of_name variable.
		
		for row in all_of_the_table:
			list_of_name.append(row[29])
			print(list_of_name)

		global variable
		#Store the value of the dropdown menu in "variable"
		variable = tk.StringVar(drop_frame) 
		variable.set(list_of_name[0])
	 	#Creates a dropdown menu, with the contents of it being the list_of_status variable
		#Once the value of the dropdown menu changes, the change_dropdown function will be called
		options = tk.OptionMenu(drop_frame, variable, *list_of_name)
		options.grid(row=0, column=1)	

		variable.trace('w', change_dropdown)

		#Prompts the user to specify the progress made for each task 
		instruction = tk.Label(drop_frame, text = "Here you specify the progress for the tasks in the property you selected",anchor='w')
		instruction.grid(row=3,column=0,padx=30)
		##Declarations of global variables. Each row represents all the variable from one category
		#A category is a home maintenance task (landscaping, snowplowing, etc.)
		#The names of each variable, followed by the first letter of the question asked (first two in \
		# the event of a same letter)
		global l_h,l_m,l_w,l_desc
		global s_h,s_m,s_w,s_desc
		global r_h,r_m,r_w,r_desc
		global w_h,w_m,w_w,w_desc
		global h_h,h_w,h_m,h_desc
		#Landscaping category
		landscape = tk.Label(drop_frame,text="Landscaping",font=subtitle_font)
		landscape.grid(row=4, column=0, padx=10)
		#Asks user if they hired and paid the contractor, and if there are any concerns
		#Displays an entry widget asking the user to briefly describe concerns
		#Yes/no dropdown
		l_h = status_info(drop_frame, "Hired?", 5,0)
		l_m = status_info(drop_frame, "Paid?", 6,0)
		l_w = status_info(drop_frame,"Concern?",7,0)
		l_desc = basic_info("Describe the issues:", drop_frame, 8,0,1)
		#Snowplowing category
		snow = tk.Label(drop_frame,text="Snowplowing",font=subtitle_font)
		snow.grid(row=9, column=0, padx=10)
		s_h = status_info(drop_frame, "Hired?", 10,0)
		s_m = status_info(drop_frame, "Paid?", 11,0)
		s_w = status_info(drop_frame,"Concern?",12,0)
		s_desc = basic_info("Describe the issues:", drop_frame, 13,0,1)
		#Roof Maintenance category
		roof = tk.Label(drop_frame,text="Roofing",font=subtitle_font)
		roof.grid(row=14, column=0 ,padx=10)
		r_h = status_info(drop_frame, "Hired?", 15,0)
		r_m = status_info(drop_frame, "Paid?", 16,0)
		r_w = status_info(drop_frame,"Concern?",17,0)
		r_desc = basic_info("Describe the issues:", drop_frame, 18,0,1)
		#Window Maintenance category
		window = tk.Label(drop_frame,text="Window Maintenance",font=subtitle_font)
		window.grid(row=4, column=2, padx=10)
		w_h = status_info(drop_frame, "Hired?", 5,2)
		w_m = status_info(drop_frame, "Paid?", 6,2)
		w_w = status_info(drop_frame,"Concern?",7,2)
		w_desc = basic_info("Describe the issues:", drop_frame, 8,2,3)
		#HVAC Maintenance category
		hvac = tk.Label(drop_frame,text="HVAC Maintenance",font=subtitle_font)
		hvac.grid(row=9, column=2, padx=10)
		h_h = status_info(drop_frame, "Hired?", 10,2)
		h_m = status_info(drop_frame, "Paid?", 11,2)
		h_w = status_info(drop_frame,"Concern?",12,2)
		h_desc = basic_info("Describe the issues:", drop_frame, 13,2,3)

		#Button to submit the info and save it in a database
		submit = tk.Button(drop_frame, text = "Save",command = retrieve)
		submit.grid(row=24,column = 1)
		# Brief warning reminding user not to keep the first dropdown menu reading "click to see"\
		# (line 784)
		heads = tk.Label(drop_frame,text="Keep in mind that if the property reads 'click to see',\n your values will not save and you will have to redo.",anchor='w')
		heads.grid(row = 26,column=0)
	
	except:
		#Warning the user to enter a property or status
		warning = tk.Label(drop_frame,text="Make sure you enter a property",font=warning_font)
		warning.grid(row=3,column=0)




def retrieve():

	#Establish a connection to a database called "home_management.db" (essentially creates the database)
	#Database is made wtih SQLite
	# Connections made at the beginning of the program, but is made again as it has to be done in any \
	#functions developed
	connect = sqlite3.connect("home_management.db")
	#Develops a cursor for that database --- all actions, querys will be done using that database
	cursor = connect.cursor()

	#Get the value from each of the dropdown widgets defined in the Tracking function, and store \
	#them in another variable



	var = variable.get()
	lh = l_h.get()
	lm = l_m.get()
	lw = l_w.get()
	ld = l_desc.get()

	sh = s_h.get()
	sm = s_m.get()
	sw = s_w.get()
	sd = s_desc.get()

	rh = r_h.get()
	rm = r_m.get()
	rw = r_w.get()
	rd = r_desc.get()


	wh = w_h.get()
	wm = w_m.get()
	ww = w_w.get()
	wd = w_desc.get()

	hh = h_h.get()
	hm = h_m.get()
	hw = h_w.get()
	hd = h_desc.get()

	l_desc.delete(0,tk.END)
	s_desc.delete(0,tk.END)
	r_desc.delete(0,tk.END)
	w_desc.delete(0,tk.END)
	h_desc.delete(0,tk.END)

	

	# A table in the home_management.db database will be created, only if one does not exist (if it \
	#does exist, the program will just continue - line 478)
	# In the table there are 29 rows, some of them only accepting integer values, some only accepting \
	# integer values (int data type), some only accepting decimals (real data type), and some \
	#accepting any value, but treated like a string (text data type)
	try:

		cursor.execute("""CREATE TABLE status (
		
			property int,
			landscape_hire text,
			landscape_paid text,
			landscape_concern text,
			landscape_issue text,

			snowplow_hire text,
			snowplow_paid text,
			snowplow_concern text,
			snowplow_issue text,

			roof_hire text,
			roof_paid text,
			roof_concern text,
			roof_issue text,

			window_hire text,
			window_paid text,
			window_concern text,
			window_issue text,

			hvac_hire text,
			hvac_paid text,
			hvac_concern text,
			hvac_issue text

		)""")
	except:
		pass
		
	


	#This section will place the values that were extracted from the entry widet, into a row in the \
	#status table (in the database)
	cursor.execute("INSERT INTO status VALUES (:var,:lh,:lm,:lw,:ld,:sh,:sm,:sw,:sd,:rh,:rm,:rw,:rd,:wh,:wm,:ww,:wd,:hh,:hm,:hw,:hd)",

		{
		'var':int(var),
		'lh':lh,
		'lm':lm,
		'lw':lw,
		'ld':ld,

		'sh':sh,
		'sm':sm,
		'sw':sw,
		'sd':sd,

		'rh':rh,
		'rm':rm,
		'rw':rw,
		'rd':rd,

		'wh':wh,
		'wm':wm,
		'ww':ww,
		'wd':wd,

		'hh':hh,
		'hm':hm,
		'hw':hw,
		'hd':hd,


		}

		)

	connect.commit()
	


def admin(root):
	'''
	This function will delete data from all tables in the database

	It takes in one formal parameter root which is the 

	'''
	headings("Administration")
	delete = Button(root, text='Delete Data', bg='blue',fg='white', borderless=1, height = 75, width = 300,command = drop)
	delete.place(relx=0.5, rely=0.5, anchor="center")


def drop():
	connect = sqlite3.connect("home_management.db")
	cursor = connect.cursor()

	try:

		cursor.execute('''DROP TABLE IF EXISTS property;''')
		cursor.execute('''DROP TABLE IF EXISTS status;''')
		global good
		good.destroy()
		good = tk.Label(root, text = "Deleted")
		good.place(relx=0.5, rely=0.6, anchor="center")


	except:

		make = tk.Label(root, text = "You need to make a table first to delete")
		make.place(relx=0.5, rely=0.6, anchor="center")
	
	connect.commit()


def switch_admin():
	'''
	This function will be used to switch to the administration page

	It takes in no parameters - called by the command of a button

	Destroys all existing widgets. On the landing page, the page variable is 1, so always \
	administration can be called.

	By calling administration, the window will switch to the administration page

	''' 
	global page
	for i in root.winfo_children():
		i.destroy()
	if page ==1:
		admin(root)
		page=2


def enter():
	'''
	This function will be used to switch to the enter new property page

	It takes in no parameters - called by the command of a button

	Destroys all existing widgets. On the landing page, the page variable is 1, so always enter \
	new property function can be called.

	By calling enter new property, the window will switch to the enter new property page (done by \
	clicking the properties button)

	''' 
	global page
	for i in root.winfo_children():
		i.destroy()
	if page ==1:
		enterNewProperty(root)
		page=2

	
def switch_to_track():
	'''
	This function will be used to switch to the tracking page

	It takes in no parameters - called by the command of a button

	Destroys all existing widgets. On the landing page, the page variable is 1, so always tracking \
	can be called.

	By calling tracking, the window will switch to the tracking page

	''' 
	global page
	for i in root.winfo_children():
		i.destroy()
	if page ==1:
		tracking(root)
		page=2

def switch_to_dashboard():
	'''
	This function will be used to switch to the dashboard page

	It takes in no parameters - called by the command of a button

	Destroys all existing widgets. On the landing page, the page variable is 1, so always dashboard \
	can be called.

	By calling dashboard, the window will switch to the dashboard page

	''' 
	global page
	for i in root.winfo_children():
		i.destroy()
	if page ==1:
		dashboard(root)
		page=2
	

page = 1 





landing(root)

connect.commit()
connect.close()



root.mainloop()




