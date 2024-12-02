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
from csdss_readlib import reader, pickler, load_pickles, get_trend_fields

# NOTE: need to use name/main for Pool to work outside of script
if __name__ == '__main__':

    # 'make_pickles' is switch to save time when repeatedly pulling
    # the same list of variables from the same files.
    # You can set this to false after the first time you read the
    # specific list of variables below from the set of the specific
    # set of files below.
    # If you change either list, you need to make pickles again.
    make_pickles = True

    # List of runs. If not storing DSS files in the same directory,
    # provide full paths or paths relative to this file.
    # structure is [["Description_1", ("File_1.dss")],
    #               ["Description_2", ("File_2.dss")],
    #          ...  ["Description_n", ("File_n.dss")]]
    # The names can be anything though, e.g. ["Alt2v1", Alt2v1_VAs.dss"]
    runs = [
        ["Baseline", ("Baseline.dss")],
        ["Alt2", ("Alt2.dss")],
        ["Alt3", ("Alt3.dss")],
    ]

    # Most commonly used fields from Trend Report
    l_tr_fields = get_trend_fields()

    # This is a list of the variables you want to retrieve.
    # These correspond to the B part in the DSS pathname.
    # Variables that are not present in all runs are thrown out
    # though this behavior can be changed if needed.
    add_field_list = [
        "test",
        "WYT_SJR_",
        "WYT_SJR_STAN_",
        "S_MELON",
        "C_MELON",
        "C_STS059",
        "D_STS059_OAK001",
        "D_STS059_UFC000",
        "D_WDWRD_61_PA3",
        "D_STS059_SSJ001",
        "D_SSJ004_61_PA1",
        "D_OAK020_61_PA2",
        "C_LJC022",
        "C_LJC010",
        "D_LJC010_60S_PA2",
        "D_LJC022_WTPWDH",
        "D_LJC022_60S_PA1",
        # "LJC_TO_CSJWCD_",
        # "LJC_TO_SEWD_",
        # "UFC_TO_CSJWCD_SJRBASE_",
        # "UFC_TO_SEWD_SJRBASE_",
        "D_CLV026_60S_PA1",
        "D_CLV026_WTPWDH",
        "D_WTPDWS_60S_NU1",
        "D_MOK035_WTPDWS",
        "D_SJR028_WTPDWS",
        "C_MELONVA",
        "S_SHSTA"
    ]

    s_default = 'S_SHSTA'

    field_list = l_tr_fields + add_field_list

    # Only do this step if we are creating pickles. Otherwise, read the data
    # from existing pickles. Facilitates quickly jumping back into analysis
    # without having to load from DSS files.
    if make_pickles == True:
        append_list, baseline_stack, c_default_units = reader(runs, field_list)
        pickler(append_list, baseline_stack, c_default_units)

    # This runs no matter what. The pickle files allow you to come back and
    # pull the same variables without waiting for the file reads to complete
    df_all_data, df_diffs, c_default_units = load_pickles()

    # Write to Excel.
    try:
        df_all_data.to_excel("DSS_contents.xlsx")
    except:
        print("Error writing output file. "
              "Make sure 'DSS_contents.xlsx' is not open.")

