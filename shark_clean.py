# Unified categories for Activity & Type

# grouping activity into upper-group (a less granual data)
import pandas as pd
import re

def clean_activity(activity):
    activity = str(activity).strip()

    if re.search(r'surf|cano|kayak|board|wind|paddle|padd|wing|kite|ski|sup', activity, flags=re.IGNORECASE):
        return 'water_sport'
    elif re.search(r'swim|play|snork|scuba|div|jump|squat|bath|Underwater|diving|float', activity, flags=re.IGNORECASE):
        return 'swimming'
    elif re.search(r'fish|scallop|lobster|wading|wade|prawn|spear', activity, flags=re.IGNORECASE):
        return 'fishing'
    elif re.search(r'torpedoed|sunk|troop|battle|disaster|squad|sank|fire|soldier|crash|plane|explod|capsized|yacht|fell|sinking|broke|wreck|USS'
                   , activity, flags=re.IGNORECASE):
        return 'disaster_war_accident'
    elif re.search(r'shark', activity, flags=re.IGNORECASE):
        return 'shark_related'
    else:
        return 'others'

# grouping type
def clean_type(type_):

    if pd.isna(type_):
        return 'Invalid'


    type_ = str(type_).strip()

    if re.search(r'Watercraft|disaster', type_, flags=re.IGNORECASE):
        return 'Unprovoked'
    elif re.search(r'Questionable', type_, flags=re.IGNORECASE):
        return 'Provoked'
    elif re.search(r'Unverified|Unconfirmed|\?|Boat|Under', type_, flags=re.IGNORECASE):
        return 'Invalid'
    else:
        return type_


# grouping shark species
def clean_species(species):

    if pd.isna(species):
        return 'Unknown'

    species = str(species).strip()

    if re.search(r'Invalid', species, flags=re.IGNORECASE):
        return 'Unknown'
    elif re.search(r'white|wf', species, flags=re.IGNORECASE):
        return 'White shark'
    elif re.search(r'bull', species, flags=re.IGNORECASE):
        return 'Bull Shark'
    elif re.search(r'tiger|ti', species, flags=re.IGNORECASE):
        return 'Tiger Shark'
    elif re.search(r'blackt', species, flags=re.IGNORECASE):
        return 'Blacktip Shark'
    elif re.search(r'lemon', species, flags=re.IGNORECASE):
        return 'Lemon Shark'
    elif re.search(r'spinner', species, flags=re.IGNORECASE):
        return 'Spinner Shark'
    elif re.search(r'nurse', species, flags=re.IGNORECASE):
        return 'Nurse Shark'
    elif re.search(r'bronz', species, flags=re.IGNORECASE):
        return 'Bronze whaler shark'
    elif re.search(r'Hammerhead', species, flags=re.IGNORECASE):
        return 'Hammerhead shark'
    elif re.search(r'mako', species, flags=re.IGNORECASE):
        return 'Mako shark'
    elif re.search(r'grey', species, flags=re.IGNORECASE):
        return 'Grey reef shark'
    else:
        return species


# group FATAL by 1 , 0
def clean_fatal(lst):

    if pd.isna(lst):
        return 0

    species = str(lst).strip()

    if re.search(r'fatal', species, flags=re.IGNORECASE):
        return 1
    else:
        return 0