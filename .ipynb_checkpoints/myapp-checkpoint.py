{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "b1e22c54",
   "metadata": {},
   "outputs": [],
   "source": [
    "##pip install streamlit\n",
    "##pip install yfinance"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "7403ba7e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting yfinance\n",
      "  Downloading yfinance-0.1.63.tar.gz (26 kB)\n",
      "Requirement already satisfied: pandas>=0.24 in c:\\users\\agnes\\anaconda3\\lib\\site-packages (from yfinance) (1.2.4)\n",
      "Requirement already satisfied: numpy>=1.15 in c:\\users\\agnes\\anaconda3\\lib\\site-packages (from yfinance) (1.20.1)\n",
      "Requirement already satisfied: requests>=2.20 in c:\\users\\agnes\\anaconda3\\lib\\site-packages (from yfinance) (2.25.1)\n",
      "Collecting multitasking>=0.0.7\n",
      "  Downloading multitasking-0.0.9.tar.gz (8.1 kB)\n",
      "Requirement already satisfied: lxml>=4.5.1 in c:\\users\\agnes\\anaconda3\\lib\\site-packages (from yfinance) (4.6.3)\n",
      "Requirement already satisfied: python-dateutil>=2.7.3 in c:\\users\\agnes\\anaconda3\\lib\\site-packages (from pandas>=0.24->yfinance) (2.8.1)\n",
      "Requirement already satisfied: pytz>=2017.3 in c:\\users\\agnes\\anaconda3\\lib\\site-packages (from pandas>=0.24->yfinance) (2021.1)\n",
      "Requirement already satisfied: six>=1.5 in c:\\users\\agnes\\anaconda3\\lib\\site-packages (from python-dateutil>=2.7.3->pandas>=0.24->yfinance) (1.15.0)\n",
      "Requirement already satisfied: chardet<5,>=3.0.2 in c:\\users\\agnes\\anaconda3\\lib\\site-packages (from requests>=2.20->yfinance) (4.0.0)\n",
      "Requirement already satisfied: idna<3,>=2.5 in c:\\users\\agnes\\anaconda3\\lib\\site-packages (from requests>=2.20->yfinance) (2.10)\n",
      "Requirement already satisfied: urllib3<1.27,>=1.21.1 in c:\\users\\agnes\\anaconda3\\lib\\site-packages (from requests>=2.20->yfinance) (1.26.4)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\agnes\\anaconda3\\lib\\site-packages (from requests>=2.20->yfinance) (2020.12.5)\n",
      "Building wheels for collected packages: yfinance, multitasking\n",
      "  Building wheel for yfinance (setup.py): started\n",
      "  Building wheel for yfinance (setup.py): finished with status 'done'\n",
      "  Created wheel for yfinance: filename=yfinance-0.1.63-py2.py3-none-any.whl size=23909 sha256=c35305fa06bb252f5e8206f03a4f2312985434a2fec1f07838e0c4c02e01930c\n",
      "  Stored in directory: c:\\users\\agnes\\appdata\\local\\pip\\cache\\wheels\\ec\\cc\\c1\\32da8ee853d742d5d7cbd11ee04421222eb354672020b57297\n",
      "  Building wheel for multitasking (setup.py): started\n",
      "  Building wheel for multitasking (setup.py): finished with status 'done'\n",
      "  Created wheel for multitasking: filename=multitasking-0.0.9-py3-none-any.whl size=8368 sha256=4a72e8e13c96a1facd02e5005d736809ce775e20dbbf0c79566d7b3508c3119b\n",
      "  Stored in directory: c:\\users\\agnes\\appdata\\local\\pip\\cache\\wheels\\57\\6d\\a3\\a39b839cc75274d2acfb1c58bfead2f726c6577fe8c4723f13\n",
      "Successfully built yfinance multitasking\n",
      "Installing collected packages: multitasking, yfinance\n",
      "Successfully installed multitasking-0.0.9 yfinance-0.1.63\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "import yfinance as yf\n",
    "import streamlit as st \n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "b67cce70",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "DeltaGenerator(_root_container=0, _provided_cursor=None, _parent=None, _block_type=None, _form_data=None)"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "st.write(\"\"\"\n",
    "# Simple Stock Price App\n",
    "Shows the stock closing price and volume of Google\"\"\")\n",
    "#define the ticker symbol         \n",
    "tickerSymbol = 'GOOGL'\n",
    "#get historical data of Google stock price \n",
    "tickerData = yf.Ticker(tickerSymbol)\n",
    "# create a DataFrame\n",
    "tickerDf = tickerData.history(period ='id', start ='2010-5-31', end ='2021-5-31')\n",
    "st.line_chart(tickerDf.Close)\n",
    "st.line_chart(tickerDf.Volume)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "55bdee75",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-14-f38c7961f23a>, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-14-f38c7961f23a>\"\u001b[1;36m, line \u001b[1;32m1\u001b[0m\n\u001b[1;33m    streamlit run myapp.py\u001b[0m\n\u001b[1;37m              ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "streamlit run myapp.py"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "23d6d50b",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
