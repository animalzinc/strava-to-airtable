from airtable.airtable import Airtable
from airtable import airtable

from stravalib.client import Client
from stravalib import unithelper

import settings

at = airtable.Airtable(settings.AIRTABLE_BASE, settings.AIRTABLE_API_KEY)

client = Client(access_token=settings.STRAVA_ACCESS_TOKEN)
athlete = client.get_athlete()

print athlete.firstname
activities= client.get_activities()

activity_list = []

for activity in activities:
	activity = client.get_activity(activity.id)

	if activity.photos.primary:
		primary_pic = activity.photos.primary.urls['600'] 
	else:
		primary_pic = []

	data = {
		"Name"						: activity.name,
		"Created At"				: activity.start_date.isoformat(),
		"Distance Meters"			: float(unithelper.meters(activity.distance)),
		"Elapsed Time in Seconds"	: activity.elapsed_time.seconds,
		"Link to Activity"			: "https://www.strava.com/activities/" + str(activity.id),
		"Notes"						: activity.description,
		"Photos"					: [{'url':primary_pic}] if primary_pic else [],
		"Strava Activity ID"		: activity.id,
	}

	print data


	response = at.create(str("Runs"), data)
	print response

print len(list(activities))