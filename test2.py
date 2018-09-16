import csv
import os
import sys



#dataCol_file_path = sys.argv[1]
dataCol_file_path = '/Users/zhuzhichao/Documents/data_analysis'

if not os.path.exists(dataCol_file_path):
    print ("The path %s does not exist!")
    sys.exit(2)

content_header = ["time_base", "pos", "iterm_id", "frequency", "value"]
for f in [s for s in os.listdir(dataCol_file_path) if os.path.splitext(s)[1] == ".DATA"]:
    outputName  = os.path.splitext(f)[0] + ".csv"
    fd          = open(os.path.join(dataCol_file_path, f), 'rb')

    data = ""
    data_all = []
    fd.seek(0, 0)
    line = fd.readline()
    while line:
        line = line.strip('\n')
        data = data + line
        line = fd.readline()
    fd.close()
    time_base = int(data[0:4], 16)

    data_info_length = 2 + 2 + 2+ 4
    data_number = len(data[4:])/data_info_length
    for i in range(data_number):
        data_tmp = data[4+i*data_info_length:4+(i+1)*data_info_length]
        pos = int(data_tmp[0:4], 16)
        iterm_id = int(data_tmp[4: 6], 16)
        frequency = int(data_tmp[6:8], 16)
        valude = int(data_tmp[8:12], 16)
        contentData = [time_base, pos, iterm_id, frequency, valude]
        data_all.append(contentData)

    with open(os.path.join(dataCol_file_path, outputName), 'w') as file:
        file.seek(0, 0)
        writer = csv.writer(file)
        writer.writerows([content_header])
        writer.writerows(data_all)
        file.close()