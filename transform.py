import pandas as pd
from logger import logger

def transform_users(raw_data):
    users = []

    for user in raw_data:
        users.append({
            "user_id": user.get("id"),
            "name": user.get("name"),
            "username": user.get("username"),
            "email": user.get("email"),
            "city": user.get("address", {}).get("city"),
            "zipcode": user.get("address", {}).get("zipcode"),
            "phone_no":user.get("phone"),
            "website":user.get("website"),
            "company_name":user.get("company",{}).get("name"),
            "latitude": user.get("address", {}).get("geo", {}).get("lat"),
            "longitude": user.get("address", {}).get("geo", {}).get("lng")
        })

    df = pd.DataFrame(users)
    logger.info("Data transformed successfully")
    return df
