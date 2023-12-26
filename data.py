from security import safe_requests

MY_AMOUNT = 10
MY_TYPE = "boolean"

def api_req(my_response):
    my_response.raise_for_status()
    jdata = my_response.json()
    q_data = []
    for d_entry in jdata['results']:
        q_data.append(d_entry)
    return q_data

response = safe_requests.get(url=f"https://opentdb.com/api.php?amount={MY_AMOUNT}&type={MY_TYPE}")
question_data = api_req(response)
