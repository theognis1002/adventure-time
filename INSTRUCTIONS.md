# Backend dev exercise

## Instructions

For this exercise, you are tasked with implementing a backend for a choose-your-own-adventure style app (as detailed below). This backend will include a web application server which exposes an API, a database which persists data (and is seeded with certain data), and an environment for running the project with Docker Compose. You must use Django/Python for the web application layer, and postgresql for the persistence layer.

### Choose Your Own Adventure overview

While you are not required to build the UI for this exercise, you are welcome to do the frontend project as well and connect the two. Regardless we've included a UI spec (refer to `designs/story-ui.v2.3.pdf`) to demonstrate how the app would be expected to work if it did have a UI. In this UI, an end user is able to load the data for a choose your own adventure story. A story consists of a set of frames that the user navigates through, viewing a single frame at a time.

Each frame expresses the following information (**note that this representation is not intended to necessarily reflect how frames are modeled on the backend**).

- **index** The frame's sequential position (starting from 0) within its story (i.e. 0, 1, etc). The frame's position must be unique within the story (i.e. no two frames that are part of the same story may have same index).
- **title** Header text displayed for each frame.
- **body** Body content displayed for each frame. This field contains HTML, and may consist of one or multiple `<p>` elements.
- **img** An optional image, represented as a URL to its source file. Note that for this exercise it's not necessary to store and serve actual image files (which we have not provided). For this field, just store the URL string.
- **colors** A map of color hex values, containing the properties:
  - **bg** The background color of the entire frame.
  - **text** The foreground color used in the frame for text, borders, etc.
- **buttons** A list of button objects. Each button represents a navigation action the user may take to advance to another frame. A frame can have zero, one, or two buttons.
  - **text** The label to display for the button.
  - **linkindex** The index of a target frame to show when the user clicks/taps the button.

Refer to `data/story.json` for sample data for a single story, represented as a JSON document.

### Project requirements

**Note feel free to pepper your code with comments explaining any decisions you made that you'd like to let us know about**

- Implement an application which models choose your own adventure stories as discussed above. The application should support multiple different stories. Aside from its frames, the only data that an individual story requires is a unique ID. The application should be backed by the database (i.e. the app should support reading/writing all story related data from/to the database).
- Expose an API for your application under the endpoint `/api/`. Your API should provide services that allow a client to do the following:
  - Retrieve a list of all stories. It's only necessary to provide the story IDs, not their full set of frame data.
  - Retrieve the data for a single frame of a specific story (given a story ID, and the frame's index).
- Require authorized access to the API. All API requests should return a 403 response unless they are properly authorized. To implement authorization, store valid authorization tokens in the database. Tokens should be represented as arbitrary unique strings, and aren't required to be expirable or support any other features. Authorized API requests must include an `Authorization` header, with the value set to the value of a token that is present in the database.
- Include a script that performs database setup (e.g. schema migrations) and seeds the database with the data for a single story, based off the frame data in `data/story.json`. The seeded story should have an ID of: 1. Additionally, the database should be seeded with an authorization token with a value of: "opensesame". Ensure that this seed script is run automatically when the project environment is spun up.
- Replace the contents of this file with setup instructions and any other relevant project details that you would normally include in a project Readme (does not have to be extensive by any means)
