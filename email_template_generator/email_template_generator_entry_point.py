import json


def email_template_generator_handler(event, context):
    print("email_template_generator_handler invoked with event: " + json.dumps(event))

    virginia_total_cases_formatted = None
    virginia_total_cases_change = None

    # Generate each paragraph as its own formula for readability
# Virginia (case and death data from VDH.  Hospitalization data from Virginia Health and Hospital Association website/dashboard).
    # Total cases: 590,625  (up 1,250 since previous day)
    # 5.5% positive test rate (7 day PCR positive rate; down 0.2% since previous day)
    # Deaths: 9,902 (up 53 since previous day)
    # Hospitalizations:  Present 1,129 (down 7 since previous day) Discharges: Cumulative 48,804 (up 98 since previous day)
    email_text = """
    Virginia (case and death data from VDH.  Hospitalization data from Virginia Health and Hospital Association website/dashboard).
    Total cases: """
    email_text += virginia_total_cases_formatted
    email_text += " ( "
    email_text += virginia_total_cases_change

