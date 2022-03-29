# Room Temperature IOT

## Run
``` cmd
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook
```
## Folder Structure 
``` cmd
room-temperature.
|   
|   
+---Code
|   |   README.md
|   |   
|   \---DataPrep
|       |   preprocess.ipynb
|       |
|       \---.ipynb_checkpoints
|               preprocess-checkpoint.ipynb
|
+---Data
|   |   README.md
|   |
|   +---Processed
|   |       room_temp_prepdata.csv
|   |
|   \---Raw
|           room_temp_rawdata.csv
|
\---Docs
        README.md
```