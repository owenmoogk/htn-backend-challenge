import json
from userData.models import User, Skill
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    # command to load json data into the model
    help = 'Load data from JSON file into User model'

    def handle(self, *args, **options):

        # Open the JSON file and load the data
        with open('userData/fixtures/input.json', 'r') as file:
            data = json.load(file)

        # Loop through each user in the data and create a User object
        for user_data in data:
            # Create the User object with the basic fields
            user = User.objects.create(
                name=user_data['name'],
                company=user_data['company'],
                email=user_data['email'],
                phone=user_data['phone']
            )
            
            # Loop through each skill in the user's skill list and create a Skill object
            for skill_data in user_data['skills']:
                skill = Skill.objects.create(
                    name=skill_data['skill'],
                    rating=skill_data['rating']
                )
                # Add the skill to the user's many-to-many skill field
                user.skills.add(skill)

            # Save the User object with the updated skills list
            user.save()