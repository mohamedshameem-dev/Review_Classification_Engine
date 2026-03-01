import pandas as pd
import sys
import json
from ollama import chat

#error handling for reading file
#for security concern i have updated incorrect file path.
try:
    filepath ="XYZ:/AI projects/sample_reviews.csv"
    df =pd.read_csv(filepath)
except Exception as e:
    print("Report not found:", e)
    sys.exit() #stop execution

batch_size = 10   # only 10 reviews will be considered for an each batch process 
for i in range(0, len(df), batch_size):
    batch = df["review_text"].iloc[i:i+batch_size].to_list()
    review_block = "\n".join(
        #idx for index starts with numericals : 1,2,3
        #if u want character yes it is possible use chr() but limitation was there. Char has (a-z)beyond that
        #it lookalike odd. Better choose numbering for your listed review comments.
        [f"{idx+1}. {review}" for idx, review in enumerate(batch)]
    )
    prompt = f"""
    Classify and detect sentiment for each review.

    Format:
    [
       {{"review_number": 1, "category": "...", "sentiment": "..."}}
    ]


    Reviews:
    {review_block}
    """
    #error handling
    try:
        response = chat(
        model="llama3",
        messages=[
            {"role": "system", "content": "You are an ecommerce classification engine."},
            {"role": "user", "content": prompt}
        ],
        options={"temperature": 0}
        )
    except Exception as e:
        print("Batch failed:", e)
        continue #next batch process

    raw_output = response.message.content.strip()

    print(f"\n=== Batch {i//batch_size + 1} RAW OUTPUT ===")
    print(raw_output)

    # ==============================
    # Safe JSON Extraction
    # ==============================
    try:
        # Extract JSON array safely
        start = raw_output.find("[")
        end = raw_output.rfind("]") + 1
        json_string = raw_output[start:end]

        final_output = json.loads(json_string)

        print(f"\n=== Batch {i//batch_size + 1} PARSED OUTPUT ===")
        print(final_output)

    except Exception as e:
        print(f"⚠ JSON parsing failed for Batch {i//batch_size + 1}: {e}")
        continue


