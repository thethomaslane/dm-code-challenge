import pandas as pd 
import plotly.graph_objects as go
import sys
import getopt
import os

#Creates a pie chart of Viscodes in registry
def plot_data(data):
	#Filters data for desired entries
	data = data.query("VISCODE != 'bl'")
	data = data.query("SVPERF == 'Y'")

	#Adds a column of 1's in order to count for pie chart
	data['COUNT'] = pd.Series([1] * len(data['ID']), index=data.index)

	#Creates the figure and opens an html page with the pie chart
	fig = go.Figure(data=[go.Pie(labels=data["VISCODE"], values=data["COUNT"], hovertemplate = 'VISCODE: %{label} <br> Count: %{value} (%{percent}) <extra></extra> ')])
	fig.update_layout(title={"text":"Viscodes from Registry", "xanchor":"left"})
	fig.write_html('viscode_registry_pie_chart.html', auto_open=True)

#Merges data left on RID and VISCODE
def merge_filter(left_df, right_df, viscode, svdose, ecsdstxt):
	merged = left_df.merge(right_df,"left", on=["RID","VISCODE"], suffixes=["","_right"])

	#Filters the data so remaining entries have desired viscode and svdose. Excludes entries with ecsdstxt
	merged = merged.query("VISCODE == '" + viscode + "'")
	merged = merged.query("SVDOSE == '" + svdose + "'")
	merged = merged.query("ECSDSTXT != " + ecsdstxt + "")
	return merged

#Exports data as a .csv to output/results.csv
def export_data(data, output):
	if output != "":
		if not os.path.exists(output):
			os.makedirs(output)
		output_file = open(os.path.join(output, "results.csv"),"w", newline="")

	else:
		output_file = open("results.csv","w", newline="")
	data.to_csv(output_file, columns=["ID", "RID", "USERID", "VISCODE", "SVDOSE", "ECSDSTXT"], index=False)
	


#Reads the command line arguments
def parse_params(argv):
	output=""
	try:
		opts, args = getopt.getopt(argv,"hv:s:e:o:",["help","viscode=","svdose=","ecsdstxt=","output"])
	except getopt.GetoptError:
		print('usage: dosing.py -v <viscode> -s <svdose> -e <ecsdstxt> -o <outputdirectory>')
		sys.exit(2)
	for opt, arg in opts:
		if opt in ("-h", "--help"):
			print('usage: dosing.py -v <viscode> -s <svdose> -e <ecsdstxt> -o <outputdirectory>')
			sys.exit()
		elif opt in ("-v", "--viscode"):
			viscode = arg
		elif opt in ("-s", "--svdose"):
			svdose = arg
		elif opt in ("-e", "--ecsdstxt"):
			ecsdstxt = arg
		elif opt in ("-o", "--output"):
			output = arg

	return viscode, svdose, ecsdstxt, output

#Uses the command line arguments to merge and filter the data then export it
def main():
	viscode, svdose, ecsdstxt, output = parse_params(sys.argv[1:])
	registry = pd.read_csv("t2_registry 20190619.csv") 
	ec = pd.read_csv("t2_ec 20190619.csv") 
	plot_data(registry)
	merged_data = merge_filter(registry, ec, viscode, svdose, ecsdstxt)
	export_data(merged_data, output)

if __name__ == "__main__":
	main()
