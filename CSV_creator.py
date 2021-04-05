# Mat Lockhart
# Python 3.8

import os

def main():
    outfile_name = "Combined_data.csv"
    separator = '|'

    with open(outfile_name, "w") as out_fl:
        # Create header
        print(f"Record_Type{separator}", end="", file=out_fl) # 1
        print(f"State_Code{separator}", end="", file=out_fl)
        print(f"Station_ID{separator}", end="", file=out_fl)
        print(f"Travel_Direction{separator}", end="", file=out_fl)
        print(f"Travel_Lane{separator}", end="", file=out_fl) # 5
        print(f"Year{separator}", end="", file=out_fl)
        print(f"Functional_Code{separator}", end="", file=out_fl)
        print(f"Number_of_Lanes{separator}", end="", file=out_fl)
        print(f"TMAS_Sample_Type{separator}", end="", file=out_fl)
        print(f"Lanes_Monitored{separator}", end="", file=out_fl) # 10
        print(f"Counting_Method{separator}", end="", file=out_fl)
        print(f"Lanes_Monitored_Vehicle_Classification{separator}", end="", file=out_fl)
        print(f"Classification_Mechanism{separator}", end="", file=out_fl)
        print(f"Classification_Method{separator}", end="", file=out_fl)
        print(f"Vehicle_Classification_Group{separator}", end="", file=out_fl) # 15
        print(f"Lanes_Monitored_Truck_Weight{separator}", end="", file=out_fl)
        print(f"Weighing_Method{separator}", end="", file=out_fl)
        print(f"Weighing_System_Callibration{separator}", end="", file=out_fl)
        print(f"Data_Retrieval_Method{separator}", end="", file=out_fl)
        print(f"Sensor_Type{separator}", end="", file=out_fl) # 20
        print(f"Sensor_Type_2{separator}", end="", file=out_fl)
        print(f"Primary_Purpose{separator}", end="", file=out_fl)
        print(f"LRS_Route_ID{separator}", end="", file=out_fl)
        print(f"LRS_Location{separator}", end="", file=out_fl)
        print(f"Lattitude{separator}", end="", file=out_fl) # 25
        print(f"Longitude{separator}", end="", file=out_fl)
        print(f"LTPP_Site_ID{separator}", end="", file=out_fl)
        print(f"Previous_Station_ID{separator}", end="", file=out_fl)
        print(f"Year_Station_Established{separator}", end="", file=out_fl)
        print(f"Year_Station_Discontinued{separator}", end="", file=out_fl) # 30
        print(f"FIPS_County_Code{separator}", end="", file=out_fl)
        print(f"HPMS_Sample_Type{separator}", end="", file=out_fl)
        print(f"HPMS_Sample_ID{separator}", end="", file=out_fl)
        print(f"National_Highway_System{separator}", end="", file=out_fl)
        print(f"Posted_Route_Signing{separator}", end="", file=out_fl) # 35
        print(f"Posted_Signed_Route_Number{separator}", end="", file=out_fl)
        print(f"Station_Location", file=out_fl) # 37

        
        i = 1
        for fl in os.listdir(f"{os.getcwd()}/raw_data"):
            with open(f"{os.getcwd()}/raw_data/{fl}", "r") as open_fl:
                for line in open_fl:
                    temp = line[0:1]
                    temp = temp.strip()
                    print(line[0:1] + separator, end="", file=out_fl) # Record_Type                                 1
                    print(line[1:3] + separator, end="", file=out_fl) # State_Code
                    print(line[3:9] + separator, end="", file=out_fl) # Station_ID
                    print(line[9:10] + separator, end="", file=out_fl) # Travel_Direction
                    print(line[10:11] + separator, end="", file=out_fl) # Travel_Lane                               5
                    print(line[11:15] + separator, end="", file=out_fl) # Year
                    print(line[15:17] + separator, end="", file=out_fl) # Functional_Code
                    print(line[17:18] + separator, end="", file=out_fl) # Number_of_Lanes
                    print(line[18:19] + separator, end="", file=out_fl) # TMAS_Sample_Type
                    print(line[19:20] + separator, end="", file=out_fl) # Lanes_Monitored                           10
                    print(line[20:21] + separator, end="", file=out_fl) # Counting_Method
                    print(line[21:22] + separator, end="", file=out_fl) # Lanes_Monitored_Vehicle_Classification
                    print(line[22:23] + separator, end="", file=out_fl) # Classification_Mechanism
                    print(line[23:24] + separator, end="", file=out_fl) # Classification_Method
                    print(line[24:26] + separator, end="", file=out_fl) # Vehicle_Classification_Group              15
                    print(line[26:27] + separator, end="", file=out_fl) # Lanes_Monitored_Truck_Weight
                    print(line[27:28] + separator, end="", file=out_fl) # Weighing_Method
                    print(line[28:29] + separator, end="", file=out_fl) # Weighing_System_Callibration
                    print(line[29:30] + separator, end="", file=out_fl) # Data_Retrieval_Method
                    print(line[30:31] + separator, end="", file=out_fl) # Sensor_Type                               20
                    print(line[31:32] + separator, end="", file=out_fl) # Sensor_Type_2
                    print(line[32:33] + separator, end="", file=out_fl) # Primary_Purpose
                    print(line[33:93] + separator, end="", file=out_fl) # LRS_Route_ID
                    print(line[93:101] + separator, end="", file=out_fl) # LRS_Location
                    print(line[101:109] + separator, end="", file=out_fl) # Lattitude                               25
                    print(line[109:118] + separator, end="", file=out_fl) # Longitude
                    print(line[118:122] + separator, end="", file=out_fl) # LTPP_Site_ID
                    print(line[122:128] + separator, end="", file=out_fl) # Previous_Station_ID
                    print(line[128:132] + separator, end="", file=out_fl) # Year_Station_Established
                    print(line[132:136] + separator, end="", file=out_fl) # Year_Station_Discontinued               30
                    print(line[136:139] + separator, end="", file=out_fl) # FIPS_County_Code
                    print(line[139:140] + separator, end="", file=out_fl) # HPMS_Sample_Type
                    print(line[140:152] + separator, end="", file=out_fl) # HPMS_Sample_ID
                    print(line[152:153] + separator, end="", file=out_fl) # National_Highway_System
                    print(line[153:155] + separator, end="", file=out_fl) # Posted_Route_Signing                    35
                    print(line[155:163] + separator, end="", file=out_fl) # Posted_Signed_Route_Number
                    print(line[164:213], end="\n", file=out_fl) # Station_Location                                    37

                    i += 1
                    if i % 100 == 0:
                        print(f"On line {i}", flush=True)
    

if __name__ == '__main__':
    main()