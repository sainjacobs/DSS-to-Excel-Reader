# CalSim_DSS_Reader

Create an environement from the yml file. Specific version requirements are:
 - Python 3.10 or 3.11
 - numpy 1.26.4
 - pydsstools 2.3.2 (pip)

## File Structure

|- cs3_viz_app_main.py (main) <br/>
|--- csdss_readlib_fullfile.py (read DSS file contents and save in pickle + Excel) <br/>
|----- TR_fields.txt <br/>
|--- cs3_plotlib.py (plotting functions) <br/>

## What this code does

These two scripts pull a list of selected variables from multiple DSS files (or just one) containing the outputs of CalSim runs into Excel. The same list of variables is used for each file and variables that are not in all files are excluded. Variables are columns. Timesteps are rows. Alternatives are blocks of rows.

The intent of this approach was twofold: (1) provide a fast, reusable way to pull variables for Excel-base comparison between alternatives with out relying on the HEC-DSS Excel add-in, and (2) pull data for dyanmic plotting using Bokeh.

The second use (dynamic plotting) is the reason for some of the idiosyncracies in the code. Hopefully, by creating a separate repo for just the DSS-file-reading functionality, we can streamline this code.

## Usage Instructions

1. Open dssReader.py in your local version of the CalSim DSS Reader.
2. In line 35, set the "model" variable equal to the string name of the type of model you wish to interpret data from (options are "CALSIM", "HEC5Q" or "DSM2")
3. Beginning in line 37 in the "runs" list, for each list entry in "runs", enter the name of each of your dss files in the parentheses along with the name of the run
(such as Baseline, Alt1, etc.). Refer to the NAA scenario as "Baseline". A NAA/Baseline scenario must be included in the runs for
the appendix generation script to function properly down the line. . Don't forget the ".dss" file extension when you are specifying file names.
4. Beginning line 56, in the "add_field_list", specify the field variables that you want to retrieve from the DSS files. These correspond to the B part in the DSS pathname.
5. Run dssReader.py.
6. When the DSS Reader has finished running, open the calsim_dss_reader directory and find the DSS Reader outputs. There should be three files: DSS_contents.xlsx, DSS_contents_CFS.xlsx, and DSS_contents_TAF.xlsx. The first output file preserves all unitsfrom the input dss file, the second converts relevant columns to CFS, and the third converts to TAF.

## Model and field variable selection

The DSS Reader can be used for CALSIM, HEC5Q, or DSM2 model outputs by changing the string in line 35. Additionally, the list of the list of fields names beginning in line 56 will need to be changed. 

Below are some example fields that can be set for each type of model. In its current form in the repo, the reader is set to run on CALSIM model outputs. 

CALSIM
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

HEC5Q
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
DSM2
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


