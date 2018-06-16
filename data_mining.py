input_data = [[{'name':'Anurag','id':0},{'name':'Prateek','id':1},{'name':'Paresh','id':2}],
              {'name':'Rani','id':3},
              {'name':'Nirbhay','id':4},
              {'city':["Sujalpur","Indore","Bhopal","Bhopal","Lucknow"]}
              ]
from pprint import pprint

def get_output(input_data):
    print("starting data mining using python ")
    output = []
    for i in input_data:
        if str(type(i))=="<class 'list'>":
            for j in i:
                outdict = {}
                outdict["name"]=j["name"]
                outdict["id"]=j["id"]
                output.append(outdict)
        elif str(type(i))=="<class 'dict'>":
            if "name" in i:
                outdict = {}
                outdict["name"] = i["name"]
                outdict["id"] = i["id"]
                output.append(outdict)
        else:
            print("new input type detected")

    for k in input_data:
        if str(type(k))=="<class 'dict'>":
            if "city" in k:
                for r in range(len(output)):
                    output[r]["city"]=k["city"][r]
    pprint(output)

get_output(input_data)