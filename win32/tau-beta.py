import win32com.client as win32

# Grab the active instance of Word
word_app = win32.GetActiveObject("Word.Application")

# Grab the active Word document
word_doc = word_app.ActiveDocument

# Create a reference to the Table object in the active Word document
# We only have 1 Table object, hence Tables.Item(1) 
word_table = word_doc.Tables.Item(1)

# Grab the Columns in the Table that we want (i.e., 5, 6, 7, 8)
# Update these indexes for your own Columns
# Word numbers Columns left to right and starts at 1

# Temperature-dependent amplitude Columns
AfQ_Column = word_table.Columns(5)
oneMinusAfQ_Column = word_table.Columns(6)

# Mobile component fraction Column
Am_Column = word_table.Columns(7)

# Immobile component fraction Column
oneMinusAm_Column = word_table.Columns(8)

# Loop through each Cell in the Af(Q) Column, excluding the Cell titled Af(Q)
# Since we only want to work with numerical Cell data
for AfQ_Cell in list(AfQ_Column.Cells)[1:]:
    
    # Grab the Text in AfQ_Cell
    AfQ_Cell_Text = AfQ_Cell.Range.Text
    
    # Clear out the Old Text
    AfQ_Cell.Range.Text = ""
    
    # Create a Field Code
    field_code = "={my_number}\#""0.00000""".format(my_number = AfQ_Cell_Text)
    
    # Select the Cell Range
    AfQ_Cell.Range.Select()
    
    # Collapse the Selection to the start of the Cell Range
    word_app.Selection.Collapse(Direction=1)
    
    # Grab the Selection Range
    select_range = word_app.Selection.Range
    
    # Set a Field Code for the Selection Range, which should be an Empty Type [-1].
    # We populate the Selection Range with our Created Field Code.
    select_range.Fields.Add(Range=select_range, Type=-1, Text=field_code, PreserveFormatting=True)

# Loop through each Cell in the A_m Column, excluding the Cell titled A_m
# Update references as needed
for Am_Cell in list(Am_Column.Cells)[1:]:
    
    Am_Cell_Text = Am_Cell.Range.Text
    Am_Cell.Range.Text = ""
    
    field_code = "={my_number}\#""0.00000""".format(my_number = Am_Cell_Text)
    
    Am_Cell.Range.Select()
    
    word_app.Selection.Collapse(Direction=1)
    select_range = word_app.Selection.Range
    select_range.Fields.Add(Range=select_range, Type=-1, Text=field_code, PreserveFormatting=True)

for oneMinusAfQ_Cell in list(oneMinusAfQ_Column.Cells)[1:]:
    
    oneMinusAfQ_Cell.Range.Text = ""
    
    # Pay heed to VBA notation (i.e., R1C1, R1C2, R1C3, etc.)
    # Ensure accurate references to Cell data and calculate [1 - Af(Q)]
    field_code = "=1 - R{row_number}C5 \#""0.00000""".format(row_number = oneMinusAfQ_Cell.Row.Index)
    
    oneMinusAfQ_Cell.Range.Select()
    
    word_app.Selection.Collapse(Direction=1)
    select_range = word_app.Selection.Range
    select_range.Fields.Add(Range=select_range, Type=-1, Text=field_code, PreserveFormatting=True)

for oneMinusAm_Cell in list(oneMinusAm_Column.Cells)[1:]:
    
    oneMinusAm_Cell.Range.Text = ""
    
    # Pay heed to VBA notation (i.e., R1C1, R1C2, R1C3, etc.)
    # Ensure accurate references to Cell data and calculate [1 - A_m]
    field_code = "=1 - R{row_number}C7 \#""0.00000""".format(row_number = oneMinusAm_Cell.Row.Index)
    
    oneMinusAm_Cell.Range.Select()
    
    word_app.Selection.Collapse(Direction=1)
    select_range = word_app.Selection.Range
    select_range.Fields.Add(Range=select_range, Type=-1, Text=field_code, PreserveFormatting=True)
