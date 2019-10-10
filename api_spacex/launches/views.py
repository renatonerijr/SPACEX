from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from launches.serializers import APISerializer
import requests
import io

class LatestLaunche(APIView):

    def __init__(self):
        self.url = 'https://api.spacexdata.com/v3/launches/{}'

    def serialize_response(self, data):
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

        # Serialize it
        data = APISerializer(data=newData)

        # Return validated_data or error if is'nt valid
        if data.is_valid():
            return data.validated_data
        else:
            return data.errors

    def get(self, format=None):

        # Request from SPACEX API
        req = requests.get(self.url.format("latest"))

        # Parse JSON to a dict
        data = req.json()
        print(type(data))
        serialized_request = self.serialize_response(data)

        #Return data
        return Response(serialized_request)
