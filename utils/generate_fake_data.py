from faker import Faker
from faker.providers import DynamicProvider
import pandas as pd

# DynamicProvider which returns a random timezone in its Standard Time Zone Name
standard_timezone_name = DynamicProvider(
    provider_name="standard_timezone_name",
    elements=[
        "Morocco Standard Time",
        "Coordinated Universal Time",
        "GMT Standard Time",
        "Greenwich Standard Time",
        "W. Europe Standard Time",
        "Central Europe Standard Time",
        "Romance Standard Time",
        "Central European Standard Time",
        "W. Central Africa Standard Time",
        "Namibia Standard Time",
        "Jordan Standard Time",
        "GTB Standard Time",
        "Middle East Standard Time",
        "Egypt Standard Time",
        "Syria Standard Time",
        "South Africa Standard Time",
        "FLE Standard Time",
        "Turkey Standard Time",
        "Jerusalem Standard Time",
        "E. Europe Standard Time",
        "Arabic Standard Time",
        "Kaliningrad Standard Time",
        "Arab Standard Time",
        "E. Africa Standard Time",
        "Iran Standard Time",
        "Arabian Standard Time",
        "Azerbaijan Standard Time",
        "Russian Standard Time",
        "Mauritius Standard Time",
        "Georgian Standard Time",
        "Caucasus Standard Time",
        "Afghanistan Standard Time",
        "Pakistan Standard Time",
        "West Asia Standard Time",
        "India Standard Time",
        "Sri Lanka Standard Time",
        "Nepal Standard Time",
        "Central Asia Standard Time",
        "Bangladesh Standard Time",
        "Ekaterinburg Standard Time",
        "Myanmar Standard Time",
        "SE Asia Standard Time",
        "N. Central Asia Standard Time",
        "China Standard Time",
        "North Asia Standard Time",
        "Malay Peninsula Standard Time",
        "W. Australia Standard Time",
        "Taipei Standard Time",
        "Ulaanbaatar Standard Time",
        "North Asia East Standard Time",
        "Tokyo Standard Time",
        "Korea Standard Time",
        "Cen. Australia Standard Time",
        "AUS Central Standard Time",
        "E. Australia Standard Time",
        "AUS Eastern Standard Time",
        "West Pacific Standard Time",
        "Tasmania Standard Time",
        "Yakutsk Standard Time",
        "Central Pacific Standard Time",
        "Vladivostok Standard Time",
        "New Zealand Standard Time",
        "Fiji Standard Time",
        "Magadan Standard Time",
        "Kamchatka Standard Time",
        "Tonga Standard Time",
        "Samoa Standard Time",
        "Azores Standard Time",
        "Cape Verde Standard Time",
        "Mid-Atlantic Standard Time",
        "E. South America Standard Time",
        "Argentina Standard Time",
        "SA Eastern Standard Time",
        "Greenland Standard Time",
        "Montevideo Standard Time",
        "Bahia Standard Time",
        "Newfoundland Standard Time",
        "Paraguay Standard Time",
        "Atlantic Standard Time",
        "Central Brazilian Standard Time",
        "SA Western Standard Time",
        "Pacific SA Standard Time",
        "Venezuela Standard Time",
        "SA Pacific Standard Time",
        "Eastern Standard Time",
        "US Eastern Standard Time",
        "Central America Standard Time",
        "Central Standard Time",
        "Central Standard Time (Mexico)",
        "Canada Central Standard Time",
        "US Mountain Standard Time",
        "Mountain Standard Time (Mexico)",
        "Mountain Standard Time",
        "Pacific Standard Time (Mexico)",
        "Pacific Standard Time",
        "Alaskan Standard Time",
        "Hawaiian Standard Time",
    ],
)
request_result = DynamicProvider(
    provider_name="request_result", elements=["success", "failure"]
)

DYNAMIC_PROVIDERS = [standard_timezone_name, request_result]
RECORDS_NUMBER = 500

faker = Faker()
for provider in DYNAMIC_PROVIDERS:
    faker.add_provider(provider)

def make_applications_logs(num):
    """Generate fake application logs

    Args:
        num (int): Number of records/rows to generate

    Returns:
        list[dict]: List of application logs records 
    """
    fake_logs = [
        {
            'datetime': faker.date_time_between(start_date="-14d", end_date="-7d"),
            'email_address': faker.company_email(),
            'timezone': faker.standard_timezone_name(),
            'src_ip': faker.ipv4_public(),
            'request_result': faker.request_result(),
            'user_agent': faker.user_agent(),
        }
        for _ in range(num)
    ]
    return fake_logs

df_application_logs = pd.DataFrame(make_applications_logs(RECORDS_NUMBER))

# Export the generate logs from the DataFrame as a CSV file
df_application_logs.to_csv(f'./data/application_logs_{RECORDS_NUMBER}.csv', index=False)
