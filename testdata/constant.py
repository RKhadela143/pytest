import os
from utilities import readdata

 
class Constant:

    URL = "https://spectrumdb.specindia.com/"
    LOGINPAGE_MESSAGE = 'OOPS, LOOKS LIKE SOMETHING WENT WRONG !!!'

    BOOK_PATH = os.path.join("..", "testdata", "testdata.xlsx")
    LOG_PATH = os.path.join("..", "logs", "logfile.log")

    d = readdata.read_date("date", BOOK_PATH);

    PERSONAL_LEAVE = "Personal Leave"
    FULL_DAY = "Full Day"
    REQUEST = "Request"
    START_DATE = d["startdate"]
    END_DATE = d["enddate"]
    REASON = "Personal"

    LEAVE_SUCCESS_MESSAGE = "Changes saved successfully."
    LEAVE_APPROVE_SUCCESS_MESSAGE = "Saved Successfully."