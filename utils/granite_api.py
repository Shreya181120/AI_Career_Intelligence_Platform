import os
from dotenv import load_dotenv

from ibm_watsonx_ai import Credentials, APIClient
from ibm_watsonx_ai.foundation_models import ModelInference

# -----------------------------
# Load Environment Variables
# -----------------------------

load_dotenv()

IBM_API_KEY = os.getenv("IBM_API_KEY")
IBM_PROJECT_ID = os.getenv("IBM_PROJECT_ID")
IBM_URL = os.getenv("IBM_URL")

MODEL_ID = os.getenv(
    "MODEL_ID",
    "meta-llama/llama-3-3-70b-instruct"
)

# -----------------------------
# Create Client
# -----------------------------

credentials = Credentials(
    url=IBM_URL,
    api_key=IBM_API_KEY
)

client = APIClient(
    credentials=credentials,
    project_id=IBM_PROJECT_ID
)

# -----------------------------
# Create Model
# -----------------------------

model = ModelInference(
    api_client=client,
    model_id=MODEL_ID
)

# -----------------------------
# Generate Response
# -----------------------------

def generate_response(prompt):

    try:

        response = model.chat(
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["choices"][0]["message"]["content"]

    except Exception as e:

        return f"Error : {e}"