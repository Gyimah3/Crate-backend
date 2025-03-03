few_shots_examples = {
    "List all the brands available in Abidjan.": """SELECT DISTINCT Brand FROM retail_data WHERE City = 'Abidjan';""",
    "What is the total sales value for Boutique channels?": """SELECT SUM(Sales_Value) FROM retail_data WHERE Channel = 'Boutique';""",
    "Who is the manufacturer with the highest sales value?": """SELECT Manufacturer, SUM(Sales_Value) AS total_sales FROM retail_data GROUP BY Manufacturer ORDER BY total_sales DESC LIMIT 1;""",
    "How many unique items are sold in the pasta category?": """SELECT COUNT(DISTINCT `Item Name`) FROM retail_data WHERE Category = 'PASTA';""",
    "Sort the items by unit price in descending order.": """SELECT `Item Name`, Unit_Price FROM retail_data ORDER BY Unit_Price DESC;""",
    "Are there any sales in the segment 'DRY PASTA' in Jan-21?": """SELECT * FROM retail_data WHERE Segment = 'DRY PASTA' AND Period = 'Jan-21';""",
    "What is the average unit price of items in 'CAPRA' manufacturer?": """SELECT AVG(Unit_Price) FROM retail_data WHERE Manufacturer = 'CAPRA';""",
    "Which city has the highest total sales volume?": """SELECT City, SUM(`Sales_Volume(KG_LTRS)`) AS total_volume FROM retail_data GROUP BY City ORDER BY total_volume DESC LIMIT 1;""",
    "List all item names that have a pack size of 200G.": """SELECT `Item Name` FROM retail_data WHERE Pack_Size = '200G';""",
    "How many different packaging types are used?": """SELECT COUNT(DISTINCT Packaging) FROM retail_data;""",
    "What is the total sales value for the brand 'MAMAN'?": """SELECT SUM(Sales_Value) FROM retail_data WHERE Brand = 'MAMAN';""",
    "List all manufacturers in alphabetical order.": """SELECT DISTINCT Manufacturer FROM retail_data ORDER BY Manufacturer;""",
    "What is the unit price of the cheapest item?": """SELECT `Item Name`, Unit_Price FROM retail_data ORDER BY Unit_Price ASC LIMIT 1;""",
    "How many cities have recorded sales in Jan-21?": """SELECT COUNT(DISTINCT City) FROM retail_data WHERE Period = 'Jan-21';""",
    "What is the highest sales volume recorded for 'Boutique' channels?": """SELECT MAX(`Sales_Volume(KG_LTRS)`) FROM retail_data WHERE Channel = 'Boutique';""",
    "Which item has the highest sales value in 'DRY PASTA' segment?": """SELECT `Item Name`, Sales_Value FROM retail_data WHERE Segment = 'DRY PASTA' ORDER BY Sales_Value DESC LIMIT 1;""",
    "How many brands are produced by 'CAPRA' manufacturer?": """SELECT COUNT(DISTINCT Brand) FROM retail_data WHERE Manufacturer = 'CAPRA';""",
    "List all items with a unit price greater than 100.": """SELECT `Item Name`, Unit_Price FROM retail_data WHERE Unit_Price > 100;""",
    "What is the total sales volume for all items in 200G pack size?": """SELECT SUM(`Sales_Volume(KG_LTRS)`) FROM retail_data WHERE Pack_Size = '200G';"""
}

retriever_tool_description = (
    "The 'sql_get_few_shot' tool is designed for efficient and accurate retrieval of "
    "SQL query examples closely related to a given user query. It identifies the most "
    "relevant pre-defined SQL query from a curated set."
)

COLUMNS_DESCRIPTIONS = {
    # "Period": "The time period for the data entry (example: 'Jan-21')",
    # "City": "The city where the data was collected (example: 'Abidjan')",
    # "Channel": "The sales channel (example: 'Boutique')",
    # "Category": "The product category (example: 'PASTA')",
    # "Segment": "The segment within the category (example: 'DRY PASTA')",
    # "Manufacturer": "The manufacturer of the product (example: 'CAPRA')",
    # "Brand": "The brand of the product (example: 'ALYSSA')",
    # "Item Name": "The name of the item (example: 'ALYSSA SPAGHETTI 200G SACHET')",
    # "Pack_Size": "The size of the product packaging (example: '200G')",
    # "Packaging": "The type of packaging (example: 'SACHET')",
    # "Unit_Price": "The price per unit of the product (example: '89.06')",
    # "Sales_Volume(KG_LTRS)": "The sales volume in kilograms or liters (example: '66,795.7')",
    # "Sales_Value": "The total sales value (example: '21,286,480.6')",
    "Year": "Year data was recorded",
    "conference": "the various conference that we have(example: 'Central Ghana Conference')",
    "Union": "various Union that we have(example: 'Northern Ghana Union Conference')",
    "Churches": "shows the total number of registered churches for the specified year and field(example: '83')",
    "Companies": "shows the total number of companies for the specified year and field.(example: '23214)'",
    "Beginning Membership":	"is the membership at the beginning of the year.",
    "Baptisms":	"is the number of additions by baptism reported for the given year.",
    "Former Member Baptisms": "varous records on Former member baptised(example: '21.0')",
    "Professions of Faith": "is the number of additions by profession of faith reported for the given year.",
    "Transfers In":	"is the number of additions by transfer of membership into this conference during the year.",
    "Transfers Out":"is the number of losses by transfer of membership out of this conference during the year.",
    "Deaths": "is the number of losses by death.",
    "Dropped": "is the number of memberships dropped by individual request.",
    "Missing": "is the number of members reported missing.",
    "TotalGain": "is the total number of members added by all methods.",
    "TotalLoss": "is the total number of members remoded by all methods.",
    "Adjust": "is used historically to note adjustments needed to insure consistency because of reporting errors or subsequent corrections.",
    "Net Growth":"shows the net growth during the year.",
    "Accession Rate": "indicates the number of accessions (baptisms and professions of faith) as a percentage of beginning membership in the given year.",
    "Death Rate": "indicates the number of deaths as a percentage of beginning membership.",
    "Ordained Ministers": "is the number of ordained ministers",
    "Licensed Ministers": "is the number of licensed ministers",
    "Beginning Membership": "The number of members the church began with within a particular year",
    "Ending Membership": "the number of members the church ended with within a particular year",


}