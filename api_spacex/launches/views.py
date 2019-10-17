from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework import status
import requests
import io

url = 'https://api.spacexdata.com/v3/launches/{}'

class LatestLaunch(APIView):

    def get(self, format=None):

        # Request from SPACEX API
        req = requests.get(url.format("latest"))

        if req.status_code > 500:
            return Response({"message":"SPACEX API Error!", "success":False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # Parse JSON to a dict
        data = req.json()
        newData = FilterAPI().filterJson(data)

        #Return data
        return Response(newData)

class NextLaunch(APIView):

    def get(self, format=None):

        # Request from SPACEX API
        req = requests.get(url.format("next"))

        if req.status_code > 500:
            return Response({"message":"SPACEX API Error!", "success":False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # Parse JSON to a dict
        data = req.json()

        # Filter JSON with specific info
        newData = FilterAPI().filterJson(data)

        #Return data
        return Response(newData)

class UpcomingLaunches(APIView):

    def get(self, format=None):

        # Request from SPACEX API
        req = requests.get(url.format("upcoming"))

        if req.status_code > 500:
            return Response({"message":"SPACEX API Error!", "success":False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # Parse JSON to a list
        data_list = req.json()
        newData = []

        # Filter JSON with specific info
        for data in data_list:
            newData.append(FilterAPI().filterJson(data))

        #Return data
        return Response(newData)

class PastLaunches(APIView):

    def get(self, format=None):

        # Request from SPACEX API
        req = requests.get(url.format("past"))

        if req.status_code > 500:
            return Response({"message":"SPACEX API Error!", "success":False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # Parse JSON to a list
        data_list = req.json()
        newData = []
        
        # Filter JSON with specific info
        for data in data_list:
            newData.append(FilterAPI().filterJson(data))

        #Return data
        return Response(newData)

class OneLaunch(APIView):

    def get(self, request, pk, format=None):
        # Request from SPACEX API
        req = requests.get(url.format(pk))

        if req.status_code == 404:
            return Response({"message":"Could'nt find any launch!", "success":False}, status=status.HTTP_404_NOT_FOUND)

        if req.status_code > 500:
            return Response({"message":"SPACEX API Error!", "success":False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # Parse JSON to a dict
        data = req.json()

        # Filter JSON with specific info
        newData = FilterAPI().filterJson(data)

        #Return data
        return Response(newData)

class FilterAPI():

    def filterJson(self, data):
        # Create a new dict with specific info from mission
        rocket = data["rocket"]
        first_stage = rocket["first_stage"]["cores"][0]
        second_stage = rocket["second_stage"]["payloads"][0]
        newData = {
                    "mission_name": data["mission_name"],
                    "flight_number": data["flight_number"],
                    "launch_year": data["launch_year"],
                    "launch_date_utc": data["launch_date_utc"],
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
                    "launch_success": data["launch_success"],
                    "launch_site": data["launch_site"]["site_name_long"],
                    "imgs": data["links"]["flickr_images"],
                    "img_mission_patch": data["links"]["mission_patch"],
                    "video_link": data["links"]["video_link"],
                    "reddit_link": data["links"]["reddit_campaign"],
                    "details": data["details"]
                  }
        return newData
