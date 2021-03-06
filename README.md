# covid19-desktop-notifier
This is a gui tool for live update of coronavirus patient data through pop-up notification.

## Demo
![The GUI](https://i.ibb.co/84GWj60/Annotation-2020-07-29-112703.png)
![Dropdown](https://i.ibb.co/mBFJCL9/Annotation-2020-07-29-112724.png)
![Notifier](https://i.ibb.co/ZgByS52/Annotation-2020-07-29-124911.png)

## Features
- Sit back and relax - the coronavirus updates will come to you.
- Get Desktop notifications
  -  State wise data of patients
  -  Total Cases in the state
  -  Active patients
  -  Death toll
- Its reliable - the source of data is official Government site ([here](https://www.mygov.in/covid-19/))

- Want to add a feature? Modify it! Raise a Pull Request too 😉

## Installation
- You need Python
- Install dependencies by running
```bash
pip install plyer
pip install tkinter
pip install requests
pip install beautifulsoup4
```
- Clone this repo and start adding features
- In case error arises in line 14 and 55 it is due to the incorrect path of the icon, correct it in accordance to your system or comment it out.
