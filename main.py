from extract import extract_users
from transform import transform_users
from validate import validate_users
from load import save_to_csv, load_to_sqlite
from insights import run_insights

def run_pipeline():
    raw_data = extract_users()

    if not raw_data:
        print("No data extracted. Pipeline stopped.")
        return

    transformed_df = transform_users(raw_data)
    validated_df = validate_users(transformed_df)

    save_to_csv(validated_df)
    load_to_sqlite(validated_df)
    run_insights()

if __name__ == "__main__":
    run_pipeline()
  