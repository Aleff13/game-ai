from model import Model
from pages import homePage
from factories import driver

model = Model()
model.loadModel("ai.keras")

dr = driver.Driver()
home = homePage.Home(dr.driver)

first = home.getElementByAccessilityId("item-1")
second = home.getElementByAccessilityId("item-2")
third = home.getElementByAccessilityId("item-3")

elements = {
    "first": home.getElementByAccessilityId("item-1"),
    "second": home.getElementByAccessilityId("item-2"),
    "third": home.getElementByAccessilityId("item-3")
}

locations = {
    1: first.location["y"],
    2: second.location["y"],
    3: third.location["y"]
}

locationsMap = {
    1: first,
    2: second,
    3: third
}

transformedLocationList = dict(sorted(locations.items(), key=lambda item: item[1]))

locationKeys = list(transformedLocationList.keys())

result = model.predict([locationKeys], True)

def transformar_entrada(entrada):
    if entrada == 1:
        return elements["first"]
    elif entrada == 2:
        return elements["second"]
    elif entrada == 3:
        return elements["third"]
    else:
        return "entrada inválida"

needToMove = transformar_entrada(result[0])

keyPlace = locationKeys[locationKeys.index(result[1])-1]

home.moveTo(needToMove, locationsMap[keyPlace])

