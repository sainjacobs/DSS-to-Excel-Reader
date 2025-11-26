# DSS Reader

## File Structure

- dssReader.py (main)
- csdss_readlib.py (functions to read DSS file contents and save in pickle + Excel)
- TR_fields.txt (default fields to read in)

## What this code does

These two scripts pull a list of selected variables from multiple DSS files (or just one) containing the outputs of a model's runs into Excel. The same list of variables is used for each file and variables that are not in all files are excluded. Variables are columns. Timesteps are rows. Alternatives are blocks of rows.

The intent of this approach was twofold: (1) provide a fast, reusable way to pull variables for Excel-based comparison between alternatives without relying on the HEC-DSS Excel add-in, and (2) pull data for dynamic plotting using Bokeh.

The second use (dynamic plotting) is the reason for some of the idiosyncrasies in the code. Hopefully, by creating a separate repo for just the DSS-file-reading functionality, we can streamline this code.

## Usage Instructions
Create an environment from the yml file with the line: `conda env create -f environment.yml`
1. Open dssReader.py in your local version of the CalSim DSS Reader.
2. Set `make_archive` to True to pull new results or False to pull previously pulled data. Generally, this should be set to True.
3. In line 20, set the "model" variable equal to the string name of the type of model you wish to interpret data from (options are "CALSIM", "HEC5Q" or "DSM2")
4. Beginning in line 29 in the "runs" list, for each list entry in "runs", enter the name of each of your dss files in the parentheses along with the name of the run
(such as Baseline, Alt1, etc.). Refer to the NAA scenario as "Baseline". A NAA/Baseline scenario must be included in the runs for
the appendix generation script to function properly down the line. Don't forget the ".dss" file extension when you are specifying file names.
5. Beginning line 48, in the "add_field_list", specify the field variables that you want to retrieve from the DSS files. These correspond to the B part in the DSS pathname.
6. Run dssReader.py.
7. When the DSS Reader has finished running, open the calsim_dss_reader directory and find the DSS Reader outputs. There should be three files: DSS_contents.xlsx, DSS_contents_CFS.xlsx, and DSS_contents_TAF.xlsx. The first output file preserves all unitsfrom the input dss file, the second converts relevant columns to CFS, and the third converts to TAF.

## Model and field variable selection

The DSS Reader can be used for CALSIM, HEC5Q, or DSM2 model outputs by changing the string in line 20 in dssReader.py. Additionally, the list of the list of fields names beginning in line 44 will need to be changed. 

Below are some example fields that can be set for each type of model. In its current form in the repo, the reader is set to run on CALSIM model outputs. 

**CALSIM:** 
 	"C_LWSTN",
        "C_CLR011",
        "C_KSWCK",
        "C_SAC257",
        "C_SAC240",
        "C_SAC201",
        "C_SAC120",
        "C_FTR059",
        "C_FTR059",
        "C_FTR003"

**HEC5Q:**
	"BLW CLEAR CREEK",
        "RED BLUFF",
        "BLW NIMBUS(HAZEL AVE)",
        "BLW ORBL BR",
        "BLW LEWISTON",
        "WHISKEYTOWN",
        "IGO",
        "ABV SACRAMENTO"
        "BLW KESWICK",
        "BALLS FERRY",
        'JELLYS FERRY',
        "BEND BRIDGE"
        'RED BLUFF DAM',
        "HAMILTON CITY",
        "BUTTE_CITY"
        "KNIGHTS LDG",
        "WATT AVE",
        "ABV CONFLUENCE",
        "AT_N_FORK",
        "BLW NEW MELONES",
        "BLW TULLOCH",
        "BLW GOODWIN"

**DSM2:**
	"SAC_DS_STMBTSL",
        "RSAN007",
        "RSAC075",
        "RSAC081",
        "CHIPS_N_437",
        "CHIPS_S_442",
        "RSAC064",
        "CHDMC006",
        "CLIFTONCOURT",
        "ROLD034",
        "CHVCT000",
        "CACHE_RYER",
        "RSAC123",
        "RSAC092",
        "RSAC101",
        "RSAN112",
        "RSAN112",
        "RSAN018",
        "ROLD024"
        "ROLD024",
        "RSAN007",
        "CLIFTONCOURT",
        "CHDMC006",
        "SLBAR002",
        "SJR_SAN_ANDREAS",
        "RSAN037",
        "SLMZU003",
        "SLMZU011",
        "SLMZU025",
        "RYC",
        "GYS",
        "3MILE_SL",
        "RSAC075",
        "RSAC101",
        "RSAC081",
        "RSAN018",
        "RSAN032",
        "RSAN037",
        "ROLD034",
        "CHVCT000"


## Support
If an issue is found, please submit a ticket through the GitHub issue tracking system.