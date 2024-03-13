# Dependencies

To run this project, you will need the following dependencies installed:

- [Python](https://python.org.br/instalacao-mac/)
- [Node.js](https://nodejs.org/en)
- [Appium](http://appium.io/docs/en/latest/)
- [React Native](https://reactnative.dev)
- [Selenium](https://selenium-python.readthedocs.io/installation.html)

Additionally, ensure you have the following installed for iOS simulation:

- iOS Simulator
- Xcode

# The Game

To set up the game, you will need to access the `basic/` directory and install some modules:

1. `cd basic/`
2. `npm install`
 
• Install Cocoapods

3. `cd /ios`
4. `bundle install` 
5. `bundle exec pod install`
6. `cd ..`

Start your ios simulator
    
7. `npx react-native run-ios`

# The model

The model generator is located inside the model/ directory. You need to train, compile, fit, and save the model. These steps are encapsulated within packages and can be called using the generate-model command. Follow these steps:

`/generate-model.sh`

Choose a name for your model.

# The automation

To run the automation, you will use the previously built model, and the game needs to be running. Follow these steps:

`touch automation/capabilities.py`

In the file you will need to put your configs like this:

```py
capabilities = {
    'platformName': 'iOS',
    'deviceName': '<device name>',
    'platformVersion': '<ios versions>',
    "automationName": "XCUITest",
    'udid': '<Your device id>',
    # 'app': apk_path
}
```

Tip: to see simulators list use the following command

`xcrun simctl list`

After this you will need to run the appium server for comunicate the device with automation

`./start-appium.sh`

Finally you can run the automation using the following command

`./run-automation.sh`
