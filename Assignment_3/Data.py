
import urllib.request as request
import json

def main():
    src = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions.json"
    with request.urlopen(src) as response:
        data = json.load(response)

    # print(data)

    big_list = data["result"]["results"]
    small_list = []

    with open("data.txt", "w", encoding="utf-8") as file:
		
	for landmark in big_list:
            title = landmark["stitle"]
            file.write(title+",")

            longitude = landmark["longitude"]
            file.write(longitude+",")

            latitude = landmark["latitude"]
            file.write(latitude+",")

            line = landmark["file"]
            line = line.split("http")
            line = line[1]
            line = str(line)
            line = "http" + line
            file.write(line + "\n")

# 	for landmark in big_list:
# 	    title = file.write(landmark["stitle"]+",")
# 	    longitude = file.write(landmark["longitude"]+",")
# 	    latitude = file.write(landmark["latitude"]+",")
# 	    line = file.write(landmark["file"] +"\n")

# 	    line = str(line)
# 	    web = line.split(".jpg")

#     title=data["result"]["results"][1]["stitle"]
    
#     longitude=data["result"]["results"][3]["longitude"]
    
#     web=data["result"]["results"][14]["file"]
    
#     latitude=data["result"]["results"][16]["latitude"]
    
#     print(big_list)
#     print(title)
#     print(longitude)
#     print(web)
#     print(latitude)



if __name__ == '__main__':
	main()







    
