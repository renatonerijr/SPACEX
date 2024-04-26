from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework import status
import requests
import io

# Use v5 for latest 

url = 'https://api.spacexdata.com/v5/launches/{}'

class LatestLaunch(APIView):

    def get(self, format=None):

        try:
            # Request from SPACEX API
            req = requests.get(url.format("latest"))

            if req.status_code > 500:
                return Response({"message":"SPACEX API Error!", "success":False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        except Exception as e:
            print(e)
            return Response({"message":"Could'nt connect to SPACEX API Servers", "success":False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # Parse JSON to a dict
        data = req.json()
        newData = FilterAPIV5().filterJson(data)

        #Return data
        return Response(newData)


class NextLaunch(APIView):

    def get(self, format=None):

        try:
            # Request from SPACEX API
            req = requests.get(url.format("next"))

            if req.status_code > 500:
                return Response({"message":"SPACEX API Error!", "success":False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        except Exception as e:
            print(e)
            return Response({"message":"Could'nt connect to SPACEX API Servers", "success":False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # Parse JSON to a dict
        data = req.json()

        # Filter JSON with specific info
        newData = FilterAPIV5().filterJson(data)

        #Return data
        return Response(newData)



class UpcomingLaunches(APIView):

    def get(self, format=None):

        try:
            # Request from SPACEX API
            req = requests.get(url.format("upcoming"))

            if req.status_code > 500:
                return Response({"message":"SPACEX API Error!", "success":False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        except Exception as e:
            print(e)
            return Response({"message":"Could'nt connect to SPACEX API Servers", "success":False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # Parse JSON to a list
        data_list = req.json()
        newData = []

        # Filter JSON with specific info
        for data in data_list:
            newData.append(FilterAPIV5().filterJson(data))

        #Return data
        return Response(newData)



class PastLaunches(APIView):

    def get(self, format=None):

        try:
            # Request from SPACEX API
            req = requests.get(url.format("past"))

            if req.status_code > 500:
                return Response({"message":"SPACEX API Error!", "success":False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        except Exception as e:
            print(e)
            return Response({"message":"Could'nt connect to SPACEX API Servers", "success":False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # Parse JSON to a list
        data_list = req.json()
        newData = []

        # Filter JSON with specific info
        for data in data_list:
            newData.append(FilterAPIV5().filterJson(data))

        #Return data
        return Response(newData)


class OneLaunch(APIView):

    def get(self, request, pk, format=None):

        try:
            # Request from SPACEX API
            # Use v3 for retrocompability
            url = 'https://api.spacexdata.com/v3/launches/{}'
            req = requests.get(url.format(pk))

            if req.status_code == 404:
                return Response({"message":"Could'nt find any launch!", "success":False}, status=status.HTTP_404_NOT_FOUND)

            if req.status_code > 500:
                return Response({"message":"SPACEX API Error!", "success":False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        except Exception as e:
            print(e)
            return Response({"message":"Could'nt connect to SPACEX API Servers", "success":False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # Parse JSON to a dict
        data = req.json()

        # Filter JSON with specific info
        newData = FilterAPIV5().filterJson(data)

        #Return data
        return Response(newData)



class FilterAPIV5():

    def filterJson(self, data):
        # Create a new dict with specific info from mission
        rocket = data["rocket"]
        if isinstance(rocket, dict):
            first_stage = rocket["first_stage"]["cores"][0] 
            second_stage = rocket["second_stage"]["payloads"][0]
        else:
            rocket = {"rocket_name": "N/A"}
            first_stage = {"reused": "N/A", "land_success": "N/A", "landing_intent": "N/A"}
            second_stage = {"customers": "N/A", "nationality": "N/A", "manufacturer": "N/A"}

        newData = {
                    "mission_name": data["mission_name"] if "mission_name" in data else "N/A",
                    "flight_number": data["flight_number"] if "flight_number" in data else "N/A",
                    "launch_year": data["launch_year"] if "launch_year" in data else "N/A",
                    "launch_date_utc": data["launch_date_utc"] if "launch_date_utc" in data else "N/A",
                    "rocket": {
                        "first_stage":{
                            "rocket_name": rocket["rocket_name"],
                            "is_reused": first_stage["reused"],
                            "land_success": first_stage["land_success"],
                            "landing_intent": first_stage["landing_intent"]
                        },
                        "second_stage":{
                            "costumers": second_stage["customers"],
                            "nationality": second_stage["nationality"],
                            "manufacturer": second_stage["manufacturer"]
                        }
                    },
                    "launch_success": data["launch_success"] if "launch_success" in data else "N/A",
                    "launch_site": data["launch_site"]["site_name_long"] if "launch_site" in data else "N/A",
                    "imgs": data["links"]["flickr_images"] if "flickr_images" in data["links"] else "N/A",
                    "img_mission_patch": data["links"]["mission_patch"] if "mission_patch" in data["links"] else "N/A",
                    "video_link": data["links"]["video_link"] if "video_link" in data["links"] else "N/A",
                    "reddit_link": data["links"]["reddit_campaign"] if "reddit_campaign" in data["links"] else "N/A",
                    "details": data["details"]
                  }
        return newData
