# MentalHealthCompanion

## Setup Instructions

This project requires a large model file (`model.safetensors`) for the sentiment analysis model. Due to its size (255MB), it is not tracked in the Git repository.

### Downloading the Model

1. Download the `model.safetensors` file from this Google Drive link:
   [Download `model.safetensors`](https://drive.google.com/file/d/1O8SnQBpOJcEcwaCqvo2MVHc0qQNgX0Ov/view?usp=drive_link)
2. Place the downloaded file into the `sentiment_model/` directory at the root of the project.

Your directory structure should look like this:

```text
MentalHealthApp/
├── sentiment_model/
│   ├── config.json
│   ├── model.safetensors  <-- Place the downloaded file here
│   ├── tokenizer_config.json
│   └── tokenizer.json
├── app.py
...
```

### Running the Application

```bash
# Example command to run the app (update if needed)
python app.py
```
