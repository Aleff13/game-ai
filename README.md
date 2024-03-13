# Dependencies

To run this project you will need:

[python](https://python.org.br/instalacao-mac/)\
[nodeJs](https://nodejs.org/en)\
[appium](http://appium.io/docs/en/latest/)\
[react-native](https://reactnative.dev)\
[selenium](https://selenium-python.readthedocs.io/installation.html)

ios-simulator
xcode

# The game

To setup the game you will need to access basic/ and install some modules:

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

The model-generator is inside the model/, need to train, compile, fit and save the model.

This steps are encapsulated inside some packages and called in the generate-model command

So, try to run:

`/generate-model.sh`

And choose the name to your model

# The automation

To run the automation you will use the previous builded model and the game needs to be running

You will need to create your capabilities file to configure driver options

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
