# MisinfoVote

The major components of the source code are:

1. Backend
   1. The backend is a Flask server that listens on port 5000.
   2. To setup and run the app, follow the instructions in the README in the backend folder.

2. Plugin
   1. The plugin is an unpacked chrome plugin that detects the presence of a social media website, identifies the posts and injects buttons and trust score indicators in the posts.
   2. Check the following [Chrome Documentation](https://developer.chrome.com/docs/extensions/get-started/tutorial/hello-world#load-unpacked) link for steps on how to install an extension to chrome from source code (unpacked.)

3. SocialMedia-Frontend (modified from the original by [ZainRK](https://github.com/ZainRk/SocialMedia-Frontend))
   1. This is the mockup of a social media page that we used to demonstrate how our plugin would work on a real website, and how it will integrate with the system seamlessly.
   2. To set up the app, run `yarn install` with this folder as root.
   3. With this folder as root, run `npm run start` to start the app on **localhost:3000**.

4. model-utils
   1. This contains the script used to train the model with our dataset

Other assets included (under `/deliverables`) are:
1. Jmeter test plan (`Misinfovote Test Plan.jmx`) - Settings for the load testing tool (Apache JMeter) used for metrics collection.
2. Postman collection (`Misinfovote.postman_collection.json`) for manual API testing using Postman tool.
3. Packed plugin (`plugin.crx`).
