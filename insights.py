import sqlite3

def run_insights():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    print("\n========== BUSINESS INSIGHTS ==========\n")

    # 1. Total valid users
    cursor.execute("SELECT COUNT(*) FROM users")
    print(f"Total Valid Users: {cursor.fetchone()[0]}")

    # 2. Users per company
    print("\nUsers per Company:")
    cursor.execute("""
        SELECT company_name, COUNT(*) AS user_count
        FROM users
        GROUP BY company_name
        ORDER BY user_count DESC
    """)
    for row in cursor.fetchall():
        print(row)

    # 3. Users per city
    print("\nUsers per City:")
    cursor.execute("""
        SELECT city, COUNT(*) AS user_count
        FROM users
        GROUP BY city
        ORDER BY user_count DESC
    """)
    for row in cursor.fetchall():
        print(row)

    # 4. Users per city per company
    print("\nUsers per City per Company:")
    cursor.execute("""
        SELECT city, company_name, COUNT(*) AS user_count
        FROM users
        GROUP BY city, company_name
        ORDER BY user_count DESC
    """)
    for row in cursor.fetchall():
        print(row)

    # 5. Phone number coverage
    print("\nPhone Number Coverage:")
    cursor.execute("""
        SELECT 
            COUNT(*) AS total_users,
            COUNT(phone_no) AS users_with_phone
        FROM users
    """)
    total, with_phone = cursor.fetchone()
    print(f"Users with phone numbers: {with_phone}/{total}")

    # 6. Email vs website mismatch
    print("\nEmail vs Website Domain Mismatch:")
    cursor.execute("""
        SELECT name, email, website
        FROM users
        WHERE website IS NOT NULL
          AND email NOT LIKE '%' || website || '%'
    """)
    mismatches = cursor.fetchall()
    if mismatches:
        for row in mismatches:
            print(row)
    else:
        print("No mismatches found")

    # 7. Hemisphere distribution (NEW)
    print("\nUsers by Hemisphere:")
    cursor.execute("""
        SELECT 
            CASE 
                WHEN CAST(latitude AS REAL) >= 0 THEN 'Northern Hemisphere'
                ELSE 'Southern Hemisphere'
            END AS hemisphere,
            COUNT(*) AS user_count
        FROM users
        GROUP BY hemisphere
    """)
    for row in cursor.fetchall():
        print(row)

    # 8. Email Domain Type Distribution (NEW)
    print("\nCompany Email Domain Distribution:")
    cursor.execute("""
        SELECT
            CASE
                WHEN email LIKE '%.com'
                OR email LIKE '%.org'
                OR email LIKE '%.net'
                THEN 'Work Email'
                ELSE 'Personal Email'
            END AS email_type,
            COUNT(*) AS user_count
        FROM users
        GROUP BY email_type;

    """)
    for row in cursor.fetchall():
        print(row)

    # 9. Website Domain Type Distribution 
    print("\nWebsite Domain Distribution:")
    cursor.execute("""
        SELECT
            CASE
                WHEN website LIKE '%.com' THEN '.com'
                WHEN website LIKE '%.org' THEN '.org'
                WHEN website LIKE '%.net' THEN '.net'
                WHEN website LIKE '%.info' THEN '.info'
                WHEN website LIKE '%.io' THEN '.io'
                ELSE 'Other'
            END AS website_domain,
            COUNT(*) AS user_count
        FROM users
        GROUP BY website_domain
        ORDER BY user_count DESC

    """)
    for row in cursor.fetchall():
        print(row)

    conn.close()