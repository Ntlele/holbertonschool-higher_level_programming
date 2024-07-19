#!/usr/bin/python3
import os

def generate_invitations(template, attendees):
    """ This funtion prints creates a template of invitations addressed to various people"""

    # 
    
    if not isinstance(template, str):
        print("Error: Template is not a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: Atendees is not a list of dictionaries")
        return
    
    
    if not template.strip():
        print("The template should not be empty")
        return
    
    if not attendees:
        print("The are no people to invite")
        return
    
    """Procesing every attendee"""
    for i, attendee in enumerate(attendees, start=1):
        #Replacing placeholders
        invitation = template.format(
            name=attendee.get("name", "N/A"),
            event_title=attendee.get("event_title", "N/A"),
            event_date=attendee.get("event_date", "N/A"),
            event_location=attendee.get("event_location", "N/A")
        )

        # Processing the template and over loding it with data
        t_filename = f"output_{i}.txt"
        with open(t_filename, 'w') as file:
            file.write(invitation)

        print(f"Generated {t_filename}")

# if __name__ == "main":
#     with open('template.txt', 'r') as f:
#         template_content = f.read()