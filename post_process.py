import json
import pandas as pd
from json import loads
from csv_import_lib import csvFileReader

cfgFile = "fileconfig4_sample_data.json"
recFile = "sample_data.csv"
baseUnitsFile = "baseunits.json"
initVol = 2.1 # initial volume in Liter

# baseUnits is an object that is read from On BioIO Server DB
# the baseUnitFile is only given as an example
# read baseUnitFile into a list - baseUnitLists
with open(baseUnitsFile, "r") as f:
  baseUnitsLists = json.load(f)

csvFileReaderData = csvFileReader(cfgFile, recFile, baseUnitsLists)
configurationFileErrorDF = csvFileReaderData["configFileError"]
recordFileErrorMessageDF = csvFileReaderData["recordFileError"]
recordOutputList = csvFileReaderData["recordOutput"] #record output in List format

def postProcess(recordOutputList):
  df = pd.DataFrame(recordOutputList)
  df = df.sort_values(by = ["age"])
  df = df.reset_index().drop(["index"], axis=1)

  df["Total_Accumulated_Carbon"] = df.iloc[0]["carbon_conc_measured"] * initVol + df["fed_carbon"] # g
  df["Carbon_In_Media"] = (initVol + df["increased_vol"]/1000) * df["carbon_conc_measured"] # g
  df["Total_Consumed_Carbon"] = df["Total_Accumulated_Carbon"] - df["Carbon_In_Media"] # g
  df["Consumed_Carbon_Between_Sampling"] = df["Total_Consumed_Carbon"].diff() # g
  df["Carbon_Consumed_Rate"] = df["Consumed_Carbon_Between_Sampling"] / df["age"].diff() # g/hr
  df["Product_Adjust"] = (initVol + df["increased_vol"]/1000) * df["product_conc"] # g
  df["Production_Rate"] = df["product_conc"].diff() * 1000 / df["age"].diff() # (mg/L)/hr
  df["Yield"] = df["Product_Adjust"].diff() * 1000 / df["Consumed_Carbon_Between_Sampling"] # mg/g

  # TODO after confirming what should the Yield in 12 hour interval is based upon
  """
  # to calculate for Yield in 12 hour interval
  mask = df["age"] % 12 == 0
  tempDF = df[mask].copy() # copy the 12 hours interval data to tempDF

  # base on Product_Adjust / consumed_carbon_between_sampling
  tempDF.loc[0, "Consumed_Carbon_Between_Sampling"] = 0
  tempDF["Yield_12hr_interval"] = tempDF["Product_Adjust"].diff() * 1000 / tempDF["Consumed_Carbon_Between_Sampling"].diff()

  # Calculate the carbon consumed in the 12 interval from the difference in the "Total_Consumed_Carbon"
  # tempDF["Yield_12hr_interval"] = tempDF["Product_Adjust"].diff() * 1000 / tempDF["Total_Consumed_Carbon"].diff()

  # Calculate Yield_12hr_interval base on Yield per hour
  # tempDF["Yield_12hr_interval"] = tempDF["Product_Adjust"].diff() * 1000 / tempDF["age"].diff()

  # merge to df dataframe
  tempDF = tempDF[["age","Yield_12hr_interval"]]
  df = df.merge(tempDF, how = "left")
  """

  print(df)
  dfJSON = df.to_json(orient = "records")
  parsed = loads(dfJSON) # make json more readable
  return parsed

def test(dataList, testFile, columnsDict):
  dataDF = pd.DataFrame(dataList)
  dataColumns = ["age", "Total_Accumulated_Carbon", "Carbon_In_Media", "Total_Consumed_Carbon",
    "Consumed_Carbon_Between_Sampling", "Carbon_Consumed_Rate", "Product_Adjust", "Production_Rate",
    "Yield"]
  dataDF = dataDF[dataColumns]
  dataDF = dataDF.set_index("age")
  testDF = pd.DataFrame(testFile)
  testDF = testDF.set_index("age")
  resultDF = dataDF.merge(testDF, how = "inner", left_index = True, right_index = True)
  for key in columnsDict.keys():
    colName = "Diff_"+ str(key)
    resultDF[colName] = resultDF[key] - resultDF[columnsDict[key]]
    print(f"\n The difference in {key} column")
    print(resultDF[[key, columnsDict[key],colName]])
  return resultDF

postProcessedOutput = postProcess(recordOutputList)

PerformTest = True

resultTestDict = {'Total_Accumulated_Carbon': 'Test_TotalCarbon',
 'Carbon_In_Media': 'Test_CarbonInMedia',
 'Total_Consumed_Carbon': 'Test_ConsumedCarbon',
 'Consumed_Carbon_Between_Sampling': 'Test_ConsumedCarbonInSample',
 'Carbon_Consumed_Rate': 'Test_CarbonConsumedRate',
 'Product_Adjust': 'Test_ProductAdjust',
 'Production_Rate': 'Test_ProdRate',
 'Yield': 'Test_Yield'}

if PerformTest:
  testcfgFile = "test_data_config.json"
  testFile = "test_data.csv"
  testbaseUnitsFile = "test_data_baseunits.json"

  with open(testbaseUnitsFile, "r") as f:
    baseLists = json.load(f)

  testData = csvFileReader(testcfgFile, testFile, baseLists)
  testResult = test(postProcessedOutput , testData["recordOutput"], resultTestDict)

#TODO to calculate Yield for 12 hour interval. Need to check formula for that as the Example
# result is different from our calculation
