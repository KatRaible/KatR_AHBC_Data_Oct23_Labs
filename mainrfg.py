# Open the file in read mode
with open('facts.txt', 'r') as file:
    # Read all lines from the file
    facts = file.readlines()

# Strip newline characters from each fact and store them in a list
facts = [fact.strip() for fact in facts]


from fastapi import FastAPI
import random

# Create an instance of FastAPI
app = FastAPI()

# Define endpoint to get a random fact
@app.get("/fact")
def get_random_fact():
    random_fact = random.choice(facts)
    return {"fact": random_fact}

# Run your FastAPI app using uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


##references facts.txt