# Mat Lockhart
# Python 3.8

import os

def main():
    outfile_name = "Traffic_flow.csv"
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
        print(f"Sample_Type_Traffic_Volume{separator}", end="", file=out_fl)
        print(f"Lanes_Monitored{separator}", end="", file=out_fl) # 10
        print(f"Counting_Method{separator}", end="", file=out_fl)
        print(f"Sample_Type_Vehicle_Classification{separator}", end="", file=out_fl)
        print(f"Lanes_Monitored_Vehicle_Classification{separator}", end="", file=out_fl)
        print(f"Classification_Method{separator}", end="", file=out_fl)
        print(f"Classification_Algorithm{separator}", end="", file=out_fl) # 15
        print(f"Classification_System{separator}", end="", file=out_fl)
        print(f"Sample_Type_Truck_Weight{separator}", end="", file=out_fl)
        print(f"Lanes_Monitored_Truck_Weight{separator}", end="", file=out_fl)
        print(f"Weighing_Method{separator}", end="", file=out_fl)
        print(f"Weighing_System_Callibration{separator}", end="", file=out_fl) # 20
        print(f"Data_Retrieval_Method{separator}", end="", file=out_fl)
        print(f"Sensor_Type{separator}", end="", file=out_fl)
        print(f"Sensor_Type_2{separator}", end="", file=out_fl)
        print(f"Primary_Purpose{separator}", end="", file=out_fl)
        print(f"LRS_Route_ID{separator}", end="", file=out_fl) # 25
        print(f"LRS_Location{separator}", end="", file=out_fl)
        print(f"Lattitude{separator}", end="", file=out_fl)
        print(f"Longitude{separator}", end="", file=out_fl)
        print(f"SHRP_Site_ID{separator}", end="", file=out_fl)
        print(f"Previous_Station_ID{separator}", end="", file=out_fl) # 30
        print(f"Year_Station_Established{separator}", end="", file=out_fl)
        print(f"Year_Station_Discontinued{separator}", end="", file=out_fl)
        print(f"FIPS_County_Code{separator}", end="", file=out_fl)
        print(f"HPMS_Sample_Type{separator}", end="", file=out_fl)
        print(f"HPMS_Sample_ID{separator}", end="", file=out_fl) # 35
        print(f"National_Highway_System{separator}", end="", file=out_fl)
        print(f"Posted_Route_Signing{separator}", end="", file=out_fl)
        print(f"Posted_Signed_Route_Number{separator}", end="", file=out_fl)
        print(f"Concurrent_Route_Signing{separator}", end="", file=out_fl)
        print(f"Concurrent_Signed_Route_Number{separator}", end="", file=out_fl) # 40
        print(f"Station_Location", file=out_fl) # 41

        
        i = 1
        maryland_count = 0
        for fl in os.listdir(f"{os.getcwd()}/raw_data"):
            with open(f"{os.getcwd()}/raw_data/{fl}", "r") as open_fl:
                for line in open_fl:
                    if(line[1:3] == "24"):
                        maryland_count += 1
                    print(line[0:1].strip() + separator, end="", file=out_fl) # Record_Type
                    print(line[1:3].strip() + separator, end="", file=out_fl) # State_Code
                    print(line[3:9].strip() + separator, end="", file=out_fl) # Station_ID
                    print(line[9:10].strip() + separator, end="", file=out_fl) # Travel_Direction
                    print(line[10:11].strip() + separator, end="", file=out_fl) # Travel_Lane
                    print(line[11:13].strip() + separator, end="", file=out_fl) # Year
                    print(line[13:15].strip() + separator, end="", file=out_fl) # Functional_Code
                    print(line[15:16].strip() + separator, end="", file=out_fl) # Number_of_Lanes
                    print(line[16:17].strip() + separator, end="", file=out_fl) # Sample_Type_Traffic_Volume
                    print(line[17:18].strip() + separator, end="", file=out_fl) # Lanes_Monitored                       10
                    print(line[18:19].strip() + separator, end="", file=out_fl) # Counting_Method
                    print(line[19:20].strip() + separator, end="", file=out_fl) # Sample_Type_Vehicle_Classification
                    print(line[20:21].strip() + separator, end="", file=out_fl) # Lanes_Monitored_Vehicle_Classification
                    print(line[21:22].strip() + separator, end="", file=out_fl) # Classification_Method
                    print(line[22:23].strip() + separator, end="", file=out_fl) # Classification_Algorithm
                    print(line[23:25].strip() + separator, end="", file=out_fl) # Classification_System
                    print(line[25:26].strip() + separator, end="", file=out_fl) # Sample_Type_Truck_Weight
                    print(line[26:27].strip() + separator, end="", file=out_fl) # Lanes_Monitored_Truck_Weight
                    print(line[27:28].strip() + separator, end="", file=out_fl) # Weighing_Method
                    print(line[28:29].strip() + separator, end="", file=out_fl) # Weighing_System_Callibration          20
                    print(line[29:30].strip() + separator, end="", file=out_fl) # Data_Retrieval_Method
                    print(line[30:31].strip() + separator, end="", file=out_fl) # Sensor_Type
                    print(line[31:32].strip() + separator, end="", file=out_fl) # Sensor_Type_2
                    print(line[32:33].strip() + separator, end="", file=out_fl) # Primary_Purpose
                    print(line[33:45].strip() + separator, end="", file=out_fl) # LRS_Route_ID
                    print(line[45:51].strip() + separator, end="", file=out_fl) # LRS_Location
                    print(line[51:59].strip() + separator, end="", file=out_fl) # Lattitude
                    print(line[59:68].strip() + separator, end="", file=out_fl) # Longitude
                    print(line[68:72].strip() + separator, end="", file=out_fl) # SHRP_Site_ID
                    print(line[72:78].strip() + separator, end="", file=out_fl) # Previous_Station_ID                 30
                    print(line[78:80].strip() + separator, end="", file=out_fl) # Year_Station_Established
                    print(line[80:82].strip() + separator, end="", file=out_fl) # Year_Station_Discontinued
                    print(line[82:85].strip() + separator, end="", file=out_fl) # FIPS_County_Code
                    print(line[85:86].strip() + separator, end="", file=out_fl) # HPMS_Sample_Type
                    print(line[86:98].strip() + separator, end="", file=out_fl) # HPMS_Sample_ID
                    print(line[98:99].strip() + separator, end="", file=out_fl) # National_Highway_System
                    print(line[99:100].strip() + separator, end="", file=out_fl) # Posted_Route_Signing
                    print(line[100:108].strip() + separator, end="", file=out_fl) # Posted_Signed_Route_Number
                    print(line[108:109].strip() + separator, end="", file=out_fl) # Concurrent_Route_Signing
                    print(line[109:117].strip() + separator, end="", file=out_fl) # Concurrent_Signed_Route_Number      40
                    print(line[117:167].strip(), end="\n", file=out_fl) # Station_Location

                    i += 1
                    if i % 100 == 0:
                        print(f"On line {i}", end="\r", flush=True)
        print(f"\nMaryland records: {maryland_count}")
    

if __name__ == '__main__':
    main()