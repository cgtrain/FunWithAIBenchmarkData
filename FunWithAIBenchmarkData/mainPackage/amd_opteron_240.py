# Name: Connor Thomas
# Email: thoma5cg@mail.uc.edu
# Assignment Number: Assignment08
# Due Date: 3/27/25
# Course #/Section: IS4010/002
# Semester/Year: 2nd/4th
# Brief description of the assignment: We are modifying a VS project to add data visualization.
# Brief description of what this module does: This module displays an image of an AMD Opteron 240.
# Citations:
# Anything else that's relevant:

import os
import subprocess
import platform
def show_team_image():
    image_path = os.path.join(os.path.dirname(__file__), 'team_image', 'amd_opteron_240.jpg')
    if not os.path.exists(image_path):
        print(f"Image file not found at: {image_path}")
        return
    if platform.system() == "Windows":
        os.startfile(image_path)