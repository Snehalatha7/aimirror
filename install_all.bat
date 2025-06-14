@echo off
cd C:\Users\91863\Documents\aimirror
call .\aimirror-env\Scripts\activate
pip install streamlit==1.23.1
pip install tensorflow==2.10.1 keras==2.10.0
pip install protobuf==3.19.6
pip install deepface==0.0.83
pip install fer==22.4.0
pip install moviepy
pip install opencv-python opencv-contrib-python
pause
