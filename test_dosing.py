import pandas
import dosing



def test_merge_filter_logic():

	#Make mock data for the left dataframe
	left_data = {"ID": ["1","2","3"], "RID":["17","18","17"], "USERID":["LEGOLAS","LEGOLAS","LEGOLAS_2"] , "VISCODE":["a01","a01", "b04",], "SVDOSE":["Y","-4","Y"]}
	mock_left_df = pandas.DataFrame(left_data, columns=["ID", "RID", "USERID", "VISCODE", "SVDOSE"])

	#Make mock data for the right dataframe
	right_data = {"ID": ["1","2","4"], "RID":["17","18","20"], "USERID":["LEGOLAS","LEGOLAS","LEGOLAS",] , "VISCODE":["a01","a01", "b03",], "ECSDSTXT":["-4","120","180"]}
	mock_right_df = pandas.DataFrame(right_data, columns=["ID","RID","USERID","VISCODE","ECSDSTXT"])

	#Make expected data for the merged and filtered data
	mock_merged_data = {"ID":["1"],"RID":["17"],"USERID":["LEGOLAS"],"VISCODE":["a01"],"SVDOSE":["Y"],"ID_right":["1"], "USERID_right":["LEGOLAS"],"ECSDSTXT":["-4"]}
	mock_merged_df = pandas.DataFrame(mock_merged_data,columns=["ID","RID","USERID","VISCODE","SVDOSE","ID_right","USERID_right","ECSDSTXT"])

	#Run merge_filter on mock dataframes
	actual_merged_data = dosing.merge_filter(mock_left_df, mock_right_df, "a01", "Y", "280")

	#Compare the two dataframes
	assert actual_merged_data.equals(mock_merged_df)
