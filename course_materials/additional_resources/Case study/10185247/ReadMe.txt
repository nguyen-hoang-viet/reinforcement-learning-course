The folder contains:

1. Input_data.xlsx

This spreadsheet contains the data related to six instances validated in the manuscript. The information is presented in different sheets, organised as follows:

a) Sheet "param":

	- lmin: lower bound for the panels' length (mm)
	- lmax: upper bound for the panels' length (mm)

b) There are six sheets (I9, I11, I12, I15, I18, I19) with the notation Ix where x is the instance presented in the manuscript. Each sheet contains the information of an order received by the company, given by a list of items with their characteristics:

	- Item: items' reference (label)
	- Width: items' width (mm)
	- Length: items' length (mm)
	- Demand: items' demand (units)

c) Sheet "SM": it contains, for model SM, the configurations' set used in the manuscript:

	- configuration: configurations' reference (label)
	- Width: configurations' width (mm)
	- Length: configurations' length (mm)

d) There are two sheets for model VSM: sheet "VSM_W1" where W1={1200} and sheet "VSM_W2" where W2={1200, 1400, 1550, 1600}. Both sheets contain the following information:

	- nc: maximum number of configurations allowed (units)
	- configuration: configurations' reference (label)
	- Width: configurations' width (mm)



2. Results are reported in 18 files, three per instance, the following notation has been stablished:

	Ix_mod_Wy.xlsx 

where: Ix denotes the instance; mod denotes the model used (SM/VSM); and, Wy denotes the set of available widths (mm) used, being W1={1200} and W2={1200, 1400, 1550, 1600}.

Files Ix_mod_W1.xslx (i.e., set W1 is used) contain four sheets named "ncB" where B is a number (1,2,3,4) that refers to the maximum number of configurations allowed (nc=1, nc=2, nc=3, nc=4).

Files Ix_VSM_W2.xslx (i.e., set W2 is used) contain eight sheets named "nwA_ncB" where A and B are numbers. A refers to the maximum number of widths that can be used (nw=1, nw=2, nw=4) and B refers to the maximum number of configurations allowed (nc=1, nc=2, nc=3, nc=4, nc=8).

Each sheet in the mentioned files contains a row per item with the following information (columns):
 
	- Item: items' reference (label)
	- li: items' width (mm)
	- wi: items' length (mm)
	- di: items' demand (units)
	- j: configurations' reference to which the item has been assigned to (label)
	- P: number of panels produced to meet the demand (units)
	- Wj: panels' width of the configuration selected for the item (mm)
	- Lj: panels' length of the configuration selected for the item (mm)
	- left: leftover generated (m^2)

