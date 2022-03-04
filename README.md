**Backend Hackathon**
*API that takes in data from an attendees.json file and builds full CRUD API*
March, 2022
General Assembly

---

***Planning***
📝 Sketches of views and interfaces in the application.
Link to [Structure of Models to Views](https://imgur.com/qfmaJhn).



***Challenges*** 
🏔 Descriptions of any unsolved problems or hurdles.
Project Schema: We would've liked to add three levels of schema. We wanted to have tasks embedded within members embedding with projects. Taylor and Tim actually spent one full day on trying to make this happen but ultimately scrapped this plan when we realized it wasn't our top priority. Kyle was so far along in the front-end React routes that it would have caused him to have re-do a lot of his work. 

---

*Demonstrating Code*
- What was the most difficult part? 
The most difficult part was figuring out what kind of json format django needed in order to load data.  I had to make a seperate program that went through the json file and reformat according to [Django Docs](https://docs.djangoproject.com/en/4.0/howto/initial-data/)

- What did you learn? 
One thing I struggled with was updating an object without needing all fields.  I learned how to use the ```partial=True``` as seen here ```data = AttendeeSerializer(attendee, data=request.data, partial=True)```