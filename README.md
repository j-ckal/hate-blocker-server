# hate-blocker-server
Developed as part of dissertation project, a server that integrates with a browser extension built to limit exposure to hateful content online

Integrates with [hate-blocker-extension](https://github.com/j-ckal/hate-blocker-extension/) to function in a web browser

## Setup
1. [Python 3.8+](https://www.python.org/) is required for this project, so install if necessary.
2. Create a virtual environment in Python in the root folder of this project. This can be done by entering the command ```python -m venv venv```
3. Enter the virtual environment using the command ```source env/bin/activate``` on Linux, or ```env\Scripts\activate.bat (or \Activate.ps1)``` on Windows
4. Install the dependencies for this project by entering the command ```pip install -r requirements.txt```
5. Start the server using the command ```flask run```, it should now respond to requests from the browser extension

Credit to [Luis von Ahn's research group](https://www.cs.cmu.edu/~biglou/resources/) for the Offensive/Profane Word List