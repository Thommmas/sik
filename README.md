# Beer Counter Website

## Description
This web application allows users to track and visualize the number of beers consumed in real time. It features a simple user interface for incrementing the beer count and a dynamic chart that updates to reflect the latest counts.

## How It Works
- **Increment Page (`increment.html`)**: Users can increase the beer count by entering their username and clicking the '+1' button.
- **Chart Page (`chart.html`)**: Displays a real-time line chart showing the beer counts over time for each user.

## Setup and Installation

### Requirements
- A modern web browser with JavaScript enabled.
- Backend setup that supports POST requests for incrementing and GET requests for fetching data (not provided here).

### Running the Application
1. Ensure that your server backend is running and properly connected to serve the `.html` files.
2. Open `increment.html` to increment the beer count.
3. Open `chart.html` to view the live chart of the beer counts.

## Files Included
- `increment.html`: Web page for users to increment the beer count.
- `chart.html`: Web page displaying the live chart of beer counts.
- `style.css`: Contains the CSS styles for the application.
- `increment.css`: Specific styles for the increment page.

## Additional Information
- Ensure that CORS policies are correctly set to allow resource sharing if your backend and frontend are served from different origins.
- This application uses Chart.js for the graphs and Axios for HTTP requests.

## Support
For any additional help or to report issues, please open an issue on the repository or contact the admin.

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.
