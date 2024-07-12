import random
import struct
import urllib
from itertools import islice
from struct import unpack

from shapely.geometry import MultiLineString

import vsketch


# unpacking functions are from https://github.com/googlecreativelab/quickdraw-dataset/blob/master/examples/binary_file_parser.py
def unpack_drawing(file_handle):
    (key_id,) = unpack("Q", file_handle.read(8))
    (country_code,) = unpack("2s", file_handle.read(2))
    (recognized,) = unpack("b", file_handle.read(1))
    (timestamp,) = unpack("I", file_handle.read(4))
    (n_strokes,) = unpack("H", file_handle.read(2))
    image = []
    for i in range(n_strokes):
        (n_points,) = unpack("H", file_handle.read(2))
        fmt = str(n_points) + "B"
        x = unpack(fmt, file_handle.read(n_points))
        y = unpack(fmt, file_handle.read(n_points))
        image.append((x, y))

    return {
        "key_id": key_id,
        "country_code": country_code,
        "recognized": recognized,
        "timestamp": timestamp,
        "image": image,
    }


def unpack_drawings(filename):
    with open(filename, "rb") as f:
        while True:
            try:
                yield unpack_drawing(f)
            except struct.error:
                break


def quickdraw_to_linestring(qd_image):
    """Returns a Shapely MultiLineString for the provided quickdraw image.
    This MultiLineString can be passed to vsketch
    """
    linestrings = []
    for i in range(0, len(qd_image["image"])):
        line = zip(qd_image["image"][i][0], qd_image["image"][i][1])
        linestrings.append(tuple(line))
    return MultiLineString(linestrings)


# Set the quickdraw set
QUICKDRAW_SET_NAME = "dog"

quickdraw_filepath, _ = urllib.request.urlretrieve(
    f"https://storage.googleapis.com/quickdraw_dataset/full/binary/{QUICKDRAW_SET_NAME}.bin",
    f"{QUICKDRAW_SET_NAME}.bin",
)

print(quickdraw_filepath)

drawing_set = unpack_drawings(quickdraw_filepath)
drawing_subset = list(islice(drawing_set, 10000))

vsk = vsketch.Vsketch()
vsk.size("125x125mm")
vsk.penWidth("0.5mm")

# Set the dimensions of the grid
grid_size = 5

vsk.scale(1 / grid_size)
samples = random.sample(drawing_subset, grid_size ** 2)
for i in range(grid_size ** 2):
    drawing = quickdraw_to_linestring(samples[i])
    vsk.geometry(drawing)
    vsk.translate(vsk.width, 0)
    if (i + 1) % grid_size == 0:
        vsk.translate(-grid_size * vsk.width, vsk.height)

vsk.display(fig_size=(12, 12))
vsk.save(f"quick_dog_1{QUICKDRAW_SET_NAME}.svg")

import random
import struct
import urllib
from itertools import islice
from struct import unpack

from shapely.geometry import MultiLineString

import vsketch


# unpacking functions are from https://github.com/googlecreativelab/quickdraw-dataset/blob/master/examples/binary_file_parser.py
def unpack_drawing(file_handle):
    (key_id,) = unpack("Q", file_handle.read(8))
    (country_code,) = unpack("2s", file_handle.read(2))
    (recognized,) = unpack("b", file_handle.read(1))
    (timestamp,) = unpack("I", file_handle.read(4))
    (n_strokes,) = unpack("H", file_handle.read(2))
    image = []
    for i in range(n_strokes):
        (n_points,) = unpack("H", file_handle.read(2))
        fmt = str(n_points) + "B"
        x = unpack(fmt, file_handle.read(n_points))
        y = unpack(fmt, file_handle.read(n_points))
        image.append((x, y))

    return {
        "key_id": key_id,
        "country_code": country_code,
        "recognized": recognized,
        "timestamp": timestamp,
        "image": image,
    }


def unpack_drawings(filename):
    with open(filename, "rb") as f:
        while True:
            try:
                yield unpack_drawing(f)
            except struct.error:
                break


def quickdraw_to_linestring(qd_image):
    """Returns a Shapely MultiLineString for the provided quickdraw image.
    This MultiLineString can be passed to vsketch
    """
    linestrings = []
    for i in range(0, len(qd_image["image"])):
        line = zip(qd_image["image"][i][0], qd_image["image"][i][1])
        linestrings.append(tuple(line))
    return MultiLineString(linestrings)


# Set the quickdraw set
QUICKDRAW_SET_NAME = "crab"

quickdraw_filepath, _ = urllib.request.urlretrieve(
    f"https://storage.googleapis.com/quickdraw_dataset/full/binary/{QUICKDRAW_SET_NAME}.bin",
    f"{QUICKDRAW_SET_NAME}.bin",
)

print(quickdraw_filepath)

drawing_set = unpack_drawings(quickdraw_filepath)
drawing_subset = list(islice(drawing_set, 10000))

vsk = vsketch.Vsketch()
vsk.size("125x125mm")
vsk.penWidth("0.5mm")

# Set the dimensions of the grid
grid_size = 5

vsk.scale(1 / grid_size)
samples = random.sample(drawing_subset, grid_size ** 2)
for i in range(grid_size ** 2):
    drawing = quickdraw_to_linestring(samples[i])
    vsk.geometry(drawing)
    vsk.translate(vsk.width, 0)
    if (i + 1) % grid_size == 0:
        vsk.translate(-grid_size * vsk.width, vsk.height)

vsk.display(fig_size=(12, 12))
vsk.save(f"quick_draw0_{QUICKDRAW_SET_NAME}.svg")

Items=["aircraft carrier","airplane","alarm clock","ambulance","angel","animal migration","ant","anvil","apple","arm","asparagus","axe","backpack","banana","bandage","barn","baseball","baseball bat","basket","basketball","bat","bathtub","beach","bear","beard","bed","bee","belt","bench","bicycle","binoculars","bird","birthday cake","blackberry","blueberry","book","boomerang","bottlecap","bowtie","bracelet","brain","bread","bridge","broccoli","broom","bucket","bulldozer","bus","bush","butterfly","cactus","cake","calculator","calendar","camel","camera","camouflage","campfire","candle","cannon","canoe","car","carrot","castle","cat","ceiling fan","cello","cell phone","chair","chandelier","church","circle","clarinet","clock","cloud","coffee cup","compass","computer","cookie","cooler","couch","cow","crab","crayon","crocodile","crown","cruise ship","cup","diamond","dishwasher","diving board","dog","dolphin","donut","door","dragon","dresser","drill","drums","duck","dumbbell","ear","elbow","elephant","envelope","eraser","eye","eyeglasses","face","fan","feather","fence","finger","fire hydrant","fireplace","firetruck","fish","flamingo","flashlight","flip flops","floor lamp","flower","flying saucer","foot","fork","frog","frying pan","garden","garden hose","giraffe","goatee","golf club","grapes","grass","guitar","hamburger","hammer","hand","harp","hat","headphones","hedgehog","helicopter","helmet","hexagon","hockey puck","hockey stick","horse","hospital","hot air balloon","hot dog","hot tub","hourglass","house","house plant","hurricane","ice cream","jacket","jail","kangaroo","key","keyboard","knee","knife","ladder","lantern","laptop","leaf","leg","light bulb","lighter","lighthouse","lightning","line","lion","lipstick","lobster","lollipop","mailbox","map","marker","matches","megaphone","mermaid","microphone","microwave","monkey","moon","mosquito","motorbike","mountain","mouse","moustache","mouth","mug","mushroom","nail","necklace","nose","ocean","octagon","octopus","onion","oven","owl","paintbrush","paint can","palm tree","panda","pants","paper clip","parachute","parrot","passport","peanut","pear","peas","pencil","penguin","piano","pickup truck","picture frame","pig","pillow","pineapple","pizza","pliers","police car","pond","pool","popsicle","postcard","potato","power outlet","purse","rabbit","raccoon","radio","rain","rainbow","rake","remote control","rhinoceros","rifle","river","roller coaster","rollerskates","sailboat","sandwich","saw","saxophone","school bus","scissors","scorpion","screwdriver","sea turtle","see saw","shark","sheep","shoe","shorts","shovel","sink","skateboard","skull","skyscraper","sleeping bag","smiley face","snail","snake","snorkel","snowflake","snowman","soccer ball","sock","speedboat","spider","spoon","spreadsheet","square","squiggle","squirrel","stairs","star","steak","stereo","stethoscope","stitches","stop sign","stove","strawberry","streetlight","string bean","submarine","suitcase","sun","swan","sweater","swing set","sword","syringe","table","teapot","teddy-bear","telephone","television","tennis racquet","tent","The Eiffel Tower","The Great Wall of China","The Mona Lisa","tiger","toaster","toe","toilet","tooth","toothbrush","toothpaste","tornado","tractor","traffic light","train","tree","triangle","trombone","truck","trumpet","t-shirt","umbrella","underwear","van","vase","violin","washing machine","watermelon","waterslide","whale","wheel","windmill","wine bottle","wine glass","wristwatch","yoga","zebra"]

print(Items[5])

from random import randint
def PickOne(List):
    Num = len(List)
    num = randint(0,Num-1)
    return Items[num]


List = Items
PickOne(List)

import random
import struct
import urllib
from itertools import islice
from struct import unpack

from shapely.geometry import MultiLineString

import vsketch

List = Items
# unpacking functions are from https://github.com/googlecreativelab/quickdraw-dataset/blob/master/examples/binary_file_parser.py
def unpack_drawing(file_handle):
    (key_id,) = unpack("Q", file_handle.read(8))
    (country_code,) = unpack("2s", file_handle.read(2))
    (recognized,) = unpack("b", file_handle.read(1))
    (timestamp,) = unpack("I", file_handle.read(4))
    (n_strokes,) = unpack("H", file_handle.read(2))
    image = []
    for i in range(n_strokes):
        (n_points,) = unpack("H", file_handle.read(2))
        fmt = str(n_points) + "B"
        x = unpack(fmt, file_handle.read(n_points))
        y = unpack(fmt, file_handle.read(n_points))
        image.append((x, y))

    return {
        "key_id": key_id,
        "country_code": country_code,
        "recognized": recognized,
        "timestamp": timestamp,
        "image": image,
    }


def unpack_drawings(filename):
    with open(filename, "rb") as f:
        while True:
            try:
                yield unpack_drawing(f)
            except struct.error:
                break


def quickdraw_to_linestring(qd_image):
    """Returns a Shapely MultiLineString for the provided quickdraw image.
    This MultiLineString can be passed to vsketch
    """
    linestrings = []
    for i in range(0, len(qd_image["image"])):
        line = zip(qd_image["image"][i][0], qd_image["image"][i][1])
        linestrings.append(tuple(line))
    return MultiLineString(linestrings)


# Set the quickdraw set
QUICKDRAW_SET_NAME = PickOne(List)

quickdraw_filepath, _ = urllib.request.urlretrieve(
    f"https://storage.googleapis.com/quickdraw_dataset/full/binary/{QUICKDRAW_SET_NAME}.bin",
    f"{QUICKDRAW_SET_NAME}.bin",
)

print(quickdraw_filepath)

drawing_set = unpack_drawings(quickdraw_filepath)
drawing_subset = list(islice(drawing_set, 10000))

vsk = vsketch.Vsketch()
vsk.size("125x125mm")
vsk.penWidth("0.5mm")

# Set the dimensions of the grid
grid_size = 5

vsk.scale(1 / grid_size)
samples = random.sample(drawing_subset, grid_size ** 2)
for i in range(grid_size ** 2):
    drawing = quickdraw_to_linestring(samples[i])
    vsk.geometry(drawing)
    vsk.translate(vsk.width, 0)
    if (i + 1) % grid_size == 0:
        vsk.translate(-grid_size * vsk.width, vsk.height)

vsk.display(fig_size=(12, 12))
vsk.save(f"quick_draw0_{QUICKDRAW_SET_NAME}.svg")



