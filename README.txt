Files in the folder:
* Results.csv
   * It contains the test cases with predicted output of the chatbot
* checkpoint_runf.tar
   * This is the fine tuned model checkpoints in tar format
   * Download checkpoint_runf.tar from https://drive.google.com/file/d/1FNYp4ftJLtxny5EQA047IiwfykKIZw64/view?usp=sharing
* Digital_counselling_chatbot.ipynb
   * Python notebook which contains code to finetune GPT2 and use interactive chat
* Test.csv
* Test.txt
* Train.csv
* Train.txt
* Val.csv
* Data.csv
   * Unprocessed scraped data
* Counsel_chat_scraper.py
   * Python file to scrape the data and get the data.csv file
   * Command to run
      * Navigate to the folder first
      * python3 counsel_chat_scraper.py
* Data_creation.ipynb
   * Process data and convert it into text file which can be used to finetune GPT2
* Report.pdf
* DigitalCounsellor.pdf
   * Presentation
* PPT_Video.txt


Steps to use the interactive chat:
* Download checkpoint_runf.tar from https://drive.google.com/file/d/1FNYp4ftJLtxny5EQA047IiwfykKIZw64/view?usp=sharing
* Untar the checkpoint file using the following command
   * tar -xvf checkpoint_runf.tar
* Open the Digital_counselling_chatbot.ipynb
   * Run the first cell to import all the requirements 
   * Run the 5th cell to load the model
   * Run the last column to use the interactive chat