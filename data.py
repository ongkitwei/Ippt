import pandas

# Calculate pushup points
# def get_pushup_points(pushup_reps):
#     data = pandas.read_csv("pushup.csv",sep=",")
#     for index, row in data[2:].iterrows():
#         if row["Age"] == str(pushup_reps):
#             # print("ok")
#             print(f'{index}- {row["Age"]}')
#             number = index
#             for index, row in data[number:number+1].iterrows():
#                 print(f'{index}- {row["<22"]}')
#                 return row["<22"]
#         else:
#             return 25
        
# Calculate situps points
def get_situp_points(situp_reps, age):
    df = pandas.read_csv("situp.csv", sep=",")

    if situp_reps == 0:
        return 0
    elif situp_reps > int(df.loc[df[age] == 25, "Age"]):
        return 25.0
    else:
        columns = df.columns
        # list_column = [c for c in columns[1:]]
        list_points = df.loc[df['Age'] == str(situp_reps), age].squeeze()
        return list_points
    
        
# Calculate 2.4Km points
def get_running_points_old(minutes, seconds):
    data = pandas.read_csv("run.csv",sep=",")
    col = data.columns

    # col[0] is "Age" column, col[1] is "<22" column
    time_dict = {}
    user_timing = int(str(minutes)+str(seconds))
    print(user_timing)
    for index, row in data[2:].iterrows():
        time_dict[int(row[col[0]].replace(":",""))] = index

    if user_timing in time_dict:
        for index, row in data[2:].iterrows():
            if index == time_dict[user_timing]:
                return row[col[1]]
    else:
        print("timing not found")
        for key in time_dict.keys():
            if key>user_timing:
                for index, row in data[2:].iterrows():
                    if index == time_dict[key]:
                        return row[col[1]]
                break

def get_pushup_points(pushup_reps, age):
    df = pandas.read_csv("pushup.csv", sep=",")
    # age = "<22"
    if pushup_reps == 0:
        return 0
    elif pushup_reps > int(df.loc[df[age] == 25, "Age"]):
        return 25.0
    else:
        columns = df.columns
        # list_column = [c for c in columns[1:]]
        list_points = df.loc[df['Age'] == str(pushup_reps), age].squeeze()
        return list_points
    

def get_running_points(minutes, seconds, age): 
    df = pandas.read_csv("run.csv", sep=",")
    list_time = df.loc[2:, "Age "]
    list_time = [f'{l.replace(":",".")}' for l in list_time]

    seconds_2d = f'{seconds:02d}'
    print(list_time)
    print("")
    if float(f'{str(minutes)}.{str(seconds_2d)}') > float(df.loc[df["Age "] == "18:20", "Age "].squeeze().replace(":",".")):
        return 0
    
    elif float(f'{str(minutes)}.{str(seconds_2d)}') < float(df.loc[df[age] == 50, "Age "].squeeze().replace(":",".")):
        return 50

    else:
        for index, li in enumerate(list_time, start=2):
            if float(li) >= float(f'{str(minutes)}.{str(seconds_2d)}'):
                print(f'end at {index}')
                print(f'choose from {index+1}')
                points = df.loc[index, age]
                return points
            else:
                pass

def get_age():
    df = pandas.read_csv("situp.csv", sep=",")
    columns = df.columns
    list_column = [c for c in columns[1:]]
    return list_column

def replace():
    anjing = "9:30"
    print(anjing.replace(":",""))

def test_function(anjing):
    print("hello" + anjing)

def conv_float():
    min = 5
    min_f = float(min)
    print(float("9.4") > 9.3)
    print(min_f)

def fill_with_0():
    number = 1
    formatted_number = f'{number:02d}'
    print(formatted_number)


if __name__ == "__main__":
    # get_situp_points(input("Enter situp reps: "))
    # print(get_running_points())
    # replace()
    # anjing = " anjing"
    # test_function(anjing=anjing.strip())
    # print(get_pushup_points(pushup_reps="45"))
    # conv_float()
    # fill_with_0()
    # get_running_points()
    # conv_float()
    df = pandas.read_csv("run.csv", sep=",")
    print(df.loc[df["Age "] == "18:20", "Age "].squeeze())