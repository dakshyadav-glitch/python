from logger import logger

def validate_users(df):
    initial_count = len(df)

    df = df.drop_duplicates(subset="user_id")
    df = df[df["email"].str.contains("@", na=False)]
    df = df[df["city"].notna()]

    df["zipcode"] = df["zipcode"].astype(str)
    df = df[df["zipcode"].str.len() >= 5]

    rejected = initial_count - len(df)
    df = df[df["website"].notna()]
    df = df[df["company_name"].notna()]

    logger.info(f"Validation completed. Rejected records: {rejected}")

    return df
