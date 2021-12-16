import sys

original = sys.argv[1]
refactor = sys.argv[2]

def getImprovement(fileName):
	print("===="+ fileName+"====")

	o_file = open(original+fileName)
	o_lines = o_file.readlines()
	
	r_file = open(refactor+fileName)
	r_lines = r_file.readlines()

	index = 1 
	for o_line in o_lines[1:5]:
		aux_line = o_line.split()
		o_value = float(aux_line[1])
		r_value = float(((r_lines[index]).split())[1])
		improvement = (o_value - r_value) / o_value * 100
		print(aux_line[0] + " " + str(improvement) + " %")
    		index += 1

def main():
	getImprovement("ate_values.txt");
	print
	getImprovement("rpe_values.txt");

if __name__ == '__main__':
	main()
   
