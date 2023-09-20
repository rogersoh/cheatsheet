# Generic CSV Uploader
## Need for a Generic CSV File Uploader
- Customers generate data during their experiments
- Such data need to be imported (uploaded) into our DB for further processing and analysis
- Often customer data are provided in the form of CSV file format
- CSV content (column definition & data types) changes depending on the type of data and therefore requires individual parsers each time
- Development of individual parser including data verification is time consuming
- A generic CSV File Uploader would remove the need for individual parser and cut development time.
- It also allow better code maintenance over time

## Future capabilities to consider during development
- Multithreading capability
This is in preparation for very large CSV files:
  - Parsing input data
  - Writing data to DB
- Consider the Generic CSV Uploader as an individual Module linked to Bio Server. This Module can be expanded in the future as import/export module, handling all data import to and export from Bio Server.
  - CSV File import / export
  - Genbank File import / export
  - etc

## Implementation note
- Requires Python 3.11.x
- Required Python packages
  - Numpy
  - Pandas
- Errors during conversion and upload will be saved in CSV file
- Parsed CSV rows will be saved in JSON object file

## CSV configuration file
- Specification of CSV columns
  - Name
  - Data Type
  - Range (min / max)
  - Categories
  - …
- JSON Format
- Must be provided along with CSV File to be uploaded

## JSON Configuration Object
```
{
  “csv_separator”: “,”,
  “continue_even_with_error” : “No”,
  “elements”:[
  {
  “column”: <string>,
  “desc”: <string>,
  “type”: <string>,
  “key_name”: <string>, # Optional - Phase 2
  “key_unit”: <string>, # Optional - Phase 2
  “record_unit”: <string>, #Optional - Phase 2
  [Optional Parameters]
  },
  ...
  ]
}
```

## JSON Configuration Object Definition
- **csv_file** : the name of the csv file with its extension
- **csv_separator** : is the delimited use to separate the list, the default is “,”, *Optional*
- **continue_err** : continue to clean the record and output to JSON even if there is error, *Optional*

----

**elements** object is the characteristic of each of the column.
- **column** : Column name
- **desc** : Description of the Column
- **type** : Column type, select from “String”, ”Number”, “List”

### Optional Parameters:

- **key_name** : database friendly alternative name of the column, it is the same as column name if not defined
- **key_unit** : units of measurement used in the database, it only applicable to the number type
- **record_unit** : units of measurement in the csv records
- **min** : either minimum length or minimum value based on the data type
- **max** : either maximum length or maximum value based on the data type
- **blank_accepted** : whether blank, null or na is accepted

## JSON Configuration Object - type “String”
```
{
  “column”: <string>,
  “desc”: <string>,
  “type”: “String”,
  “key_name”: <string>,
  “min”: <integer>, # Min length; Optional
  “max”: <integer>,  # Max length; Optional
  “cap”: “upper|lower|keep”, # Optional;
  “blank_accepted”: “[Yes|No]”,
  # Whether blank, null or na is allow on the column, Optional
}
```
- column names are case sensitive and must be unique
- “key_name”,”key_unit”, “record_unit”, “min”, “max”, “cap”  and “blank_accepted” parameters are optional
- “blank_accepted” settings: “[Yes|No]”
- “cap” settings:
  - “keep” → It means keeping input string as is (default behavior).
  - “upper” → Convert string to uppercase
  - “lower” → Convert string to lowercase


## JSON Configuration Object - type "Number"
```
{
  “column”: <string>,
  “desc”: <string>,
  “type”: “Number”,
  “key_name”: <string>,
  “key_unit”: <string>,
  “record_unit”: <string>,
  “min”: <integer>, # Min value; optional
  “max”: <integer>,  # Max value; optional
  “blank_accepted”: “[Yes|No]” # Whether blank is allow on the column, Optional
}
```
- column names are case sensitive and must be unique
- “key_name”,“key_unit”,“record_unit”, “min”, “max”, “cap”  and “blank_accepted” parameters are optional
- “blank_accepted” settings: “[Yes|No]”
- “cap” settings:
  - “keep” → It means keeping input string as is (default behavior).
  - “upper” → Convert string to uppercase
  - “lower” → Convert string to lowercase