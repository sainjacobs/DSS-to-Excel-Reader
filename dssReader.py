# -------------------------------------------------------------------
# DSS File reader 0.1
# Sam Waers, P.E.; Frankie Nuffer-Rodriguez
#
# Run this file in same directory as dssReadFuncs.py
# See the "import" statements at the top of  in dssReadFuncs.py
# for a list of dependencies which will need to be installed
# in the environment you use for this script.
# -------------------------------------------------------------------

# Import data handling functions from our local module
from csdss_readlib import file_reader, pickler, load_pickles, get_trend_fields
import time
import pandas as pd
# NOTE: need to use name/main for Pool to work outside of script

start_time = time.time()

if __name__ == '__main__':

    # 'make_pickles' is switch to save time when repeatedly pulling
    # the same list of variables from the same files.
    # You can set this to false after the first time you read the
    # specific list of variables below from the set of the specific
    # set of files below.
    # If you change either list, you need to make pickles again.
    make_archive = True

    # List of runs. If not storing DSS files in the same directory,
    # provide full paths or paths relative to this file.
    # structure is [["Description_1", ("File_1.dss")],
    #               ["Description_2", ("File_2.dss")],
    #          ...  ["Description_n", ("File_n.dss")]]
    # The names can be anything though, e.g. ["Alt2v1", Alt2v1_VAs.dss"]
    model = "CALSIM"

    runs = [
        ["Baseline", ("Reclamation_LTO_2021_NAA_CALSIM3_L2020A_090723.dss")],
        ["ALT1", ("CS3_ALT1_2022MED_09092023_L2020A_DV_dp.dss")],
        ["Alt2woTUCPwoVA", ("Reclamation_LTO_2021_Alt2v1_woTUCP_CALSIM3_L2020A_091324.dss")],
        ["Alt2woTUCPDeltaVA", ("Reclamation_LTO_2021_Alt2v2_woTUCP_CALSIM3_L2020A_091324.dss")],
        ["Alt2woTUCPAllVA", ("Reclamation_LTO_2021_Alt2v3_woTUCP_CALSIM3_L2020A_091324.dss")],
        ["Alt2wTUCPwoVA", ("Reclamation_LTO_2021_Alt2v1_wTUCP_CALSIM3_L2020A_091324.dss")],
        ["ALT3", ("Reclamation_LTO_2021_ALT3_CALSIM3_L2020A_092423.dss")],
        ["Alt4", ("Reclamation_LTO_2021_ALT4_CALSIM3_L2020A_091624.dss")]
        # ["Alt8", ("CS3DV_Iter6.dss")],
    ]

    l_tr_fields = get_trend_fields()

    # This is a list of the variables you want to retrieve.
    # These correspond to the B part in the DSS pathname.
    # Variables that are not present in all runs are thrown out
    # though this behavior can be changed if needed.

    add_field_list: list = [
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
    ]

    s_default = 'S_SHSTA'

    field_list = l_tr_fields + add_field_list

    # Only do this step if we are creating pickles. Otherwise, read the data
    # from existing pickles. Facilitates quickly jumping back into analysis
    # without having to load from DSS files.
    if make_archive == True:

        append_list, baseline_stack, c_default_units = file_reader(runs, field_list, model)
        pickler(append_list, baseline_stack, c_default_units)

    # This runs no matter what. The pickle files allow you to come back and
    # pull the same variables without waiting for the file reads to complete
    df_all_data, df_diffs, c_default_units = load_pickles()

    # Add a row with units below column titles to clarify output
    l_units = []
    for col in df_all_data.columns:
        if col in c_default_units:
            l_units.append(c_default_units[col])
        else:
            l_units.append("(none)")

    # Add units to original writeout (contains mixed units)
    df_units = pd.DataFrame(columns=df_all_data.columns)
    df_units.loc[0] = l_units
    df_all_data_units = df_units = pd.concat([df_units, df_all_data], axis=0)

    ### Unit-standard outputs ###
    ## Create versions where all CFS adn TAF are standardized
    # TODO - Put a Duration (days) column in output
    l_durations = [df_all_data['Date'][row].day for row in df_all_data.index]

    # Create TAF version, where all CFS vars are converted to TAF
    df_taf = df_all_data.copy(deep=True)
    for col in df_taf.columns:
        if col in c_default_units and df_all_data_units[col].iloc[0] == 'CFS':
            df_taf[col] = df_taf[col] * 24 * 3600 * l_durations / 43560 / 1000

    # Create CFS version, where all TAF vars are converted to CFS
    df_cfs = df_all_data.copy(deep=True)
    for col in df_cfs.columns:
        if col in c_default_units and df_all_data_units[col].iloc[0] == 'TAF':
            df_cfs[col] = df_cfs[col] / 24 / 3600 / l_durations * 43560 * 1000

    # Write original output to Excel.
    try:
        df_all_data.to_excel("DSS_contents.xlsx")
    except:
        print("Error writing output file. "
              "Make sure 'DSS_contents.xlsx' is not open.")
    # Write original output + units to Excel.
    try:
        df_all_data_units.to_excel("DSS_contents_Units.xlsx")
    except:
        print("Error writing output file. "
              "Make sure 'DSS_contents_Units.xlsx' is not open.")
    # Write TAF version to Excel.
    try:
        df_taf.to_excel("DSS_contents_TAF.xlsx")
    except:
        print("Error writing output file. "
              "Make sure 'DSS_contents_TAF.xlsx' is not open.")
    # Write CFS vresion to Excel.
    try:
        df_cfs.to_excel("DSS_contents_CFS.xlsx")
    except:
        print("Error writing output file. "
              "Make sure 'DSS_contents_CFS.xlsx' is not open.")

    print(f'Total runtime: {(time.time()-start_time)/60} minutes')
    print(f'Pulled: {len(runs)} files')

